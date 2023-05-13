"""
你要用大语言对话模型 LLMChat（如 ChatGPT）作为工具与CSV表格交互。
请编写一个预设 messages，实现对用户输入问题的意图判断，
其中意图判断范围为 *[画图任务，在线搜索，离线问答]*，
编写代码实现构建 messages 的过程即可。
"""

import os
import pandas as pd
import openai

openai.organization = os.getenv('OPENAI_ORG_ID')
openai.api_key = os.getenv('OPENAI_API_KEY')


class PromptTask:
    def __init__(self, csv_path):
        """ CSV 表格数据 """
        self.csv_data = pd.read_csv(csv_path)

    def generate_messages(self, input_question):
        """ 生成满足题目的 messages, 提示: 要用到 csv_data 的内容 """
        return []

    def chat(self, messages):
        res = openai.ChatCompletion.create(
          model='gpt-3.5-turbo',
          messages=messages
        )
        return res['choices'][0]['message']['content']


if __name__ == '__main__':
    promptTask = PromptTask('data/PromptTask/demo.csv')
    input_question = '均值是多少'

    messages = promptTask.generate_messages(input_question)
    print(messages)

    result = promptTask.chat(messages)
    print(result)
