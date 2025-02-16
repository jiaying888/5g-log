import pandas as pd
import numpy as np
##数据清洗
# 读取数据
df = pd.read_csv('./my_5g_logs.csv')        
#df.head()
# 提取错误代码（正则表达式版）
#优先匹配 `ERR-\d{4}`---ERR-XXXX四位数字，若未找到则尝试匹配 `NORMAL`。如果两者均未匹配，结果为 `NaN`。
df['error_code'] = df['raw_log'].str.extract(r'(ERR-\d{4}|NORMAL)')  
# 处理缺失值
print("清洗前数据量:", len(df))
df = df.dropna(subset=['error_code'])  # 从df中删除'error_code'列包含缺失值(NaN)的行。
print("清洗后数据量:", len(df))

# 定义错误类型映射
error_mapping = {
    'ERR-1001': '硬件故障',
    'ERR-2003': '信号干扰',
    'ERR-3005': '软件异常',
    'NORMAL': '正常状态'
}
df['error_type'] = df['error_code'].map(error_mapping)   #新增一列'error_type'

# 保存结果
df.to_csv('cleaned_logs.csv', index=False)
print("数据清洗完成！")