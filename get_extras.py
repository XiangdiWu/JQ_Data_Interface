import pandas as pd
import jqdatasdk as jq
import os
from Utils.get_stock_list import get_stock_list
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_is_st(field, start_date, end_date):
    """
    判断多只股票在一段时间是否是ST
    存储方式: 按日期存储
    数据来源: jqdatasdk
    每个交易日使用对应的股票列表，自动处理已退市股票

    参数：
    field: 字段名称
    start_date: 开始日期
    end_date: 结束日期
    """
    # 获取该日期范围内的所有交易日
    from Utils.get_trading_date import get_trading_dates
    trading_dates = get_trading_dates(start_date, end_date)
    
    if not trading_dates:
        print("未找到交易日")
        return
    
    print(f"计划获取 {len(trading_dates)} 个交易日的数据")
    
    # 按日期处理，每个交易日使用对应的股票列表
    all_results = []
    
    for i, trading_date in enumerate(trading_dates):
        print(f"\n=== 处理交易日 {i+1}/{len(trading_dates)}: {trading_date} ===")
        
        # 获取该交易日的股票列表
        stock_list = get_stock_list(trading_date)
        print(f"  获取到 {len(stock_list)} 只股票")
        
        try:
            # 获取该日期的数据（格式：date为索引，stock_code为列）
            date_results = jq.get_extras(field, stock_list, trading_date, trading_date)
            
            if date_results is not None and not date_results.empty:
                # 命名索引
                date_results.index.name = 'date'
                
                # 直接stack：将列索引(stock_code)转换为行索引
                date_results_stacked = date_results.stack().to_frame('is_st')
                
                # 命名双索引
                date_results_stacked.index.names = ['date', 'code']
                
                # 重置索引：将双索引转换为普通列
                date_results_stacked = date_results_stacked.reset_index()
                
                # 确保date列为字符串格式（用于文件名）
                date_results_stacked['date'] = pd.to_datetime(date_results_stacked['date']).dt.strftime('%Y-%m-%d')
                
                all_results.append(date_results_stacked)
                
                print(f"  成功获取 {trading_date} 数据: {len(date_results_stacked)} 条记录")
            else:
                print(f"  {trading_date} 未获取到数据")
                
        except Exception as e:
            print(f"  获取 {trading_date} 数据时出错: {e}")
            continue
    
    if not all_results:
        print("未获取到任何数据")
        return
    
    # 合并所有结果
    results_stacked = pd.concat(all_results, ignore_index=True)
    
    # 创建保存目录
    save_dir = get_path('is_st')
    
    # 6. 按日期分组，分别保存
    for date_value, group in results_stacked.groupby('date'):
        filename = f"{date_value}.csv"
        save_path = os.path.join(save_dir, filename)
        
        # 保存该日期的数据
        group.to_csv(save_path, index=False, encoding='utf-8-sig')
        print(f"{date_value} 数据已保存至: {save_path}")
    
    print(f"\n 所有数据已按日期分组保存，共 {results_stacked['date'].nunique()} 个文件")


if __name__ == "__main__":
    start_date = '2025-08-28'
    end_date = '2025-08-28'
    get_is_st('is_st', start_date, end_date)