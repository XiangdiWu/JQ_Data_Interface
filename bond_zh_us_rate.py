import akshare as ak
import pandas as pd
from datetime import datetime, timedelta
import os
from Config.data_path import get_path

def get_bond_rate(start_date):
    """
    获取中美国债收益率
    每天执行一次
    数据来源: akshare
    """
    bond_zh_us_rate_df = ak.bond_zh_us_rate(start_date)
    # print(bond_zh_us_rate_df)

    # 空值填充为前一日的值
    bond_zh_us_rate_df = bond_zh_us_rate_df.fillna(method='ffill')

    save_path = os.path.join(get_path('bond_rate'), 'bond_zh_us_rate.csv')
    bond_zh_us_rate_df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"中美国债收益率数据已保存至: {save_path}")

if __name__ == "__main__":
    # 获取当前日期并计算昨天日期
    # current_date = datetime.now().date()
    # yesterday = current_date - timedelta(days=1)
    # start_date=yesterday
    start_date="2025-09-01"
    get_bond_rate(start_date)
    # get_bond_zh_rate_last()
