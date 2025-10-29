import os
from openai import OpenAI
import time


# api_key = "API 密钥"


# 背景知识和标签定义文件路径
label_content_path = r"D:\jupyter-notebook\LLM_RAG_Fine-tune\knowledge\TC_category.txt"
examples_content_path = r"D:\jupyter-notebook\LLM_RAG_Fine-tune\prompt\examples.txt"

# 读取标签定义和示例内容
def read_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read().strip()
        return content
    except UnicodeDecodeError:
        print(f"Failed to read file with {encoding} encoding. Trying gbk...")
        return read_file(file_path, encoding='gbk')

label_content = read_file(label_content_path)
examples_content = read_file(examples_content_path)

# 动态调整 Prompt
def create_dynamic_prompt(sentence, label_content, examples_content, max_length=13000):
    sentence_tokens = len(sentence.split())
    label_tokens = len(label_content.split())
    examples_tokens = len(examples_content.split())

    remaining_tokens = max_length - sentence_tokens

    if remaining_tokens < label_tokens + examples_tokens:
        reduced_examples = examples_content
        while remaining_tokens < label_tokens + len(reduced_examples.split()):
            reduced_examples = reduce_content(reduced_examples)
        
        if remaining_tokens < label_tokens + len(reduced_examples.split()):
            reduced_labels = label_content
            while remaining_tokens < len(reduced_labels.split()) + len(reduced_examples.split()):
                reduced_labels = reduce_content(reduced_labels)
        else:
            reduced_labels = label_content
    else:
        reduced_labels = label_content
        reduced_examples = examples_content

    return f"""
你是一位优秀的数据标注专家，精通汉语语法。

标签列表：
{reduced_labels}

例子列表：
{reduced_examples}

你的任务是根据提供的标签和例子，对给定的句子进行标注。
任务要求：
1. 根据标签规则和例子，对每个句子进行标注。
2. 输出格式为 JSON 字符串，包含原始文本和标注结果。
3. 如果之前的标注结果有误，请严格按用户提供的正确标注结果更正。

你不可以自己创造新标签，否则接受惩罚。

待标注句子：
{sentence}
"""

def reduce_content(content):
    lines = content.split('\n')
    return '\n'.join(lines[:-1])  # 去掉最后一行

# 读取待标注的新语料（TXT文件）
new_sentences_path = r"D:\jupyter-notebook\LLM_RAG_Fine-tune\data\test.txt"
output_path = r"D:\jupyter-notebook\LLM_RAG_Fine-tune\data\annotations_results.txt"


output_dir = os.path.dirname(output_path)
os.makedirs(output_dir, exist_ok=True)

new_sentences = [line.strip() for line in read_file(new_sentences_path).splitlines() if line.strip()]



# 使用模型生成标注结果
start_time = time.time()
with open(output_path, 'w', encoding='utf-8') as output_file:
    for i, sentence in enumerate(new_sentences[:50]):  # 只标注前50条语料
        # 创建动态 Prompt
        sentence_specific_prompt = create_dynamic_prompt(sentence, label_content, examples_content)
        correct_annotation = None
        attempts = 0
        max_attempts = 3  # 设置最大尝试次数

        while correct_annotation is None and attempts < max_attempts:
            try:
                # 调用模型生成标注结果
                completion = client.chat.completions.create(
                    model="qwen2.5-3b-instruct",  # 限时免费
                    messages=[
                        {"role": "system", "content": sentence_specific_prompt},
                        {"role": "user", "content": sentence}
                    ],
                    temperature=0.5,  # 添加温度参数
                    top_p=0.5  # 添加 top_p 参数
                )
                # 假设模型返回的结果是一个包含标注信息的字符串
                annotation = completion.choices[0].message.content
                if not annotation:
                    raise ValueError("Empty annotation received from model.")
                
                # 用户交互部分
                print(f"第 {i + 1} 句: {sentence}")
                print(f"初始标注结果: {annotation}")
                user_input = input("请确认正确（输入 y 表示正确，其他键表示错误）: ")
                if user_input.lower() == 'y':
                    correct_annotation = annotation
                    # 将正确的标注结果添加到 examples_content 中
                    examples_content += f"\n{sentence}\n{correct_annotation}"
                else:
                    attempts += 1
                    if attempts < max_attempts:
                        feedback = input("具体原因和正确结果: ")
                        sentence_specific_prompt += f"\n错误标注结果：{annotation}\n具体原因：{feedback}\n"
                        print(f"标注结果错误，模型将重新生成标注结果。尝试次数：{attempts}")
                    else:
                        print("达到最大尝试次数，跳过此句子。")
                        correct_annotation = f'{{"text": "{sentence}", "error": "Max attempts reached"}}'
            except Exception as e:
                output_file.write(f'{{"text": "{sentence}", "error": "{str(e)}"}}\n')
                correct_annotation = f'{{"text": "{sentence}", "error": "{str(e)}"}}'
                break

        if correct_annotation:
            output_file.write(correct_annotation + "\n")

end_time = time.time()
total_time = end_time - start_time
print(f"标注结果已保存到 {output_path}")
print(f"标注过程总耗时: {total_time:.2f} 秒")