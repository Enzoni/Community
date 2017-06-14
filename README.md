# Community

爬取并统计杭州所有地块的占地面积和绿化率。主要原理为从请求到的网页代码中，利用正则表达式提取相关的字段信息，并制表列出。

难点在于观察网页的地址和内容变化规律。一旦掌握这个部分，整个程序的编写就很轻松了。

### 程序源码
`community.py` 完整程序，包括抓取数据和统计模块。内附详细注解。

`statistic.py` 仅统计模块


### 测试环境

* Python 2.7
* Linux Mint 18.1 Cinammon 64-bit
* Kernel 4.4.0-63-generic


### 需要的第三方库（模块）

`PrettyTable`   用于制表

`requests`    这是一个便捷的网络库

我已经Fork了这两个项目，请访问我的主页获取它们。


### 安装第三方库（Windows用户）

#### 方法一：下载解压到本地，手动执行安装脚本

1 下载第三方包，解压

2 在命令提示符里输入cmd，然后用cd进入到第三方包的路径下

3 输入Python setup.py build

4 输入python setup.py install

#### 方法二：利用pip工具安装（可能需要自由的互联网访问）

1 下载安装pip

2 输入 pip install *** 


### 产生的文件

`data.json` 存放json格式的数据，供程序使用

`datatable.txt`用户友好的可读数据表

