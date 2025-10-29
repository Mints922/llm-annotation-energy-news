# API Prompt Version 2 (Refined)

**Date:** 2024-11-17 
**Purpose:** Introduce role specification, step-by-step reasoning (思维链), and self-reflection to enhance model interpretability and category accuracy.  
**Model:** Qwen-long 
**Language:** Chinese  
**Interface:** API  
**Output format:** JSON

---

## 1. Overview
This document provides guidelines for annotating Chinese sentences, emphasizing sentences structures. Annotations prioritize semantic accuracy and preserve original content.

## 2. Core Prompt Content
- T-C Structures: Non-agentive topics (e.g., places, concepts) followed by descriptions of states/processes.
- S-P Structures: Agentive subjects (e.g., entities, persons) with clear action predicates.
- Chains: <topic chain> for multi-comment topics; <subject chain> for multi-predicate subjects; <interleaved chain> for alternating T/S.

Base annotations on semantics; avoid altering text.

## 3. Prompt Template

"""
你精通汉语话题-说明结构和主谓结构识别，擅长句子标注。
#核心思维推理
话题-说明结构与主谓结构的识别是标注工作的关键。话题-说明结构中的话题通常为非施事角色（如地理名词、抽象概念等），后续部分用于描述话题。主谓结构通常包含施事角色和明确动作谓语。
话题链表示连续说明一个或多个话题，主语链表示一个主语连接多个谓语，交错链表示话题和主语交替出现，各自连接说明或谓语部分。
标注应基于句义进行，保持语义-功能对应关系。严禁添加或删除原句内容。

#标注规则：
1.链式结构： 句子含有多个说明或谓语部分时，使用<话题链>、<主语链>或<交错链>，体现逻辑结构。
2.话题-说明结构识别： 当句子的主语为非施事角色，且主要描述状态、过程或性质，应标注为T-C结构。使用 {TC_category_7}文档中的分类进行推理标注。
3.主谓句识别： 当句子中主语具有强动作性（如国家、机构、具体人等）且执行明确动作，应标注为主谓结构（如{施动句}）
3.标注一致性与准确性： 标注必须保持原句内容，不得增删或修改，避免改变句意。
4.结构识别顺序：
-优先识别 计价/计数句>值得/情理句>说时/说地句>所存句>可能句>能力句>揣测句。

#常见错误与纠正：
错误 1：误将话题-说明结构标注为施动句： 非施事角色的句子，应优先考虑话题-说明结构。避免误标为施动句。
纠正示例：<话题链>{事物状态句} 哈欧班列【T当事/事物】||从哈尔滨出发【C状态】。
错误 2：遗漏多个说明部分。
纠正：为每个说明部分标注，并使用 <主语链> 或 <话题链>，如 <话题链2>。
错误 3：不当增删信息： 标注仅基于句子原始内容。任何额外解释应避免。
纠正：仅标注句子原始内容，保持原句不变。
错误 4：不同功能小句统一标注。
纠正：根据语义功能分别标注不同的小句，如 {施动句} 和 {事物性质句}。
错误 5：误标共事句。
纠正：共事句需满足话题与说明部分复指关系，如“黑山，中国未来的伙伴”可标注为共事句，否则则为其他类型。
错误6：短语内部切分。
纠正：短语内部不需要切分，一个短语可以是一个语义角色，如“
<话题链>{致事句} 泰国东北部成品油管道项目完工后【T致事】，将极大缩短成品油交货周期，节约物流成本，提高输量并保持油品供给的稳定性【C结果】。”
错误7：切分失误如{施动句}中方【S施动】||援助的太阳能路灯维修项目开工仪式在中非共和国首都班吉举行
纠正：识别语义重心，正确切分是“{成事句}中方援助的太阳能路灯维修项目开工仪式【T成事】在中非共和国首都班吉举行【C制作】。”

#特殊标注说明：
1.背景信息标注： 时间、地点等背景性信息，若后面的部分不是对其的说明，应视为描述背景
-示例：{说时句} 日前【D独立语/插入】||清洁能源【T当事/事物】形势大好【C状态】。
2.共事句定义与区分规则：
- 共事句：句首施事在后续部分有语义复指关系时，标注为共事句。
- 区分规则：无复指关系且句子表达具体施事行为时，标注为施动句。
- 示例：<共事句>“中国，我去过这里”有复指关系，标注为共事句。相反，“山东省同马雷市签署了协议”应标注为施动句。
3.交错链使用场景：当句子包含交替出现的多个话题和主语时，使用 <交错链> 标识。
-示例：清洁能源是未来的发展方向，中国政府在积极推动政策。
-标注：<交错链>{事物性质句} 清洁能源【T当事/事物】||是未来的发展方向【C性质】，{施动句} 中国政府【S施动】||积极推动政策【V所动】。

#输出格式：
1.标注格式为<链条标记> {句型类别} 话题/主语部分【标记】||说明/谓语部分【标记】。
2.对于包含多个链条的小句，使用 <链条标记> {句型类别}。
#标注示例：
-输入：我们要支持绿色能源发展。
-输出：{施愿句} 我们【S施愿】||要支持绿色能源发展【V所愿】。

-输入：随着巨轮汽笛鸣响，项目实现首船天然气出口。
-输出：<话题链>{事物状态句2} 随着【D独立语】巨轮【T当事/事物】||汽笛鸣响【C状态】，项目【T当事/事物】||实现首船天然气出口【C状态】。

-输入：中国与阿盟签订协议。
-输出：{施动句} 中国【S施动】||与阿盟签订协议【V所动】。
"""

## 4. Rules
1. Chain Structure: When a sentence contains multiple explanatory or predicative components, use <Topic Chain>, <Subject Chain>, or <Interleaved Chain> to reflect the logical structure.

2. Topic-Comment Structure Identification: When the subject is non-agentive and primarily describes state, process, or property, annotate as a T-C structure. Apply classification from the {TC_category_7} document for inference annotation.

3. Predicate-Subject Sentence Identification: When the subject exhibits strong agency (e.g., nation, institution, specific person) and performs a clear action, annotate as a predicate-subject structure (e.g., {agentive sentence}).

## 5. Known Issues

### Performance Issues
- Excessive prompt length and redundancy
- Extended model response time due to prompt complexity

### Documentation Structure
- Error cases should be moved to a error case repository rather than embedded in the prompt

### Model Behavior Control
- Insufficient constraints on model outputs
- Model occasionally mismatches binary label pairs
- Model fails to maintain consistent label relationships

### Label Generation Issues
- Model tends to generate non-existent labels by inferring from the 69 existing categories
- Need stricter constraints on label vocabulary

### Required Improvements
- Add explicit constraints in prompt to control model outputs
- Implement strict label pair matching rules
- Limit label generation to predefined categories only
- Optimize prompt length and structure