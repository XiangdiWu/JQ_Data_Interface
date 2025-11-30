"""
财务数据字段统一配置文件
管理所有财务数据表的字段定义，字段名包含表名前缀
"""

# 资产负债表字段
BALANCE_SHEET_FIELDS_QUARTER = [
    'balance.code', 'balance.pubDate', 'balance.statDate',
    'balance.cash_equivalents', 'balance.settlement_provi', 'balance.lend_capital', 'balance.trading_assets',
    'balance.bill_receivable', 'balance.account_receivable', 'balance.advance_payment', 'balance.insurance_receivables',
    'balance.reinsurance_receivables', 'balance.reinsurance_contract_reserves_receivable', 'balance.interest_receivable',
    'balance.dividend_receivable', 'balance.other_receivable', 'balance.bought_sellback_assets', 'balance.inventories',
    'balance.non_current_asset_in_one_year', 'balance.other_current_assets', 'balance.total_current_assets',
    'balance.loan_and_advance', 'balance.hold_for_sale_assets', 'balance.hold_to_maturity_investments',
    'balance.longterm_receivable_account', 'balance.longterm_equity_invest', 'balance.investment_property',
    'balance.fixed_assets', 'balance.constru_in_process', 'balance.construction_materials', 'balance.fixed_assets_liquidation',
    'balance.biological_assets', 'balance.oil_gas_assets', 'balance.intangible_assets', 'balance.development_expenditure',
    'balance.good_will', 'balance.long_deferred_expense', 'balance.deferred_tax_assets', 'balance.other_non_current_assets',
    'balance.total_non_current_assets', 'balance.total_assets', 'balance.shortterm_loan', 'balance.borrowing_from_centralbank',
    'balance.deposit_in_interbank', 'balance.borrowing_capital', 'balance.trading_liability', 'balance.notes_payable',
    'balance.accounts_payable', 'balance.advance_peceipts', 'balance.sold_buyback_secu_proceeds', 'balance.commission_payable',
    'balance.salaries_payable', 'balance.taxs_payable', 'balance.interest_payable', 'balance.dividend_payable', 'balance.other_payable',
    'balance.reinsurance_payables', 'balance.insurance_contract_reserves', 'balance.proxy_secu_proceeds',
    'balance.receivings_from_vicariously_sold_securities', 'balance.non_current_liability_in_one_year',
    'balance.other_current_liability', 'balance.total_current_liability', 'balance.longterm_loan', 'balance.bonds_payable',
    'balance.longterm_account_payable', 'balance.specific_account_payable', 'balance.estimate_liability',
    'balance.deferred_tax_liability', 'balance.other_non_current_liability', 'balance.total_non_current_liability',
    'balance.total_liability', 'balance.paidin_capital', 'balance.capital_reserve_fund', 'balance.treasury_stock',
    'balance.specific_reserves', 'balance.surplus_reserve_fund', 'balance.ordinary_risk_reserve_fund',
    'balance.retained_profit', 'balance.foreign_currency_report_conv_diff', 'balance.equities_parent_company_owners',
    'balance.minority_interests', 'balance.total_owner_equities', 'balance.total_sheet_owner_equities'
]

# 利润表字段
INCOME_STATEMENT_FIELDS_QUARTER = [
    'income.code', 'income.pubDate', 'income.statDate',
    'income.total_operating_revenue', 'income.operating_revenue', 'income.interest_income', 'income.premiums_earned',
    'income.commission_income', 'income.total_operating_cost', 'income.operating_cost', 'income.interest_expense',
    'income.commission_expense', 'income.refunded_premiums', 'income.net_pay_insurance_claims',
    'income.withdraw_insurance_contract_reserve', 'income.policy_dividend_payout', 'income.reinsurance_cost',
    'income.operating_tax_surcharges', 'income.sale_expense', 'income.administration_expense', 'income.financial_expense',
    'income.asset_impairment_loss', 'income.fair_value_variable_income', 'income.investment_income',
    'income.invest_income_associates', 'income.exchange_income', 'income.operating_profit', 'income.non_operating_revenue',
    'income.non_operating_expense', 'income.disposal_loss_non_current_liability', 'income.total_profit',
    'income.income_tax_expense', 'income.net_profit', 'income.np_parent_company_owners', 'income.minority_profit',
    'income.basic_eps', 'income.diluted_eps', 'income.other_composite_income', 'income.total_composite_income',
    'income.ci_parent_company_owners', 'income.ci_minority_owners'
]

# 现金流量表字段
CASH_FLOW_FIELDS_QUARTER = [
    'cash_flow.code', 'cash_flow.pubDate', 'cash_flow.statDate',
    'cash_flow.goods_sale_and_service_render_cash', 'cash_flow.net_deposit_increase', 'cash_flow.net_borrowing_from_central_bank',
    'cash_flow.net_borrowing_from_finance_co', 'cash_flow.net_original_insurance_cash', 'cash_flow.net_cash_received_from_reinsurance_business',
    'cash_flow.net_insurer_deposit_investment', 'cash_flow.net_deal_trading_assets', 'cash_flow.interest_and_commission_cashin',
    'cash_flow.net_increase_in_placements', 'cash_flow.net_buyback', 'cash_flow.tax_levy_refund', 'cash_flow.other_cashin_related_operate',
    'cash_flow.subtotal_operate_cash_inflow', 'cash_flow.goods_and_services_cash_paid', 'cash_flow.net_loan_and_advance_increase',
    'cash_flow.net_deposit_in_cb_and_ib', 'cash_flow.original_compensation_paid', 'cash_flow.handling_charges_and_commission',
    'cash_flow.policy_dividend_cash_paid', 'cash_flow.staff_behalf_paid', 'cash_flow.tax_payments', 'cash_flow.other_operate_cash_paid',
    'cash_flow.subtotal_operate_cash_outflow', 'cash_flow.net_operate_cash_flow', 'cash_flow.invest_withdrawal_cash',
    'cash_flow.invest_proceeds', 'cash_flow.fix_intan_other_asset_dispo_cash', 'cash_flow.net_cash_deal_subcompany',
    'cash_flow.other_cash_from_invest_act', 'cash_flow.subtotal_invest_cash_inflow', 'cash_flow.fix_intan_other_asset_acqui_cash',
    'cash_flow.invest_cash_paid', 'cash_flow.impawned_loan_net_increase', 'cash_flow.net_cash_from_sub_company',
    'cash_flow.other_cash_to_invest_act', 'cash_flow.subtotal_invest_cash_outflow', 'cash_flow.net_invest_cash_flow',
    'cash_flow.cash_from_invest', 'cash_flow.cash_from_mino_s_invest_sub', 'cash_flow.cash_from_borrowing', 'cash_flow.cash_from_bonds_issue',
    'cash_flow.other_finance_act_cash', 'cash_flow.subtotal_finance_cash_inflow', 'cash_flow.borrowing_repayment',
    'cash_flow.dividend_interest_payment', 'cash_flow.proceeds_from_sub_to_mino_s', 'cash_flow.other_finance_act_payment',
    'cash_flow.subtotal_finance_cash_outflow', 'cash_flow.net_finance_cash_flow', 'cash_flow.exchange_rate_change_effect',
    'cash_flow.cash_equivalent_increase', 'cash_flow.cash_equivalents_at_beginning', 'cash_flow.cash_and_equivalents_at_end'
]

# 财务指标字段
INDICATOR_FIELDS_QUARTER = [
    'indicator.code', 'indicator.pubDate', 'indicator.statDate',
    'indicator.eps', 'indicator.adjusted_profit', 'indicator.operating_profit', 'indicator.value_change_profit', 
    'indicator.roe', 'indicator.inc_return', 'indicator.roa', 'indicator.net_profit_margin', 'indicator.gross_profit_margin', 
    'indicator.expense_to_total_revenue', 'indicator.operation_profit_to_total_revenue', 'indicator.net_profit_to_total_revenue', 
    'indicator.operating_expense_to_total_revenue', 'indicator.ga_expense_to_total_revenue', 'indicator.financing_expense_to_total_revenue', 
    'indicator.operating_profit_to_profit', 'indicator.invesment_profit_to_profit', 'indicator.adjusted_profit_to_profit', 
    'indicator.goods_sale_and_service_to_revenue', 'indicator.ocf_to_revenue', 'indicator.ocf_to_operating_profit', 
    'indicator.inc_total_revenue_year_on_year', 'indicator.inc_total_revenue_annual', 'indicator.inc_revenue_year_on_year', 
    'indicator.inc_revenue_annual', 'indicator.inc_operation_profit_year_on_year', 'indicator.inc_operation_profit_annual', 
    'indicator.inc_net_profit_year_on_year', 'indicator.inc_net_profit_annual', 'indicator.inc_net_profit_to_shareholders_year_on_year', 
    'indicator.inc_net_profit_to_shareholders_annual'
]

# 根据聚宽的数据文档，年度字段和季度字段有所不同
BALANCE_SHEET_FIELDS_ANNUAL = [
    'balance.code', 'balance.pubDate', 'balance.statDate'
]

INCOME_STATEMENT_FIELDS_ANNUAL = [
    'income.code', 'income.pubDate', 'income.statDate'
]

CASH_FLOW_FIELDS_ANNUAL = [
    'cash_flow.code', 'cash_flow.pubDate', 'cash_flow.statDate'
]

INDICATOR_FIELDS_ANNUAL = [
    'indicator.code', 'indicator.pubDate', 'indicator.statDate'
]

# 银行指标字段，银行行业代码 801780
BANK_INDICATOR_FIELDS_ANNUAL = [
    'bank_indicator.code', 'bank_indicator.pubDate', 'bank_indicator.statDate',
    'bank_indicator.total_loan', 'bank_indicator.total_deposit', 'bank_indicator.interest_earning_assets',
    'bank_indicator.non_interest_earning_assets', 'bank_indicator.interest_earning_assets_yield',
    'bank_indicator.interest_bearing_liabilities', 'bank_indicator.non_interest_bearing_liabilities',
    'bank_indicator.interest_bearing_liabilities_interest_rate', 'bank_indicator.non_interest_income',
    'bank_indicator.non_interest_income_ratio', 'bank_indicator.net_interest_margin',
    'bank_indicator.net_profit_margin', 'bank_indicator.core_level_capital',
    'bank_indicator.net_core_level_capital', 'bank_indicator.core_level_capital_adequacy_ratio',
    'bank_indicator.net_level_1_capital', 'bank_indicator.level_1_capital_adequacy_ratio',
    'bank_indicator.net_capital', 'bank_indicator.capital_adequacy_ratio',
    'bank_indicator.weighted_risky_asset', 'bank_indicator.deposit_loan_ratio',
    'bank_indicator.short_term_asset_liquidity_ratio_CNY', 'bank_indicator.short_term_asset_liquidity_ratio_FC',
    'bank_indicator.Nonperforming_loan_rate', 'bank_indicator.single_largest_customer_loan_ratio',
    'bank_indicator.top_ten_customer_loan_ratio', 'bank_indicator.bad_debts_reserve',
    'bank_indicator.non_performing_loan_provision_coverage', 'bank_indicator.cost_to_income_ratio',
    'bank_indicator.former_core_capital', 'bank_indicator.former_net_core_capital',
    'bank_indicator.former_net_core_capital_adequacy_ratio', 'bank_indicator.former_net_capital',
    'bank_indicator.former_capital_adequacy_ratio', 'bank_indicator.former_weighted_risky_asset',
    'bank_indicator.normal_amount', 'bank_indicator.normal_amount_ratio',
    'bank_indicator.concerned_amount', 'bank_indicator.concerned_amount_ratio',
    'bank_indicator.secondary_amount', 'bank_indicator.secondary_amount_ratio',
    'bank_indicator.suspicious_amount', 'bank_indicator.suspicious_amount_ratio',
    'bank_indicator.loss_amount', 'bank_indicator.loss_amount_ratio',
    'bank_indicator.short_term_loan_average_balance', 'bank_indicator.short_term_loan_annualized_average_interest_rate',
    'bank_indicator.mid_term_loan_annualized_average_balance', 'bank_indicator.mid_term_loan_annualized_average_interest_rate',
    'bank_indicator.enterprise_deposits_average_balance', 'bank_indicator.enterprise_deposits_average_interest_rate',
    'bank_indicator.savings_deposit_average_balance', 'bank_indicator.savings_deposit_average_interest_rate'
]

# 证券指标字段，证券行业代码 801193
SECURITY_INDICATOR_FIELDS_ANNUAL = [
    'security_indicator.code', 'security_indicator.pubDate', 'security_indicator.statDate',
    'security_indicator.net_capital', 'security_indicator.net_assets',
    'security_indicator.net_capital_to_reserve', 'security_indicator.net_capital_to_net_asset',
    'security_indicator.net_capital_to_debt', 'security_indicator.net_asset_to_debt',
    'security_indicator.net_capital_to_sales_department_number', 'security_indicator.own_stock_to_net_capital',
    'security_indicator.own_security_to_net_capital', 'security_indicator.operational_risk_reserve',
    'security_indicator.broker_risk_reserve', 'security_indicator.own_security_risk_reserve',
    'security_indicator.security_underwriting_reserve', 'security_indicator.asset_management_reserve',
    'security_indicator.own_equity_derivatives_to_net_capital', 'security_indicator.own_fixed_income_to_net_capital',
    'security_indicator.margin_trading_reserve', 'security_indicator.branch_risk_reserve'
]

# 保险指标字段，保险行业代码 801194
INSURANCE_INDICATOR_FIELDS_ANNUAL = [
    'insurance_indicator.code', 'insurance_indicator.pubDate', 'insurance_indicator.statDate',
    'insurance_indicator.investment_assets', 'insurance_indicator.total_investment_rate_of_return',
    'insurance_indicator.net_investment_rate_of_return', 'insurance_indicator.earned_premium',
    'insurance_indicator.earned_premium_growth_rate', 'insurance_indicator.payoff_cost',
    'insurance_indicator.compensation_rate', 'insurance_indicator.not_expired_duty_reserve',
    'insurance_indicator.outstanding_claims_reserve', 'insurance_indicator.comprehensive_cost_ratio',
    'insurance_indicator.comprehensive_compensation_rate', 'insurance_indicator.solvency_adequacy_ratio',
    'insurance_indicator.actual_capital', 'insurance_indicator.minimum_capital'
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