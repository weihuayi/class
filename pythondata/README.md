# Python 数据分析课件

## 内容设计的基本原则

总体目标：帮助学生掌握一系列 Python 数据分析用到的基础编程环境和工具

* 强化各种工具的基础数据结构模型和概念
* 强化基础操作
* 课后大量练习


## 主要内容

1. Python 编程环境搭建 (2 节)
1. IPython 基础 (2 节)
1. Python 语法基础 (4 节)
1. Numpy 基础 (6 节)
1. Pandas 数据处理 (6 节)
1. Matplotlib 数据可视化 (4 节)
1. 机器学习基础 (8 节)

## 课件制作工具配置

```
sudo apt install python3-notebook jupyter jupyter-core python3-ipykernel
sudo -H pip3 install jupyter_contrib_nbextensions 
sudo jupyter contrib nbextension install
sudo -H pip3 isntall RISE
```


## 参考文献

1. [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
1. [Python - 100天从新手到大师](https://github.com/jackfrued/Python-100-Days)
1. [可视化Python执行过程](http://www.pythontutor.com/visualize.html#mode=edit)

## Ubuntu 上 Python 数据分析环境的搭建

```
$ sudo apt install git            # 版本控制软件
$ sudo apt install python3        # Python3 自带解释器
$ sudo apt install python3-pip    # Python3 软件包安装、卸载和升级管理器.
$ sudo apt install python3-tk     # Python interface to Tcl/Tk used by matplotlib 
$ sudo apt install ipython3       # 增强 Python3 交互解释器
$ sudo apt install spyder3        # 集成开发环境
$ sudo -H pip3 install numpy          # 多维数组模块
$ sudo -H pip3 install scipy          # 科学计算模块 
$ sudo -H install matplotlib     # 可视化模块
$ sudo -H install pandas         # 数据分析和清洗模块
$ sudo -H pip3 install jupyter # Jupyter-notebook 
$ sudo -H pip3 uninstall prompt-toolkit #解决冲突问题
$ sudo -H pip3 install jupyter_contrib_nbextensions # Jupyter notebook 扩展功能模块
$ sudo jupyter contrib nbextension install # 把扩展功能模块安装入 Jupyter
$ sudo -H pip3 isntall RISE # Jupyter notebook 的幻灯片扩展，可以把 Notebook 转化为 PPT
$ sudo rm ~/.jupyter
```


