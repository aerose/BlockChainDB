[TOC]
<font face = "Consolas">


# Simple BloChain DataBase
BCDB,简单的区块链数据库
* 本地部署
* 支持命令行和Web交互

## git获取最新版本(latest version)
`https://github.com/aerose/BlockChainDB.git`

## 项目原理(Introductions)
* 本项目通过BlockChain数据结构构建数据库,每一个数据库为一条私链,通过sha256生成hash,支持的命令为`find` `add` `revoke`
* 依据项目需求,没有配备共识机制
* 在传统数据库的基础上引入了区块链的安全性,但牺牲了部分效率
## 依赖库(Packages)
请安装以下库:
```
sudo pip3 install pycryptodome
sudo pip3 install flask
sudo pip3 install prompt_toolkit
sudo pip3 install python-Levenshtein
sudo pip3 install fuzzywuzzy
```
> 加密算法实现来自`pycryptodome`
Web框架为`flask`
命令行交互界面依赖`prompt_toolkit`
字符串模糊匹配使用Levenshtein Distance算法,实现来自`python-Levenshtein`和`fuzzywuzzy`

## 运行和测试(Install & Usage)
本项目为本地运行的数据库,请获取项目源代码后,在目录下执行:
> windows及Linux均可通过如下命令访问
### Web:
```
...\blockChainDB>python WebServer.py [-h] [-p PORT] [-v]
optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port to listen on,default 5000
  -v, --version         show program's version number and exit
```
随后应该可以通过`http://localhost:5000/`或指定port访问
### 命令行:
> 本项目使用fish Shell风格的代码提示和自动补全
```
...\blockChainDB>python CMDserver.py [-h] [-u USE] [-v]
optional arguments:
  -h, --help         show this help message and exit
  -u USE, --use USE  DB to use
  -v, --version      show program's version number and exit
```
添加`-u`参数成功后可直接进入二级数据库管理界面
可通过`Tab`或输入`help`得到各阶段提示
界面一可用命令:
```text
BCDB>help

    simple BlockChain DataBase Operation Index

    use <DBname>        select the database
    create <DBname>     create a database
    delete <DBname>     delete a database
    showall             show all database names
    q or quit           quit
```
use后进入二级管理界面,以下为支持的命令
```text
DBname>help

    simple BlockChain DataBase Operation Index

    find <str> [-v]     select the msg(<*> to show all)(-v or --verbose show in verbose way)
    add <str>           insert a new msg
    revoke              revoke the latest insert
    q or quit           logout
```
## 数据迁移(Data transfer)
替换`blockChainDB\app\chain_data`中的`data`文件即可
history历史命令文件在同目录下的`history.txt`中,修改历史命令可直接在该文件中操作

## 建议(Suggestions)
* 如需保存数据,请通过正常方式结束程序(Web与CMD界面均有quit接口),否则数据可能无法正常保存
