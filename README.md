## 项目概述
实现5G基站日志的自动化标注系统，包含数据清洗→预标注→质量分析全流程

## 技术亮点
- 正则表达式精准提取设备ID和错误代码
- 基于Label Studio API的自动化流水线

## 快速复现
1. `pip install -r requirements.txt`
2. 运行`python data_cleaning.py`
3. 启动Label Studio并创建项目
4. 运行`python auto_import.py` 导入预标注数据
5. 运行`python visualization.py` 查看故障类型分布饼图
