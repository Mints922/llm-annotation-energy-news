# API Prompt Version 2 (Refined)

**Date:** 2024-10-14 
**Purpose:** Introduce role specification, step-by-step reasoning (思维链), and self-reflection to enhance model interpretability and category accuracy.  
**Model:** Qwen-long 
**Language:** Chinese  
**Interface:** API  
**Output format:** JSON

---

## 1. Overview

This version marks the transition from basic API prompts to structured, multi-layered prompting.  
It introduces:
- Explicit **role assignment** (“你是一个句类标注专家”)  
- **Reasoning chain** (“说明判断理由”)  
- **Self-reflection step** for model verification  
- Unified **JSON output structure**

These modifications were implemented after analyzing systematic errors in V1, particularly the model’s tendency to:
1. Misclassify sentences with overlapping semantic roles;
2. Produce inconsistent label names;
3. Fail to explain decision criteria transparently.

---

## 2. Prompt Template

"""
你是一位资深的数据标注专家，负责对中文文本进行精细的话题-说明结构标注，并依据一套详细的label体系进行分类。请仔细阅读并吸收以下知识文档中关于汉语句式句型的话题-说明标注规范和疑难辨析，这将帮助你精确识别文本中的主题（topic）及其对应的评论（comment），同时理解它们之间的关系（relations）。在此基础上，你还需要掌握一个包含69类标签的体系，这些标签将用于进一步精确描述文本的主题类型和评论特征。请准备就绪后，展示你的学习成果，我们将会通过一系列例句来检验你的标注能力。
**You are a senior data annotation expert, responsible for the Chinese text fine topic-description structure annotation, and according to a set of detailed label system for classification. Please read and absorb the following documentation on the topic of Chinese sentence patterns-specification and problem identification, which will help you to accurately identify the topic of the text and its corresponding comment, and understand the relations between them. On top of this, you'll need to master a system of 69 tags that will be used to describe the topic type and comment characteristics of the text more precisely. When you are ready, please show your learning results. We will check your labeling ability through a series of sample sentences.

已学习的知识文档：
{knowledge_document}

已学习的标签定义：
{label_content}
"""

思维链提示
prompt_thought_chain = """
在分析每个句子时，请按照以下步骤进行思维推理：
1. 识别出句子中的主题部分，考虑它属于哪一种话题类型；
2. 找出与主题直接相关的说明或评论部分，判断其表述的内容；
3. 根据整体语境和先前学习的label类别，决定最合适的标签来描述这段文本的主题-说明关系及特征；
4. 在这一过程中，不断反思并优化你的判断逻辑，确保标注的准确性和深度。
"""
** 1. identify the topic part of the sentence and consider which topic type it belongs to; 2. identify the part of the description or comment that is directly related to the topic and determine what it expresses; 3. decide on the most appropriate label to describe the topic-description relationship and features of the passage, based on the overall context and the previously learned categories of labels; 4. in the process, continually reflect on and optimize the logic of your judgments to ensure the accuracy and depth of labeling.

待标注的句子
sentences = [
    "西北地区拥有大面积可利用清洁能源。",
    "在西北地区发电通常是清洁能源。",
    "2010年，全国多为火力发电。",
    "近年来，太阳能发电技术得到了快速发展。"
]

## 3. Output Format

{
  "topic_type": "T域事/空域",
  "topic_content": "西北地区",
  "comment_type": "C所存",
  "comment_content": "拥有大面积可利用清洁能源"
}

分析：
1. 识别主题部分：“在西北地区发电”，这部分描述了一个特定的地理位置和活动，属于“说地”话题类型。
2. 说明或评论部分：“通常是清洁能源”，这部分提供了对上述活动的具体描述，即发电的类型。
3. 根据整体语境和先前学习的label类别，决定最合适的标签来描述这段文本的主题-说明关系及特征。这里，句子的主题是“西北地区的发电”，说明部分描述了这种发电的性质，即“通常是清洁能源”。因此，这是一个“说地-所为”结构。


## 4. Structural Elements
| Section                | Function                   |
| ---------------------- | -------------------------- |
| **Role Specification** | 定义模型身份与任务范围，增强其遵守标注逻辑的能力。  |
| **Task Instruction**   | 说明输入内容与输出要求，避免模型产生冗余描述。    |
| **Reasoning Chain**    | 要求模型在输出前展示判断思路，提高可解释性。     |
| **Output Format**      | 限制输出结构，方便自动解析与错误分析。        |
| **Self-reflection**    | 促使模型自检结果是否符合语义功能逻辑，减少低级错误。 |


## 5. Known Issues

模型在处理含多重从句或链式结构时，推理链过长，可能超出token限制；
对语义边界模糊类别存在混淆；
自我反思段落在部分情况下生成冗长文本，需后处理截断。
** When the model handles structures containing multiple clauses or chains, the inference chain is too long and may exceed the token limit; there is still confusion about categories with fuzzy semantic boundaries, such as evaluative sentences and co-occurring sentences; self-reflective passages generate lengthy text in some cases, which needs to be truncated by post-processing.

