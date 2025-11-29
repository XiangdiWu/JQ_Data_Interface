import jqdatasdk as jq
import pandas as pd
import os
from Utils.get_stock_list import get_stock_list
from Utils.get_trading_date import get_trading_dates
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_factor_list():
    """
    获取聚宽因子库中所有因子的信息
    """
    factors = jq.get_all_factors()
    print(f"获取到 {len(factors)} 个因子")
    
    # 保存因子列表
    save_dir = get_path('factor_list')
    filename = "all_factors.csv"
    save_path = os.path.join(save_dir, filename)
    
    # 将因子列表转换为DataFrame并保存
    if isinstance(factors, list):
        df = pd.DataFrame({'factor_name': factors})
    else:
        df = pd.DataFrame(factors)
    
    df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"因子列表已保存至: {save_path}")
    
    return factors

def get_jq_factors(factors, start_date=None, end_date=None, count=None):
    """
    获取质量因子、基础因子、情绪因子、成长因子、风险因子、每股因子等数百个因子数据
    每个交易日使用对应的股票列表，自动处理已退市股票

    参数
    factors: 因子名称，单个因子（字符串）或一个因子列表
    start_date:开始日期，字符串或 datetime 对象，与 count参数二选一
    end_date: 结束日期， 字符串或 datetime 对象，可以与 start_date 或 count 配合使用
    count: 截止 end_date 之前交易日的数量（含 end_date 当日），与 start_date 参数二选一
    """
    
    # 获取交易日列表
    if count is not None:
        # 使用count时，获取最近的count个交易日
        trading_dates = get_trading_dates(end_date, count=count)
    else:
        # 使用日期范围时，获取start_date到end_date的交易日
        trading_dates = get_trading_dates(start_date, end_date)
    
    if not trading_dates:
        print("未找到交易日")
        return pd.DataFrame()
    
    print(f"计划获取 {len(trading_dates)} 个交易日的因子数据")
    
    # 创建保存目录
    save_dir = get_path('factor_data')
    
    # 按日期处理，每个交易日使用对应的股票列表
    all_results = []
    
    for i, trading_date in enumerate(trading_dates):
        print(f"\n=== 处理交易日 {i+1}/{len(trading_dates)}: {trading_date} ===")
        
        # 获取该交易日的股票列表
        securities = get_stock_list(trading_date)
        print(f"  获取到 {len(securities)} 只股票")
        
        try:
            # 获取该日期的因子数据
            date_results = jq.get_factor_values(securities, factors, trading_date, trading_date, count=None)
            
            if date_results is not None and not date_results.empty:
                # 处理数据格式
                if isinstance(date_results, pd.DataFrame):
                    # 确保有日期列
                    if 'date' not in date_results.columns:
                        date_results = date_results.reset_index()
                        if 'time' in date_results.columns:
                            date_results = date_results.rename(columns={'time': 'date'})
                        elif 'index' in date_results.columns:
                            date_results = date_results.rename(columns={'index': 'date'})
                    
                    # 确保date列为字符串格式（用于文件名）
                    date_results['date'] = pd.to_datetime(date_results['date']).dt.strftime('%Y-%m-%d')
                    
                    all_results.append(date_results)
                    
                    day_records = len(date_results)
                    day_stocks = date_results['code'].nunique() if 'code' in date_results.columns else 0
                    
                    print(f"  成功获取 {trading_date} 因子数据: {day_records} 条记录，{day_stocks} 只股票")
                else:
                    print(f"  {trading_date} 数据格式异常: {type(date_results)}")
            else:
                print(f"  {trading_date} 未获取到因子数据")
                
        except Exception as e:
            print(f"  获取 {trading_date} 因子数据时出错: {e}")
            continue
    
    if not all_results:
        print("未获取到任何因子数据")
        return pd.DataFrame()
    
    # 合并所有结果
    results = pd.concat(all_results, ignore_index=True)
    
    # 按日期分组，分别保存
    for date_value, group in results.groupby('date'):
        # 生成文件名：2024-08-21.csv
        filename = f"{date_value}.csv"
        save_path = os.path.join(save_dir, filename)
        
        # 保存该日期的数据（不包含索引）
        group.to_csv(save_path, index=False, encoding='utf-8-sig')
        print(f"{date_value} 因子数据已保存至: {save_path} (共 {len(group)} 行)")
    
    print(f"所有因子数据已按日期分组保存，共 {results['date'].nunique()} 个文件")
    
    return results


def get_jq_factors_kanban():
    df = jq.get_factor_kanban_values(
        universe='hs300',
        bt_cycle='month_3',
        model='long_only',
        category=['quality','basics','emotion','growth','risk','pershare'],
        skip_paused=False,
        commision_slippage=0
        )
    print(df)


if __name__ == "__main__":
    # 获取因子列表
    factors = get_factor_list()
    
    # 示例因子（可以修改为需要的因子）
    sample_factors = ['market_cap', 'pe_ratio', 'pb_ratio', 'roe', 'roa'] if isinstance(factors, list) else factors[:5]
    
    print(f"\n使用示例因子: {sample_factors}")
    
    # 示例1: 使用日期范围获取
    print("\n示例1: 使用日期范围获取因子数据")
    start_date = '2025-06-22'
    end_date = '2025-06-30'
    # result1 = get_jq_factors(sample_factors, start_date=start_date, end_date=end_date, count=None)
    
    # 示例2: 使用count获取最近N个交易日
    print("\n示例2: 使用count获取最近5个交易日的因子数据")
    count = 5
    end_date = '2025-06-30'
    # result2 = get_jq_factors(sample_factors, end_date=end_date, count=count)
    
    print("\n请取消注释相应的示例代码来运行测试")