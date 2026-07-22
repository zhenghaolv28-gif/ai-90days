# Day 01 学习报告
## 投入时间
今天学习了20分钟。
## 今天完成
1.使用codex下载python，vs code，Git

2.学习在Github创建仓库以及README.md,day01/hello.py

3.学会一点python语句

4.根据AI提示，在本地运行Github文件

## 运行证据
### 运行命令：
PS C:\Users\86183> cd E:\AI-Coding\ai-90days
PS E:\AI-Coding\ai-90days> py -3.13 .\day01\hello.py
### 运行结果:
我的名字:Deku
目标岗位:AI应用开发相关岗位
每天学习时间:2-5
90天预计学习时间:180-450

## 我理解的三个知识点
1.当前目录和相对路径
因为day01/hello.py放在E:\AI-Coding\ai-90days里。

2.GitHub远程文件与本地文件
本地没有刷新及网络有问题。

3.Python变量与计算
days保存了学习时间，值为90、min_hours_per_day和min_total_hours分别保存了每天最小学习时间，值为2；90天的最小学习时间总值，值为180。

## 今天遇到的问题
GitHub与本地是两份文件，GitHub的修改不会自动进入本地，需要成功执行git pull；网络故障也会造成拉取失败。

## 我的排查过程
询问AI，然后未操作成功，便自己前往本地文件修改成Github文件一样内容。因为本地有手工修改，AI先使用git stash将修改临时备份，再通过git pull把GitHub的最新版本同步到本地。我目前理解stash相当于临时储物柜，可以防止本地修改丢失；这部分操作暂时还不能独立完成。

## AI提供的帮助
检查并下载python，vs code, Git。

## 我亲自验证的内容
本地运行hello.py文件出错的地方然后前去Github修改，未更新的hello.py的内容。

## 明天计划
根据AI颁布明天任务去进行。