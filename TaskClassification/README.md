# 题目描述

你要用大语言对话模型 LLMChat（如 ChatGPT）作为工具与CSV表格交互。请编写一个预设 messages，实现对用户输入问题的意图判断，其中意图判断范围为 *[画图任务，在线搜索，离线问答]*，编写代码实现构建 messages 的过程即可。

## Tips1：

messages 是 LLMChat 的输入参数，类型为 `list<dict>`，代表历史对话记录，
其中角色参数包含 'user' 和 'assistant'，'user' 代表用户，'assistant' 代表 LLMChat，'content' 代表对应的输入和输出

messages 设计参考如下：

### 示例1：直接提问

```python
message = [
    {
        'role': 'user',
        'content': '<your_prompt with input_question>'
    }
]
```

### 示例2：多轮预设

```python
messages = [
    {
        'role': 'user',
        'content': '<your_prompt>'
    },
    {
        'role': 'assistant',
        'content': '<some_info>'
    },
    ...
    {
        'role': 'user',
        'content': '<input_question>'
    },
]
```


## Tips2：

csv 文件示例为 `data/PromptTask/demo.csv`，简单起见，表格数据可直接嵌入 prompt 中，作为静态文本

### 背景说明：

用 ChatGPT 对 CSV 表格进行综合分析，有些问题可以根据输入表格数值直接回答，
有些问题需要利用表格数据画图显示，还有部分问题与表格数值无关需要在线搜索后总结回复

### 期望效果：

| | 输入 | 输出 |
| - | - | - |
| 示例1 | 今天天气怎么样 | 在线搜索 |
| 示例2 | 表中数据画图显示 | 画图任务 |
| 示例3 | 均值是多少 | 离线问答 |
