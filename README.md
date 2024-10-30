# 配置管理器
帮你记录你所有工具的配置内容信息

## Usage
### 打开工具管理界面
```bash
$ sconfig
```
执行命令后会打开一个终端的管理界面，左边记录了添加的工具列表，右边记录的工具配置的路径

### 添加工具的配置路径
```bash
$ sconfig add <tool_name> <config_path>
# Options:
# --only <os_type> # 只适用于某个系统 目前计划按照支持ubuntu,macOS,Windows
```

### 删除工具某个配置路径
```bash
$ sconfig remove <tool_name>
```


### 同步配置
会将本地的配置同步到个人的github仓库中
```bash
$ sconfig sync
```

具体实现方法: 判断git仓库的commit情况，有过有新的则会从git上pull下来，反正如果本地有新的内容将会从push到git上