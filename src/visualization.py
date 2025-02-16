##导入库
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.express as px

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

##数据加载与预处理
df = pd.read_csv('cleaned_logs.csv')
#生成统计数据
error_dist = df.groupby('error_type').agg(
    count=('error_type', 'count'),
    example_log=('raw_log', lambda x: x.iloc[0])  # 每个类别取一条示例
).reset_index()

error_dist['percentage'] = (error_dist['count'] / len(df) * 100).round(1)   #计算错误类型占比
#error_dist.head()
#可视化看板--饼图
plt.figure(figsize=(10, 6))
plt.pie(error_dist['count'], 
        labels=error_dist['error_type'],
        autopct='%1.1f%%',
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'],
        explode=(0.1, 0, 0, 0))  # 突出最大占比

plt.title("错误类型分布比例", fontsize=14)
plt.savefig('error_pie.png', dpi=300, bbox_inches='tight')  # 保存为图片
plt.show()