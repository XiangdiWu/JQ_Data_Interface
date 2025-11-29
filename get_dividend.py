import jqdatasdk as jq
from jqdatasdk import finance
import pandas as pd
import os
from Config.config import JQ_USERNAME, JQ_PASSWORD
jq.auth(JQ_USERNAME, JQ_PASSWORD)
from Config.data_path import get_path
import datetime

def get_dividend(end_date):
    """
    获取历史分红信息，按证券代码分别存储为CSV文件
    """    
    # 确保目录存在
    save_dir = get_path('dividend')
    
    # 获取当日所有股票代码
    stock_list = pd.read_csv(get_path('cn_stock_instruments', 'all_securities_stock.csv'))['code'].tolist()
    print(f"获取到 {len(stock_list)} 只股票")
    
    for code in stock_list:
        """
        由上市公司年报、中报、一季报、三季报统计出的分红转增情况。
        """
        q = jq.query(finance.STK_XR_XD).filter(finance.STK_XR_XD.code==code).order_by(finance.STK_XR_XD.report_date)
        df = jq.finance.run_query(q)
        
        if df.empty:
            print(f"{code} 无分红数据")
        else:
            file_path = os.path.join(save_dir, f"{code}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"{code} 分红数据已保存至: {file_path}")
    # 生成一个日志文件，记录保存的日期
    log_path = os.path.join(save_dir, "dividend.log")
    with open(log_path, 'a') as f:
        f.write(f"{end_date}\n")

def get_dividend_delta(last_date):
    """
    从上次拉取数据后，获取分红信息，添加到对应证券代码CSV文件中
    """
    # 确保目录存在
    save_dir = get_path('dividend')
    
    # 获取当日所有股票代码
    stock_list = pd.read_csv(get_path('cn_stock_instruments', 'all_securities_stock.csv'))['code'].tolist()
    print(f"获取到 {len(stock_list)} 只股票")
    
    for code in stock_list:
        # 获取增量数据
        q = jq.query(finance.STK_XR_XD).filter(finance.STK_XR_XD.report_date>=last_date, finance.STK_XR_XD.code==code).order_by(finance.STK_XR_XD.report_date)
        new_df = jq.finance.run_query(q)
        
        if new_df.empty:
            print(f"{code} 无新增分红数据")
        else:
            file_path = os.path.join(save_dir, f"{code}.csv")
            
            # 检查文件是否存在
            if os.path.exists(file_path):
                # 读取现有数据
                existing_df = pd.read_csv(file_path)
                
                # 获取现有数据的最新报告日期
                if not existing_df.empty and 'report_date' in existing_df.columns:
                    latest_date = existing_df['report_date'].max()
                    # 过滤掉已存在的数据，避免重复
                    new_df = new_df[new_df['report_date'] > latest_date]
                    
                    if new_df.empty:
                        print(f"{code} 无真正新增的分红数据")
                        continue
                
                # 合并数据
                combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            else:
                combined_df = new_df
            
            # 保存合并后的数据
            combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"{code} 新增 {len(new_df)} 条分红数据，已保存至: {file_path}")

    # 生成一个日志文件，记录保存的日期
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    log_path = os.path.join(save_dir, "dividend.log")
    with open(log_path, 'a') as f:
        f.write(f"{end_date}\n")

if __name__ == '__main__':
    end_date = '2025-08-27'
    # get_dividend(end_date)
    get_dividend_delta(end_date)