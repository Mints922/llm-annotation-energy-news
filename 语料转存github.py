import pandas as pd
import os

# 创建必要的目录结构
def create_directories():
    dirs = ['corpus/raw', 'corpus/annotated']
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)

# 处理单个文档
def process_document(row):
    doc_id = row['ID']
    
    # 保存原始文本
    with open(f'corpus/raw/{doc_id}.txt', 'w', encoding='utf-8') as f:
        f.write(row['title'] + '\n\n' + row['content'])
    
    # 保存标注文本
    with open(f'corpus/annotated/{doc_id}.txt', 'w', encoding='utf-8') as f:
        f.write(row['annotated'])

# 修改 main 函数中的读取 Excel 部分
def main():
    # 读取Excel文件时转换日期格式
    df = pd.read_excel('meta_data_with_annotated_uniformed.xlsx')
    
    # 将时间戳转换为字符串格式
    df['year'] = df['year'].astype(str)
    
    # 处理每个文档
    for _, row in df.iterrows():
        process_document(row)
    
    # 生成元数据CSV
    df[['ID', 'title', 'year', 'source', 'place', 'place_detail', 'genre']].to_csv(
        'corpus/raw/metadata.csv', index=False
    )

if __name__ == '__main__':
    main()