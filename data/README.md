# 数据来源说明 / Data Sources

## 推荐数据来源 / Recommended Sources

### 1. Numbeo（最推荐，全球城市数据）
- **网址**：https://www.numbeo.com/cost-of-living/
- **内容**：全球各城市生活成本指数，包含餐饮、交通、房租、餐饮等
- **优点**：数据全面，可直接下载 CSV
- **覆盖**：中国主要城市都有

### 2. 国家统计局
- **网址**：http://www.stats.gov.cn/
- **内容**：各城市平均工资、CPI、居民消费支出
- **优点**：官方权威数据

### 3. 中国房价行情网
- **网址**：https://www.creprice.cn/
- **内容**：各城市房价、租金数据

### 4. 各城市地铁/公交官网
- 用于收集交通成本数据

## 数据字段建议 / Suggested Columns

| 字段名 | 说明 | 单位 |
|--------|------|------|
| city | 城市名称 | - |
| province | 省份 | - |
| tier | 城市等级（一线/新一线/二线） | - |
| avg_salary | 平均月薪（税后） | 元 |
| rent_1br_city | 一居室房租（市中心） | 元/月 |
| rent_1br_suburb | 一居室房租（郊区） | 元/月 |
| meal_inexpensive | 普通餐厅一餐 | 元 |
| meal_midrange | 中档餐厅两人餐 | 元 |
| public_transport_monthly | 公交地铁月卡 | 元 |
| gasoline | 汽油价格 | 元/升 |
| utilities | 水电网燃气月均 | 元 |
| fitness | 健身月卡 | 元 |
| cinema | 电影票 | 元 |
| apartment_price_city | 市中心房价 | 元/平米 |
| apartment_price_suburb | 郊区房价 | 元/平米 |

## 使用说明 / Usage

1. 收集数据后整理为 CSV 格式
2. 放入 `data/` 目录，命名为 `city_cost_data.csv`
3. Notebook 中替换数据读取路径即可运行
4. 示例数据已内置在 Notebook 中，可直接运行查看效果
