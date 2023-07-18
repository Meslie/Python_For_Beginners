# 字典
linux_command = {'lscpu':'lscpu命令来自英文词组“list the CPU architecture”的缩写，其功能是用于显示CPU架构信息。lscpu命令会从/proc/cpuinfo文件中收集有关本机CPU架构的信息，并整理成易读的格式输出到Shell终端，运维人员可以很方便地了解到本机CPU数量、架构、线程、核心、套接字等重要指标信息。',
                 'lsmod':'lsmod命令用于显示已经加载到内核中的模块的状态信息。 执行lsmod命令后会列出所有已载入系统的模块。linux操作系统的核心具有模块化的特性，因此在编译核心时，务须把全部的功能都放入核心。可以将这些功能编译成独立的模块，待需要时再分别载入。',
                 'lsblk':'lsblk命令来自英文词组“list block devices”的缩写，其功能是用于查看系统的磁盘使用情况。',
                 'wget':'wget命令来自英文词组“web get”的缩写，其功能是用于从指定网址下载网络文件。wget命令非常稳定，一般即便网络波动也不会导致下载失败，而是不断地尝试重连，直至整个文件下载完毕。 wget命令支持如HTTP、HTTPS、FTP等常见协议，可以在命令行中直接下载网络文件。',
                 'git':'git命令的功能是用于管理分布式版本控制系统，是著名的Git版本控制系统的客户端，能够敏捷高效地处理任何或大或小的代码项目。Git是Linus Torvalds为了帮助管理Linux内核项目而开发的一个开放源代码的版本控制系统，因其开源及去中心化的理念，与此前常用的CVS、Subversion等版本控制系统有着本质区别，成为了当今最受欢迎的版本控制系统。'}
linux_command['gzip'] = '压缩'

len_linux_command = len(linux_command)
print(len_linux_command)

query = input('请输入您要查询的Linux命令：')
if query in linux_command:
    print(linux_command[query])
else:
    print('暂未收录！本词典已收录：' + str(len_linux_command) +'条词条')