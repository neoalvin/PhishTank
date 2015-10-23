开发环境：ubuntu15.04 +MySQL+Python2.7

Docker中运行方式
生成的镜像：172.29.152.190:5000/ubuntu:alvin
运行镜像
cd home
cd phishtank                                                #程序文件路径/home/phishtank
python main.py                                           #运行主程序
根据提示的信息输入相关序号选择执行方式
1-在本机中创建所需数据库（默认已创建）
2-利用已有xml文件执行程序（解析/导入数据库）
3-执行完整程序（下载/解析/导入数据库/定时更新数据）

一.运行方法
1.更改config.py文件中的MySQL设置
2.从项目根目录下启动终端：
python main.py
3.根据给出的响应提示，输入相应序号做出运行程序的相关选择：
    1：创建数据库
    2：利用现有的xml文件直接解析并导入到MySQL中
    3：执行完整的程序

二.模块功能
1.config.py
设置MySQL数据库相关参数

2.dbconfig.py
实现MySQL数据库的相关操作

3.download.py
下载xml文件到本地

4.getphish.py
解析xml文件，提取钓鱼网站相关信息
这里只提取了它的ID，网址，及相关链接

5.main.py
主模块，进行相关测试，并执行最终程序
函数说明：
test_db()                    #测试数据库功能
test_createdb()         #创建数据库
test_download()        #测试下载模块功能
test_xmlread()           #测试xml文件解析模块
xml_to_db()                #将xml中的数据导入到MySQL
do_action()                 #利用现有xml文件执行程序
do_action_main()       #执行完整的程序（下载，解析，导入到数据库）
timer()                        #实现每三小时更新数据

