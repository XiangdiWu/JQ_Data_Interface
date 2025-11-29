import pandas as pd
import jqdatasdk as jq
import os
from Utils.get_stock_list import get_stock_list
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_stock_concept(date):
    """
    获取股票所属概念
    存储方式: 按日期存储
    数据来源: jqdatasdk
    使用指定日期对应的股票列表，自动处理已退市股票
    
    参数：
    date: 日期，默认为None
    回测模块: 默认值会随着回测日期变化而变化, 等于context.current_dt
    研究模块: 默认是今天
    """
    # 获取该日期的股票列表
    stock_list = get_stock_list(date)
    print(f"获取到 {len(stock_list)} 只股票")
    
    concept_dict = jq.get_concept(security=stock_list, date=date)
    print("原始数据:")
    print(concept_dict)
    print()

    # 将字典转换为DataFrame
    data_rows = []
    for stock_code, concepts in concept_dict.items():
        for concept_name in concepts:
            row = {
                'stock_code': stock_code,
                'concept_name': concept_name
            }
            data_rows.append(row)
    
    df = pd.DataFrame(data_rows)
    
    print("转换后的DataFrame:")
    print(df.head(10))
    print()

    # 创建保存目录
    save_dir = get_path('stock_concept')
    
    # 生成文件名
    filename = f"{date}.csv"
    save_path = os.path.join(save_dir, filename)
    
    # 保存为 CSV 文件
    df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"股票所属概念列表已保存至: {save_path}")
    print()  # 空行分隔

if __name__ == "__main__":
    date = '2025-08-27'
    get_stock_concept(date)