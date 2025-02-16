import pandas as pd
import numpy as np
from label_studio_sdk import Client   #e5ea95f7b959bda252319ea20d2b753fb768c8ef

# 连接本地Label Studio
ls = Client(url='http://localhost:8080', api_key='e5ea95f7b959bda252319ea20d2b753fb768c8ef')

# 获取项目
project = ls.get_project(7)  

# 读取清洗后的数据
df = pd.read_csv('./cleaned_logs.csv')

# 批量导入label studio预标注结果
tasks = []
for _, row in df.iterrows():   #遍历dataframe的每一行
    tasks.append({
        'data': {'raw_log': row['raw_log']},
        'annotations': [{
            'result': [{
                'type': 'choices',
                'value': {'choices': [row['error_type']]},
                'from_name': 'error_type',
                'to_name': 'log'
            }]
        }]
    })
project.import_tasks(tasks)
print(f"成功导入{len(tasks)}条预标注数据！")