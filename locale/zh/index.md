---
site: 沙纸：sandpaper_site
---

[GAP](https://www.gap-system.org) 是一个用于离散计算代数的系统，
特别强调计算组理论。 GAP提供一个
编程语言。 a 由数千个函数库组成，实现代数
算法，以GAP语写成，也包括代数
对象的大型数据库， 例如，[小团体图书馆](https://gap-packages.github.io/smallgrp/)
其中除其他外，包括除1024外，2000年最多所有423,164,062组秩序。

这个课程介绍了GAP。 它围绕着一个共同的任务，即
在小群组库中搜索有趣的例子和计数器，
和一个我们将感兴趣的特定研究问题是**找到
非微不足道的群体示例，其元素的平均顺序是一个整数**。

该课程将引导学员沿着路径工作到 GAP 命令
线，并交互探索代数对象，然后将GAP 代码保存到
文件， 创建函数和回归测试，然后执行
全面搜索并通过添加新属性扩展系统。

在这条路上，学习者将熟悉：

- 基本构造GAP编程语言，

- (b) 如何在全球适应行动方案系统中找到必要的信息；和

- 将GAP代码组织成复杂程序的良好设计做法。

::::::::::::::::::::::::::::::::::::::::::  prereq

## 必备条件

The lesson is oriented on learners possessing the minimal theoretical
background (at least at the level of an undergraduate group theory course)
and willing to learn how concepts from abstract algebra may be
explored using computational tools.
不需要先前从事全球评估方案工作的经验。

学习者只需要了解档案和目录
(包括主页和工作目录)的概念，并知道如何启动 GAP。

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  checklist

## 准备好了

1. 在您的主目录中，创建一个新的目录，叫做`avgord`。
2. 启动 GAP：

- 在 Linux 和 macOS 上，打开终端并调用 `path-to your-gap-installation/gap-4.X.Y/gap`
  (路径视需要而定)；
- 在 Windows 上，使用 开始菜单或在 GAP 安装后创建的桌面快捷键
  启动 GAP 。

3. 将当前目录设置为“avgord”：

- 在 Linux 和 macOS 上，调用 `ChangeDirectoryCurrent("/Users/username/avgord");`
  (必要时路径)； 记得键入您主目录
  的完整路径而不是"~"。
- 在 Windows上，调用 `ChangeDirectoryCurrent("C:/Users/username/avgord");`
  (必要时请记得使用`/` 代替`\`)；

4. 验证当前目录设置是否正确：调用 `DirectoryCurrent()`
  并检查输出路径是否指向了 `avgord` 目录。

::::::::::::::::::::::::::::::::::::::::::::::::::


