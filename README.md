# 记录我的所有配置文件内容

## 带做事项
- 一件安装所有配置以及应用
- 可配置性的记录文件应该去哪个位置
- 自动下载安装我需要用到的软件

## 实现方式
1. 创建一个可能叫做元数据的文件 configs.toml ？名字可能会换掉
2. 创建一个命令名比如说叫 sconfig
3. 对于需要同步文件或目录可以使用  

## Usage
添加目录或文件作为同步记录
```sh
scofig add <config_group> <fold | file>
```
将会在 configs.toml 记录一条内容比如
```toml
[configs.uv]
bck_path = ".config" # 备份指定的位置
```