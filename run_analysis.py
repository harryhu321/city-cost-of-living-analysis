#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
城市生活成本分析 - 批量生成图表脚本
"""

import sys
import os
import warnings

warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'PingFang SC', 'Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('Set2')

# 导入工具函数
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from utils import (calculate_disposable_income, plot_radar_chart, 
                   plot_cost_breakdown, plot_salary_vs_cost,
                   calculate_cost_index, plot_affordability_ranking)

# ===== 2025年数据 =====
cities_data = [
    # 一线城市
    {'city': '北京', 'tier': '一线', 'avg_salary_before_tax': 13400, 'rent_1br': 4200, 'food_monthly': 3000, 'transport_monthly': 300, 'utilities_monthly': 400, 'other_monthly': 1500, 'house_price_per_sqm': 56500},
    {'city': '上海', 'tier': '一线', 'avg_salary_before_tax': 13700, 'rent_1br': 4000, 'food_monthly': 3200, 'transport_monthly': 350, 'utilities_monthly': 420, 'other_monthly': 1600, 'house_price_per_sqm': 65000},
    {'city': '深圳', 'tier': '一线', 'avg_salary_before_tax': 12800, 'rent_1br': 3700, 'food_monthly': 2800, 'transport_monthly': 280, 'utilities_monthly': 450, 'other_monthly': 1400, 'house_price_per_sqm': 65400},
    {'city': '广州', 'tier': '一线', 'avg_salary_before_tax': 11200, 'rent_1br': 2300, 'food_monthly': 2500, 'transport_monthly': 250, 'utilities_monthly': 380, 'other_monthly': 1200, 'house_price_per_sqm': 30000},
    
    # 新一线城市
    {'city': '杭州', 'tier': '新一线', 'avg_salary_before_tax': 12300, 'rent_1br': 2200, 'food_monthly': 2400, 'transport_monthly': 220, 'utilities_monthly': 350, 'other_monthly': 1100, 'house_price_per_sqm': 32900},
    {'city': '成都', 'tier': '新一线', 'avg_salary_before_tax': 10000, 'rent_1br': 1850, 'food_monthly': 1800, 'transport_monthly': 150, 'utilities_monthly': 280, 'other_monthly': 900, 'house_price_per_sqm': 14700},
    {'city': '武汉', 'tier': '新一线', 'avg_salary_before_tax': 10100, 'rent_1br': 1950, 'food_monthly': 1900, 'transport_monthly': 160, 'utilities_monthly': 290, 'other_monthly': 950, 'house_price_per_sqm': 14500},
    {'city': '南京', 'tier': '新一线', 'avg_salary_before_tax': 10900, 'rent_1br': 2100, 'food_monthly': 2200, 'transport_monthly': 200, 'utilities_monthly': 320, 'other_monthly': 1000, 'house_price_per_sqm': 27500},
    {'city': '西安', 'tier': '新一线', 'avg_salary_before_tax': 8900, 'rent_1br': 1650, 'food_monthly': 1700, 'transport_monthly': 140, 'utilities_monthly': 260, 'other_monthly': 800, 'house_price_per_sqm': 15500},
    {'city': '重庆', 'tier': '新一线', 'avg_salary_before_tax': 8500, 'rent_1br': 1400, 'food_monthly': 1700, 'transport_monthly': 150, 'utilities_monthly': 270, 'other_monthly': 850, 'house_price_per_sqm': 12800},
    {'city': '苏州', 'tier': '新一线', 'avg_salary_before_tax': 10600, 'rent_1br': 2200, 'food_monthly': 2300, 'transport_monthly': 210, 'utilities_monthly': 330, 'other_monthly': 1050, 'house_price_per_sqm': 21000},
    {'city': '长沙', 'tier': '新一线', 'avg_salary_before_tax': 9100, 'rent_1br': 1650, 'food_monthly': 1800, 'transport_monthly': 150, 'utilities_monthly': 270, 'other_monthly': 850, 'house_price_per_sqm': 9800},
    
    # 二线城市
    {'city': '青岛', 'tier': '二线', 'avg_salary_before_tax': 8000, 'rent_1br': 1750, 'food_monthly': 1800, 'transport_monthly': 150, 'utilities_monthly': 280, 'other_monthly': 800, 'house_price_per_sqm': 17500},
    {'city': '大连', 'tier': '二线', 'avg_salary_before_tax': 7400, 'rent_1br': 1550, 'food_monthly': 1700, 'transport_monthly': 130, 'utilities_monthly': 290, 'other_monthly': 750, 'house_price_per_sqm': 14500},
    {'city': '厦门', 'tier': '二线', 'avg_salary_before_tax': 10300, 'rent_1br': 2400, 'food_monthly': 2000, 'transport_monthly': 180, 'utilities_monthly': 300, 'other_monthly': 900, 'house_price_per_sqm': 39000},
]

df = pd.DataFrame(cities_data)

# 计算税后工资
df['avg_salary_after_tax'] = (df['avg_salary_before_tax'] * 0.8).round(0)

# 计算月度总支出和可支配收入
df = calculate_disposable_income(
    df, 
    salary_col='avg_salary_after_tax',
    rent_col='rent_1br',
    food_col='food_monthly',
    transport_col='transport_monthly',
    utilities_col='utilities_monthly',
    other_col='other_monthly'
)

# 计算生活成本指数
df = calculate_cost_index(df, reference_city='北京')

# 计算买房所需年限
df['house_total_price'] = df['house_price_per_sqm'] * 90
df['years_to_buy_house'] = (df['house_total_price'] / (df['disposable_income'] * 12)).round(1)

# 创建输出目录
output_dir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(output_dir, exist_ok=True)

print("=" * 60)
print("城市生活成本分析 - 2025年数据")
print("=" * 60)
print(f"\n覆盖城市: {len(df)} 个")
print(f"城市等级分布:\n{df['tier'].value_counts().to_string()}")

# ===== 1. 生活成本排名 =====
print("\n" + "=" * 60)
print("1. 生活成本排名（月均支出）")
print("=" * 60)
cost_ranking = df.sort_values('monthly_expenses', ascending=False)[
    ['city', 'tier', 'monthly_expenses', 'cost_index', 'avg_salary_after_tax']
].reset_index(drop=True)
cost_ranking.index = cost_ranking.index + 1
cost_ranking.columns = ['城市', '等级', '月均支出', '成本指数(北京=100)', '税后月薪']
print(cost_ranking.to_string())

# 生成图1：生活成本排名
fig, ax = plt.subplots(figsize=(12, 8))
ranked = df.sort_values('monthly_expenses', ascending=True)
tier_colors = {'一线': '#e74c3c', '新一线': '#f39c12', '二线': '#2ecc71'}
colors = [tier_colors[t] for t in ranked['tier']]
bars = ax.barh(ranked['city'], ranked['monthly_expenses'], color=colors, alpha=0.8)
for bar, val in zip(bars, ranked['monthly_expenses']):
    ax.text(val + 50, bar.get_y() + bar.get_height()/2,
            f'{val:,.0f}元', va='center', fontsize=9)
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=label, alpha=0.8)
                   for label, color in tier_colors.items()]
ax.legend(handles=legend_elements, loc='lower right')
plt.xlabel('月均生活支出（元）', fontsize=11)
plt.title('各城市生活成本排名（2025年）', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '01_cost_ranking.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ 已保存: images/01_cost_ranking.png")

# ===== 2. 支出结构分析 =====
print("\n" + "=" * 60)
print("2. 房租收入比")
print("=" * 60)
df['rent_to_income_ratio'] = (df['rent_1br'] / df['avg_salary_after_tax'] * 100).round(1)
rent_ratio = df.sort_values('rent_to_income_ratio', ascending=True)[
    ['city', 'rent_1br', 'avg_salary_after_tax', 'rent_to_income_ratio']
].reset_index(drop=True)
rent_ratio.columns = ['城市', '月房租', '税后月薪', '房租收入比(%)']
print(rent_ratio.to_string())

# 生成图2：支出结构堆叠图
selected_cities = ['北京', '上海', '深圳', '杭州', '成都', '武汉', '长沙', '西安']
cost_cols = ['rent_1br', 'food_monthly', 'transport_monthly', 'utilities_monthly', 'other_monthly']
cost_labels = ['房租', '餐饮', '交通', '水电网', '其他']
df_plot = df[df['city'].isin(selected_cities)].copy()
df_plot = df_plot.rename(columns=dict(zip(cost_cols, cost_labels)))
fig = plot_cost_breakdown(df_plot, selected_cities, cost_labels, figsize=(12, 6))
plt.savefig(os.path.join(output_dir, '02_cost_breakdown.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ 已保存: images/02_cost_breakdown.png")

# ===== 3. 雷达图 =====
radar_cities = ['北京', '上海', '成都', '杭州']
radar_df = df[df['city'].isin(radar_cities)].copy()
radar_dims = ['rent_1br', 'food_monthly', 'transport_monthly', 
              'house_price_per_sqm', 'avg_salary_after_tax']
radar_labels = ['房租成本', '餐饮成本', '交通成本', '房价水平', '收入水平']
for col in radar_dims:
    max_val = radar_df[col].max()
    radar_df[col + '_norm'] = radar_df[col] / max_val * 100
radar_norm_cols = [col + '_norm' for col in radar_dims]
radar_data = radar_df[['city'] + radar_norm_cols]
radar_data.columns = ['city'] + radar_labels
fig = plot_radar_chart(radar_data, radar_cities, radar_labels, figsize=(10, 10))
plt.savefig(os.path.join(output_dir, '03_radar_chart.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ 已保存: images/03_radar_chart.png")

# ===== 4. 收入vs支出散点图 =====
fig = plot_salary_vs_cost(df, x_col='avg_salary_after_tax', 
                          y_col='monthly_expenses', figsize=(10, 7))
plt.savefig(os.path.join(output_dir, '04_salary_vs_cost.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ 已保存: images/04_salary_vs_cost.png")

# ===== 5. 可支配收入排名 =====
print("\n" + "=" * 60)
print("3. 每月可支配收入（存款）排名")
print("=" * 60)
savings_ranking = df.sort_values('savings_rate', ascending=False)[
    ['city', 'tier', 'avg_salary_after_tax', 'monthly_expenses', 
     'disposable_income', 'savings_rate']
].reset_index(drop=True)
savings_ranking['savings_rate'] = (savings_ranking['savings_rate'] * 100).round(1)
savings_ranking.index = savings_ranking.index + 1
savings_ranking.columns = ['城市', '等级', '税后月薪', '月均支出', '月存款', '存款率(%)']
print(savings_ranking.to_string())

fig = plot_affordability_ranking(df, metric='disposable_income', top_n=15, figsize=(12, 8))
plt.savefig(os.path.join(output_dir, '05_disposable_income_ranking.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ 已保存: images/05_disposable_income_ranking.png")

# ===== 6. 买房压力测算 =====
print("\n" + "=" * 60)
print("4. 买房压力排名（90平米全款）")
print("=" * 60)
house_ranking = df.sort_values('years_to_buy_house', ascending=True)[
    ['city', 'tier', 'house_price_per_sqm', 'disposable_income', 'years_to_buy_house']
].reset_index(drop=True)
house_ranking.index = house_ranking.index + 1
house_ranking.columns = ['城市', '等级', '房价(元/平)', '月存款(元)', '全款买房需(年)']
print(house_ranking.to_string())

fig, ax = plt.subplots(figsize=(12, 8))
ranked = df.sort_values('years_to_buy_house', ascending=True)
colors = [tier_colors[t] for t in ranked['tier']]
bars = ax.barh(ranked['city'], ranked['years_to_buy_house'], color=colors, alpha=0.8)
for bar, val in zip(bars, ranked['years_to_buy_house']):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2,
            f'{val}年', va='center', fontsize=9)
legend_elements = [Patch(facecolor=color, label=label, alpha=0.8)
                   for label, color in tier_colors.items()]
ax.legend(handles=legend_elements, loc='lower right')
plt.xlabel('全款买房所需年数（90平米）', fontsize=11)
plt.title('各城市买房压力排名（2025年）', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '06_housing_affordability.png'), dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ 已保存: images/06_housing_affordability.png")

# ===== 总结 =====
print("\n" + "=" * 60)
print("📊 核心结论")
print("=" * 60)

# 性价比最高（存款率最高）
top_savings = df.sort_values('savings_rate', ascending=False).head(3)
print(f"\n💰 存款率最高 TOP3:")
for _, row in top_savings.iterrows():
    print(f"   {row['city']}: {row['savings_rate']*100:.1f}%（月存{row['disposable_income']:.0f}元）")

# 买房最容易
top_house = df.sort_values('years_to_buy_house', ascending=True).head(3)
print(f"\n🏠 买房最容易 TOP3:")
for _, row in top_house.iterrows():
    print(f"   {row['city']}: {row['years_to_buy_house']}年")

# 生活成本最低
low_cost = df.sort_values('monthly_expenses', ascending=True).head(3)
print(f"\n💸 生活成本最低 TOP3:")
for _, row in low_cost.iterrows():
    print(f"   {row['city']}: {row['monthly_expenses']:.0f}元/月")

print(f"\n📁 所有图表已保存到 images/ 目录")
print("=" * 60)
