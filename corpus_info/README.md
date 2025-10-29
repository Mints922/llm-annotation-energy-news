# 中文新闻语料库

本语料库包含"一带一路"相关新闻文本及其话题-说明结构标注。
The corpus contains "Belt and Road" news articles and their topic-commentary structure annotations.

## 目录结构
corpus/
├── raw/              # 原始新闻文本
│   ├── doc_ .txt     # 单篇新闻原文
│   └── metadata.csv  # 元数据信息
└── annotated/        # 标注文本
│   └── doc_ .txt
└── corpus_description.md
└── README.md


## Data Description

### Raw Text (raw/)
- Contains the complete original text of news articles
- Each article stored separately as a .txt file
- File naming format: doc_XXXX.txt (e.g., doc_0001.txt)

### Metadata (metadata.csv)
Includes the following fields:
- ID: Unique document identifier
- title: News headline- 
- year: Publication date
- source: News source
- place: Region
- place_detail: Specific location
- genre: News category

- ### Annotated Text (annotated/)
- Includes topic-description structure annotation results
- One-to-one correspondence with raw text
- Uses standardized annotation conventions
  
## Corpus Statistics
- Total documents: 185 articles
- Time span: 2016-2024 
- Source Organizations: https://www.yidaiyilu.gov.cn/


- ## Usage Instructions
1. Raw text files can be opened directly with a text editor.
2. Metadata is in CSV format; opening with Excel is recommended.
3. Annotated text contains specific tags; refer to annotation guidelines.

## Copyright NoticeThis 
Corpus is for research purposes only. Commercial use is prohibited.

