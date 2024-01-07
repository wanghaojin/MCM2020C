import pandas as pd

# 加载Excel文件
file_path = 'hair-review-body-elreport.xlsx'  # 替换为您的文件路径
df = pd.read_excel(file_path)

# 过滤条件：
# 1. 'valence_avg' 必须是数字
# 2. 'pos_dichotomous' 必须是数字或空
filtered_df = df[pd.to_numeric(df['valence_avg'], errors='coerce').notna()]
filtered_df['pos_dichotomous'] = pd.to_numeric(df['pos_dichotomous'], errors='coerce')
filtered_df['pos_dichotomous'].fillna(-1, inplace=True)

# 提取所需的列
output_data = filtered_df[['valence_avg', 'pos_dichotomous']]

# 格式化输出
formatted_output = output_data.apply(lambda row: f"{row['valence_avg']} {int(row['pos_dichotomous'])}", axis=1)

# 打印格式化后的数据
for line in formatted_output:
    print(line)
print("998967483 1")
