from jqdatasdk import *
from Config.config import JQ_USERNAME, JQ_PASSWORD
auth(JQ_USERNAME, JQ_PASSWORD)
from Config.data_path import get_path
from Config.fields_config import get_fields
import pandas as pd
import os

"""
获取银行、券商、保险公司财务指标数据
数据来源: jqdatasdk
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

class PlanTwo:
    def _get_bank_indicator_annual(code, end_date, count=None):
        """
        获取截至end_date的银行财务指标数据
        """
        # 使用统一的字段配置
        fields = get_fields('bank_indicator_annual')
        
        try:
            print(f"开始获取{code}的银行财务指标数据")

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
                print(f"成功获取{code}的银行财务指标数据，共{len(df)}期")
                
                # 保存数据
                bank_indicator_dir = os.path.join(get_path('financial_data'), 'bank_indicator_annual')
                os.makedirs(bank_indicator_dir, exist_ok=True)
                file_path = os.path.join(bank_indicator_dir, f"{code}.csv")
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
                print(f"银行财务指标数据已保存至: {file_path}")
                
                return df
            else:
                print(f"{code} 无银行财务指标数据")
                return pd.DataFrame()
                
        except Exception as e:
            print(f"获取{code}银行财务指标数据失败: {e}")
            return pd.DataFrame()

    def _get_security_indicator_annual(code, end_date, count=None):
        """
        获取截至end_date的券商财务指标数据
        """
        # 使用统一的字段配置
        fields = get_fields('security_indicator_annual')
        
        try:
            print(f"开始获取{code}的券商财务指标数据")

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
                print(f"成功获取{code}的券商财务指标数据，共{len(df)}期")
                
                # 保存数据
                security_indicator_dir = os.path.join(get_path('financial_data'), 'security_indicator_annual')
                os.makedirs(security_indicator_dir, exist_ok=True)
                file_path = os.path.join(security_indicator_dir, f"{code}.csv")
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
                print(f"券商财务指标数据已保存至: {file_path}")
                
                return df
            else:
                print(f"{code} 无券商财务指标数据")
                return pd.DataFrame()
                
        except Exception as e:
            print(f"获取{code}券商财务指标数据失败: {e}")
            return pd.DataFrame()

    def _get_insurance_indicator_annual(code, end_date, count=None):
        """
        获取截至end_date的保险财务指标数据
        """
        # 使用统一的字段配置
        fields = get_fields('insurance_indicator_annual')
        
        try:
            print(f"开始获取{code}的保险财务指标数据")

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
                print(f"成功获取{code}的保险财务指标数据，共{len(df)}期")
                
                # 保存数据
                insurance_indicator_dir = os.path.join(get_path('financial_data'), 'insurance_indicator_annual')
                os.makedirs(insurance_indicator_dir, exist_ok=True)
                file_path = os.path.join(insurance_indicator_dir, f"{code}.csv")
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
                print(f"保险财务指标数据已保存至: {file_path}")
                
                return df
            else:
                print(f"{code} 无保险财务指标数据")
                return pd.DataFrame()
                
        except Exception as e:
            print(f"获取{code}保险财务指标数据失败: {e}")
            return pd.DataFrame()

    def _get_finance_stock_list(end_date):
        """
        获取end_date的银行、券商、保险上市公司股票代码列表
        """
        bank_stock_list = get_industry_stocks(industry_code='801780', date=end_date)
        print(bank_stock_list[:5])
        security_stock_list = get_industry_stocks(industry_code='801193', date=end_date)
        print(security_stock_list[:5])
        insurance_stock_list = get_industry_stocks(industry_code='801194', date=end_date)
        print(insurance_stock_list[:5])
        return bank_stock_list, security_stock_list, insurance_stock_list

    def get_finance_stock_indicator(end_date):
        bank_stock_list, security_stock_list, insurance_stock_list = _get_finance_stock_list(end_date)
        # 获取银行、券商、保险上市公司财务指标数据
        for code in bank_stock_list:
            _get_bank_indicator_annual(code, end_date, count=None)
        for code in security_stock_list:
            _get_security_indicator_annual(code, end_date, count=None)
        for code in insurance_stock_list:
            _get_insurance_indicator_annual(code, end_date, count=None)

if __name__ == '__main__':
    end_date = '2025-08-27'

    # 测试获取单只银行的财务指标数据
    print("\n=== 测试获取单只银行的财务指标数据 ===")
    code = normalize_code('601398')
    PlanTwo._get_bank_indicator_annual(code, end_date, count=None)
    code = normalize_code('002926')
    PlanTwo._get_security_indicator_annual(code, end_date, count=None)
    code = normalize_code('601336')
    PlanTwo._get_insurance_indicator_annual(code, end_date, count=None)

    # 测试获取某年全部保险公司的财务指标数据
    print("\n=== 测试获取某年全部保险公司的财务指标数据 ===")
    df = get_fundamentals(query(insurance_indicator),statDate=2024)
    print(df)