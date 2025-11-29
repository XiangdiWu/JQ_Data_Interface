import pandas as pd
import jqdatasdk as jq
import os
from Utils.get_stock_list import get_stock_list
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_mtss_info(start_date, end_date, fields):
    """
    获取多只股票在一个时间段内的融资融券信息，并按日期分别存储
    数据来源: jqdatasdk
    每个交易日使用对应的股票列表，自动处理已退市股票

    参数：
    start_date: 开始日期
    end_date: 结束日期
    fields: 字段列表
    """
    # 获取该日期范围内的所有交易日
    from Utils.get_trading_date import get_trading_dates
    trading_dates = get_trading_dates(start_date, end_date)
    
    if not trading_dates:
        print("未找到交易日")
        return pd.DataFrame()
    
    print(f"计划获取 {len(trading_dates)} 个交易日的数据")
    
    # 创建保存目录
    save_dir = get_path('mtss_info')
    
    # 按日期处理，每个交易日使用对应的股票列表
    all_results = []
    
    for i, trading_date in enumerate(trading_dates):
        print(f"\n=== 处理交易日 {i+1}/{len(trading_dates)}: {trading_date} ===")
        
        # 获取该交易日的股票列表
        stock_list = get_stock_list(trading_date)
        print(f"  获取到 {len(stock_list)} 只股票")
        
        try:
            # 获取该日期的数据
            date_results = jq.get_mtss(stock_list, trading_date, trading_date, fields)
            
            if date_results is not None and not date_results.empty:
                # 确保date列存在且格式正确
                if 'date' not in date_results.columns:
                    raise ValueError("数据中未找到 'date' 列")
                
                # 将date列转换为字符串格式（用于文件名）
                date_results['date'] = pd.to_datetime(date_results['date']).dt.strftime('%Y-%m-%d')
                
                all_results.append(date_results)
                
                print(f"  成功获取 {trading_date} 数据: {len(date_results)} 条记录")
            else:
                print(f"  {trading_date} 未获取到数据")
                
        except Exception as e:
            print(f"  获取 {trading_date} 数据时出错: {e}")
            continue
    
    if not all_results:
        print("未获取到任何数据")
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
        print(f"{date_value} 数据已保存至: {save_path} (共 {len(group)} 行)")
    
    print(f"所有数据已按日期分组保存，共 {results['date'].nunique()} 个文件")
    
    return results

def get_mtss_info_by_date(date):
    """
    获取融资融券标的列表
    数据来源: jqdatasdk
    参数：
    date: 日期, 默认为None,不指定时返回上交所、深交所最近一次披露的的可融资标的列表的list
    """
    # 获取融资标的列表，并赋值给 margincash_stocks
    margincash_stocks = jq.get_margincash_stocks(date)
    print(margincash_stocks)

    # 获取融券标的列表，并赋值给 marginsec_stocks
    marginsec_stocks= jq.get_marginsec_stocks(date)
    print(marginsec_stocks)
    """
    获取融资融券信息，只需要一种方法，因此未处理后续存储
    """

if __name__ == "__main__":
    start_date = '2025-08-27'
    end_date = '2025-08-27'
    df = get_mtss_info(start_date, end_date, fields=None)

    # 查看前几行
    print("\n数据预览:")
    print(df.head())

    # 判断平安银行是否在可融资列表
    # result = '000001.XSHE' in jq.get_margincash_stocks(date='2018-07-02')
    # print(result)

    # 判断平安银行是否在可融券列表
    # result = '000001.XSHE' in get_marginsec_stocks(date='2018-07-05')
    # print(result)