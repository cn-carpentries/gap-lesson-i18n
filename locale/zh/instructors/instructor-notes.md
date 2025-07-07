---
title: 讲师笔记
permalink: /guide/
---

## A. 总表

- 对于第一课，很好能访问 Windows (VM 或远程桌面) 到
  展示一些适合GAP的窗口特定方面。

- 在启动前，检查每个人都安装了GAP并知道如何启动它。
  还提醒它不建议在带空格的路径中安装，例如
  “我的文档”。

- 学习者理解如何操作位于不同目录中的文件
  非常重要。 `ChangeDirectoryCurrent` 是IO package 的
  函数 (需要强制) 如果
  GAP安装得当，它应该是可用的 (i)。 - 按照
  讲习班的指示安装。 如果出现任何问题，故障排除的第一步是
  以检查`LoadPackage("io");`是否返回 `fail`。 如果是，Windows用户的补救办法
  是输入文件的完整路径。 Linux 和 macOS 用户
  受到的影响小于， 他们应如何启动GAP的方式是
  导航到终端中所需的目录并从那里启动GAP。

- 帮助调整终端设置。 特别向Windows用户显示他们的
  可以永久改变迷你外壳中的颜色和字体(从
  \`gap开始)。 页：1

- 解释如何复制和粘贴输入和输出(尤其是在Windows)。

- 解释如何读取课程页面：GAP输入是没有GAP提示的类型。
  GAP输出为离子蓝色颜色。 错误以红色显示。 GAP promts 不是显示的
  ，除非这真的是必需的(例如演示
  多行输入的工作)。

- It is important that instructor starts GAP with `-r` option to avoid
  interfering with own GAP settings e.g. locally installed packages and
  other content of `.gap` directory.

- 在 GAP 以 "-r" 选项启动时使用颜色提示来忽略所有用户
  首选项(如果设置的话)，调用 `ColorPrompt(true);` 。

## [与 GAP的第一次会议]({% link \_剧集/01-command-line.md %})

- 强调横幅包含有用于引用GAP或
  报告错误的版本信息。 软件包的选择可能不同， 但缺少**IO** 和
  **Browse** 软件包表示这些，或许还有其他一些需要编译的软件包
  没有被编译。

- 第二次调用 `LogTo("logfile");` 不会打开新的文件，但会报告
  GAP 已经登录到另一个文件。 In this case, either ignore it if
  you would like to continue logging to the file already in use, or call `LogTo();`
  to close the current log file and then call `LogTo` with an argument to start
  logging to a new file.

- 显示 `factorial` 的一个错误的示例，并且指出这个错误为
  的时候也会发生。 。某些文件必须读取，或者某些软件包需要加载
  才能定义函数。

- 讨论为什么GAP手册而不是
  使用GAP帮助系统是错误的做法。

- Be aware that help selection screen will look differently if **Browse**
  package is not compiled.

- 解释如何切换到使用 MathJax 支持来查看手册的 HTML 版本。

- 请注意`AsList`和`AsSSortedList`之间的差异。

- 帮助调用 `WriteGapInifile` 和自定义 GAP ，例如 使用浏览器作为
  查看器。

- 演示如何输入 \`Sum( list( elts, order ) / 长度( elts );
  显示如何使用命令行编辑和移动一条线周围的
  来组装此命令。 或许执行部分命令以查看其结果，
  而不是按顺序键入整个命令的顺序。

- 使用 Etherpad 来投票计算列表的平均顺序。
  然后讨论每种情况可能比其他情况更可取的情况。

1. 挑战解决方案: `Filtered( elts, g -> 2^g = 2);` 和
  `Filtered( elts, g -> (1,2)^g = (1,2);`.

## [更多的 GAP 对象]({% link \_some-objects.md %})

- 浮点、圆环形、限定场元素在
  课程中没有被进一步使用，但我们简短地提到它们以表明它们存在。

- Emphasize that organising complex objects into nested records may
  be more efficient than nested lists.

- 请注意，`w:="超口径过剩。IsSubset(w,'s);`
  会导致一个没有方法的错误。 这可能是介绍
  这种特殊类型的错误消息的一个很好的时刻。

- 扩展带有新类型对象的 GAP。 引用了
  [创建新对象](https://docs.gap-system.org/doc/ref/chap79.html)
  和 [Extending the System](https://docs.gap-system.org/doc/ref/chap80.html)
  的 GAP 参考手册。
  而且，[圆包](https://gap-packages.github.io/circle/)
  提供了一个用新的乘数对象扩展GAP的例子。

1. 挑战解决方案:
  `r:=c[1]; i在 [2.. 如果c[i][2]>r[2] r:=c[i]; fi; od; r;`

## [GAP中的函数]({% link \_剧集/03-func.md %})

- 花一些时间处理GAP函数的结构：关键词`function`、
  `local`、`return`、`end`和其他语言构造。

- 告诉如何探索断路循环，同时显示一个错误的
  消息。

## [使用回归测试]({% link \_sourodes/01-command-line.md %})(04-testing.html)

- 学生可能需要帮助格式化考试，因为错误的评论
  和/或不同格式的输出。

- 制作测试文件复现的覆盖面：随机与明确的示例，
  用双分数制止输出等。

- 参考`Test`的其他选项，如比较输出到
  的空格，显示测试进度，等等。

- 提到`TestDirectory`函数来运行一组测试集合。

- 提及描述和代码覆盖工具。

## [小群组搜索]({% link \_剧集/05-small groups.md %})

- 请以一些例子来概括`SmallGroup`、`AllSmallGroups`、`NrSmallGroups`和
  `SmallGroupsInformation`。

- 讨论为什么迭代比AllSmallGroups耗尽记忆力的更好
  (提到自学对象的概念)。

- 一个附带问题是如何将一个由 \`SmallGroup' 返回的 pc 组转换为
  其他表示, 如：permutation 或 fp 组。

- 实时编程是教导如何开发大部分功能
  的首选方式。

1. 挑战的解决方案:
  `Sum(液态([1..2000], n -> 不是 IsPrimePowerInt(n),NrSmallGroups); NrSmallGroups(1536); Last 2-last;`.
  除了`SmallGroup(105,1)`和`SmallGroup(357,1)`以外，另一个
  组是 `SmallGroup(1785,1)`。

## [属性和方法]({% link \_sourodes/06-attributes.md %})

- 为什么宣布`Random`为属性不是一个好主意？

1. 挑战的想法：尝试`k:=1` 然后`k:=k+1;n:=2^k;AvgOrdOfCollection(DihedralGroup(n);time;AvgOrdOfGroup(DihedralGroup(n);time;`。
  即使是 `k=20` ，第一个函数也需要 15 秒和 2 — 在 MacBook Pro 上约为115s
  。


