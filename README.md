# Community

爬取并统计杭州所有地块的占地面积和绿化率。
### 程序源码
`community.py` 主程序，包括抓取数据和统计

`statistic.py` 仅统计模块


### 测试环境

* Python 2.7
* Linux Mint 18.1 Cinammon 64-bit
* Kernel 4.4.0-63-generic


### 需要的第三方库

* PrettyTable
* requests


### 安装第三方库（Windows用户）

#### 方法一

1 下载第三方包，解压

2 在命令提示符里输入cmd，然后用cd进入到第三方包的路径下

3 输入Python setup.py build

4 输入python setup.py install

#### 方法二

1 下载安装Pip

2 输入 pip install ***


### 产生的文件

`data.json` 存放json格式的数据，供程序使用

`datatable.txt`用户友好的可读数据表

