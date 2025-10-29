# llm-annotation-energy-news
Labeling Sentence Types and  Intrasentential Structure in Energy News Using LLMs


This repository provides the replication materials for the study:

> **LLM-based Semantic–Functional Annotation of Chinese Energy News under the Belt and Road Initiative**  
> *Nebula*  
> Submitted to *Lingua* (2025)

---

## 🧩 Project Overview

This project investigates how large language models (LLMs) can perform **complex semantic–functional sentence annotation** 
based on a linguistically grounded classification system proposed by Qiu (2013, *The Theory of Topic-Comment Structure Syntax*).  
The study focuses on Chinese news reports concerning **energy cooperation under the Belt and Road Initiative (BRI)**, 
and demonstrates that with proper prompt design, an LLM can learn to recognize and annotate nuanced topic–comment 
and semantic–functional sentence categories without explicit machine-learning training.

The annotation process is conducted using the **Qwen-long ** model via API calls, followed by **human verification** 
based on Qiu’s theoretical framework.

---

## 📊 Corpus Summary

- **Documents:** 185  
- **Sentences:** 11,259  
- **Total Characters:** 517,024 (Chinese)  
- **Time Span:** 2016–2024  
- **Sources:** 60+ online news outlets, including *People’s Daily*, *Xinhua News Agency*, and *Economic Daily*  
- **Annotation Accuracy:** 75% (Qwen-long + full human verification)  

The corpus was **automatically segmented** using *spaCy* (Chinese model), and preprocessed to remove duplicates, HTML tags, and headlines.  
The texts were officially published on  
[https://www.yidaiyilu.gov.cn/](https://www.yidaiyilu.gov.cn/).

---

## 🧠 Annotation Framework

The annotation system is based on Qiu’s (2013) *The Theory of Topic-Comment Structure Syntax*, emphasizing **functional roles and semantic relationships** 
within the clause.  
It defines **69 distinct sentence types**, such as:

| Category (示例类别) | Function / Semantic Role |
|--------------------|--------------------------|
| 成事句 (eventive clause) | Describes the completion or realization of an event |
| 施动句 (agentive clause) | Highlights the agent performing an action |
| 所归句 (attributive clause) | Indicates the state or result attributed to an entity |
| 评价句 (evaluative clause) | Expresses assessment or judgment |

Each sentence undergoes **two levels of analysis**:  
1. **Sentence-level classification** (determining clause type and functional role)  
2. **Intra-sentence role labeling** (identifying semantic participants, such as agent, patient, or cause)

This dual-layer design allows linguistic and pragmatic structures to be jointly represented.

---

##  Model and Technical Configuration

The main annotation experiments were performed using the **Qwen-long** model through API access.  
Model selection was based on preliminary testing across several LLMs; *Qwen-long* showed the strongest ability to distinguish Chinese topic–comment contrasts and maintain theoretical consistency across multiple turns.

**Model configuration:**

```yaml
model: qwen-long
temperature: 0.1
top_p: 0.1
input_max_tokens: 10000
output_max_tokens: 8192

##  Corpus Information
- **Corpus name:** Belt and Road Energy News Corpus (一带一路能源新闻语料)
- **Source:** Official Belt and Road portal and affiliated Chinese media
- **Total text length:** 517,024 Chinese characters  
- **Number of annotated sentences:** 11,259  
  - 主谓句 (subject–predicate): 3,394  
  - 话说句 (topic–comment): 7,379  
- **Model used:** Qwen-long
- **Accuracy:** ~75% after manual verification  
- **Annotation language:** Chinese  
- **Annotation goal:** Identify sentence-level semantic and functional types within discourse chains.

---

## Four-Layer Prompt Framework

| Layer | Function | Description |
|-------|-----------|-------------|
| **Layer 1 — Discourse Type Identification** | Sentence-level differentiation | Distinguish topic–comment vs. subject–predicate sentences |
| **Layer 2 — Internal Clause Segmentation** | Structure division | Split each sentence into discourse-relevant segments |
| **Layer 3 — Segment-Level Role Labeling** | Semantic function labeling | Label roles such as agent, patient, cause, result, evaluation, etc. |
| **Layer 4 — Sentence-Type Classification** | Hierarchical sentence classification | Assign final class (e.g., 成事句, 致事句, 评价句, etc.) |

This layered approach allows controlled information flow and hierarchical reasoning—**similar to discourse-, syntax-, and word-level augmentations** in dependency-based dialogue models, but adapted for semantic function analysis in Chinese.

---

## Repository Structure

LLM-Semantic-Annotation/
│
├── data/
│ ├── raw/ # Raw Belt and Road energy news texts
│ ├── processed/ # Cleaned and segmented corpus
│ ├── annotated/ # Final LLM-labeled and verified corpus
│
├── prompts/
│ ├── layer1_discourse_type.txt
│ ├── layer2_segmentation.txt
│ ├── layer3_role_labeling.txt
│ └── layer4_sentence_type.txt
│
├── scripts/
│ ├── preprocess.py # Data cleaning and segmentation
│ ├── run_annotation.py # Execute multi-layer LLM annotation
│ ├── evaluate.py # Accuracy evaluation and error analysis
│
├── notebooks/
│ └── annotation_demo.ipynb # Example notebook for interactive annotation
│
├── config.yaml # Model and environment configuration
├── requirements.txt # Dependencies for environment setup
├── LICENSE
└── README.md


---

## Environment Setup

### 1. Create a Python environment
```bash
conda create -n llm-annotation python=3.10
conda activate llm-annotation

### 2. Install dependencies
pip install -r requirements.txt

### 3. (Optional) Configure model API
model:
  name: qwen-long
  temperature: 0.1
  max_tokens: 2048
api:
  provider: openai-compatible
  endpoint: https://api.xxx.com/v1
  key: your_api_key_here

from openai import OpenAI
import yaml

# Load config
config = yaml.safe_load(open("config.yaml"))
client = OpenAI(api_key=config["api"]["key"], base_url=config["api"]["endpoint"])

prompt = open("prompts/layer4_sentence_type.txt").read()
response = client.chat.completions.create(
    model=config["model"]["name"],
    messages=[{"role": "user", "content": prompt}],
    temperature=config["model"]["temperature"]
)
print(response.choices[0].message["content"])

## Reproducibility Statement

All experiments in this repository are fully replicable using:

The four-layer prompt templates provided in /prompts/;
The same LLM model configuration (Qwen-long 72B);
The provided Belt and Road Energy News Corpus (processed version);
Deterministic decoding (temperature=0.1).
Each layer’s output can be independently verified and manually corrected.
The full pipeline achieves approximately 75% annotation accuracy after human verification.

## Citation
If you find this work useful, please cite our paper:

@inprogress{yourname2025llmsemanticannotation,
  title={Leveraging Large Language Models for Hierarchical Semantic Annotation: A Case Study on the Belt and Road Energy News Corpus},
  author={Your Name},
  year={2025},
  institution={Nanjing Normal University}
}

## Contact
For any questions or feedback, please contact Xingyun Zhang at x922@cumt.edu.cn.
author: Xingyun Zhang
date: 2025-10-27
license: MIT
url: https://github.com/xingyunzhang/LLM-Semantic-Annotation
email: <EMAIL>
institution: China University of Mining and Technology

## License
This project is licensed under the MIT License.
Corpus data is shared academic use only.