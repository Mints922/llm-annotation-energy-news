# Prompts Overview

This directory contains the complete prompt series used in large language model (LLM)-based annotation experiments for the *Belt and Road Initiative Energy News Corpus* (11,259 clauses).  
All prompts were written in Chinese and iteratively refined to align with our proprietary functional-syntactic annotation schema (69 sentence classes).

The prompt design evolved across more than one hundred iterations, reflecting a continuous process of **error-driven refinement** and **prompt engineering adaptation** as the project moved from a web-based interface to API-based automated annotation.

---

## 1. Design Background

- **Model:** Qwen-long 
- **Language:** Chinese  
- **Task:** Assign one of 69 functional sentence categories to each input sentence  
- **Output format:** Plain text (web version), structured JSON (API version)  
- **Evaluation accuracy:** 75% after manual verification

The prompts were constructed to guide the model in identifying sentence-level semantic functions rather than syntactic structures.  
This required translating the theoretical annotation schema into operational instructions understandable by the model.

---

## 2. Prompt Evolution Stages

| Stage | Description | File |
|--------|--------------|------|
| **Stage 1. Web-based short prompts** | Early exploratory phase using 2–3 sentence prompts directly entered through the web interface. These prompts defined the basic labeling task without reasoning steps. 
| **Stage 2. API adaptation** | Reformatted prompts for API calls, with clearer task definition, output constraints, and error control. | `api_prompt_v1.md` |
| **Stage 3. Structured reasoning & reflection** | Introduced multi-layered prompting, including role specification, step-by-step reasoning (思维链), and self-evaluation mechanisms to enhance stability and interpretability. | `api_prompt_v2.md` |
| **Stage 4. Category-specific adjustments** | Developed auxiliary prompts to address systematic errors, e.g., ambiguous boundary classes (“共事句”), chained clause structures, and evaluative sentences. | `api_prompt_v3.md` |
/` |
| **Stage 5. Final production version** | The finalized, parameter-stabilized prompt used in large-scale annotation. | `api_prompt_final.md` |

---

## 3. Folder Structure

prompts/
│
├── README.md # This document
│
├── base_prompts/ # Early 2–3 sentence prompts (web input)
│ ├── example_01.md
│ ├── example_02.md
│ └── ...
│
├── api_prompt_v1.md # First API-compatible prompt
├── api_prompt_v2_refined.md # Introduced reasoning and reflection
├── api_prompt_final.md # Final version used in corpus annotation
│
└── error_case_prompts/ # Prompts targeting specific ambiguity types
├── ambiguous_boundary.md
├── chained_structure.md
└── evaluative_sentences.md


---

## 4. Theoretical Alignment

Each prompt is designed to operationalize the functional-syntactic framework developed by Qiu (2013) in her book *汉语话说结构句法学*(The Theory of Topic-Comment Structure Syntax).  
The annotation categories (e.g., 成事句, 致事句, 共事句, 评价句, 所归句) correspond to different **semantic-functional relations** rather than syntactic configurations.

Due to licensing restrictions, only representative examples of the annotation labels are included in this repository.  
Full schema details are available upon reasonable academic request.

---

## 5. Prompt Design Logic

1. **Web-based stage:**  
   - Goal: Test whether the models can understand the classification concept and choose the right model for our task.  
   - Prompt form: 2–3 sentences describing the labeling task and requesting a category output.  
   - Example structure:  
     > 你理解汉语的话题-评论结构吗,你能以小句为基本单元，将小句的内部结构切分并标注为话题-评论吗，你能否根据已有的标注语料，对生语料进行标注？
     "Do you understand the topic-comment structure of Chinese, can you take the clause as the basic unit, cut the internal structure of the clause and label it as topic-comment, can you label the raw corpus according to the existing labeled corpus?"

2. **API stage:**  
   - Goal: Formalize prompt for programmatic batch processing.  
   - Additions: role instruction (“你擅长句子标注”"You are good at labeling clauses"), reasoning chain (“请说明判断理由”), and structured output (JSON).  
   - The iterative improvement focused on controlling ambiguity, stabilizing category naming, and optimizing model interpretability.

3. **Error-focused subprompts:**  
   - Developed based on failure analysis from prior runs.  
   - Each subprompt targets a known weakness (e.g., vague category boundaries, nested clause structures).

---

## 6. Usage Notes

- All prompts are in UTF-8 plain text.  
- For reproducibility, the final API prompt can be directly used with `temperature=0.1` and `top_p=0.1`.  
- Earlier versions are included for methodological transparency but are not optimized for reuse.

---

## 7. Citation

If you use or adapt these prompts in your research, please cite:

> Xingyun Zhang. (2025). *Large Language Models for Functional Sentence Annotation in Chinese Energy News Discourse: An Error-driven Prompt Engineering Approach.*

---

## 8. License and Restrictions

- **Annotation schema:** proprietary; only demonstrative examples provided.  
- **Prompts:** shared under a Creative Commons Attribution-NonCommercial license (CC BY-NC 4.0).  
- **Do not redistribute or repurpose the schema labels without authorization.**

---

*Last updated:* 2025-10-28  
*Maintainer:* Xingyun Zhang, China University of Mining and Technology
*Contact:* X922@cumt.edu.cn
