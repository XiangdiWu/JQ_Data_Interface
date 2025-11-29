import pandas as pd
import jqdatasdk as jq
import datetime
import os
from Utils.get_stock_list import get_stock_list
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_daily_price(security_list, start_date, end_date, frequency='daily', fields=None, skip_paused=False, fq='post', count=None, panel=False, fill_paused=True):
    """
    获取股票日线数据
    get_price()用于获取历史数据，可查询多个标的多个数据字段，返回数据格式为 DataFrame
    使用说明见: https://www.joinquant.com/help/api/help#name:api
    
    参数：
    security_list: 股票代码列表
    start_date: 查询开始时间
    end_date: 查询结束时间
    frequency: 数据频率，默认为 daily (日线)
    fields: 查询字段，默认为 ['open', 'close', 'high', 'low', 'volume', 'money']
    skip_paused: 是否跳过停牌，默认为 False
    fq: 复权方式，默认为 'post' (后复权)
    count: 查询天数，与 start_date 二选一
    panel: 是否返回 Panel 对象，默认为 False (返回 DataFrame)
    fill_paused: 是否填充停牌数据，默认为 True
    """
    # 默认字段
    if fields is None:
        fields = ['open', 'close', 'high', 'low', 'volume', 'money']
    
    # 每次最多处理500只股票
    batch_size = 500
    all_data = []
    
    # 分批处理股票列表
    for i in range(0, len(security_list), batch_size):
        batch_stocks = security_list[i:i + batch_size]
        print(f"处理第 {i//batch_size + 1} 批股票，共 {len(batch_stocks)} 只")
        
        try:
            # 批量获取价格数据
            if count is not None:
                # 使用count参数获取最近N个交易日数据
                df = jq.get_price(batch_stocks, count=count, frequency=frequency, 
                                 fields=fields, skip_paused=skip_paused, fq=fq, 
                                 panel=panel, fill_paused=fill_paused)
            else:
                # 使用日期范围获取数据
                df = jq.get_price(batch_stocks, start_date=start_date, end_date=end_date, 
                                 frequency=frequency, fields=fields, skip_paused=skip_paused, 
                                 fq=fq, panel=panel, fill_paused=fill_paused)
            
            if df is not None and not df.empty:
                print(f"成功获取第 {i//batch_size + 1} 批价格数据，共 {len(df)} 条记录")
                
                # 如果是Panel格式，转换为DataFrame
                if panel:
                    df = df.to_frame()
                
                all_data.append(df)
            else:
                print(f"第 {i//batch_size + 1} 批未获取到价格数据")
                
        except Exception as e:
            print(f"获取第 {i//batch_size + 1} 批价格数据时出错: {e}")
            # 如果批量失败，尝试逐只股票获取
            print("尝试逐只股票获取数据...")
            for security in batch_stocks:
                try:
                    if count is not None:
                        single_df = jq.get_price(security, count=count, frequency=frequency,
                                               fields=fields, skip_paused=skip_paused, fq=fq,
                                               panel=panel, fill_paused=fill_paused)
                    else:
                        single_df = jq.get_price(security, start_date=start_date, end_date=end_date,
                                               frequency=frequency, fields=fields, skip_paused=skip_paused,
                                               fq=fq, panel=panel, fill_paused=fill_paused)
                    
                    if single_df is not None and not single_df.empty:
                        # 如果是Panel格式，转换为DataFrame
                        if panel:
                            single_df = single_df.to_frame()
                        all_data.append(single_df)
                        print(f"  成功获取 {security} 的价格数据，共 {len(single_df)} 条记录")
                except Exception as single_e:
                    print(f"  获取 {security} 价格数据时出错: {single_e}")
    
    if all_data:
        # 合并所有数据
        result_df = pd.concat(all_data, ignore_index=True)
        
        # 确保有日期列，如果没有则从索引中提取
        if 'date' not in result_df.columns:
            result_df = result_df.reset_index()
            # 重命名时间列为date
            if 'time' in result_df.columns:
                result_df = result_df.rename(columns={'time': 'date'})
            elif 'index' in result_df.columns:
                result_df = result_df.rename(columns={'index': 'date'})
        
        # 按日期和股票代码排序
        if 'date' in result_df.columns and 'code' in result_df.columns:
            result_df = result_df.sort_values(['date', 'code']).reset_index(drop=True)
        
        print(f"总共获取到 {len(result_df)} 条价格记录，涉及 {result_df['code'].nunique() if 'code' in result_df.columns else 'N/A'} 只股票")
        print("数据预览:")
        print(result_df.head(10))
        
        # 创建保存目录
        save_dir = get_path('stock_price')
        
        # 按日期分别保存文件
        if 'date' in result_df.columns:
            unique_dates = result_df['date'].unique()
            for date in sorted(unique_dates):
                date_df = result_df[result_df['date'] == date].copy()
                # 删除不需要的列（如index列）
                if 'index' in date_df.columns:
                    date_df = date_df.drop('index', axis=1)
                
                # 将日期转换为字符串格式 YYYY-MM-DD
                date_str = pd.to_datetime(date).strftime('%Y-%m-%d')
                filename = f"{date_str}.csv"
                save_path = os.path.join(save_dir, filename)
                
                # 保存为 CSV 文件
                date_df.to_csv(save_path, index=False, encoding='utf-8-sig')
                print(f"{date_str} 的价格数据已保存至: {save_path}，共 {len(date_df)} 条记录")
        else:
            # 如果没有日期列，按时间范围保存一个文件
            if count is not None:
                filename = f"latest_{count}_days_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
            else:
                filename = f"{start_date}_{end_date}.csv"
            
            save_path = os.path.join(save_dir, filename)
            result_df.to_csv(save_path, index=False, encoding='utf-8-sig')
            print(f"价格数据已保存至: {save_path}")
        
        return result_df
    else:
        print("未获取到任何价格数据")
        return pd.DataFrame()

if __name__ == "__main__":
    security_list = get_stock_list()
    start_date = '2024-08-21'
    end_date = '2025-08-19'
    frequency = 'daily'  # 日线
    fields = ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']
    skip_paused = False  # 不跳过停牌
    fq = 'post'  # 后复权
    count = None
    panel = False  # 返回DataFrame
    fill_paused = True  # 填充停牌数据
    
    # print("=== 按日期范围获取价格数据 (以列表前2只股票为例) ===")
    # result1  get_daily_price(security_list[:2], start_date, end_date, frequency, fields, skip_paused, fq, count, panel, fill_paused)
        
    # print("=== 按交易天数获取价格数据  (以列表前2只股票为例) ===")
    # result2 = get_daily_price(security_list[:2], None, None, frequency, fields, skip_paused, fq, count=5, panel=panel, fill_paused=fill_paused)

    print("=== 按日期范围获取所有股票价格数据 ===")
    result3 = get_daily_price(security_list[:100], start_date, end_date, frequency, fields, skip_paused, fq, count, panel, fill_paused)
