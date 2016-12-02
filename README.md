Webpy
---
A Simple python web service for IT automation

### 使用

**安装依赖**

```
pip install -r requirements.txt
```

**启动server**

```
cd webpy/web
python app.py <port> # 启动server并在port上监听
```

### handler例子-Jdk7Installer

访问： curl http://<server_url>:<port>/Jdk7Installer?host=<ip>&host=<ip>

### 扩展handler

在handlers里面创建任意的xxxHandler.py文件, 在里面定义好Handler类和Handler的name即可

```
name = xxx

class xxHandler(Handler):
  pass # define your content
  
```

访问： curl <server_url>:<port>/${custom_handler_name}, 如果handler想接受参数，参考Jdk7Installer
>NOTE: ${custom_handler_name} 是在XXXHandler里面的name指定的名字

### 后续计划

考虑增加查询命令，查询帮助等的api

