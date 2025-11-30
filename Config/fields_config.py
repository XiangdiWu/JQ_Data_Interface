"""
财务数据字段统一配置文件
管理所有财务数据表的字段定义，字段名包含表名前缀
"""

# 资产负债表字段
BALANCE_SHEET_FIELDS_QUARTER = [
    'balance.code',                              # 股票代码(带后缀: .XSHE/.XSHG)
    'balance.pubDate',                           # 日期
    'balance.statDate',                           # 日期
    'balance.cash_equivalents',                   # 货币资金(元)
    'balance.settlement_provi',                   # 结算备付金(元)
    'balance.lend_capital',                       # 拆出资金(元)
    'balance.trading_assets',                    # 交易性金融资产(元)
    'balance.bill_receivable',                   # 应收票据(元)
    'balance.account_receivable',                # 应收账款(元)
    'balance.advance_payment',                   # 预付款项(元)
    'balance.insurance_receivables',             # 应收保费(元)
    'balance.reinsurance_receivables',           # 应收分保账款(元)
    'balance.reinsurance_contract_reserves_receivable', # 应收分保合同准备金(元)
    'balance.interest_receivable',               # 应收利息(元)
    'balance.dividend_receivable',               # 应收股利(元)
    'balance.other_receivable',                  # 其他应收款(元)
    'balance.bought_sellback_assets',            # 买入返售金融资产(元)
    'balance.inventories',                       # 存货(元)
    'balance.contract_assets',                   # 合同资产(元)(jqdatasdk1.9.5新增)
    'balance.receivable_fin',                     # 应收款项融资(元)(jqdatasdk1.9.5新增)
    'balance.non_current_asset_in_one_year',     # 一年内到期的非流动资产(元)
    'balance.other_current_assets',              # 其他流动资产(元)
    'balance.total_current_assets',              # 流动资产合计(元)
    'balance.loan_and_advance_current_assets',   # 流动资产-发放贷款及垫款(元)(jqdatasdk1.9.5新增)
    'balance.loan_and_advance',                  # 发放委托贷款及垫款(元)
    'balance.loan_and_advance_noncurrent_assets', # 非流动资产-发放贷款及垫款(元)(jqdatasdk1.9.5新增)
    'balance.hold_for_sale_assets',              # 可供出售金融资产(元)
    'balance.hold_sale_asset',                   # 划分为持有待售的资产(元)(jqdatasdk1.9.5新增)
    'balance.bond_invest',                       # 债权投资(元)(jqdatasdk1.9.5新增)
    'balance.other_bond_invest',                 # 其他债权投资(元)(jqdatasdk1.9.5新增)
    'balance.other_equity_tools_invest',         # 其他权益工具投资(元)(jqdatasdk1.9.5新增)
    'balance.hold_to_maturity_investments',     # 持有至到期投资(元)
    'balance.longterm_receivable_account',       # 长期应收款(元)
    'balance.longterm_equity_invest',            # 长期股权投资(元)
    'balance.investment_property',               # 投资性房地产(元)
    'balance.fixed_assets',                      # 固定资产(元)
    'balance.constru_in_process',               # 在建工程(元)
    'balance.construction_materials',            # 工程物资(元)
    'balance.fixed_assets_liquidation',         # 固定资产清理(元)
    'balance.biological_assets',                 # 生产性生物资产(元)
    'balance.oil_gas_assets',                   # 油气资产(元)
    'balance.intangible_assets',                 # 无形资产(元)
    'balance.development_expenditure',           # 开发支出(元)
    'balance.good_will',                         # 商誉(元)
    'balance.usufruct_assets',                   # 使用权资产(元)(jqdatasdk1.9.5新增)
    'balance.long_deferred_expense',            # 长期待摊费用(元)
    'balance.deferred_tax_assets',               # 递延所得税资产(元)
    'balance.derivative_financial_asset',         # 衍生金融资产(元)(jqdatasdk1.9.5新增)
    'balance.other_non_current_financial_assets', # 其他非流动金融资产(元)(jqdatasdk1.9.5新增)
    'balance.other_non_current_assets',          # 其他非流动资产(元)
    'balance.total_non_current_assets',          # 非流动资产合计(元)
    'balance.total_assets',                      # 资产总计(元)
    'balance.shortterm_loan',                    # 短期借款(元)
    'balance.borrowing_from_centralbank',        # 向中央银行借款(元)
    'balance.deposit_in_interbank',              # 吸收存款及同业存放(元)
    'balance.borrowing_capital',                 # 拆入资金(元)
    'balance.trading_liability',                 # 交易性金融负债(元)
    'balance.derivative_financial_liability',    # 衍生金融负债(元)(jqdatasdk1.9.5新增)
    'balance.notes_payable',                     # 应付票据(元)
    'balance.accounts_payable',                  # 应付账款(元)
    'balance.contract_liability',                # 合同负债(元)(jqdatasdk1.9.5新增)
    'balance.advance_peceipts',                 # 预收款项(元)
    'balance.sold_buyback_secu_proceeds',       # 卖出回购金融资产款(元)
    'balance.commission_payable',               # 应付手续费及佣金(元)
    'balance.salaries_payable',                 # 应付职工薪酬(元)
    'balance.taxs_payable',                      # 应交税费(元)
    'balance.interest_payable',                 # 应付利息(元)
    'balance.dividend_payable',                 # 应付股利(元)
    'balance.other_payable',                    # 其他应付款(元)
    'balance.reinsurance_payables',             # 应付分保账款(元)
    'balance.insurance_contract_reserves',      # 保险合同准备金(元)
    'balance.proxy_secu_proceeds',              # 代理买卖证券款(元)
    'balance.receivings_from_vicariously_sold_securities', # 代理承销证券款(元)
    'balance.non_current_liability_in_one_year', # 一年内到期的非流动负债(元)
    'balance.estimate_liability_current',        # 流动负债-预计负债(元)(jqdatasdk1.9.5新增)
    'balance.deferred_earning_current',           # 流动负债-递延收益(元)(jqdatasdk1.9.5新增)
    'balance.hold_sale_liability',                # 划分为持有待售的负债(元)(jqdatasdk1.9.5新增)
    'balance.other_current_liability',           # 其他流动负债(元)
    'balance.total_current_liability',           # 流动负债合计(元)
    'balance.longterm_loan',                     # 长期借款(元)
    'balance.bonds_payable',                     # 应付债券(元)
    'balance.longterm_account_payable',          # 长期应付款(元)
    'balance.longterm_salaries_payable',         # 长期应付职工薪酬(元)(jqdatasdk1.9.5新增)
    'balance.specific_account_payable',          # 专项应付款(元)
    'balance.preferred_shares_noncurrent',       # 非流动负债-优先股(元)(jqdatasdk1.9.5新增)
    'balance.pepertual_liability_noncurrent',    # 非流动负债-永续债(元)(jqdatasdk1.9.5新增)
    'balance.estimate_liability',                # 预计负债(元)
    'balance.deferred_tax_liability',            # 递延所得税负债(元)
    'balance.deferred_earning',                   # 非流动负债-递延收益(元)(jqdatasdk1.9.5新增)
    'balance.lease_liability',                    # 租赁负债(元)(jqdatasdk1.9.5新增)
    'balance.other_non_current_liability',       # 其他非流动负债(元)
    'balance.total_non_current_liability',       # 非流动负债合计(元)
    'balance.total_liability',                   # 负债合计(元)
    'balance.paidin_capital',                    # 实收资本(或股本)(元)
    'balance.other_equity_tools',                 # 其他权益工具(元)(jqdatasdk1.9.5新增)
    'balance.capital_reserve_fund',              # 资本公积(元)
    'balance.treasury_stock',                    # 减:库存股(元)
    'balance.specific_reserves',                 # 专项储备(元)
    'balance.surplus_reserve_fund',              # 盈余公积(元)
    'balance.ordinary_risk_reserve_fund',        # 一般风险准备(元)
    'balance.other_comprehensive_income',        # 其他综合收益(元)(jqdatasdk1.9.5新增)
    'balance.retained_profit',                   # 未分配利润(元)
    'balance.foreign_currency_report_conv_diff', # 外币报表折算差额(元)
    'balance.equities_parent_company_owners',    # 归属于母公司股东权益合计(元)
    'balance.preferred_shares_equity',            # 其中：优先股-所有者权益(元)(jqdatasdk1.9.5新增)
    'balance.pepertual_liability_equity',        # 所有者权益-永续债(元)(jqdatasdk1.9.5新增)
    'balance.minority_interests',                # 少数股东权益(元)
    'balance.total_owner_equities',              # 股东权益合计(元)
    'balance.total_sheet_owner_equities'         # 负债和股东权益合计(元)
]

# 利润表字段
INCOME_STATEMENT_FIELDS_QUARTER = [
    'income.code',                              # 股票代码(带后缀: .XSHE/.XSHG)
    'income.pubDate',                           # 日期
    'income.statDate',                           # 日期
    # 营业收入
    'income.total_operating_revenue',            # 营业总收入(元)
    'income.operating_revenue',                  # 营业收入(元)
    'income.interest_income',                   # 利息收入(元)
    'income.premiums_earned',                   # 已赚保费(元)
    'income.commission_income',                 # 手续费及佣金收入(元)
    # 营业成本
    'income.total_operating_cost',              # 营业成本(元)
    'income.operating_cost',                    # 营业成本(元)
    'income.interest_expense',                  # 利息支出(元)
    'income.commission_expense',                # 手续费及佣金支出(元)
    'income.refunded_premiums',                 # 退保金(元)
    'income.net_pay_insurance_claims',          # 赔付支出净额(元)
    'income.withdraw_insurance_contract_reserve', # 提取保险合同准备金净额(元)
    'income.policy_dividend_payout',            # 保单红利支出(元)
    'income.reinsurance_cost',                  # 分保费用(元)
    # 营业税金及期间费用
    'income.operating_tax_surcharges',          # 营业税金及附加(元)
    'income.sale_expense',                      # 销售费用(元)
    'income.rd_expenses',                       # 研发费用(元)(jqdatasdk1.9.5新增)
    'income.administration_expense',            # 管理费用(元)
    'income.financial_expense',                 # 财务费用(元)
    'income.interest_cost_fin',                 # 财务费用 - 利息费用(元)(jqdatasdk1.9.5新增)
    'income.interest_income_fin',                # 财务费用 - 利息收入(元)(jqdatasdk1.9.5新增)
    'income.other_earnings',                    # 其他收益(元)(jqdatasdk1.9.5新增)
    # 其他损益
    'income.asset_impairment_loss',             # 资产减值损失(元)
    'income.credit_impairment_loss',            # 信用减值损失(元)(jqdatasdk1.9.5新增)
    'income.fair_value_variable_income',        # 公允价值变动收益(元)
    'income.investment_income',                 # 投资收益(元)
    'income.invest_income_associates',          # 对联营企业和合营企业的投资收益(元)
    'income.asset_deal_income',                 # 资产处置收益(元)(jqdatasdk1.9.5新增)
    'income.exchange_income',                   # 汇兑收益(元)
    'income.net_open_hedge_income',             # 净敞口套期收益(元)(jqdatasdk1.9.5新增)
    # 利润构成
    'income.operating_profit',                  # 营业利润(元)
    'income.sust_operate_net_profit',           # 持续经营净利润(元)(jqdatasdk1.9.5新增)
    'income.discon_operate_net_profit',         # 终止经营净利润(元)(jqdatasdk1.9.5新增)
    'income.non_operating_revenue',             # 营业外收入(元)
    'income.non_operating_expense',             # 营业外支出(元)
    'income.disposal_loss_non_current_liability', # 非流动资产处置净损失(元)
    'income.total_profit',                      # 利润总额(元)
    'income.income_tax_expense',               # 所得税费用(元)
    'income.net_profit',                        # 净利润(元)
    'income.np_parent_company_owners',          # 归属于母公司股东的净利润(元)
    'income.minority_profit',                   # 少数股东损益(元)
    # 每股收益
    'income.basic_eps',                          # 基本每股收益(元)
    'income.diluted_eps',                       # 稀释每股收益(元)
    # 综合收益
    'income.other_composite_income',            # 其他综合收益(元)
    'income.other_composite_income_mino_at',    # 归属于少数股东的其他综合收益的税后额(元)(jqdatasdk1.9.5新增)
    'income.total_composite_income',             # 综合收益总额(元)
    'income.ci_parent_company_owners',          # 归属于母公司所有者的综合收益总额(元)
    'income.ci_minority_owners'                 # 归属于少数股东的综合收益总额(元)
]

# 现金流量表字段
CASH_FLOW_FIELDS_QUARTER = [
    'cash_flow.code',                                          # 股票代码(带后缀: .XSHE/.XSHG)
    'cash_flow.pubDate',                                       # 日期
    'cash_flow.statDate',                                       # 日期
    # 经营活动现金流入
    'cash_flow.goods_sale_and_service_render_cash',             # 销售商品、提供劳务收到的现金(元)
    'cash_flow.net_deposit_increase',                          # 客户存款和同业存放款项净增加额(元)
    'cash_flow.net_borrowing_from_central_bank',               # 向中央银行借款净增加额(元)
    'cash_flow.net_borrowing_from_finance_co',                # 向其他金融机构拆入资金净增加额(元)
    'cash_flow.net_original_insurance_cash',                   # 收到原保险合同保费取得的现金(元)
    'cash_flow.net_cash_received_from_reinsurance_business',   # 收到再保险业务现金净额(元)
    'cash_flow.net_insurer_deposit_investment',               # 保户储金及投资款净增加额(元)
    'cash_flow.net_deal_trading_assets',                      # 交易性金融资产(元)
    'cash_flow.interest_and_commission_cashin',                # 收取利息、手续费及佣金的现金(元)
    'cash_flow.net_increase_in_placements',                   # 拆入资金净增加额(元)
    'cash_flow.net_buyback',                                   # 回购业务资金净增加额(元)
    'cash_flow.tax_levy_refund',                               # 收到的税费返还(元)
    'cash_flow.other_cashin_related_operate',                  # 收到其他与经营活动有关的现金(元)
    'cash_flow.subtotal_operate_cash_inflow',                  # 经营活动现金流入小计(元)
    # 经营活动现金流出
    'cash_flow.goods_and_services_cash_paid',                  # 购买商品、接受劳务支付的现金(元)
    'cash_flow.net_loan_and_advance_increase',                 # 客户贷款及垫款净增加额(元)
    'cash_flow.net_deposit_in_cb_and_ib',                     # 存放中央银行和同业款项净增加额(元)
    'cash_flow.original_compensation_paid',                    # 支付原保险合同赔付款项的现金(元)
    'cash_flow.handling_charges_and_commission',               # 支付利息、手续费及佣金的现金(元)
    'cash_flow.policy_dividend_cash_paid',                     # 支付保单红利的现金(元)
    'cash_flow.staff_behalf_paid',                             # 支付给职工以及为职工支付的现金(元)
    'cash_flow.tax_payments',                                  # 支付的各项税费(元)
    'cash_flow.other_operate_cash_paid',                       # 支付其他与经营活动有关的现金(元)
    'cash_flow.subtotal_operate_cash_outflow',                 # 经营活动现金流出小计(元)
    'cash_flow.net_operate_cash_flow',                         # 经营活动产生的现金流量净额(元)
    # 投资活动现金流入
    'cash_flow.invest_withdrawal_cash',                         # 收回投资收到的现金(元)
    'cash_flow.invest_proceeds',                               # 取得投资收益收到的现金(元)
    'cash_flow.fix_intan_other_asset_dispo_cash',              # 处置固定资产、无形资产和其他长期资产收回的现金净额(元)
    'cash_flow.net_cash_deal_subcompany',                      # 处置子公司及其他营业单位收到的现金净额(元)
    'cash_flow.other_cash_from_invest_act',                    # 收到其他与投资活动有关的现金(元)
    'cash_flow.subtotal_invest_cash_inflow',                   # 投资活动现金流入小计(元)
    # 投资活动现金流出
    'cash_flow.fix_intan_other_asset_acqui_cash',               # 购建固定资产、无形资产和其他长期资产支付的现金(元)
    'cash_flow.invest_cash_paid',                              # 投资支付的现金(元)
    'cash_flow.impawned_loan_net_increase',                    # 质押贷款净增加额(元)
    'cash_flow.net_cash_from_sub_company',                     # 取得子公司及其他营业单位支付的现金净额(元)
    'cash_flow.other_cash_to_invest_act',                      # 支付其他与投资活动有关的现金(元)
    'cash_flow.subtotal_invest_cash_outflow',                   # 投资活动现金流出小计(元)
    'cash_flow.net_invest_cash_flow',                          # 投资活动产生的现金流量净额(元)
    # 筹资活动现金流入
    'cash_flow.cash_from_invest',                              # 吸收投资收到的现金(元)
    'cash_flow.cash_from_mino_s_invest_sub',                   # 其中:子公司吸收少数股东投资收到的现金(元)
    'cash_flow.cash_from_borrowing',                           # 取得借款收到的现金(元)
    'cash_flow.cash_from_bonds_issue',                         # 发行债券收到的现金(元)
    'cash_flow.other_finance_act_cash',                        # 收到其他与筹资活动有关的现金(元)
    'cash_flow.subtotal_finance_cash_inflow',                  # 筹资活动现金流入小计(元)
    # 筹资活动现金流出
    'cash_flow.borrowing_repayment',                            # 偿还债务支付的现金(元)
    'cash_flow.dividend_interest_payment',                     # 分配股利、利润或偿付利息支付的现金(元)
    'cash_flow.proceeds_from_sub_to_mino_s',                   # 其中:子公司支付给少数股东的股利、利润(元)
    'cash_flow.other_finance_act_payment',                     # 支付其他与筹资活动有关的现金(元)
    'cash_flow.subtotal_finance_cash_outflow',                 # 筹资活动现金流出小计(元)
    'cash_flow.net_finance_cash_flow',                         # 筹资活动产生的现金流量净额(元)
    # 现金及现金等价物变动
    'cash_flow.exchange_rate_change_effect',                    # 四、汇率变动对现金及现金等价物的影响
    'cash_flow.cash_equivalent_increase',                       # 五、现金及现金等价物净增加额
    'cash_flow.cash_equivalents_at_beginning',                 # 加:期初现金及现金等价物余额(元)
    'cash_flow.cash_and_equivalents_at_end'                    # 期末现金及现金等价物余额(元)
]

# 财务指标字段
INDICATOR_FIELDS_QUARTER = [
    'indicator.code',      # 股票代码
    'indicator.pubDate',   # 日期
    'indicator.statDate',  # 日期
    'indicator.eps',                                           # 每股收益EPS(元)
    'indicator.adjusted_profit',                               # 扣除非经常损益后的净利润(元)
    'indicator.operating_profit',                              # 经营活动净收益(元)
    'indicator.value_change_profit',                            # 价值变动净收益(元)
    'indicator.roe',                                           # 净资产收益率ROE(%)
    'indicator.inc_return',                                     # 净资产收益率(扣除非经常损益)(%)
    'indicator.roa',                                           # 总资产净利率ROA(%)
    'indicator.net_profit_margin',                             # 销售净利率(%)
    'indicator.gross_profit_margin',                           # 销售毛利率(%)
    'indicator.expense_to_total_revenue',                      # 营业总成本/营业总收入(%)
    'indicator.operation_profit_to_total_revenue',             # 营业利润/营业总收入(%)
    'indicator.net_profit_to_total_revenue',                  # 净利润/营业总收入(%)
    'indicator.operating_expense_to_total_revenue',           # 营业费用/营业总收入(%)
    'indicator.ga_expense_to_total_revenue',                   # 管理费用/营业总收入(%)
    'indicator.financing_expense_to_total_revenue',            # 财务费用/营业总收入(%)
    'indicator.operating_profit_to_profit',                    # 经营活动净收益/利润总额(%)
    'indicator.invesment_profit_to_profit',                    # 价值变动净收益/利润总额(%)
    'indicator.adjusted_profit_to_profit',                     # 扣除非经常损益后的净利润/净利润(%)
    'indicator.goods_sale_and_service_to_revenue',             # 销售商品提供劳务收到的现金/营业收入(%)
    'indicator.ocf_to_revenue',                               # 经营活动产生的现金流量净额/营业收入(%)
    'indicator.ocf_to_operating_profit',                       # 经营活动产生的现金流量净额/经营活动净收益(%)
    'indicator.inc_total_revenue_year_on_year',                # 营业总收入同比增长率(%)
    'indicator.inc_total_revenue_annual',                      # 营业总收入环比增长率(%)
    'indicator.inc_revenue_year_on_year',                      # 营业收入同比增长率(%)
    'indicator.inc_revenue_annual',                            # 营业收入环比增长率(%)
    'indicator.inc_operation_profit_year_on_year',             # 营业利润同比增长率(%)
    'indicator.inc_operation_profit_annual',                   # 营业利润环比增长率(%)
    'indicator.inc_net_profit_year_on_year',                    # 净利润同比增长率(%)
    'indicator.inc_net_profit_annual',                          # 净利润环比增长率(%)
    'indicator.inc_net_profit_to_shareholders_year_on_year',   # 归属母公司股东的净利润同比增长率(%)
    'indicator.inc_net_profit_to_shareholders_annual'          # 归属母公司股东的净利润环比增长率(%)
]

# 根据聚宽的数据文档，年度字段和季度字段有所不同
BALANCE_SHEET_FIELDS_ANNUAL = [
    'balance.code',      # 股票代码(带后缀: .XSHE/.XSHG)
    'balance.pubDate',   # 日期
    'balance.statDate'   # 日期
]

INCOME_STATEMENT_FIELDS_ANNUAL = [
    'income.code',      # 股票代码(带后缀: .XSHE/.XSHG)
    'income.pubDate',   # 日期
    'income.statDate'   # 日期
]

CASH_FLOW_FIELDS_ANNUAL = [
    'cash_flow.code',      # 股票代码(带后缀: .XSHE/.XSHG)
    'cash_flow.pubDate',   # 日期
    'cash_flow.statDate'   # 日期
]

INDICATOR_FIELDS_ANNUAL = [
    'indicator.code',      # 股票代码
    'indicator.pubDate',   # 日期
    'indicator.statDate'   # 日期
]

# 银行指标字段，银行行业代码 801780
BANK_INDICATOR_FIELDS_ANNUAL = [
    'bank_indicator.code',                              # 股票代码(带后缀: .XSHE/.XSHG)
    'bank_indicator.pubDate',                           # 发布日期
    'bank_indicator.statDate',                           # 统计日期
    # 存贷款业务指标
    'bank_indicator.total_loan',                        # 贷款总额(元)
    'bank_indicator.total_deposit',                     # 存款总额(元)
    # 资产负债结构指标
    'bank_indicator.interest_earning_assets',           # 生息资产(元)
    'bank_indicator.non_interest_earning_assets',        # 非生息资产(元)
    'bank_indicator.interest_earning_assets_yield',     # 生息资产收益率(%)
    'bank_indicator.interest_bearing_liabilities',      # 计息负债(元)
    'bank_indicator.non_interest_bearing_liabilities', # 非计息负债(元)
    'bank_indicator.interest_bearing_liabilities_interest_rate', # 计息负债成本率(%)
    # 收入结构指标
    'bank_indicator.non_interest_income',               # 非利息收入(元)
    'bank_indicator.non_interest_income_ratio',         # 非利息收入占比(%)
    # 盈利能力指标
    'bank_indicator.net_interest_margin',               # 净息差(%)
    'bank_indicator.net_profit_margin',                 # 净利差(%)
    # 资本充足率指标(2013年新标准)
    'bank_indicator.core_level_capital',                # 核心一级资本(2013)(元)
    'bank_indicator.net_core_level_capital',            # 核心一级资本净额(2013)(元)
    'bank_indicator.core_level_capital_adequacy_ratio', # 核心一级资本充足率(2013)(%)
    'bank_indicator.net_level_1_capital',               # 一级资本净额（2013）(元)
    'bank_indicator.level_1_capital_adequacy_ratio',    # 一级资本充足率（2013）(%)
    'bank_indicator.net_capital',                        # 资本净额（2013）(元)
    'bank_indicator.capital_adequacy_ratio',            # 资本充足率（2013）(%)
    'bank_indicator.weighted_risky_asset',              # 风险加权资产合计（2013）(元)
    # 流动性指标
    'bank_indicator.deposit_loan_ratio',                # 存贷款比例(%)
    'bank_indicator.short_term_asset_liquidity_ratio_CNY', # 短期资产流动性比例（人民币）(%)
    'bank_indicator.short_term_asset_liquidity_ratio_FC',  # 短期资产流动性比例（外币）(%)
    # 资产质量指标
    'bank_indicator.Nonperforming_loan_rate',           # 不良贷款率(%)
    'bank_indicator.single_largest_customer_loan_ratio', # 单一最大客户贷款比例(%)
    'bank_indicator.top_ten_customer_loan_ratio',        # 最大十家客户贷款比例(%)
    'bank_indicator.bad_debts_reserve',                  # 贷款呆账准备金(元)
    'bank_indicator.non_performing_loan_provision_coverage', # 不良贷款拨备覆盖率(%)
    # 运营效率指标
    'bank_indicator.cost_to_income_ratio',              # 成本收入比(%)
    # 资本充足率指标(旧标准)
    'bank_indicator.former_core_capital',                # 核心资本 (旧)(元)
    'bank_indicator.former_net_core_capital',           # 核心资本净额（旧）(元)
    'bank_indicator.former_net_core_capital_adequacy_ratio', # 核心资本充足率 (旧)(%)
    'bank_indicator.former_net_capital',                # 资本净额 (旧)(元)
    'bank_indicator.former_capital_adequacy_ratio',     # 资本充足率 (旧)(%)
    'bank_indicator.former_weighted_risky_asset',        # 加权风险资产净额（旧）(元)
    # 贷款五级分类指标-金额
    'bank_indicator.normal_amount',                      # 正常-金额(元)
    'bank_indicator.concerned_amount',                  # 关注-金额(元)
    'bank_indicator.secondary_amount',                   # 次级-金额(元)
    'bank_indicator.suspicious_amount',                  # 可疑-金额(元)
    'bank_indicator.loss_amount',                        # 损失-金额(元)
    # 贷款五级分类指标-占比
    'bank_indicator.normal_amount_ratio',                # 正常金额占比(%)
    'bank_indicator.concerned_amount_ratio',             # 关注金额占比(%)
    'bank_indicator.secondary_amount_ratio',             # 次级金额占比(%)
    'bank_indicator.suspicious_amount_ratio',            # 可疑金额占比(%)
    'bank_indicator.loss_amount_ratio',                  # 损失金额占比(%)
    # 贷款利率指标
    'bank_indicator.short_term_loan_average_balance',     # 短期贷款-平均余额(元)
    'bank_indicator.short_term_loan_annualized_average_interest_rate', # 短期贷款-年平均利率(%)
    'bank_indicator.mid_term_loan_annualized_average_balance', # 中长期贷款-平均余额(元)
    'bank_indicator.mid_term_loan_annualized_average_interest_rate', # 中长期贷款-年平均利率(%)
    # 存款利率指标
    'bank_indicator.enterprise_deposits_average_balance', # 企业存款-平均余额(元)
    'bank_indicator.enterprise_deposits_average_interest_rate', # 企业存款-年平均利率(%)
    'bank_indicator.savings_deposit_average_balance',    # 储蓄存款-平均余额(元)
    'bank_indicator.savings_deposit_average_interest_rate' # 储蓄存款-年平均利率(%)
]

# 证券指标字段，证券行业代码 801193
SECURITY_INDICATOR_FIELDS_ANNUAL = [
    'security_indicator.code',                              # 股票代码(带后缀: .XSHE/.XSHG)
    'security_indicator.pubDate',                           # 发布日期
    'security_indicator.statDate',                           # 统计日期
    # 基本财务指标
    'security_indicator.net_capital',                        # 净资本(元)
    'security_indicator.net_assets',                         # 净资产(元)
    # 风险控制指标
    'security_indicator.net_capital_to_reserve',            # 净资本/各项风险准备之和(%)
    'security_indicator.net_capital_to_net_asset',          # 净资本/净资产(%)
    'security_indicator.net_capital_to_debt',                # 净资本/负债(%)
    'security_indicator.net_asset_to_debt',                  # 净资产/负债(%)
    # 运营效率指标
    'security_indicator.net_capital_to_sales_department_number', # 净资本/营业部家数(%)
    # 自营业务规模指标
    'security_indicator.own_stock_to_net_capital',           # 自营股票规模/净资本(%)
    'security_indicator.own_security_to_net_capital',        # 证券自营业务规模/净资本(%)
    # 风险准备金指标
    'security_indicator.operational_risk_reserve',            # 营运风险准备(元)
    'security_indicator.broker_risk_reserve',                # 经纪业务风险准备(元)
    'security_indicator.own_security_risk_reserve',          # 证券自营业务风险准备(元)
    'security_indicator.security_underwriting_reserve',       # 证券承销业务风险准备(元)
    'security_indicator.asset_management_reserve',            # 证券资产管理业务风险准备(元)
    # 自营投资结构指标
    'security_indicator.own_equity_derivatives_to_net_capital', # 自营权益类证券及证券衍生品/净资本(%)
    'security_indicator.own_fixed_income_to_net_capital',     # 自营固定收益类证券/净资本(%)
    # 专项业务风险准备
    'security_indicator.margin_trading_reserve',              # 融资融券业务风险资本准备(元)
    'security_indicator.branch_risk_reserve'                  # 分支机构风险资本准备(元)
]

# 保险指标字段，保险行业代码 801194
INSURANCE_INDICATOR_FIELDS_ANNUAL = [
    'insurance_indicator.code',                              # 股票代码(带后缀: .XSHE/.XSHG)
    'insurance_indicator.pubDate',                           # 发布日期
    'insurance_indicator.statDate',                           # 统计日期
    # 投资业务指标
    'insurance_indicator.investment_assets',                 # 投资资产(元)
    'insurance_indicator.total_investment_rate_of_return',   # 总投资收益率(%)
    'insurance_indicator.net_investment_rate_of_return',     # 净投资收益率(%)
    # 保费业务指标
    'insurance_indicator.earned_premium',                    # 已赚保费(元)
    'insurance_indicator.earned_premium_growth_rate',        # 已赚保费增长率(%)
    # 赔付业务指标
    'insurance_indicator.payoff_cost',                       # 赔付支出(元)
    'insurance_indicator.compensation_rate',                 # 退保率(寿险业务)(%)
    # 准备金指标(产险业务)
    'insurance_indicator.not_expired_duty_reserve',          # 未到期责任准备金（产险业务）(元)
    'insurance_indicator.outstanding_claims_reserve',         # 未决赔款准备金（产险业务）(元)
    # 综合经营指标(产险业务)
    'insurance_indicator.comprehensive_cost_ratio',          # 综合成本率（产险业务）(%)
    'insurance_indicator.comprehensive_compensation_rate',   # 综合赔付率（产险业务）(%)
    # 偿付能力指标
    'insurance_indicator.solvency_adequacy_ratio',           # 偿付能力充足率(%)
    'insurance_indicator.actual_capital',                     # 实际资本(元)
    'insurance_indicator.minimum_capital'                    # 最低资本(元)
]

# 字段映射字典
FINANCIAL_FIELDS = {
    'balance_quarter': BALANCE_SHEET_FIELDS_QUARTER,
    'income_quarter': INCOME_STATEMENT_FIELDS_QUARTER,
    'cash_flow_quarter': CASH_FLOW_FIELDS_QUARTER,
    'indicator_quarter': INDICATOR_FIELDS_QUARTER,
    'balance_annual': BALANCE_SHEET_FIELDS_ANNUAL,
    'income_annual': INCOME_STATEMENT_FIELDS_ANNUAL,
    'cash_flow_annual': CASH_FLOW_FIELDS_ANNUAL,
    'indicator_annual': INDICATOR_FIELDS_ANNUAL,
    'bank_indicator_annual': BANK_INDICATOR_FIELDS_ANNUAL,
    'security_indicator_annual': SECURITY_INDICATOR_FIELDS_ANNUAL,
    'insurance_indicator_annual': INSURANCE_INDICATOR_FIELDS_ANNUAL
}

# 获取字段配置的函数
def get_fields(table_name):
    """
    根据表名获取对应的字段列表
    
    Args:
        table_name (str): 表名 ('balance_quarter', 'income_quarter', 'cash_flow_quarter', 'indicator_quarter', 'balance_annual', 'income_annual', 'cash_flow_annual', 'indicator_annual', 'bank_indicator_annual', 'security_indicator_annual', 'insurance_indicator_annual')
    
    Returns:
        list: 字段列表
    """
    return FINANCIAL_FIELDS.get(table_name, [])

def get_all_fields():
    """
    获取所有财务数据表的字段
    
    Returns:
        dict: 包含所有表字段的字典
    """
    return FINANCIAL_FIELDS.copy()

# 字段描述映射（可选，用于文档说明）
FIELD_DESCRIPTIONS = {
    'balance_quarter': '资产负债表字段',
    'income_quarter': '利润表字段', 
    'cash_flow_quarter': '现金流量表字段',
    'indicator_quarter': '财务指标字段',
    'balance_annual': '资产负债表字段（年度）',
    'income_annual': '利润表字段（年度）',
    'cash_flow_annual': '现金流量表字段（年度）',
    'indicator_annual': '财务指标字段（年度）',
    'bank_indicator_annual': '银行指标字段（年度）',
    'security_indicator_annual': '证券指标字段（年度）',
    'insurance_indicator_annual': '保险指标字段（年度）'
}

if __name__ == '__main__':
    # 测试字段配置
    print("财务数据字段配置测试")
    print("=" * 50)
    
    for table_name, fields in FINANCIAL_FIELDS.items():
        print(f"\n{FIELD_DESCRIPTIONS[table_name]}:")
        print(f"字段数量: {len(fields)}")
        print(f"前5个字段: {fields[:5]}")
    
    print(f"\n获取资产负债表字段:")
    balance_fields = get_fields('balance_quarter')
    print(f"字段数量: {len(balance_fields)}")
    print(f"前3个字段: {balance_fields[:3]}")