import pandas as pd
import jqdatasdk as jq
import datetime
import os
from Utils.get_stock_list import get_stock_list
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_valuation(start_date, end_date):
    """
    按日期范围获取估值数据，确保每个交易日的数据完整性
    
    参数：
    start_date: 开始日期 (格式: '2025-08-20')
    end_date: 结束日期 (格式: '2025-08-27')
    stock_list: 股票代码列表，如果为None则每个交易日获取对应的全部A股（考虑退市等变化）
    
    返回：
    所有日期的估值数据字典 {date: DataFrame}
    """
    # 默认字段：获取主要估值指标
    fields = [
        'capitalization',      # 总股本
        'circulating_cap',      # 流通股本
        'market_cap',           # 总市值
        'circulating_market_cap', # 流通市值
        'turnover_ratio',       # 换手率
        'pe_ratio',            # 市盈率(TTM)
        'pe_ratio_lyr',        # 市盈率(LYR)
        'pb_ratio',            # 市净率
        'ps_ratio',            # 市销率(TTM)
        'pcf_ratio'            # 市现率(TTM)
    ]

    # 获取交易日列表
    trade_dates = jq.get_trade_days(start_date=start_date, end_date=end_date)
    print(f"交易日范围: {len(trade_dates)} 个交易日")
        
    for trade_date in trade_dates:
        # 获取当前交易日的股票列表
        date_str = trade_date.strftime('%Y-%m-%d')
        stock_list = get_stock_list(date_str)
        print(stock_list[:10])

        # 获取当前交易日的估值数据
        df = jq.get_valuation(stock_list, start_date=date_str, end_date=date_str, fields=fields)
        print(f"获取到 {date_str} 的估值数据: {len(df)} 条记录")

        # 保存数据
        if not df.empty:
            save_dir = get_path('stock_valuation')
            filename = f"{date_str}.csv"
            save_path = os.path.join(save_dir, filename)
            df.to_csv(save_path, index=False, encoding='utf-8-sig')
            print(f"估值数据已保存至: {save_path}")
        else:
            print(f"{date_str} 无估值数据，跳过保存")

if __name__ == "__main__":
    result = get_valuation('2025-08-22', '2025-08-27')