# model_download.py
from modelscope import snapshot_download

model_dir = snapshot_download('qwen/Qwen1.5-7B-Chat', cache_dir='/mnt/workspace/qewen1.5_deploy', revision='master')