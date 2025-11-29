import jqdatasdk as jq
import pandas as pd
import os
from Utils.get_stock_list import get_stock_list
from Utils.get_trading_date import get_trading_dates
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_stock_moneyflow(start_date, end_date, count=None, fields=None):
    """
    按日期范围获取资金流向数据，确保每个交易日的数据完整性
    
    参数：
    start_date: 开始日期 (格式: '2025-08-20')
    end_date: 结束日期 (格式: '2025-08-27')
    count: 数量, 与 start_date 二选一，表示获取 end_date 之前 count 个交易日的数据
    fields: 字段列表，默认获取主要资金流向指标
    """
    # 获取交易日列表
    if count is not None:
        trading_dates = get_trading_dates(end_date, count=count)
    else:
        trading_dates = get_trading_dates(start_date, end_date)
    
    print(f"交易日范围: {len(trading_dates)} 个交易日")
    
    # 默认字段
    if fields is None:
        fields = [
            'change_pct',        # 涨跌幅(%)
            'net_amount_main',   # 主力净额(万)
            'net_pct_main',      # 主力净占比(%)
            'net_amount_xl',     # 超大单净额(万)
            'net_pct_xl',        # 超大单净占比(%)
            'net_amount_l',      # 大单净额(万)
            'net_pct_l',         # 大单净占比(%)
            'net_amount_m',      # 中单净额(万)
            'net_pct_m',         # 中单净占比(%)
            'net_amount_s',      # 小单净额(万)
            'net_pct_s'          # 小单净占比(%)
        ]
        
    for trading_date in trading_dates:
        # 获取当前交易日的股票列表
        stock_list = get_stock_list(trading_date)
        print(stock_list[:10])

        # 获取当前交易日的资金流向数据
        df = jq.get_money_flow(stock_list, start_date=trading_date, end_date=trading_date, fields=fields)
        
        if df is not None and not df.empty:
            # 确保有日期列
            if 'date' not in df.columns:
                df = df.reset_index()
                if 'time' in df.columns:
                    df = df.rename(columns={'time': 'date'})
                elif 'index' in df.columns:
                    df = df.rename(columns={'index': 'date'})
            
            # 统一股票代码字段名为code
            if 'sec_code' in df.columns:
                df = df.rename(columns={'sec_code': 'code'})
            
            print(f"获取到 {trading_date} 的资金流向数据: {len(df)} 条记录")
            if not df.empty:
                print(df.head(5))
            
            # 保存数据
            save_dir = get_path('money_flow')
            filename = f"{trading_date}.csv"
            save_path = os.path.join(save_dir, filename)
            df.to_csv(save_path, index=False, encoding='utf-8-sig')
            print(f"资金流向数据已保存至: {save_path}")
        else:
            print(f"{trading_date} 无资金流向数据，跳过保存")

if __name__ == '__main__':
    print("=== 按时间区间获取资金流向数据 ===")
    start_date = '2025-08-21'
    end_date = '2025-08-27'
    result = get_stock_moneyflow(start_date=start_date, end_date=end_date)