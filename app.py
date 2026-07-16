#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Streamlit interactive demo for city cost of living analysis."""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="城市生活成本计算器",
    page_icon="🏙️",
    layout="wide"
)

# --- Load data from run_analysis.py (same source) ---
@st.cache_data
def load_data():
    cities_data = [
        {'city': '北京', 'tier': '一线', 'avg_salary_before_tax': 13400, 'rent_1br': 4200, 'food_monthly': 3000, 'transport_monthly': 300, 'utilities_monthly': 400, 'other_monthly': 1500, 'house_price_per_sqm': 56500},
        {'city': '上海', 'tier': '一线', 'avg_salary_before_tax': 13700, 'rent_1br': 4000, 'food_monthly': 3200, 'transport_monthly': 350, 'utilities_monthly': 420, 'other_monthly': 1600, 'house_price_per_sqm': 65000},
        {'city': '深圳', 'tier': '一线', 'avg_salary_before_tax': 12800, 'rent_1br': 3700, 'food_monthly': 2800, 'transport_monthly': 280, 'utilities_monthly': 450, 'other_monthly': 1400, 'house_price_per_sqm': 65400},
        {'city': '广州', 'tier': '一线', 'avg_salary_before_tax': 11200, 'rent_1br': 2300, 'food_monthly': 2500, 'transport_monthly': 250, 'utilities_monthly': 380, 'other_monthly': 1200, 'house_price_per_sqm': 30000},
        {'city': '杭州', 'tier': '新一线', 'avg_salary_before_tax': 12300, 'rent_1br': 2200, 'food_monthly': 2400, 'transport_monthly': 220, 'utilities_monthly': 350, 'other_monthly': 1100, 'house_price_per_sqm': 32900},
        {'city': '成都', 'tier': '新一线', 'avg_salary_before_tax': 10000, 'rent_1br': 1850, 'food_monthly': 1800, 'transport_monthly': 150, 'utilities_monthly': 280, 'other_monthly': 900, 'house_price_per_sqm': 14700},
        {'city': '武汉', 'tier': '新一线', 'avg_salary_before_tax': 10100, 'rent_1br': 1950, 'food_monthly': 1900, 'transport_monthly': 160, 'utilities_monthly': 290, 'other_monthly': 950, 'house_price_per_sqm': 14500},
        {'city': '南京', 'tier': '新一线', 'avg_salary_before_tax': 10900, 'rent_1br': 2100, 'food_monthly': 2200, 'transport_monthly': 200, 'utilities_monthly': 320, 'other_monthly': 1000, 'house_price_per_sqm': 27500},
        {'city': '西安', 'tier': '新一线', 'avg_salary_before_tax': 8900, 'rent_1br': 1650, 'food_monthly': 1700, 'transport_monthly': 140, 'utilities_monthly': 260, 'other_monthly': 800, 'house_price_per_sqm': 15500},
        {'city': '重庆', 'tier': '新一线', 'avg_salary_before_tax': 8500, 'rent_1br': 1400, 'food_monthly': 1700, 'transport_monthly': 150, 'utilities_monthly': 270, 'other_monthly': 850, 'house_price_per_sqm': 12800},
        {'city': '苏州', 'tier': '新一线', 'avg_salary_before_tax': 10600, 'rent_1br': 2200, 'food_monthly': 2300, 'transport_monthly': 210, 'utilities_monthly': 330, 'other_monthly': 1050, 'house_price_per_sqm': 21000},
        {'city': '长沙', 'tier': '新一线', 'avg_salary_before_tax': 9100, 'rent_1br': 1650, 'food_monthly': 1800, 'transport_monthly': 150, 'utilities_monthly': 270, 'other_monthly': 850, 'house_price_per_sqm': 9800},
        {'city': '青岛', 'tier': '二线', 'avg_salary_before_tax': 8000, 'rent_1br': 1750, 'food_monthly': 1800, 'transport_monthly': 150, 'utilities_monthly': 280, 'other_monthly': 800, 'house_price_per_sqm': 17500},
        {'city': '大连', 'tier': '二线', 'avg_salary_before_tax': 7400, 'rent_1br': 1550, 'food_monthly': 1700, 'transport_monthly': 130, 'utilities_monthly': 290, 'other_monthly': 750, 'house_price_per_sqm': 14500},
        {'city': '厦门', 'tier': '二线', 'avg_salary_before_tax': 10300, 'rent_1br': 2400, 'food_monthly': 2000, 'transport_monthly': 180, 'utilities_monthly': 300, 'other_monthly': 900, 'house_price_per_sqm': 39000},
    ]
    df = pd.DataFrame(cities_data)
    df['monthly_expenses'] = df['rent_1br'] + df['food_monthly'] + df['transport_monthly'] + df['utilities_monthly'] + df['other_monthly']
    return df


def estimate_after_tax(salary_before_tax):
    """Simplified after-tax estimation (same as project methodology: ~80%)."""
    if salary_before_tax <= 5000:
        return salary_before_tax * 0.97
    elif salary_before_tax <= 8000:
        return salary_before_tax * 0.9
    elif salary_before_tax <= 17000:
        return salary_before_tax * 0.8
    elif salary_before_tax <= 30000:
        return salary_before_tax * 0.75
    else:
        return salary_before_tax * 0.7


df = load_data()

# --- UI ---
st.title("🏙️ 城市生活成本计算器")
st.markdown("输入你的税前月薪，看看在不同城市每月能剩多少钱、多少年能买房。")
st.divider()

# Sidebar inputs
with st.sidebar:
    st.header("⚙️ 参数设置")
    salary_input = st.number_input(
        "税前月薪（元）",
        min_value=3000,
        max_value=100000,
        value=10000,
        step=1000,
        help="输入你的税前月薪，系统将自动估算税后收入"
    )
    
    selected_cities = st.multiselect(
        "选择城市对比",
        options=df['city'].tolist(),
        default=['北京', '成都', '杭州', '长沙'],
        help="选择 1-15 个城市进行对比"
    )
    
    st.divider()
    st.markdown("**计算说明**")
    st.caption("• 税后收入按简化模型估算（约 80%）")
    st.caption("• 支出数据使用各城市平均水平")
    st.caption("• 买房按 90㎡全款计算")

if not selected_cities:
    st.warning("请至少选择一个城市")
    st.stop()

# Calculate results
after_tax = estimate_after_tax(salary_input)

results = []
for _, row in df[df['city'].isin(selected_cities)].iterrows():
    expenses = row['monthly_expenses']
    disposable = after_tax - expenses
    savings_rate = disposable / after_tax if after_tax > 0 else 0
    house_total = row['house_price_per_sqm'] * 90
    years_to_buy = house_total / (disposable * 12) if disposable > 0 else float('inf')
    
    results.append({
        '城市': row['city'],
        '等级': row['tier'],
        '税后月薪': f"¥{after_tax:,.0f}",
        '月均支出': f"¥{expenses:,.0f}",
        '可支配收入': disposable,
        '存款率': savings_rate,
        '买房年限(90㎡)': years_to_buy,
        '房租': row['rent_1br'],
        '餐饮': row['food_monthly'],
        '交通': row['transport_monthly'],
    })

result_df = pd.DataFrame(results)

# Display metrics
st.subheader(f"💰 税前 ¥{salary_input:,} → 税后约 ¥{after_tax:,.0f}")

# Key metrics in columns
cols = st.columns(len(selected_cities))
for i, (_, row) in enumerate(result_df.iterrows()):
    with cols[i]:
        delta_color = "normal" if row['可支配收入'] > 0 else "inverse"
        st.metric(
            label=f"{row['城市']} ({row['等级']})",
            value=f"¥{row['可支配收入']:,.0f}",
            delta=f"存款率 {row['存款率']*100:.1f}%",
            delta_color=delta_color
        )

st.divider()

# Comparison table
st.subheader("📊 详细对比")

display_df = result_df[['城市', '等级', '税后月薪', '月均支出']].copy()
display_df['可支配收入'] = result_df['可支配收入'].apply(lambda x: f"¥{x:,.0f}")
display_df['存款率'] = result_df['存款率'].apply(lambda x: f"{x*100:.1f}%")
display_df['买房年限(90㎡)'] = result_df['买房年限(90㎡)'].apply(
    lambda x: f"{x:.1f}年" if x < 999 else "∞"
)

st.dataframe(display_df, use_container_width=True, hide_index=True)

# Bar chart comparison
st.subheader("📈 可支配收入对比")
chart_df = result_df[['城市', '可支配收入']].copy()
chart_df = chart_df.set_index('城市')
st.bar_chart(chart_df, color='#4ade80')

# Expense breakdown
st.subheader("🍕 支出构成")
expense_df = result_df[['城市', '房租', '餐饮', '交通']].copy()
expense_df = expense_df.set_index('城市')
st.bar_chart(expense_df)

# Footer
st.divider()
st.caption("数据来源：2025年公开数据整理 | [GitHub 仓库](https://github.com/harryhu321/city-cost-of-living-analysis)")
