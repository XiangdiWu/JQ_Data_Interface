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

用finance.run_query方法获取金融领域上市公司财务数据(按报告期)
测试结果: 已通过

用finance.run_query的方法获取非金融领域上市公司财务数据(按报告期)
测试结果: 权限未明确

实际使用时，需要替换代码中的测试代码， 目前获取的是列表前10个公司的财务数据
"""

def _get_finance_company_balance_sheet(code, end_date):
    """
    获取截至end_date的金融领域上市公司各报告期资产负债表
    """
    q=query(finance.FINANCE_BALANCE_SHEET_PARENT).filter(
        finance.FINANCE_BALANCE_SHEET_PARENT.code==code,
        finance.FINANCE_BALANCE_SHEET_PARENT.pub_date<=end_date,  #指定发布日期<=2019-04-27
        finance.FINANCE_BALANCE_SHEET_PARENT.report_type==0  #指定为本期
            ).order_by(
        finance.FINANCE_BALANCE_SHEET_PARENT.pub_date.desc(),  #先用pub_date排序
        finance.FINANCE_BALANCE_SHEET_PARENT.end_date.desc()   #再也end_date排序(同一天可能发布多个季度的数据)
            )
    df=finance.run_query(q)
    print(f"获取{code}截至{end_date}的资产负债表")
    
    # 保存数据
    if not df.empty:
        # 创建资产负债表目录
        balance_dir = os.path.join(get_path('financial_data'), 'finance_balance_sheet')
        os.makedirs(balance_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(balance_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"资产负债表数据已保存至: {file_path}")
    else:
        print(f"{code} 无资产负债表数据")
    
def _get_finance_company_income_statement(code, end_date):
    """
    获取截至end_date的金融领域上市公司各报告期利润表
    """
    q=query(finance.STK_INCOME_STATEMENT).filter(
        finance.STK_INCOME_STATEMENT.code==code,
        finance.STK_INCOME_STATEMENT.pub_date<=end_date,  #指定发布日期<=2019-04-27
        finance.STK_INCOME_STATEMENT.report_type==0  #指定为本期
            ).order_by(
        finance.STK_INCOME_STATEMENT.pub_date.desc(),  #先用pub_date排序
        finance.STK_INCOME_STATEMENT.end_date.desc()   #再也end_date排序(同一天可能发布多个季度的数据)
            )
    df=finance.run_query(q)
    print(f"获取{code}截至{end_date}的利润表")
    
    # 保存数据
    if not df.empty:
        # 创建利润表目录
        income_dir = os.path.join(get_path('financial_data'), 'finance_income_statement')
        os.makedirs(income_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(income_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"利润表数据已保存至: {file_path}")
    else:
        print(f"{code} 无利润表数据")

def _get_finance_company_cash_flow(code, end_date):
    """
    获取截至end_date的金融领域上市公司各报告期现金流量表
    """
    q=query(finance.FINANCE_CASHFLOW_STATEMENT).filter(
        finance.FINANCE_CASHFLOW_STATEMENT.code==code,
        finance.FINANCE_CASHFLOW_STATEMENT.pub_date<=end_date,  #指定发布日期<=2019-04-27
        finance.FINANCE_CASHFLOW_STATEMENT.report_type==0  #指定为本期
            ).order_by(
        finance.FINANCE_CASHFLOW_STATEMENT.pub_date.desc(),  #先用pub_date排序
        finance.FINANCE_CASHFLOW_STATEMENT.end_date.desc()   #再也end_date排序(同一天可能发布多个季度的数据)
            )
    df=finance.run_query(q)
    print(f"获取{code}截至{end_date}的现金流量表")
    
    # 保存数据
    if not df.empty:
        # 创建现金流量表目录
        cash_flow_dir = os.path.join(get_path('financial_data'), 'finance_cash_flow')
        os.makedirs(cash_flow_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(cash_flow_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"现金流量表数据已保存至: {file_path}")
    else:
        print(f"{code} 无现金流量表数据")

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

def get_all_finance_company_data(end_date):
    """
    获取截至end_date的金融领域上市公司各报告期财务数据
    """
    stock_list = _get_finance_stock_list(end_date)
    print(f"获取到 {len(stock_list)} 只股票")
    
    # for code in stock_list:
    for code in stock_list[:10]: # 测试用，只获取前10只股票
        print(f"\n=== 获取{code}截至{end_date}的财务数据 ===")
        try:
            _get_finance_company_balance_sheet(code, end_date)
            _get_finance_company_income_statement(code, end_date)
            _get_finance_company_cash_flow(code, end_date)

        except Exception as e:
            print(f"获取{code}财务数据时出错: {e}")
            continue
    
    print(f"\n获取金融领域所有股票截至{end_date}的财务数据完成")

def _get_balance_sheet(code, end_date):
    """
    获取截至end_date的资产负债表
    """
    q = query(balance).filter(
        balance.code == code,
        balance.pubDate <= end_date,
    ).order_by(
        balance.pubDate.desc(),
        balance.statDate.desc()
    )
    df = finance.run_query(q)
    print(f"获取{code}截至{end_date}的资产负债表")
    
    # 保存数据
    if not df.empty:
        # 创建资产负债表目录
        balance_dir = os.path.join(get_path('financial_data'), 'balance_sheet')
        os.makedirs(balance_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(balance_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"资产负债表数据已保存至: {file_path}")
    else:
        print(f"{code} 无资产负债表数据")

def _get_income_statement(code, end_date):
    """
    获取截至end_date的利润表
    """
    q = query(income).filter(
        income.code == code,
        income.pubDate <= end_date,
    ).order_by(
        income.pubDate.desc(),
        income.statDate.desc()
    )
    df = finance.run_query(q)
    print(f"获取{code}截至{end_date}的利润表")
    
    # 保存数据
    if not df.empty:
        # 创建利润表目录
        income_dir = os.path.join(get_path('financial_data'), 'income_statement')
        os.makedirs(income_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(income_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"利润表数据已保存至: {file_path}")
    else:
        print(f"{code} 无利润表数据")

def _get_cash_flow(code, end_date):
    """
    获取截至end_date的现金流量表
    """
    q = query(cash_flow).filter(
        cash_flow.code == code,
        cash_flow.pubDate <= end_date,
    ).order_by(
        cash_flow.pubDate.desc(),
        cash_flow.statDate.desc()
    )
    df = finance.run_query(q)
    print(f"获取{code}截至{end_date}的现金流量表")
    
    # 保存数据
    if not df.empty:
        # 创建现金流量表目录
        cash_flow_dir = os.path.join(get_path('financial_data'), 'cash_flow')
        os.makedirs(cash_flow_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(cash_flow_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"现金流量表数据已保存至: {file_path}")
    else:
        print(f"{code} 无现金流量表数据")

def _get_indicator(code, end_date):
    """
    获取截至end_date的指标数据
    """
    q = query(indicator).filter(
        indicator.code == code,
        indicator.pubDate <= end_date,
    ).order_by(
        indicator.pubDate.desc(),
        indicator.statDate.desc()
    )
    df = finance.run_query(q)
    print(f"获取{code}截至{end_date}的指标数据")
    
    # 保存数据
    if not df.empty:
        # 创建指标数据目录
        indicator_dir = os.path.join(get_path('financial_data'), 'indicator')
        os.makedirs(indicator_dir, exist_ok=True)
        
        # 按股票代码保存
        file_path = os.path.join(indicator_dir, f"{code}.csv")
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"指标数据已保存至: {file_path}")
    else:
        print(f"{code} 无指标数据")

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

def example_query(code, statDate):
    """
    查询平安银行2024年的年报
    查询项目: 年报日期、股票代码、基本每股收益、销售商品提供劳务收到的现金
    过滤条件: 股票代码为000001.XSHE
    """
    q = query(
            income.statDate,
            income.code,
            income.basic_eps,
            cash_flow.goods_sale_and_service_render_cash
        ).filter(
            income.code == code,
        )
    result = get_fundamentals(q, statDate) 
    print("查询平安银行2024年的年报")
    print("查询项目: 年报日期、股票代码、基本每股收益、销售商品提供劳务收到的现金")
    print(result)

if __name__ == '__main__':
    # 测试获取所有股票的财务数据（谨慎使用，数据量大）
    end_date = '2025-08-27'
    print("\n=== 获取所有金融上市公司股票财务数据 ===")
    # get_all_finance_company_data(end_date)
    print("\n=== 获取所有非金融上市公司股票财务数据 ===")
    get_all_financial_data(end_date)
    
    # 示例查询（指定股票代码和统计时间）
    code = '000001.XSHE'
    statDate='2024' # statDate='2024q1'则可查询季度数据
    # example_query(code, statDate)