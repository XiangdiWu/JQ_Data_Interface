import akshare as ak
import pandas as pd
from datetime import datetime, timedelta
import os
import sys
# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Config.data_path import get_path

def get_bond_zh_rate_last():
    """
    获取最新一日中国国债收益率10年
    """
    save_path = os.path.join(get_path('bond_rate'), 'bond_zh_us_rate.csv')
    if os.path.exists(save_path):
        df = pd.read_csv(save_path)
        if not df.empty and '中国国债收益率10年' in df.columns:
            china_10y_yield = df['中国国债收益率10年'].iloc[-1] # 获取最新一日数据
            print(f"中国国债收益率10年: {china_10y_yield}%")
            if isinstance(china_10y_yield, str):
                china_10y_yield = float(china_10y_yield)
            return china_10y_yield
        else:
            print("未找到中国国债收益率10年数据")
    else:
        print(f"数据文件不存在: {save_path}")

if __name__ == "__main__":
    df = get_bond_zh_rate_last()
    print(df)