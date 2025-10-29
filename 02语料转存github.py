import pandas as pd
import os

# 创建必要的目录结构
def create_directories():
    dirs = ['corpus/raw', 'corpus/annotated']
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)

def process_document(row):
    doc_id = row['ID']
    
    # 保存原始文本
    with open(f'corpus/raw/{doc_id}.txt', 'w', encoding='utf-8') as f:
        f.write(row['title'] + '\n\n' + row['content'])
    
    # 保存标注文本
    with open(f'corpus/annotated/{doc_id}.txt', 'w', encoding='utf-8') as f:
        f.write(row['annotated'])

def main():
    # ⭐ 关键修改：首先创建目录
    create_directories()
    
    # 读取Excel文件
    df = pd.read_excel('原始数据+二级标注+分类.xlsx')
    
    # 将时间戳转换为字符串格式
    df['year'] = df['year'].astype(str)
    
    # 处理每个文档
    for _, row in df.iterrows():
        process_document(row)
    
    # 生成元数据CSV
    df[['ID', 'title', 'year', 'source', 'place', 'place_detail', 'genre']].to_csv(
        'corpus/raw/metadata.csv', 
        index=False,
        encoding='utf-8-sig'
    )
    
    print(f"处理完成！共处理 {len(df)} 个文档")

if __name__ == '__main__':
    main()