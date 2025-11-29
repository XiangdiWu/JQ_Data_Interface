# JQData 财务数据获取系统

基于 JoinQuant API 的金融数据获取、存储和管理系统。提供完整的A股市场数据获取解决方案，包括股票行情、财务报表、估值指标、资金流向等多维度数据。

## 📋 项目概述

本项目旨在构建一个完整的金融数据获取和管理系统，通过 JoinQuant API 获取A股市场的各类数据，并按照规范的目录结构进行本地存储。系统支持增量更新、数据去重、异常处理等功能，适用于量化研究、投资分析等场景。

## 🗂️ 项目结构

```
JQ/
├── Config/                    # 配置文件
│   ├── config.py            # JoinQuant认证配置
│   ├── data_path.py         # 数据存储路径配置
│   └── index_config.py      # 指数配置
├── Database/                 # 数据存储目录
│   ├── all_trading_days.csv # 交易日历
│   ├── stock_price/         # 股票行情数据
│   ├── stock_valuation/     # 估值数据
│   ├── financial_data/      # 财务报表数据
│   │   ├── balance_sheet/   # 资产负债表
│   │   ├── income_statement/ # 利润表
│   │   └── cash_flow/       # 现金流量表
│   ├── dividend/            # 分红送股数据
│   ├── money_flow/          # 资金流向数据
│   └── ...                  # 其他数据目录
├── Utils/                    # 工具模块
│   ├── get_stock_list.py    # 获取股票列表
│   ├── get_trading_date.py  # 交易日工具
│   └── get_stock_ud.py      # 涨跌停状态
├── Financial/                # 财务数据分析
├── auth.py                   # 用户认证
├── get_price.py             # 获取股票行情
├── get_valuation.py         # 获取估值数据
├── get_dividend_new.py      # 获取分红数据
├── get_money_flow.py        # 获取资金流向
├── financial_query.py       # 财务报表查询
└── README.md                # 项目说明
```

## 🚀 快速开始

### 环境要求

- Python 3.7+
- JoinQuant 账户
- 必要的Python包：pandas, jqdatasdk

### 安装依赖

```bash
pip install pandas jqdatasdk
```

### 配置认证

1. 编辑 `Config/config.py` 文件，填入您的 JoinQuant 账户信息：

```python
# JQData认证配置
JQ_USERNAME = 'your_username'
JQ_PASSWORD = 'your_password'
```

2. 运行认证测试：

```python
python auth.py
```

### 基本使用

#### 获取股票行情数据

```python
from get_price import get_price_data

# 获取指定日期的股票行情
date = '2025-08-27'
get_price_data(date)
```

#### 获取财务报表数据

```python
from financial_query import get_all_finance_company_data

# 获取金融公司财务数据
end_date = '2025-08-27'
get_all_finance_company_data(end_date)
```

#### 获取分红数据

```python
from get_dividend_new import get_dividend_data

# 获取分红数据（支持增量更新）
get_dividend_data()
```

## 📊 功能模块

### 1. 基础数据模块

- **交易日历**: `all_trading_days.py` - 获取A股交易日历
- **证券信息**: `get_all_securities.py` - 获取股票上市/退市信息
- **股票列表**: `Utils/get_stock_list.py` - 获取指定日期的股票列表

### 2. 行情数据模块

- **股票行情**: `get_price.py` - 获取日线行情数据
- **估值指标**: `get_valuation.py` - 获取PE、PB等估值指标
- **资金流向**: `get_money_flow.py` - 获取资金流向数据
- **涨跌停状态**: `Utils/get_stock_ud.py` - 获取涨跌停和停牌信息

### 3. 财务数据模块

- **财务报表**: `financial_query.py` - 获取资产负债表、利润表、现金流量表
- **分红送股**: `get_dividend_new.py` - 获取分红送股信息（支持增量更新）
- **融资融券**: `get_mtss.py` - 获取融资融券数据

### 4. 行业概念模块

- **行业分类**: `get_stock_industry.py` - 获取股票行业分类
- **概念板块**: `get_stock_concept.py` - 获取股票概念分类
- **指数成分**: `get_index_stocks.py` - 获取指数成分股

### 5. 工具模块

- **交易日工具**: `Utils/get_trading_date.py` - 交易日相关工具函数
- **债券数据**: `bond_zh_us_rate.py` - 中美国债收益率

## 📁 数据存储规范

### 目录结构

- **按数据类型分类**: 不同类型数据存储在不同目录
- **按日期组织**: 日度数据按日期存储，文件名格式为 `YYYY-MM-DD.csv`
- **按代码组织**: 财务数据按股票代码存储，文件名格式为 `{code}.csv`

### 文件格式

- **编码**: UTF-8-SIG（支持中文）
- **格式**: CSV（逗号分隔）
- **索引**: 不包含DataFrame索引列

### 示例文件路径

```
Database/stock_price/2025-08-27.csv          # 指定日期行情数据
Database/stock_valuation/2025-08-27.csv     # 指定日期估值数据
Database/financial_data/balance_sheet/000001.XSHE.csv  # 平安银行资产负债表
Database/dividend/000001.XSHE.csv            # 平安银行分红数据
```

## ⚙️ 配置说明

### 数据路径配置

`Config/data_path.py` 定义了各类数据的存储路径：

```python
def get_path(data_type):
    paths = {
        'stock_price': 'Database/stock_price',
        'stock_valuation': 'Database/stock_valuation',
        'financial_data': 'Database/financial_data',
        'dividend': 'Database/dividend',
        # ... 更多路径配置
    }
    return paths[data_type]
```

### 异常处理

所有模块都包含完善的异常处理机制：

- API调用失败自动重试
- 数据为空时的友好提示
- 详细的错误日志记录

## 🚨 注意事项

1. **API限制**: 注意 JoinQuant API 的调用频率限制
2. **数据权限**: 某些财务数据需要相应的权限
3. **存储空间**: 全量数据可能占用较大存储空间
4. **网络环境**: 确保网络连接稳定

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进项目：

1. Fork 本项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

---

**注意**: 本项目仅用于学习和研究目的，不构成投资建议。使用本项目进行投资决策的风险由用户自行承担。