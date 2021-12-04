# rtthread_software_package_list_show

## 简介

这个是用来生成RTTHREAD官方的软件包的一个小脚本，生成的样式参考   [rtthread_softlist](rtthread_softlist.md)

## 用法

先用命令把官方packages下下来，并且更新到最新的版本

```
git submodule init
git submodule update --remote
```

安装python3.X版本，在命令行里面输入命令

```
python update_softpackage.py
```

即可更新软件包

## PR

这个是个初期版本，欢迎PR修改。

后续可以提供多个样式版本，方便生成不同的head头标题。



