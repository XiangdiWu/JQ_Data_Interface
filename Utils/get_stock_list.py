import pandas as pd
import os
import sys
from datetime import datetime

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Config.data_path import get_path
from Utils.get_trading_date import *

def get_stock_list(trade_date):
    """
    获取指定日期的股票代码列表
    根据cn_stock_instruments文件中股票start_date,end_date字段判断股票是否已经退市
    已经退市的股票不应在股票代码列表中
    
    Args:
        trade_date (str): 交易日期，格式：'YYYY-MM-DD'
    
    Returns:
        list: 股票代码列表，格式：['000001.XSHE', '000002.XSHE', ...]
    """
    # 读取股票代码列表文件
    file_path = get_path('cn_stock_instruments')
    
    # 构建文件名
    file_name = 'all_securities_stock.csv'
    full_file_path = os.path.join(file_path, file_name)
    
    try:
        # 读取股票数据
        stock_df = pd.read_csv(full_file_path)
        
        # 转换日期格式
        stock_df['start_date'] = pd.to_datetime(stock_df['start_date'])
        stock_df['end_date'] = pd.to_datetime(stock_df['end_date'])
        target_date = pd.to_datetime(trade_date)
        
        # 过滤出在指定日期有效的股票
        # 股票有效条件：start_date <= target_date <= end_date 且 type为stock
        valid_stocks = stock_df[
            (stock_df['start_date'] <= target_date) & 
            (stock_df['end_date'] >= target_date) & 
            (stock_df['type'] == 'stock')
        ]
        
        # 获取股票代码列表
        stock_list = valid_stocks['code'].tolist()
        
        return stock_list
        
    except FileNotFoundError:
        print(f"股票数据文件未找到: {full_file_path}")
        return []
    except Exception as e:
        print(f"获取股票列表时出错: {e}")
        return []

# 示例用法
if __name__ == "__main__":
    # 测试获取指定日期的股票列表
    test_date = '2025-11-27'  # 使用已知存在的文件日期
    print(f"测试日期: {test_date}")
    
    stock_list = get_stock_list(test_date)
    print(f"股票数量: {len(stock_list)}")
    print("前10只股票:")
    print(stock_list[:10])