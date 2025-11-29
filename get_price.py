import jqdatasdk as jq
import os
from Utils.get_stock_list import get_stock_list
from Utils.get_trading_date import get_trading_dates
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_daily_price(start_date, end_date, frequency, fields, skip_paused, fq, panel, fill_paused):
    """
    按日期范围获取价格数据，确保每个交易日的数据完整性
    
    参数：
    start_date: 开始日期 (格式: '2025-08-20')
    end_date: 结束日期 (格式: '2025-08-27')
    frequency: 数据频率，默认为 daily (日线)
    fields: 查询字段，默认为 ['open', 'close', 'high', 'low', 'volume', 'money']
    skip_paused: 是否跳过停牌，默认为 False
    fq: 复权方式，默认为 'post' (后复权)
    panel: 是否返回 Panel 对象，默认为 False (返回 DataFrame)
    fill_paused: 是否填充停牌数据，默认为 True
    
    返回：
    所有日期的价格数据字典 {date: DataFrame}
    """
    # 获取交易日列表
    trading_dates = get_trading_dates(start_date, end_date)
    print(f"交易日范围: {len(trading_dates)} 个交易日")
        
    for trading_date in trading_dates:
        # 获取当前交易日的股票列表
        stock_list = get_stock_list(trading_date)
        # print(stock_list[:10])

        # 获取当前交易日的价格数据
        df = jq.get_price(stock_list, start_date=trading_date, end_date=trading_date,
                        frequency=frequency, fields=fields, skip_paused=skip_paused,
                        fq=fq, panel=panel, fill_paused=fill_paused)
        
        if df is not None and not df.empty:
            # 处理Panel格式
            if panel:
                df = df.to_frame()
            
            # 确保有日期列
            if 'date' not in df.columns:
                df = df.reset_index()
                if 'time' in df.columns:
                    df = df.rename(columns={'time': 'date'})
                elif 'index' in df.columns:
                    df = df.rename(columns={'index': 'date'})
            
            print(f"获取到 {trading_date} 的价格数据: {len(df)} 条记录")
            if not df.empty:
                print(df.head(5))
            
            # 删除多余的index列
            if 'index' in df.columns:
                df = df.drop('index', axis=1)
            
            # 保存数据
            save_dir = get_path('stock_price')
            filename = f"{trading_date}.csv"
            save_path = os.path.join(save_dir, filename)
            df.to_csv(save_path, index=False, encoding='utf-8-sig')
            print(f"价格数据已保存至: {save_path}")
        else:
            print(f"{trading_date} 无价格数据，跳过保存")

if __name__ == "__main__":
    # 参数设置
    frequency = 'daily' # 日线
    fields = ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']
    skip_paused = False # 不跳过停牌
    fq = 'post' # 后复权
    panel = False # 不返回Panel对象
    fill_paused = True # 填充停牌数据
    
    print("=== 按时间区间获取价格数据===")
    start_date = '2025-08-21'
    end_date = '2025-08-27'
    result1 = get_daily_price(start_date=start_date, end_date=end_date,
                                frequency=frequency, fields=fields, skip_paused=skip_paused,
                                fq=fq, panel=panel, fill_paused=fill_paused)