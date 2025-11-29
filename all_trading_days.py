import akshare as ak
import pandas as pd
import os
from Config.data_path import get_path

"""
获取 A 股全部交易日数据
每年执行一次
数据来源：akshare
"""
def get_a_share_trading_days():
    # 使用 akshare 获取交易日数据
    trade_date_df = ak.tool_trade_date_hist_sina()
    
    # 转换为日期格式
    trade_date_df['trade_date'] = pd.to_datetime(trade_date_df['trade_date'])
    
    # 保存为 date.pkl 文件
    save_path = get_path('trading_days')
    trade_date_df.to_pickle(save_path)
    print(f"交易日数据已保存至: {save_path}")

    # # 保存为 csv 文件
    # save_path = get_path('all_trading_days_csv')
    # trade_date_df.to_csv(save_path)
    # print(f"交易日数据已保存至: {save_path}")

def check_date_pkl():
    # 获取 date.pkl 文件路径
    file_path = get_path('trading_days')
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print("错误：date.pkl 文件不存在，请先运行 all_trading_days.py 生成数据。")
        return
    
    # 读取数据
    df = pd.read_pickle(file_path)
    
    # 显示基本信息
    print("=== date.pkl 文件信息 ===")
    print("\n1. 前 5 行和后 5 行数据：")
    print(df.head())
    print(df.tail())

    print("\n2. 数据列名：")
    print(df.columns)
    
    print("\n3. 数据类型：")
    print(df.dtypes)
    
    print("\n4. 数据形状（行数, 列数）：")
    print(df.shape)
    
    print("\n5. 数据统计摘要：")
    print(df.describe())

if __name__ == "__main__":
    get_a_share_trading_days()
    # check_date_pkl()
