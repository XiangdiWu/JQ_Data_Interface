import pandas as pd
import pickle
import os
import sys
from datetime import datetime

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Config.data_path import get_path

def get_trading_dates(start_date, end_date=None, count=None):
    """
    根据起始日期获取交易日
    
    Args:
        start_date (str): 起始日期，格式：'YYYY-MM-DD'
        end_date (str, optional): 结束日期，格式：'YYYY-MM-DD'。如果为None，则获取从start_date开始的所有交易日
        count (int, optional): 获取交易日的数量。如果指定，则返回前count个交易日
    
    Returns:
        list: 交易日期列表，格式：['YYYY-MM-DD', ...]
    """
    # 获取交易日数据文件路径
    trading_days_file = get_path('trading_days')
    
    try:
        # 读取交易日数据
        with open(trading_days_file, 'rb') as f:
            df = pickle.load(f)
        
        # 使用pandas向量化操作，性能更优
        start_dt = pd.to_datetime(start_date)
        
        # 布尔索引过滤
        mask = df['trade_date'] >= start_dt
        if end_date:
            end_dt = pd.to_datetime(end_date)
            mask = mask & (df['trade_date'] <= end_dt)
        
        filtered_df = df[mask]
        
        # 如果指定了数量，则取前count个
        if count:
            filtered_df = filtered_df.head(count)
        
        # 转换为字符串列表
        return filtered_df['trade_date'].dt.strftime('%Y-%m-%d').tolist()
        
    except FileNotFoundError:
        print(f"交易日数据文件未找到: {trading_days_file}")
        return []
    except Exception as e:
        print(f"获取交易日时出错: {e}")
        return []

def get_latest_trading_date():
    """
    获取最新交易日（考虑当前日期）
    
    如果今天是交易日，返回今天；
    如果今天不是交易日，返回上一个交易日
    
    Returns:
        str: 最新交易日期，格式：'YYYY-MM-DD'，如果找不到则返回None
    """
    trading_days_file = get_path('trading_days')
    
    try:
        # 读取交易日数据
        with open(trading_days_file, 'rb') as f:
            df = pickle.load(f)
        
        # 获取当前日期
        today = pd.to_datetime(datetime.now().strftime('%Y-%m-%d'))
        
        # 找到小于等于今天的最大交易日
        past_trading_days = df[df['trade_date'] <= today]
        
        if not past_trading_days.empty:
            latest_date = past_trading_days.iloc[-1]['trade_date']
            return latest_date.strftime('%Y-%m-%d')
        
        return None
        
    except FileNotFoundError:
        print(f"交易日数据文件未找到: {trading_days_file}")
        return None
    except Exception as e:
        print(f"获取最新交易日时出错: {e}")
        return None

def get_previous_trading_date(date, offset=1):
    """
    获取指定日期之前的第offset个交易日
    
    Args:
        date (str): 基准日期，格式：'YYYY-MM-DD'
        offset (int): 偏移量，正数表示之前的交易日，负数表示之后的交易日
    
    Returns:
        str: 交易日期，格式：'YYYY-MM-DD'，如果找不到则返回None
    """
    trading_days_file = get_path('trading_days')
    
    try:
        # 读取交易日数据
        with open(trading_days_file, 'rb') as f:
            df = pickle.load(f)
        
        target_dt = pd.to_datetime(date)
        
        # 使用pandas高效查找
        if target_dt in df['trade_date'].values:
            # 如果基准日期是交易日，直接找到索引
            target_index = df[
                df['trade_date'] == target_dt
            ].index[0]
        else:
            # 如果基准日期不是交易日，找到第一个小于基准日期的交易日
            past_dates = df[df['trade_date'] < target_dt]
            if past_dates.empty:
                return None
            target_index = past_dates.index[-1]  # 取最后一个小于目标日期的交易日
        
        # 计算偏移后的索引
        # 对于get_last_trading_date，正数offset表示之前的交易日（更早的日期，索引更小）
        new_index = target_index - offset
        if 0 <= new_index < len(df):
            result_date = df.iloc[new_index]['trade_date']
            return result_date.strftime('%Y-%m-%d')
        
        return None
        
    except FileNotFoundError:
        print(f"交易日数据文件未找到: {trading_days_file}")
        return None
    except Exception as e:
        print(f"获取之前交易日时出错: {e}")
        return None
    
def get_next_trading_date(date, offset=1):
    """
    获取指定日期之后的第offset个交易日
    
    Args:
        date (str): 基准日期，格式：'YYYY-MM-DD'
        offset (int): 偏移量，正数表示之后的交易日，负数表示之前的交易日
    
    Returns:
        str: 交易日期，格式：'YYYY-MM-DD'，如果找不到则返回None
    """
    trading_days_file = get_path('trading_days')
    
    try:
        # 读取交易日数据
        with open(trading_days_file, 'rb') as f:
            df = pickle.load(f)
        
        target_dt = pd.to_datetime(date)
        
        # 使用pandas高效查找
        if target_dt in df['trade_date'].values:
            # 如果基准日期是交易日，直接找到索引
            target_index = df[df['trade_date'] == target_dt].index[0]
        else:
            # 如果基准日期不是交易日，找到第一个大于基准日期的交易日
            future_dates = df[df['trade_date'] > target_dt]
            if future_dates.empty:
                return None
            target_index = future_dates.index[0]
        
        # 计算偏移后的索引
        new_index = target_index + offset
        if 0 <= new_index < len(df):
            result_date = df.iloc[new_index]['trade_date']
            return result_date.strftime('%Y-%m-%d')
        
        return None
        
    except FileNotFoundError:
        print(f"交易日数据文件未找到: {trading_days_file}")
        return None
    except Exception as e:
        print(f"获取下一个交易日时出错: {e}")
        return None

def is_trading_day(date):
    """
    判断指定日期是否为交易日
    
    Args:
        date (str): 日期，格式：'YYYY-MM-DD'
    
    Returns:
        bool: True表示是交易日，False表示不是交易日
    """
    trading_days_file = get_path('trading_days')
    
    try:
        # 读取交易日数据
        with open(trading_days_file, 'rb') as f:
            df = pickle.load(f)
        
        target_dt = pd.to_datetime(date)
        
        # 使用pandas高效查找
        return target_dt in df['trade_date'].values
        
    except FileNotFoundError:
        print(f"交易日数据文件未找到: {trading_days_file}")
        return False
    except Exception as e:
        print(f"判断交易日时出错: {e}")
        return False

# 示例用法
if __name__ == "__main__":
    # 测试获取交易日
    print("从2025-01-01开始的10个交易日:")
    dates = get_trading_dates('2025-01-01', count=10)
    print(dates)
    
    # 测试获取日期范围内的交易日
    print("\n2025-01-01到2025-01-10之间的交易日:")
    dates = get_trading_dates('2025-01-01', '2025-01-10')
    print(dates)
    
    # 测试获取前一个交易日
    print("\n2025-01-06的前一个交易日:")
    last_date = get_previous_trading_date('2025-01-06', 1)
    print(last_date)
    
    print("\n2025-01-06的前2个交易日:")
    last_date2 = get_previous_trading_date('2025-01-06', 2)
    print(last_date2)
    
    # 测试获取最新交易日
    print("\n最新交易日:")
    latest_date = get_latest_trading_date()
    print(latest_date)
    
    # 测试获取下一个交易日
    print("\n2025-01-01的下一个交易日:")
    next_date = get_next_trading_date('2025-01-01', 1)
    print(next_date)
    
    # 测试判断是否为交易日
    print("\n2025-01-01是否为交易日:")
    is_trading = is_trading_day('2025-01-01')
    print(is_trading)