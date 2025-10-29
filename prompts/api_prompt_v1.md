# API Prompt Version 1

**Date:** 2024-10-14
**Purpose:** Convert web-based short prompts into an API-compatible format for automated annotation.  
**Model:** Qwen-long
**Language:** Chinese
**Interface:** API
**Output format:** Plain text / JSON(simplified)

---

This version marks the transition from basic web-based manual prompts to the first API-compatible format.  
It retains a concise structure but introduces fixed input-output formatting for programmatic control.

It includes:
- Explicit **role assignment** (“你是一名数据标注员”)  
- Simple **task instruction** (“请判断以下句子属于哪一类句子”)  
- Preliminary **structured output** (category name only or minimal JSON)

These modifications were implemented after analyzing systematic issues observed in the web-based phase, particularly:
1. Inconsistent label wording (模型输出类别名称不稳定)；
2. Random non-label text (模型输出含多余描述)；
3. Lack of format control (输出难以解析)。

---

## 2. Prompt Template

"""你是一名数据标注员，你要先学习{pdf_content}，再学习{label_content}中所有的标签定义，你的任务是对给定的句子进行二元组功能标注。
标注步骤：

1. 进行话题-说明两部分切分。
   话题是指句首成分，即句子的出发点，是信息中的焦点；说明成分是指除了句首成分后剩下的部分，关于话题成分的描述，是信息结构中的新信息成分。
2. 请按照以下格式返回结果：
   [
     {
       "text": "原始句子",
       "topic": "topic标签内容",
       "comment": "comment标签内容",
       "relations": "话题和后面成分的关系"
     }
   ]

## 3. Output Format

请检查标注结果，如果有错误，请输入错误原因，如果没有错误请输入'无'： 标注错误，正确的标签内容是：{"text": "这本书的内容||非常丰富。", "topic": "T当事/事物", "comment": "C性质", "relations": "T当事/事物-C有生"}
错误标注：{
  "text": "这本书的内容||非常丰富。",
  "topic": "这本书的内容",
  "comment": "非常丰富",
  "relations": "【T材料-C所存】"
}
错误原因：标注错误，正确的标签内容是：{"text": "这本书的内容||非常丰富。", "topic": "T当事/事物", "comment": "C性质", "relations": "T当事/事物-C有生"}
请输入正确的标注（格式：{"text": "原始句子", "topic": "topic标签内容", "comment": "comment标签内容", "relations": "话题和后面成分的关系"}）： 格式：{"text": "这本书的内容||非常丰富。", "topic": "T当事/事物", "comment": "C性质", "relations": "T当事/事物-C有生"}

## 4. Structural Elements

| Section                | Function                  |
| ---------------------- | ------------------------- |
| **Role Specification** | 让模型明白自己是“句类标注专家”，以限定任务范围。 |
| **Task Instruction**   | 指定任务目标与输入句子。              |
| **Output Constraint**  | 要求模型仅输出标签名称，以便API自动化读取。   |

## 5. Known Issues

- 模型在匹配二元标签组时，存在匹配错误，如前例所示；
- 未提供推理说明，导致后续误差难以追踪。