"""
数据存储路径统一配置
用于管理项目中所有数据文件的存储路径
"""

import os

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库根目录
DATABASE_ROOT = os.path.join(PROJECT_ROOT, 'Database')

# 数据文件路径配置
DATABASE_PATHS = {
    # 通用数据文件
    'trading_days': os.path.join(DATABASE_ROOT, 'date.pkl'),
    'all_trading_days_csv': os.path.join(DATABASE_ROOT, 'all_trading_days.csv'),
    # 股票数据
    'stock_price': os.path.join(DATABASE_ROOT, 'stock_price'),
    'stock_valuation': os.path.join(DATABASE_ROOT, 'stock_valuation'),
    'stock_industry': os.path.join(DATABASE_ROOT, 'stock_industry'),
    'stock_concept': os.path.join(DATABASE_ROOT, 'stock_concept'),
    'stock_ud': os.path.join(DATABASE_ROOT, 'stock_ud'),
    'is_st': os.path.join(DATABASE_ROOT, 'is_st'),
    'mtss_info': os.path.join(DATABASE_ROOT, 'mtss_info'),
    'money_flow': os.path.join(DATABASE_ROOT, 'money_flow'),
    # 分红数据
    'dividend': os.path.join(DATABASE_ROOT, 'dividend'),
    # 财务数据
    'financial_data': os.path.join(DATABASE_ROOT, 'financial_data'),
    # 因子数据
    'factor_list': os.path.join(DATABASE_ROOT, 'factor_list'),
    'factor_data': os.path.join(DATABASE_ROOT, 'factor_data'),
    # 债券数据
    'bond_rate': os.path.join(DATABASE_ROOT, 'bond_rate'),    
    # 市场数据
    'index_stocks': os.path.join(DATABASE_ROOT, 'index_stocks'),
    'cn_stock_instruments': os.path.join(DATABASE_ROOT, 'cn_stock_instruments'),
    'cn_index_instruments': os.path.join(DATABASE_ROOT, 'cn_index_instruments'),
    'cn_etf_instruments': os.path.join(DATABASE_ROOT, 'cn_etf_instruments'),
}

def get_path(data_type, filename=None):
    """
    获取数据文件路径
    
    Args:
        data_type (str): 数据类型，对应DATABASE_PATHS中的key
        filename (str, optional): 文件名
    
    Returns:
        str: 完整的文件路径
    """
    if data_type not in DATABASE_PATHS:
        raise ValueError(f"未知的数据类型: {data_type}")
    
    path = DATABASE_PATHS[data_type]
    
    if filename:
        return os.path.join(path, filename)
    
    return path

def ensure_directories():
    """确保所有配置的目录都存在"""
    for path in DATABASE_PATHS.values():
        # 如果是文件路径（有扩展名），则创建其父目录
        if os.path.splitext(path)[1]:  # 有扩展名，是文件
            os.makedirs(os.path.dirname(path), exist_ok=True)
        else:  # 没有扩展名，是目录
            os.makedirs(path, exist_ok=True)

if __name__ == '__main__':
    ensure_directories()