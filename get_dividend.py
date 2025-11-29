import jqdatasdk as jq
from jqdatasdk import finance
import pandas as pd
import os
from Config.config import JQ_USERNAME, JQ_PASSWORD
jq.auth(JQ_USERNAME, JQ_PASSWORD)
from Config.data_path import get_path
import datetime

def _prepare_dividend_dir():
    """公共准备函数"""
    save_dir = get_path('dividend')
    os.makedirs(save_dir, exist_ok=True)
    stock_list = pd.read_csv(...)['code'].tolist()
    return save_dir, stock_list

def _log_dividend_operation(save_dir, operation, date_info):
    """公共日志函数"""
    log_path = os.path.join(save_dir, "dividend.log")
    with open(log_path, 'a') as f:
        f.write(f"{operation}: {date_info}\n")

def _deduplicate_dividend(new_df, existing_df):
    """
    对分红数据进行去重，返回真正新增的数据行
    
    参数:
        new_df: 新获取的数据DataFrame
        existing_df: 已存在的数据DataFrame
    
    返回:
        DataFrame: 去重后的新增数据
    """
    if new_df.empty or existing_df.empty:
        return new_df
        
    # 方法1: 使用唯一标识列（聚宽STK_XR_XD表通常有id列）
    if 'id' in new_df.columns and 'id' in existing_df.columns:
        # 找出已存在的id
        existing_ids = set(existing_df['id'].astype(str))
        # 过滤掉已存在的记录
        mask = ~new_df['id'].astype(str).isin(existing_ids)
        dedup_df = new_df[mask].copy()
        
        if len(dedup_df) < len(new_df):
            print(f"  基于ID去重: 原始{len(new_df)}条 → 新增{len(dedup_df)}条")
        return dedup_df
    
    # 方法2: 使用复合键 (code, report_date) 去重
    elif 'code' in new_df.columns and 'report_date' in new_df.columns:
        # 创建复合键
        existing_keys = set(
            existing_df.apply(
                lambda x: f"{x['code']}_{x['report_date']}", 
                axis=1
            )
        )
        
        # 筛选新数据
        new_keys = new_df.apply(
            lambda x: f"{x['code']}_{x['report_date']}", 
            axis=1
        )
        mask = ~new_keys.isin(existing_keys)
        dedup_df = new_df[mask].copy()
        
        if len(dedup_df) < len(new_df):
            print(f"  基于复合键去重: 原始{len(new_df)}条 → 新增{len(dedup_df)}条")
        return dedup_df
    
    # 方法3: 如果以上列都不存在，直接返回原始数据（有风险）
    else:
        print("警告: 数据缺少id和code/report_date列，无法去重，可能产生重复数据")
        return new_df
    
def get_dividend(end_date):
    """获取截至end_date的历史分红信息"""
    save_dir, stock_list = _prepare_dividend_dir()
    print(f"获取到 {len(stock_list)} 只股票")
    
    for code in stock_list:
        try:
            q = jq.query(finance.STK_XR_XD).filter(
                finance.STK_XR_XD.code == code,
                finance.STK_XR_XD.report_date <= end_date
            ).order_by(finance.STK_XR_XD.report_date)
            df = jq.finance.run_query(q)
            
            if df.empty:
                print(f"{code} 无分红数据")
                continue
                
            file_path = os.path.join(save_dir, f"{code}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"{code} 分红数据已保存")
            
        except Exception as e:
            print(f"处理 {code} 失败: {e}")
            continue
    
    _log_dividend_operation(save_dir, "全量更新", f"截至 {end_date}")

# 修复后的get_dividend_delta函数
def get_dividend_delta(last_date):
    """从last_date之后获取增量分红数据"""
    save_dir, stock_list = _prepare_dividend_dir()
    print(f"获取到 {len(stock_list)} 只股票")
    
    # 确认last_date是字符串
    last_date = pd.to_datetime(last_date).strftime('%Y-%m-%d')
    
    for code in stock_list:
        try:
            # 使用 > 而不是 >=
            q = jq.query(finance.STK_XR_XD).filter(
                finance.STK_XR_XD.code == code,
                finance.STK_XR_XD.report_date > last_date
            ).order_by(finance.STK_XR_XD.report_date)
            new_df = jq.finance.run_query(q)
            
            if new_df.empty:
                continue  # 无新增数据，跳过
                
            file_path = os.path.join(save_dir, f"{code}.csv")
            
            if os.path.exists(file_path):
                existing_df = pd.read_csv(file_path)
                # 使用更健壮的去重逻辑
                new_df = _deduplicate_dividend(new_df, existing_df)
                
                if new_df.empty:
                    print(f"{code} 无真正新增数据")
                    continue
                    
                combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            else:
                combined_df = new_df
            
            combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"{code} 新增 {len(new_df)} 条数据")
            
        except Exception as e:
            print(f"处理 {code} 失败: {e}")
            continue
    
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    _log_dividend_operation(save_dir, "增量更新", f"{last_date} -> {current_date}")

if __name__ == '__main__':
    get_dividend('2025-06-15')
    get_dividend_delta('2025-06-15')