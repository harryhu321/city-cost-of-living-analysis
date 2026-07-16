"""
城市生活成本分析工具函数
Utility functions for city cost of living analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi


def calculate_disposable_income(df, salary_col='avg_salary_after_tax',
                                 rent_col='rent_monthly', food_col='food_monthly',
                                 transport_col='transport_monthly',
                                 utilities_col='utilities_monthly',
                                 other_col='other_monthly'):
    """
    计算每月可支配收入
    Calculate monthly disposable income
    """
    df['monthly_expenses'] = df[rent_col] + df[food_col] + df[transport_col] + \
                             df[utilities_col] + df[other_col]
    df['disposable_income'] = df[salary_col] - df['monthly_expenses']
    df['savings_rate'] = df['disposable_income'] / df[salary_col]
    return df


def plot_radar_chart(city_data, cities, categories, figsize=(10, 10)):
    """
    绘制多城市雷达图对比
    Plot radar chart for multi-city comparison
    """
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, polar=True)
    
    # 角度
    angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
    angles += angles[:1]
    
    colors = plt.cm.Set2(np.linspace(0, 1, len(cities)))
    
    for i, city in enumerate(cities):
        values = city_data[city_data['city'] == city][categories].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=city, color=colors[i])
        ax.fill(angles, values, alpha=0.1, color=colors[i])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    plt.title('各城市生活成本维度对比', size=14, fontweight='bold', pad=20)
    
    return fig


def plot_cost_breakdown(df, cities, cost_cols, figsize=(12, 6)):
    """
    绘制各城市支出堆叠柱状图
    Plot stacked bar chart for cost breakdown
    """
    plot_data = df[df['city'].isin(cities)].set_index('city')[cost_cols]
    
    ax = plot_data.plot(kind='bar', stacked=True, figsize=figsize, 
                        colormap='Set2', edgecolor='white')
    
    plt.title('各城市月度支出构成对比', fontsize=14, fontweight='bold')
    plt.ylabel('金额（元/月）', fontsize=11)
    plt.xlabel('城市', fontsize=11)
    plt.xticks(rotation=0)
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    
    return ax.figure


def plot_salary_vs_cost(df, x_col='avg_salary_after_tax', y_col='monthly_expenses',
                        size_col=None, figsize=(10, 7)):
    """
    收入 vs 支出散点图
    Scatter plot: salary vs expenses
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if size_col:
        sizes = df[size_col] / df[size_col].max() * 500
        scatter = ax.scatter(df[x_col], df[y_col], s=sizes, alpha=0.6, c='steelblue')
    else:
        scatter = ax.scatter(df[x_col], df[y_col], s=100, alpha=0.6, c='steelblue')
    
    # 添加城市标签
    for idx, row in df.iterrows():
        ax.annotate(row['city'], (row[x_col], row[y_col]),
                   xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    # 添加对角线（收入=支出）
    max_val = max(df[x_col].max(), df[y_col].max()) * 1.1
    ax.plot([0, max_val], [0, max_val], 'r--', alpha=0.5, label='收入=支出线')
    
    plt.xlabel('平均税后月薪（元）', fontsize=11)
    plt.ylabel('月均生活支出（元）', fontsize=11)
    plt.title('各城市收入 vs 支出对比', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    
    return fig


def calculate_cost_index(df, reference_city='北京'):
    """
    计算生活成本指数（以某城市为基准=100）
    Calculate cost of living index relative to reference city
    """
    ref_value = df[df['city'] == reference_city]['monthly_expenses'].values[0]
    df['cost_index'] = df['monthly_expenses'] / ref_value * 100
    return df


def plot_affordability_ranking(df, metric='disposable_income', top_n=15, figsize=(12, 8)):
    """
    绘制城市性价比排名
    Plot city affordability ranking
    """
    ranked = df.sort_values(metric, ascending=True).tail(top_n)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    colors = ['#2ecc71' if x > 0 else '#e74c3c' for x in ranked[metric]]
    bars = ax.barh(ranked['city'], ranked[metric], color=colors, alpha=0.8)
    
    # 添加数值标签
    for bar, val in zip(bars, ranked[metric]):
        width = bar.get_width()
        ax.text(width + 50, bar.get_y() + bar.get_height()/2,
                f'{val:,.0f}', va='center', fontsize=10)
    
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.xlabel(f'{metric}（元/月）', fontsize=11)
    plt.title(f'各城市月度可支配收入排名（Top {top_n}）', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    
    return fig
