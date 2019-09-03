## python安装依赖

```shell
python -m pip install -r requirements.txt
```

## 启动客户端

```bash
python ./client.py
```

## 启动服务端

```bash
python ./server.py
```

## 编译proto

```shell
python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ mixer_auth.proto
```
