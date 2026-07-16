# 中国城市生活成本与性价比分析 | City Cost of Living Analysis
<div align="center">

![生活成本排名](images/01_cost_ranking.png)

![收入vs支出性价比](images/04_salary_vs_cost.png)

**💰 税前1万，在各城市分别能剩多少钱？**

</div>


<div align="center">

![Python](https://img.shields.io/badge/Python-Data_Analysis-blue.svg)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib_Plotly-green.svg)
![Cities](https://img.shields.io/badge/覆盖城市-15+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**💰 税前1万，在各城市分别能剩多少钱？**

用数据说话，帮你选择最适合的城市发展

</div>

## 📖 项目简介 | About

对于应届生和职场人来说，「去哪个城市发展」是人生重要决策之一。本项目从**生活成本、收入水平、买房压力、性价比**等多个维度，对中国主要城市进行系统性对比分析。

This project provides a comprehensive comparison of cost of living, salaries, and housing affordability across major Chinese cities, helping you make more informed career and relocation decisions.

### 🎯 核心问题
- 各城市生活成本到底差多少？
- 工资高就一定存得多吗？
- 哪个城市性价比最高？
- 攒钱买房，各城市分别需要多少年？
- 不同人群适合去哪些城市？

## 📊 分析维度 | Analysis Dimensions

| 维度 | 说明 |
|------|------|
| 🏠 **生活成本排名** | 房租、餐饮、交通、水电等月度支出对比 |
| 📈 **收入 vs 支出** | 各城市税后工资与生活成本对比，算性价比 |
| 💰 **可支配收入** | 每月到底能存下多少钱？存款率排名 |
| 🏘️ **买房压力** | 各城市全款买房需要攒多少年 |
| 🎯 **多维度雷达图** | 重点城市全方位对比 |
| 💡 **城市选择建议** | 不同人群的城市推荐 |

## 🏆 部分结论预览 | Highlights

> ⚠️ 以下为示例数据结论，完整分析请运行 Notebook

- **性价比之王**：长沙、成都、重庆 —— 收入中等但生活成本低，存款率高
- **搞钱首选**：深圳、上海、北京 —— 薪资天花板最高，但生活压力也最大
- **均衡之选**：广州、杭州 —— 收入不错，压力比北上深小一截
- **买房最容易**：长沙、重庆、西安 —— 房价相对友好，定居压力小

## 📁 项目结构 | Project Structure

```
city-cost-of-living-analysis/
├── notebooks/
│   └── city_cost_analysis.ipynb  # 完整分析报告
├── data/
│   └── README.md                 # 数据来源说明
├── src/
│   └── utils.py                  # 可视化工具函数
├── images/                       # 分析图表（运行后生成）
├── requirements.txt              # 依赖包
└── README.md
```

## 🛠️ 技术栈 | Tech Stack

- **数据处理**：Pandas, NumPy
- **可视化**：Matplotlib, Seaborn, Plotly
- **分析方法**：描述性统计、指数计算、多维度对比

## 🚀 快速开始 | Getting Started

```bash
# 1. 克隆项目
git clone https://github.com/你的用户名/city-cost-of-living-analysis.git
cd city-cost-of-living-analysis

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行 Notebook
jupyter notebook notebooks/city_cost_analysis.ipynb
```

## 📋 数据来源 | Data Sources

项目内置示例数据，真实数据推荐来源：

| 数据类型 | 推荐来源 |
|---------|---------|
| 生活成本 | [Numbeo](https://www.numbeo.com/cost-of-living/) |
| 平均工资 | 国家统计局、各城市人社局 |
| 房价租金 | 中国房价行情网、链家 |
| 交通成本 | 各地地铁/公交官网 |

详细数据收集说明见 [data/README.md](./data/README.md)

## 📈 可视化预览 | Visualizations

- 各城市生活成本排名柱状图
- 支出构成堆叠图（房租/餐饮/交通占比）
- 重点城市多维度雷达图
- 收入 vs 支出散点图
- 可支配收入/买房压力排名
- （更多图表运行 Notebook 查看）

## 💡 适用场景 | Use Cases

- 应届生/求职者选择城市
- 考虑换城市工作的打工人
- 数据分析练习项目
- 数据可视化参考
- 社交媒体内容创作素材

## 🤝 如何贡献 | Contributing

欢迎贡献！你可以：

- ⭐ Star 支持一下
- 🐛 提交 Issue 反馈问题
- ✏️ 补充更多城市数据
- 🎨 优化可视化效果
- 📝 补充更多分析维度

## 📝 免责声明 | Disclaimer

- 项目数据为公开数据整理和估算，仅供参考
- 具体薪资因行业、公司、个人能力差异很大
- 选择城市请结合行业机会、家庭、个人偏好等综合考虑

---

<div align="center">

**觉得有用的话点个 Star 支持一下吧 ⭐**

*用数据，看清每个城市的真实生活成本*

</div>
