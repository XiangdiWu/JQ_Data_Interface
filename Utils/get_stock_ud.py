import pandas as pd
import os
import sys

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Config.data_path import get_path
from Utils.get_trading_date import get_trading_dates

def get_stock_ud(start_date=None, end_date=None, count=None):
    """
    判断股票涨跌停情况
    如果high=high_limit，说明当天存在涨停的情况，zt=1
    如果low=low_limit，说明当天存在跌停的情况，dt=1
    
    参数：
    start_date: 开始日期（与count二选一）
    end_date: 结束日期（可选，当使用count时作为结束日期）
    count: 查询交易日天数，表示获取end_date之前几个交易日的数据（与start_date二选一）
    
    Returns:
        dict: 按日期分组的数据字典 {date: DataFrame}
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
        return {}
    
    print(f"计划处理 {len(trading_dates)} 个交易日的涨跌停数据")
    
    # 创建保存目录
    save_dir = get_path('stock_ud')
    
    # 按日期处理
    daily_data_dict = {}
    processed_days = []
    
    for i, trading_date in enumerate(trading_dates):
        print(f"\n=== 处理交易日 {i+1}/{len(trading_dates)}: {trading_date} ===")
        
        try:
            # 读取价格数据文件
            price_file = os.path.join(get_path('stock_price_old'), f"{trading_date}.csv")
            
            if not os.path.exists(price_file):
                print(f"  价格数据文件不存在: {price_file}")
                continue
            
            # 读取价格数据
            df = pd.read_csv(price_file)
            
            if df.empty:
                print(f"  {trading_date} 价格数据为空")
                continue
            
            # 初始化结果DataFrame
            result_df = pd.DataFrame(columns=['date', 'code', 'zt', 'dt'])
            
            # 处理每只股票
            for _, row in df.iterrows():
                code = row['code']
                high = row['high']
                low = row['low']
                high_limit = row['high_limit']
                low_limit = row['low_limit']
                
                # 检查数据是否有效
                if pd.isna(high) or pd.isna(low) or pd.isna(high_limit) or pd.isna(low_limit):
                    continue
                
                # 判断涨跌停
                zt = 1 if abs(high - high_limit) < 1e-6 else 0  # 涨停
                dt = 1 if abs(low - low_limit) < 1e-6 else 0    # 跌停
                
                # 添加到结果
                result_row = {
                    'date': trading_date,
                    'code': code,
                    'zt': zt,
                    'dt': dt
                }
                result_df = pd.concat([result_df, pd.DataFrame([result_row])], ignore_index=True)
            
            if not result_df.empty:
                # 保存结果
                save_path = os.path.join(save_dir, f"{trading_date}.csv")
                result_df.to_csv(save_path, index=False, encoding='utf-8-sig')
                
                # 统计涨跌停情况
                zt_count = result_df['zt'].sum()
                dt_count = result_df['dt'].sum()
                total_stocks = len(result_df)
                
                print(f"  成功处理 {trading_date} 数据: {total_stocks} 只股票")
                print(f"  涨停股票: {zt_count} 只 ({zt_count/total_stocks*100:.1f}%)")
                print(f"  跌停股票: {dt_count} 只 ({dt_count/total_stocks*100:.1f}%)")
                print(f"  数据已保存至: {save_path}")
                
                # 保存到字典
                daily_data_dict[trading_date] = result_df
                processed_days.append(trading_date)
            else:
                print(f"  {trading_date} 未获取到有效数据")
                
        except Exception as e:
            print(f"  处理 {trading_date} 数据时出错: {e}")
            continue
    
    # 输出汇总信息
    print(f"\n=== 涨跌停数据处理汇总 ===")
    print(f"计划处理: {len(trading_dates)} 个交易日")
    print(f"成功处理: {len(processed_days)} 个交易日")
    print(f"完成日期: {processed_days}")
    
    # 统计总体涨跌停情况
    if daily_data_dict:
        total_records = sum(len(df) for df in daily_data_dict.values())
        total_zt = sum(df['zt'].sum() for df in daily_data_dict.values())
        total_dt = sum(df['dt'].sum() for df in daily_data_dict.values())
        
        print(f"总记录数: {total_records}")
        print(f"总涨停次数: {total_zt}")
        print(f"总跌停次数: {total_dt}")
        print(f"涨停比例: {total_zt/total_records*100:.2f}%")
        print(f"跌停比例: {total_dt/total_records*100:.2f}%")
    
    return daily_data_dict

def get_stock_ud_by_date(date):
    """
    获取指定日期的涨跌停数据
    
    参数：
    date: 日期字符串，格式为 'YYYY-MM-DD'
    
    Returns:
        DataFrame: 涨跌停数据，包含列：date, code, zt, dt
    """
    return get_stock_ud(start_date=date, end_date=date)

if __name__ == "__main__":
    # 示例1: 使用日期范围处理
    print("=== 示例1: 使用日期范围处理涨跌停数据 ===")
    start_date = '2024-08-21'
    end_date = '2024-08-23'
    result1 = get_stock_ud(start_date=start_date, end_date=end_date)
    
    # 示例2: 使用count处理最近N个交易日
    print("\n=== 示例2: 使用count处理最近3个交易日的涨跌停数据 ===")
    count = 3
    # result2 = get_stock_ud(count=count)
    
    # 示例3: 处理单个交易日
    print("\n=== 示例3: 处理单个交易日的涨跌停数据 ===")
    date = '2024-08-21'
    # result3 = get_stock_ud_by_date(date)
    
    print("\n请取消注释相应的示例代码来运行测试")