from jqdatasdk import *
from Config.config import JQ_USERNAME, JQ_PASSWORD
auth(JQ_USERNAME, JQ_PASSWORD)
from Config.data_path import get_path
from Utils.get_stock_list import get_stock_list
import pandas as pd
import os

"""
获取财务数据
数据来源: jqdatasdk

获取所有上市公司股票财务数据（按季度或年度）
- 资产负债表
- 利润表
- 现金流量表
- 财务指标

get_fundamentals(query_object, date=None, statDate=None) 单独一期，默认最新
❗️ 程序复杂，不建议使用
❗️ 经测试无法正常获取数据，需要进一步研究
"""

def _get_finance_stock_list(end_date):
    """
    获取end_date的金融领域上市公司股票代码列表
    """
    # 获取行业板块成分股
    industry_list = ['801190', '801780', '801790']  # 金融服务、银行、非银金融
    all_stocks = []
    
    for industry_code in industry_list:
        stocks = get_industry_stocks(industry_code=industry_code, date=end_date)
        all_stocks.extend(stocks)
    
    # 去重并返回
    stock_list = list(set(all_stocks))
    return stock_list

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

def _get_balance_sheet(code, end_date):
    """
    获取截至end_date的资产负债表，整合多个统计日期为一张表
    """
    # 获取所有季度节点日期
    quarter_dates = get_all_statsDate(end_date)
    
    # 存储所有日期的数据
    all_data = []
    
    print(f"开始获取{code}的资产负债表数据，共{len(quarter_dates)}个季度")
    
    for i, date in enumerate(quarter_dates):
        try:
            # 构建查询对象
            q = query(balance).filter(balance.code == code)
            
            # 获取指定统计日期的数据
            df = get_fundamentals(q, statDate=date)
            
            if not df.empty:
                all_data.append(df)
                print(f"  ✓ {date} 数据获取成功 ({i+1}/{len(quarter_dates)})")
            else:
                print(f"  ✗ {date} 无数据 ({i+1}/{len(quarter_dates)})")
                
        except Exception as e:
            print(f"  ✗ {date} 获取失败: {e} ({i+1}/{len(quarter_dates)})")
    
    # 合并所有数据
    if all_data:
        # 按统计日期排序（最新的在前）
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df = combined_df.sort_values('stat_date', ascending=False)
        
        print(f"获取{code}截至{end_date}的资产负债表，共{len(combined_df)}期数据")
        
        # 保存数据
        balance_dir = os.path.join(get_path('financial_data'), 'balance_sheet')
        os.makedirs(balance_dir, exist_ok=True)
        
        file_path = os.path.join(balance_dir, f"{code}.csv")
        combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"资产负债表数据已保存至: {file_path}")
        
        return combined_df
    else:
        print(f"{code} 无资产负债表数据")
        return pd.DataFrame()

def _get_income_statement(code, end_date):
    """
    获取截至end_date的利润表，整合多个统计日期为一张表
    """
    # 获取所有季度节点日期
    quarter_dates = get_all_statsDate(end_date)
    
    # 存储所有日期的数据
    all_data = []
    
    print(f"开始获取{code}的利润表数据，共{len(quarter_dates)}个季度")
    
    for i, date in enumerate(quarter_dates):
        try:
            # 构建查询对象
            q = query(income).filter(income.code == code)
            
            # 获取指定统计日期的数据
            df = get_fundamentals(q, statDate=date)
            
            if not df.empty:
                all_data.append(df)
                print(f"  ✓ {date} 数据获取成功 ({i+1}/{len(quarter_dates)})")
            else:
                print(f"  ✗ {date} 无数据 ({i+1}/{len(quarter_dates)})")
                
        except Exception as e:
            print(f"  ✗ {date} 获取失败: {e} ({i+1}/{len(quarter_dates)})")
    
    # 合并所有数据
    if all_data:
        # 按统计日期排序（最新的在前）
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df = combined_df.sort_values('stat_date', ascending=False)
        
        print(f"获取{code}截至{end_date}的利润表，共{len(combined_df)}期数据")
        
        # 保存数据
        income_dir = os.path.join(get_path('financial_data'), 'income_statement')
        os.makedirs(income_dir, exist_ok=True)
        
        file_path = os.path.join(income_dir, f"{code}.csv")
        combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"利润表数据已保存至: {file_path}")
        
        return combined_df
    else:
        print(f"{code} 无利润表数据")
        return pd.DataFrame()

def _get_cash_flow(code, end_date):
    """
    获取截至end_date的现金流量表，整合多个统计日期为一张表
    """
    # 获取所有季度节点日期
    quarter_dates = get_all_statsDate(end_date)
    
    # 存储所有日期的数据
    all_data = []
    
    print(f"开始获取{code}的现金流量表数据，共{len(quarter_dates)}个季度")
    
    for i, date in enumerate(quarter_dates):
        try:
            # 构建查询对象
            q = query(cash_flow).filter(cash_flow.code == code)
            
            # 获取指定统计日期的数据
            df = get_fundamentals(q, statDate=date)
            
            if not df.empty:
                all_data.append(df)
                print(f"  ✓ {date} 数据获取成功 ({i+1}/{len(quarter_dates)})")
            else:
                print(f"  ✗ {date} 无数据 ({i+1}/{len(quarter_dates)})")
                
        except Exception as e:
            print(f"  ✗ {date} 获取失败: {e} ({i+1}/{len(quarter_dates)})")
    
    # 合并所有数据
    if all_data:
        # 按统计日期排序（最新的在前）
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df = combined_df.sort_values('stat_date', ascending=False)
        
        print(f"获取{code}截至{end_date}的现金流量表，共{len(combined_df)}期数据")
        
        # 保存数据
        cash_flow_dir = os.path.join(get_path('financial_data'), 'cash_flow')
        os.makedirs(cash_flow_dir, exist_ok=True)
        
        file_path = os.path.join(cash_flow_dir, f"{code}.csv")
        combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"现金流量表数据已保存至: {file_path}")
        
        return combined_df
    else:
        print(f"{code} 无现金流量表数据")
        return pd.DataFrame()

def _get_indicator(code, end_date):
    """
    获取截至end_date的指标数据，整合多个统计日期为一张表
    """
    # 获取所有季度节点日期
    quarter_dates = get_all_statsDate(end_date)
    
    # 存储所有日期的数据
    all_data = []
    
    print(f"开始获取{code}的指标数据，共{len(quarter_dates)}个季度")
    
    for i, date in enumerate(quarter_dates):
        try:
            # 构建查询对象
            q = query(indicator).filter(indicator.code == code)
            
            # 获取指定统计日期的数据
            df = get_fundamentals(q, statDate=date)
            
            if not df.empty:
                all_data.append(df)
                print(f"  ✓ {date} 数据获取成功 ({i+1}/{len(quarter_dates)})")
            else:
                print(f"  ✗ {date} 无数据 ({i+1}/{len(quarter_dates)})")
                
        except Exception as e:
            print(f"  ✗ {date} 获取失败: {e} ({i+1}/{len(quarter_dates)})")
    
    # 合并所有数据
    if all_data:
        # 按统计日期排序（最新的在前）
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df = combined_df.sort_values('stat_date', ascending=False)
        
        print(f"获取{code}截至{end_date}的指标数据，共{len(combined_df)}期数据")
        
        # 保存数据
        indicator_dir = os.path.join(get_path('financial_data'), 'indicator')
        os.makedirs(indicator_dir, exist_ok=True)
        
        file_path = os.path.join(indicator_dir, f"{code}.csv")
        combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"指标数据已保存至: {file_path}")
        
        return combined_df
    else:
        print(f"{code} 无指标数据")
        return pd.DataFrame()

def get_all_financial_data(end_date):
    """
    获取截至end_date的所有非金融上市公司财务数据
    """
    # 获取上市公司股票代码列表
    stock_list = get_stock_list(end_date)
    
    # 获取非金融上市公司股票代码列表
    finance_stock_list = _get_finance_stock_list(end_date)
    non_finance_stock_list = list(set(stock_list) - set(finance_stock_list))
    
    # 获取非金融上市公司财务数据
    # for code in non_finance_stock_list:
    for code in non_finance_stock_list[:10]: # 测试用，只获取前10只股票
        print(f"获取{code}截至{end_date}的财务数据")
        try:
            _get_balance_sheet(code, end_date)
            _get_income_statement(code, end_date)
            _get_cash_flow(code, end_date)
            _get_indicator(code, end_date)
            print(f"{code} 获取财务数据成功")
        except Exception as e:
            print(f"{code} 获取财务数据失败: {e}")

def get_all_financial_data_planb(end_date):
    """
    获取截至end_date的所有上市公司财务数据
    """
    # 获取上市公司股票代码列表
    stock_list = get_stock_list(end_date)
    
    # for code in stock_list:
    for code in stock_list[:10]: # 测试用，只获取前10只股票
        print(f"获取{code}截至{end_date}的财务数据")
        try:
            _get_balance_sheet(code, end_date)
            _get_income_statement(code, end_date)
            _get_cash_flow(code, end_date)
            _get_indicator(code, end_date)
            print(f"{code} 获取财务数据成功")
        except Exception as e:
            print(f"{code} 获取财务数据失败: {e}")

def test_single_stock_financial_data(code, end_date):
    """
    测试单只股票的财务数据获取功能
    """
    print(f"\n=== 测试获取{code}的财务数据 ===")
    
    try:
        # 测试资产负债表
        print("\n--- 资产负债表 ---")
        balance_df = _get_balance_sheet(code, end_date)
        
        # 测试利润表
        print("\n--- 利润表 ---")
        income_df = _get_income_statement(code, end_date)
        
        # 测试现金流量表
        print("\n--- 现金流量表 ---")
        cash_flow_df = _get_cash_flow(code, end_date)
        
        # 测试指标数据
        print("\n--- 指标数据 ---")
        indicator_df = _get_indicator(code, end_date)
        
        # 显示数据概览
        print(f"\n=== 数据概览 ===")
        print(f"资产负债表: {len(balance_df)} 期数据")
        print(f"利润表: {len(income_df)} 期数据")
        print(f"现金流量表: {len(cash_flow_df)} 期数据")
        print(f"指标数据: {len(indicator_df)} 期数据")
        
        return {
            'balance': balance_df,
            'income': income_df,
            'cash_flow': cash_flow_df,
            'indicator': indicator_df
        }
        
    except Exception as e:
        print(f"测试失败: {e}")
        return None

if __name__ == '__main__':
    # 测试获取所有季度节点日期
    print("\n=== 测试获取所有季度节点日期 ===")
    test_end_date = '2025-08-27'
    quarter_dates = get_all_statsDate(test_end_date)
    print(f"从2005年1月1日至{test_end_date}的所有季度节点日期:")
    print(f"共{len(quarter_dates)}个季度")
    print("前5个季度日期:", quarter_dates[:5])
    print("最后5个季度日期:", quarter_dates[-5:])
    
    # 测试单只股票的财务数据获取
    # test_code = '000001.XSHE'  # 平安银行
    test_code = '002371.XSHE'  # 北方华创
    test_single_stock_financial_data(test_code, test_end_date)
    
    # 测试获取所有股票的财务数据（谨慎使用，数据量大）
    end_date = '2025-08-27'
    print("\n=== 获取所有非金融上市公司股票财务数据 ===")
    # get_all_financial_data(end_date)
    print("\n=== 获取所有上市公司股票财务数据 ===")
    # get_all_financial_data_planb(end_date)