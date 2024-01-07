import pandas as pd

# 加载Excel文件
file_path = 'hair-review-body-elreport.xlsx'  # 使用您上传的文件路径
df = pd.read_excel(file_path)

# 过滤条件：
# 1. 'valence_avg', 'pos_dichotomous', 'star_rating' 必须是数字或NaN
filtered_df = df.copy()
filtered_df['valence_avg'] = pd.to_numeric(df['valence_avg'], errors='coerce')
filtered_df['pos_dichotomous'] = pd.to_numeric(df['pos_dichotomous'], errors='coerce')
filtered_df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')

# 填充NaN为-1
filtered_df['pos_dichotomous'].fillna(-1, inplace=True)

# 保留只有有效数字的行
filtered_df = filtered_df.dropna(subset=['valence_avg', 'pos_dichotomous', 'star_rating'])

# 提取所需的列
output_data = filtered_df[['valence_avg', 'pos_dichotomous', 'star_rating', 'review_id']]

# 格式化输出
formatted_output = output_data.apply(lambda row: f"{row['valence_avg']} {int(row['pos_dichotomous'])} {int(row['star_rating'])} {row['review_id']}", axis=1)

# 打印格式化后的数据
for line in formatted_output:
    print(line)

print("998967483 1 1")
