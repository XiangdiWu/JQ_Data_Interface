## Joinquant_Data_Interface

1、✅ 验证登陆情况 auth.py

1、✅ 运行数据存储路径 Config/data_path.py

2、✅ 获取交易日列表 all_trading_days.py（Akshare）

3、✅ 获取证券信息列表 get_all_securities.py（如股票上市和退市信息列表）

4、✅ 工具：获取交易日 Utils/get_trading_date.py

5、✅ 工具：获取股票列表 Utils/get_stock_list.py

6、✅ 获取指数、行业、概念成份股 get_index_stocks.py

7、✅ 股票数据：获取股票行情 get_price.py（包括后复权因子）

8、✅ 股票数据：判断股票是否ST get_extras.py

9、✅ 股票数据：获取股票估值 get_valuation.py

10、✅ 股票数据：获取股票所属行业 get_stock_industry.py

11、✅ 股票数据：获取股票所属概念 get_stock_concept.py

12、✅ 股票数据：获取股票融资融券信息 get_mtss.py

13、❗️ 股票数据：获取股票财务数据 financial_data.py（JoinQuant）

14、股票数据：获取股票分红送股信息 get_dividend_new.py

15、股票数据：获取股票资金流向 get_money_flow.py

16、✅ 工具：获取股票涨停、跌停、停牌信息 get_stock_ud.py

17、❗️ 工具：根据报告期财务数据得到季度财务数据 get_quarterly_financial_data.py（或不必需）

18、✅ 债券数据：中美国债收益率 bond_zh_us_rate.py（Akshare）

## Todo

[ ] 完善除权除息数据处理和后复权因子计算

[ ] 完善财务数据获取

[ ] 完善财务数据处理

[ ] 使用run_offset_query方法获取数据

[ ] 增加数据获取时间统计

[ ] 项目性能优化，比如使用多进程和增加缓存机制等

[ ] 完善数据增量更新

[ ] 完善日度数据更新任务调度

[ ] 丰富数据存储类型

[ ] 完善Tick数据获取

[ ] 完善Tick数据处理

[ ] 完善分钟频率数据获取

[ ] 完善其他资产类别数据获取和处理

## 具体来看

### JoinQuant财务数据获取

| 类别             | 聚宽方法                  | 聚宽数据源   | 代码文件                  | 采纳情况  | 备注 | Akshare数据源 |
| --------------- | ------------------------ | ------- | --------------------- | ----- | -- | ---------- |
| 金融公司财务报表（报告期）   | finance.run_query        | ✅ 完成    | financial_query.py    | ✅ 采纳  |    |            |
| 金融公司财务报表（季度）    | get_fundamentals+query   | ❌ 获取失败  | financial_data_old.py | ❌ 不采纳 |    |            |
| 金融公司财务报表（季度）    | get_history_fundamentals |         | financial_data.py     | ✅ 采纳  |    |            |
| 金融公司财务报表（年度）    | get_fundamentals+query   |         |                       | ❌ 不采纳 |    |            |
| 金融公司财务报表（年度）    | get_history_fundamentals |         | 未完成                   | ✅ 采纳  |    |            |
| 普通公司财务报表（报告期）   | finance.run_query        | ❌ 权限未明确 | financial_query.py    | ❌ 不采纳 |    |            |
| 普通公司财务报表（报告期）   | 未知                       | 未知      | 未完成                   |       |    |            |
| 普通公司财务报表（季度）    | get_fundamentals+query   | ❌ 获取失败  | financial_data_old.py | ❌ 不采纳 |    |            |
| 普通公司财务报表（季度）    | get_history_fundamentals |         | financial_data.py     | ✅ 采纳  |    |            |
| 普通公司财务报表（年度）    | get_fundamentals+query   |         | 未完成                   | ❌ 不采纳 |    |            |
| 普通公司财务报表（年度）    | get_history_fundamentals |         | 未完成                   | ✅ 采纳  |    |            |
| 金融公司财务指标（普通-季度） |                          |         |                       |       |    |            |
| 金融公司财务指标（普通-年度） |                          |         |                       |       |    |            |
| 银行公司财务指标（年度）    |                          |         |                       |       |    |            |
| 券商公司财务指标（年度）    |                          |         |                       |       |    |            |
| 保险公司财务指标（年度）    |                          |         |                       |       |    |            |
| 普通公司财务指标（季度）    |                          | ✅ 完成    | financial_data_new.py | ✅ 采纳  |    |            |
| 普通公司财务指标（年度）    |                          |         | 未完成                   | ✅ 采纳