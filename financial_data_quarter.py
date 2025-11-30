from jqdatasdk import *
from Config.config import JQ_USERNAME, JQ_PASSWORD
auth(JQ_USERNAME, JQ_PASSWORD)
from Config.data_path import get_path
from Config.fields_config import get_fields
from Utils.get_stock_list import get_stock_list
import pandas as pd
import os

"""
获取财务数据
数据来源: jqdatasdk

获取所有上市公司股票财务数据（按季度）
- 资产负债表
- 利润表
- 现金流量表
- 财务指标

get_history_fundamentals(security, fields, watch_date=None, stat_date=None, count=1, interval='1q', stat_by_year=False)
"""

def get_all_statsDate(end_date):
    """
    获取自2005年1月1日至end_date的所有季度节点日期
    如 2025-03-31、2025-06-30、2025-09-30、2025-12-31
    
    Args:
        end_date (str): 结束日期，格式为 'YYYY-MM-DD'
    
    Returns:
        list: 季度节点日期列表，格式为 ['YYYY-MM-DD', ...]
    """
    from datetime import datetime, timedelta
    import pandas as pd
    
    # 解析结束日期
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    
    # 起始日期：2005年1月1日
    start_dt = datetime(2005, 1, 1)
    
    # 存储所有季度日期
    quarter_dates = []
    
    # 从2005年开始，逐季度生成日期
    current_year = start_dt.year
    current_quarter = 1  # 1: Q1, 2: Q2, 3: Q3, 4: Q4
    
    while True:
        # 计算当前季度的结束日期
        if current_quarter == 1:
            quarter_end = datetime(current_year, 3, 31)
        elif current_quarter == 2:
            quarter_end = datetime(current_year, 6, 30)
        elif current_quarter == 3:
            quarter_end = datetime(current_year, 9, 30)
        else:  # current_quarter == 4
            quarter_end = datetime(current_year, 12, 31)
        
        # 检查是否在日期范围内
        if quarter_end > end_dt:
            break
        
        # 确保季度结束日期不早于起始日期
        if quarter_end >= start_dt:
            quarter_dates.append(quarter_end.strftime('%Y-%m-%d'))
        
        # 移动到下一个季度
        current_quarter += 1
        if current_quarter > 4:
            current_quarter = 1
            current_year += 1
    
    return quarter_dates

def _get_balance_sheet_quarter(code, end_date, count=None):
    """
    获取截至end_date的资产负债表，整合多个统计日期为一张表
    
    Args:
        code (str): 股票代码，如 '000001.XSHE'
        end_date (str): 结束日期，格式为 'YYYY-MM-DD'
        count (int): 获取的期数，如果为None则获取所有可用的季度数据
    """
    # 使用统一的字段配置
    fields = get_fields('balance_quarter')
    
    try:        
        # 如果没有指定count，计算从2005年到end_date的季度数
        if count is None:
            quarter_dates = get_all_statsDate(end_date)
            count = len(quarter_dates)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1q', 
            stat_by_year=False
        )
        
        if not df.empty:
            print(f"成功获取{code}的资产负债表数据，共{len(df)}期")
            
            # 保存数据
            balance_dir = os.path.join(get_path('financial_data'), 'balance_sheet_quarter')
            os.makedirs(balance_dir, exist_ok=True)
            file_path = os.path.join(balance_dir, f"{code}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"资产负债表数据已保存至: {file_path}")
            
            return df
        else:
            print(f"{code} 无资产负债表数据")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"获取{code}资产负债表数据失败: {e}")
        return pd.DataFrame()

def _get_income_statement_quarter(code, end_date, count=None):
    """
    获取截至end_date的利润表，整合多个统计日期为一张表
    """
    # 使用统一的字段配置
    fields = get_fields('income_quarter')
    
    try:
        print(f"开始获取{code}的利润表数据")
        
        # 如果没有指定count，计算从2005年到end_date的季度数
        if count is None:
            quarter_dates = get_all_statsDate(end_date)
            count = len(quarter_dates)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1q', 
            stat_by_year=False
        )
        
        if not df.empty:
            print(f"成功获取{code}的利润表数据，共{len(df)}期")
            
            # 保存数据
            income_dir = os.path.join(get_path('financial_data'), 'income_statement_quarter')
            os.makedirs(income_dir, exist_ok=True)
            file_path = os.path.join(income_dir, f"{code}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"利润表数据已保存至: {file_path}")
            
            return df
        else:
            print(f"{code} 无利润表数据")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"获取{code}利润表数据失败: {e}")
        return pd.DataFrame()

def _get_cash_flow_quarter(code, end_date, count=None):
    """
    获取截至end_date的现金流量表，整合多个统计日期为一张表
    """
    # 使用统一的字段配置
    fields = get_fields('cash_flow_quarter')
    
    try:
        print(f"开始获取{code}的现金流量表数据")
        
        # 如果没有指定count，计算从2005年到end_date的季度数
        if count is None:
            quarter_dates = get_all_statsDate(end_date)
            count = len(quarter_dates)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1q', 
            stat_by_year=False
        )
        
        if not df.empty:
            print(f"成功获取{code}的现金流量表数据，共{len(df)}期")
            
            # 保存数据
            cash_flow_dir = os.path.join(get_path('financial_data'), 'cash_flow_quarter')
            os.makedirs(cash_flow_dir, exist_ok=True)
            file_path = os.path.join(cash_flow_dir, f"{code}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"现金流量表数据已保存至: {file_path}")
            
            return df
        else:
            print(f"{code} 无现金流量表数据")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"获取{code}现金流量表数据失败: {e}")
        return pd.DataFrame()

def _get_indicator_quarter(code, end_date, count=None):
    """
    获取截至end_date的财务指标数据，整合多个统计日期为一张表
    """
    # 使用统一的字段配置
    fields = get_fields('indicator_quarter')
    
    try:
        print(f"开始获取{code}的财务指标数据")
        
        # 如果没有指定count，计算从2005年到end_date的季度数
        if count is None:
            quarter_dates = get_all_statsDate(end_date)
            count = len(quarter_dates)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1q', 
            stat_by_year=False
        )
        
        if not df.empty:
            print(f"成功获取{code}的财务指标数据，共{len(df)}期")
            
            # 保存数据
            indicator_dir = os.path.join(get_path('financial_data'), 'indicator_quarter')
            os.makedirs(indicator_dir, exist_ok=True)
            file_path = os.path.join(indicator_dir, f"{code}.csv")
            df.to_csv(file_path, index=False, encoding='utf-8-sig')
            print(f"财务指标数据已保存至: {file_path}")
            
            return df
        else:
            print(f"{code} 无财务指标数据")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"获取{code}财务指标数据失败: {e}")
        return pd.DataFrame()

def get_all_financial_data(end_date):
    """
    获取截至end_date的所有上市公司财务数据
    """
    # 获取上市公司股票代码列表
    stock_list = get_stock_list(end_date)
    
    # 获取非金融上市公司财务数据
    # for code in stock_list:
    for code in stock_list[:2]: # 测试用，只获取前2只股票
        print(f"获取{code}截至{end_date}的财务数据")
        try:
            _get_balance_sheet_quarter(code, end_date, count=None)
            _get_income_statement_quarter(code, end_date, count=None)
            _get_cash_flow_quarter(code, end_date, count=None)
            _get_indicator_quarter(code, end_date, count=None)
            print(f"{code} 获取财务数据成功")
        except Exception as e:
            print(f"{code} 获取财务数据失败: {e}")

def test_single_stock_financial_data(code, end_date, count=None):
    """
    测试单只股票的财务数据获取功能
    
    Args:
        code (str): 股票代码
        end_date (str): 结束日期
        count (int): 获取的季度数量，None表示获取全部
    """
    print(f"\n=== 测试获取{code}的财务数据 ===")
    if count is not None:
        print(f"获取最近{count}个季度的数据")
    else:
        print("获取全部历史季度数据")
    
    try:
        # 测试资产负债表
        print("\n--- 资产负债表 ---")
        balance_df = _get_balance_sheet_quarter(code, end_date, count)
        
        # 测试利润表
        print("\n--- 利润表 ---")
        income_df = _get_income_statement_quarter(code, end_date, count)
        
        # 测试现金流量表
        print("\n--- 现金流量表 ---")
        cash_flow_df = _get_cash_flow_quarter(code, end_date, count)
        
        # 测试指标数据
        print("\n--- 指标数据 ---")
        indicator_df = _get_indicator_quarter(code, end_date, count)
        
        # 显示数据概览
        print(f"\n=== 数据概览 ===")
        for name, df in [('资产负债表', balance_df), ('利润表', income_df), 
                        ('现金流量表', cash_flow_df), ('指标数据', indicator_df)]:
            if not df.empty:
                print(f"{name}: {len(df)} 期数据，时间范围 {df['statDate'].min()} 到 {df['statDate'].max()}")
            else:
                print(f"{name}: 无数据")
        
        return {
            'balance': balance_df,
            'income': income_df,
            'cash_flow': cash_flow_df,
            'indicator': indicator_df
        }
        
    except Exception as e:
        print(f"测试失败: {e}")
        return None

def test_financial_data_with_count(code, end_date, count=12):
    """
    测试获取指定数量季度的财务数据
    
    Args:
        code (str): 股票代码
        end_date (str): 结束日期
        count (int): 获取的季度数量
    """
    return test_single_stock_financial_data(code, end_date, count)

if __name__ == '__main__':
    # 测试单只股票的财务数据获取功能
    test_end_date = '2025-08-27'
    test_code = '002371.XSHE'
    get_all_financial_data(test_end_date)

    # 测试获取最近20个季度的数据
    print("\n" + "="*50)
    print("测试获取最近20个季度的财务数据")
    print("="*50)
    test_financial_data_with_count(test_code, test_end_date, count=20)
    
    # 测试获取全部历史数据
    print("\n" + "="*50)
    print("测试获取全部历史财务数据")
    print("="*50)
    test_single_stock_financial_data(test_code, test_end_date, count=None)
    
    # 测试获取所有股票的财务数据（谨慎使用，数据量大）
    end_date = '2025-08-27'
    quarter_dates = get_all_statsDate(end_date)
    count = len(quarter_dates)
    print("\n=== 获取所有上市公司股票财务数据 ===")
    get_all_financial_data(end_date)