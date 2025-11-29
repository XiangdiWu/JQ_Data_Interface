import pandas as pd
import jqdatasdk as jq
import os
from Config.config import JQ_USERNAME, JQ_PASSWORD
from Config.index_config import INDEX_SYMBOL_LIST, INDUSTRY_INDEX_SYMBOL_LIST, CONCEPT_INDEX_SYMBOL_LIST
from Config.data_path import get_path

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_all_index_stocks(index_symbol_list, date):
    """
    获取指数成分股列表
    存储方式: 按日期存储
    数据来源: jqdatasdk
    
    参数：
    index_symbol: 指数代码
    date: 日期，默认为None
    回测模块: 默认值会随着回测日期变化而变化, 等于context.current_dt
    研究模块: 默认是今天
    """
    for index_symbol in index_symbol_list:
        # 获取指数成分股列表（返回的是股票代码列表）
        stock_list = jq.get_index_stocks(index_symbol, date)
        _data_to_csv(stock_list, index_symbol, date)

def get_all_industry_stocks(industry_code_list, date):
    # 获取行业板块成分股
    for industry_code in industry_code_list:
        stock_list = jq.get_industry_stocks(industry_code, date)
        _data_to_csv(stock_list, industry_code, date)

def get_all_concept_stocks(concept_code_list, date):
    # 获取概念板块成分股
    for concept_code in concept_code_list:
        stock_list = jq.get_concept_stocks(concept_code, date)
        _data_to_csv(stock_list, concept_code, date)

def _data_to_csv(stock_list, symbol, date):
    """
    将数据保存为CSV文件
    """
        # 将股票代码列表转换为DataFrame
    df = pd.DataFrame({'code': stock_list})
    
    # 显示前5行
    print(f"{symbol} 指数成分股前5个:")
    print(df.head(5))

    # 创建保存目录
    save_dir = get_path('index_stocks')

    # 生成文件名
    filename = f"{symbol}_{date}.csv"
    save_path = os.path.join(save_dir, filename)

    # 保存为 CSV 文件
    df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"{symbol} 指数成分股列表已保存至: {save_path}")
    print()  # 空行分隔

if __name__ == "__main__":
    date = '2025-08-27'
    index_symbol_list = ['000001.XSHG']
    industry_code_list = ['801120']
    concept_code_list = ['GN036']
    # get_all_index_stocks(index_symbol_list, date)
    # get_all_industry_stocks(industry_code_list, date)
    get_all_concept_stocks(concept_code_list, date)

    # get_all_index_stocks(INDEX_SYMBOL_LIST, date)
    # get_all_industry_stocks(INDUSTRY_INDEX_SYMBOL_LIST, date)
    # get_all_concept_stocks(CONCEPT_INDEX_SYMBOL_LIST, date)

