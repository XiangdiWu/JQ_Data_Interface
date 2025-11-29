import pandas as pd
import jqdatasdk as jq
import datetime
import os
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

"""
获取全部证券，每天执行一次
证券类别: 
'stock', 'fund', 'index', 'futures', 'options', 'etf', 'lof', 'fja', 'fjb', 
'open_fund', 'bond_fund', 'stock_fund', 'QDII_fund'(QDII基金), 
'money_market_fund', 'mixture_fund'
数据来源: jqdatasdk
"""

def get_all_securities_stock():
    """
    获取最近一天全部日期的股票代码列表

    全部日期：可查询的日期区间
    """
    # 使用 jqdatasdk 获取股票代码数据
    stock_df = jq.get_all_securities(types = ['stock'], date=None)
    # print(stock_df)
    stock_df.index.name = 'code'  # 命名索引列
    stock_df = stock_df.reset_index()         # 将索引转换为普通列

    # 创建 cn_stock_instruments 文件夹（如果不存在）
    save_dir = get_path('cn_stock_instruments')
    
    # 生成文件名（当前日期）
    save_path = os.path.join(save_dir, "all_securities_stock.csv")
    
    # 保存为 CSV 文件
    stock_df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"股票代码列表已保存至: {save_path}")
    # 生成一个日志文件，记录保存的日期
    log_path = os.path.join(save_dir, "all_securities_stock.log")
    with open(log_path, 'a') as f:
        f.write(f"{today}\n")

def get_all_securities_index():
    """
    获取最近一天全部日期的指数代码列表
    """
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 使用 jqdatasdk 获取指数代码数据
    index_df = jq.get_all_securities(types = ['index'], date=None)
    # print(index_df)
    index_df.index.name = 'code'  # 命名索引列
    index_df = index_df.reset_index()         # 将索引转换为普通列
    
    # 创建 cn_index_instruments 文件夹（如果不存在）
    save_dir = get_path('cn_index_instruments')
    
    # 生成文件名（当前日期）
    save_path = os.path.join(save_dir, f"{today}.csv")
    
    # 保存为 CSV 文件
    index_df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"指数代码列表已保存至: {save_path}")

def get_all_securities_etf():
    """
    获取最近一天全部日期的ETF基金代码列表
    """
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 使用 jqdatasdk 获取ETF基金代码数据
    etf_df = jq.get_all_securities(types = ['etf'], date=None)
    # print(etf_df)
    etf_df.index.name = 'code'  # 命名索引列
    etf_df = etf_df.reset_index()         # 将索引转换为普通列
    
    # 创建 cn_etf_instruments 文件夹（如果不存在）
    save_dir = get_path('cn_etf_instruments')
    
    # 生成文件名（当前日期）
    save_path = os.path.join(save_dir, f"{today}.csv")
    
    # 保存为 CSV 文件
    etf_df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"ETF基金代码列表已保存至: {save_path}")
    

if __name__ == "__main__":
    date = today = datetime.datetime.now().strftime('%Y-%m-%d')

    # 获取最近一天全部日期的股票代码列表
    get_all_securities_stock()

    # 获取最近一天全部日期的指数代码列表
    # get_all_securities_index(date)

    # 获取最近一天全部日期的ETF基金代码列表
    # get_all_securities_etf(date)