# Reflection Prompt (Final Version)

**Date:** 2025-11-18
**File:** `reflection_prompt.txt`  
**Stage:** Final production version  
**Model:** Qwen-long  
**Language:** Chinese  
**Interface:** API  
**Output format:** JSON  
**Status:** Stable version used for full corpus annotation

---

## 1. Overview

This prompt represents the **final and production-ready version** of the annotation instruction used to guide the large language model (LLM) in performing *functional-syntactic labeling* on the Chinese Belt and Road Energy News Corpus.

Compared with previous iterations, this version integrates:
- Explicit reasoning procedure (“思维推理”)
- Clear step-by-step annotation rules
- Error-prevention guidelines
- Strict JSON-format output
- Reflection-oriented self-check mechanism

It operationalizes the annotation logic required by the functional sentence classification system while ensuring model interpretability and consistency.

---

## 2. Design Features

| Feature | Description |
|----------|-------------|
| **Structured reasoning** | Guides the model to analyze each sentence by decomposing it into sentence-initial and subsequent parts. |
| **Dual structural distinction** | Explicitly defines two core sentence types: topic–comment and subject–predicate. |
| **Semantic-function mapping** | Encourages correspondence between semantic relations and functional labels. |
| **Chain annotation** | Allows multi-predicate or multi-comment labeling (e.g., 话题链 / 主语链). |
| **Error avoidance** | Includes explicit counterexamples and corrections for common model errors. |
| **Reflection-based control** | Directs the model to verify output completeness and conformity to schema constraints. |

---

## 3. Core Prompt Content

The full instruction text is stored in [`reflection_prompt.txt`](./reflection_prompt.txt).  
Below is the **structural outline**:

Each part explicitly maps to an annotation logic layer:
- “思维推理” = reasoning chain
- “标注规则” = task constraints
- “常见错误” = reflection and self-correction
- “限制” = boundary control for schema validity

---

## 4. Usage Notes

- Used in API batch annotation scripts (see `scripts/run_annotation.py`)
- Parameter setting: `temperature=0.1`, `top_p=0.1`
- Input: single Chinese sentence per call  
- Output: structured JSON containing labeled sentence segments
- The prompt must remain in UTF-8 encoding to preserve label characters.

---

## 5. Version Rationale

This version emerged after over 100 iterative refinements:
- **From web prompts:** 2–3 sentence instructions focusing on basic classification  
- **To API V1:** fixed-format labeling output  
- **To API V2:** added reasoning and reflection  
- **To this final reflection prompt:** merged interpretability, constraint enforcement, and self-consistency verification.

---

## 6. Reproducibility & Citation

If you reproduce, adapt, or extend this prompt, please cite:

> Xingyun Zhang. (2025). *Large Language Models for Functional Sentence Annotation in Chinese Energy News Discourse: An Error-driven Prompt Engineering Approach.*

---

## 7. Notes on Intellectual Property

- The **annotation schema** used in this project is proprietary and cannot be distributed.  
- Only the **prompt text** and **corpus metadata** are publicly shared for reproducibility.  
- The labels shown in examples are demonstrative and not exhaustive.

---

*Last updated:* 2025-10-28  
*Maintainer:* Xingyun Zhang, China University of Mining and Technology
*Contact:* X922@cumt.edu.cn