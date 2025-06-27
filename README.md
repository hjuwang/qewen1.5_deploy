# 部署大模型qewen1.5

## 环境准备

```
----------------
ubuntu 22.04
python 3.12
cuda 12.1
pytorch 2.3.0
----------------
```

必须要使用python3.12 ,别的版本不太行，容易出问题
使用 python 虚拟环境，避免包冲突

```shell

python3.12 -m venv myvenv

# 激活
source myvenv/bin/activate
```

安装依赖

```shell
pip install -r requirements.txt
```
## 下载模型
 使用魔塔社区的下载函数直接下载
 执行下载脚本
 ```
python model_download.py
 ```

根据模型的大小，下载需要的时间各不相同。  
注意根据自己的环境替换模型的下载目录
![alt text](image.png)

## API 部署


```shell
python api.py
```
![alt text](image-2.png)
同样别忘了替换模型的目录
![alt text](image-1.png)

## 本地接口测试

请求
```
curl -X POST "http://127.0.0.1:6006" \
     -H 'Content-Type: application/json' \
     -d '{"prompt": "你好，请做个自我介绍", "history": []}'
```

响应
```
{
    "response": "您好，我是AI助手，全名通义千问。由阿里云研发，我是一款大型预训练语言模型，专门设计用于理解和生成各语言文本，如对话、写作、问答等。我可以帮助您解答问题、提供信息、进行创作，还能与您进行多轮互动，就像现在这样。在 中，如有任何问题或需要帮助，请随时告诉我，我会尽力提供支持。",
    "status": 200,
    "time": "2025-06-27 11:04:32"
}
```