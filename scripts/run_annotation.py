#!/usr/bin/env python3.10
# run_annotation_safe.py
# Secure annotation loop for Qwen-long 
# Requirements: OpenAI
# note:原句标注

import os
import time
from openai import OpenAI
import json
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


api_key = "API密钥" 
client = OpenAI(
    api_key=api_key, 
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def read_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read().strip()
        return content
    except UnicodeDecodeError:
        logging.warning(f"Failed to read file with {encoding} encoding. Trying gbk...")
        return read_file(file_path, encoding='gbk')

# Prompt
static_prompt = """
你精通汉语话题-说明结构和主谓结构识别，擅长句子标注。
思维推理：
1. 句子由句首部分和后续部分构成。
2. 句子分为话题-说明类型和主语-谓语类型。
3. 句首和后续存在语义-功能对应关系。
4. 话题链=话题+多个说明部分；主语链=主语+多个谓语。
5. 强化句义理解，对应语义-功能标注句子。
6. 输出json格式。

标注规则：
1. 主谓句通常包含一个明显的施事和动作，施事包括国家、机构、人称等。
2. 如果句子包含多个说明部分或谓语部分，每个部分都需要单独标注。
3. **仅标注给定句子的内容，不要添加额外的信息，主语缺失可以补主语。**
4. **确保标注结果与原始句子完全一致，除缺失主语外不要添加或修改原始句子的内容。**

常见错误及正确标注：
1. 错误：将主谓句误标为话题-说明结构。
   正确：确保主谓句中有明显的施事和动作，如“中国政府推动了经济改革”应标注为主谓句。
2. 错误：遗漏多个说明部分的标注、任意断句。
   正确：确保每个说明部分或谓语都单独标注，如<主语链3>“我们【S施愿】要着眼长远【V所愿1】、把握机遇【V所愿2】、乘势而上【V所愿3】”应标注为多个谓语部分；
   如<话题链3>“这【T当事/事件】是中阿友好合作新的历史起点【C性质1】，标志着双方关系进入了一个新的阶段【C性质2】”应标注为多个说明部分。
3. 错误：标注时添加额外的信息。
   正确：仅标注给定句子的内容，不要添加额外的信息。
4. 错误：标注时任意断句、补充主语。
   正确：确保每个句子不再切分，<话题链2>俄罗斯【T当事/事物】是中国最大邻国和全面战略协作伙伴【C性质1】，也是开展各领域合作的重要优先合作伙伴【C性质2】。
限制：
1. 不要改动标签关系匹配。
2. 不要增加标签中没有的定义。
3. 不可以匹配标签中不存在的二元组关系。
""" 

# 动态创建 Prompt
def create_initial_prompt(label_content, examples_content):
    return f"""
标签内容:
{label_content}

示例内容:
{examples_content}
"""

def create_sentence_prompt(sentence):
    return f"""
待标注句子：
{sentence}
"""


def main():
    label_file_path = r"D:\jupyter-notebook\TC_category_7.txt"
    examples_file_path = r"D:\jupyter-notebook\examples_7.txt"
    
    label_content = read_file(label_file_path)
    examples_content = read_file(examples_file_path)
    
    new_sentences = [line.strip() for line in read_file(r"D:\jupyter-notebook\energy_corp\2018-14.txt").splitlines() if line.strip()]
    
    output_file_path = r"D:\jupyter-notebook\energy_corp\\2018-14.json"
    
    batch_size = 10
    num_batches = (len(new_sentences) + batch_size - 1) // batch_size
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
       
        initial_prompt = create_initial_prompt(label_content, examples_content)
        system_message = {
            "role": "system",
            "content": static_prompt + initial_prompt
        }
        
        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, len(new_sentences))
            batch_sentences = new_sentences[start_idx:end_idx]
            
            for sentence in batch_sentences:
                sentence_specific_prompt = create_sentence_prompt(sentence)
                try:
                    completion = client.chat.completions.create(
                        model="qwen-long",
                        messages=[
                            system_message,
                            {"role": "user", "content": sentence_specific_prompt}
                        ],
                        temperature=0.1,
                        top_p=0.1
                    )
                    annotation = completion.choices[0].message.content.strip()
                    
                    annotation = annotation.replace('```json', '').replace('```', '').strip()
                    #logging.info(f"Generated annotation for sentence '{sentence}': {annotation}")
                    output_file.write(f'{annotation}\n')
                except Exception as e:
                    logging.error(f"Error generating annotation for sentence '{sentence}': {e}")
                
    print("results are saved")

if __name__ == "__main__":
    main()
