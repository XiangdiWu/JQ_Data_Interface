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

获取所有上市公司股票财务数据（按年度）
- 资产负债表
- 利润表
- 现金流量表
- 财务指标

get_history_fundamentals(security, fields, watch_date=None, stat_date=None, count=count, interval='1y', stat_by_year=True)
"""

def get_annual_count(end_date):
    """
    获取自2005年1月1日至end_date的年度数量
    如 2025-03-31、2025-06-30、2025-09-30、2025-12-31
    
    Args:
        end_date (str): 结束日期，格式为 'YYYY-MM-DD'
    
    Returns:
        int: 年度数量
    """
    from datetime import datetime
    
    # 解析结束日期
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    
    # 起始日期：2005年1月1日
    start_dt = datetime(2005, 1, 1)
    
    # 计算年度数量
    count = end_dt.year - start_dt.year + 1
    
    return count

def _get_balance_sheet_annual(code, end_date, count=None):
    """
    获取截至end_date的资产负债表，整合多个统计日期为一张表
    
    Args:
        code (str): 股票代码，如 '000001.XSHE'
        end_date (str): 结束日期，格式为 'YYYY-MM-DD'
        count (int): 获取的期数，如果为None则获取所有可用的季度数据
    """
    # 使用统一的字段配置
    fields = get_fields('balance_annual')
    
    try:        
        # 如果没有指定count，计算从2005年到end_date的年度数
        if count is None:
            count = get_annual_count(end_date)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1y', 
            stat_by_year=True
        )
        
        if not df.empty:
            print(f"成功获取{code}的资产负债表数据，共{len(df)}期")
            
            # 保存数据
            balance_dir = os.path.join(get_path('financial_data'), 'balance_sheet_annual')
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

def _get_income_statement_annual(code, end_date, count=None):
    """
    获取截至end_date的利润表，整合多个统计日期为一张表
    """
    # 使用统一的字段配置
    fields = get_fields('income_annual')
    
    try:
        print(f"开始获取{code}的利润表数据")
        
        # 如果没有指定count，计算从2005年到end_date的年度数
        if count is None:
            count = get_annual_count(end_date)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1y', 
            stat_by_year=True
        )
        
        if not df.empty:
            print(f"成功获取{code}的利润表数据，共{len(df)}期")
            
            # 保存数据
            income_dir = os.path.join(get_path('financial_data'), 'income_statement_annual')
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

def _get_cash_flow_annual(code, end_date, count=None):
    """
    获取截至end_date的现金流量表，整合多个统计日期为一张表
    """
    # 使用统一的字段配置
    fields = get_fields('cash_flow_annual')
    
    try:
        print(f"开始获取{code}的现金流量表数据")
        
        # 如果没有指定count，计算从2005年到end_date的年度数
        if count is None:
            count = get_annual_count(end_date)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1y', 
            stat_by_year=True
        )
        
        if not df.empty:
            print(f"成功获取{code}的现金流量表数据，共{len(df)}期")
            
            # 保存数据
            cash_flow_dir = os.path.join(get_path('financial_data'), 'cash_flow_annual')
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

def _get_indicator_annual(code, end_date, count=None):
    """
    获取截至end_date的财务指标数据，整合多个统计日期为一张表
    """
    # 使用统一的字段配置
    fields = get_fields('indicator_annual')
    
    try:
        print(f"开始获取{code}的财务指标数据")
        
        # 如果没有指定count，计算从2005年到end_date的年度数
        if count is None:
            count = get_annual_count(end_date)
        
        # 使用get_history_fundamentals获取历史数据
        df = get_history_fundamentals(
            security=code, 
            fields=fields, 
            watch_date=end_date, 
            count=count, 
            interval='1y', 
            stat_by_year=True
        )
        
        if not df.empty:
            print(f"成功获取{code}的财务指标数据，共{len(df)}期")
            
            # 保存数据
            indicator_dir = os.path.join(get_path('financial_data'), 'indicator_annual')
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
    
    # for code in stock_list:
    for code in stock_list[:2]: # 测试用，只获取前2只股票
        print(f"获取{code}截至{end_date}的财务数据")
        try:
            _get_balance_sheet_annual(code, end_date)
            _get_income_statement_annual(code, end_date)
            _get_cash_flow_annual(code, end_date)
            _get_indicator_annual(code, end_date)
            print(f"{code} 获取财务数据成功")
        except Exception as e:
            print(f"{code} 获取财务数据失败: {e}")

def test_single_stock_financial_data(code, end_date, count=None):
    """
    测试单只股票的财务数据获取功能
    
    Args:
        code (str): 股票代码
        end_date (str): 结束日期
        count (int): 获取的年度数量
    """
    print(f"\n=== 测试获取{code}的财务数据 ===")
    if count is not None:
        print(f"获取最近{count}个年度的数据")
    else:
        print("获取全部历史年度数据")
    
    try:
        # 测试资产负债表
        print("\n--- 资产负债表 ---")
        balance_df = _get_balance_sheet_annual(code, end_date, count)
        
        # 测试利润表
        print("\n--- 利润表 ---")
        income_df = _get_income_statement_annual(code, end_date, count)
        
        # 测试现金流量表
        print("\n--- 现金流量表 ---")
        cash_flow_df = _get_cash_flow_annual(code, end_date, count)
        
        # 测试指标数据
        print("\n--- 指标数据 ---")
        indicator_df = _get_indicator_annual(code, end_date, count)
        
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
    测试获取指定数量年度的财务数据
    
    Args:
        code (str): 股票代码
        end_date (str): 结束日期
        count (int): 获取的年度数
    """
    return test_single_stock_financial_data(code, end_date, count)
    
if __name__ == '__main__':
    # 测试单只股票的财务数据获取功能
    test_end_date = '2025-08-27'
    test_code = '002371.XSHE'
    # get_all_financial_data(test_end_date)

    # 测试获取最近20个季度的数据
    print("\n" + "="*50)
    print("测试获取最近20个年度的财务数据")
    print("="*50)
    # test_financial_data_with_count(test_code, test_end_date, count=20)
    
    # 测试获取全部历史数据
    print("\n" + "="*50)
    print("测试获取全部历史财务数据")
    print("="*50)
    # test_single_stock_financial_data(test_code, test_end_date, count=None)

    # 获取所有股票的财务数据（谨慎使用，数据量大）
    end_date = '2025-08-27'
    annual_count = get_annual_count(end_date)
    print(f"从2005年到{end_date}共有{annual_count}个年度")
    print("\n=== 获取所有上市公司股票财务数据 ===")
    # get_all_financial_data(end_date)