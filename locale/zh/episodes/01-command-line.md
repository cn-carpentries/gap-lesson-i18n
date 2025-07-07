---
title: 与GAP的第一次会话
teaching: 30
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 节省时间的技巧和方法
- 使用 GAP的帮助系统
- GAP语言中的基本对象和构造

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 使用 GAP 命令行

::::::::::::::::::::::::::::::::::::::::::::::::::

如果正确安装 GAP ，您应该能够启动它。 准确地说，
您如何启动 GAP 将取决于您的操作系统以及您如何安装
GAP。 GAP始于显示系统版本的
和加载组件信息的 \*banner \*，然后显示命令行提示
`gap>`, 例如：

```output

```

要离开GAP，请在GAP提示符中输入 `quit;` 。 请记住，所有 GAP 命令，
包括这个命令，必须用分号完成！ 练习进入
`quit;` 离开GAP，然后开始新的GAP会话。 在继续之前，您
可能希望输入以下命令，以不同颜色显示 GAP 提示和用户输入
：

```gap

```

开始尝试GAP的最简单方式是作为一个计算器：

```gap
( 1 + 2^32 ) / (1 - 2*3*107 );
```

```output
-6700417
```

如果您想记录您在 GAP 会话中所做的事情，那么您可以稍后查看
。 您可以使用 LogTo\` 函数启用日志记录。

```gap
LogTo("gap-intro.log")；
```

This will create a file file `gap-intro.log` in the current directory which
will contain all subsequent input and output that appears on your terminal.
要停止登录，您可以在没有参数的情况下调用 `LogTo` ，例如在 `LogTo();`,
或退出 GAP。 Note that `LogTo` blanks the file before starting, if it
already exists!

It can be useful to leave some comments in the log file in case you
return to it in the future. GAP中的注释以符号`#`开头，
继续到行尾。 您可以在
GAP 提示后输入以下内容：

```gap
# GAP 软件木工课程
```

然后按返回键后，GAP将显示一个新提示, 但评论
将被写入日志文件。

日志文件记录所有与 GAP 的交互，这些交互发生在调用
到 `LogTo` 之后，但不是之前。 如果我们想要将其记录下来，我们可以重复上述
的计算。 Instead of retyping it, we will use the Up and Down
arrow keys to scroll the _command line history_. 重复此操作，直到您再次看到
的公式，然后按返回键(指向
命令中的光标位置不重要)：

```gap
( 1 + 2^32 ) / (1 - 2*3*107 );
```

```output
-6700417
```

您也可以编辑现有的命令。 再次按住，然后使用
左箭头和右箭头键， 删除或后空格来编辑它，并将
32 替换为 64 (其他一些有用的快捷方式是
Ctrl-A和Ctrl-E 来移动光标到
行的开头和结尾。 分别为两部分。 现在按返回键(命令行中的
光标的任何位置)：

```gap
( 1 + 2^64 ) / (1 - 2*3*107 );
```

```output
-18446744073709551617/641
```

It is useful to know that if the command line history is long, one could
perform a partial search by typing the initial part of the command and using
Up and Down arrow keys after that, to scroll only the lines that begin with
the same string.

如果您想要存储一个值以供日后使用，您可以使用`:=`来分配它到一个名称

```gap
universe := 6*7;
```

:::::::::::::::::::::::::::::::::::::::::  callout

## `:=`, `=` 和 `<>`

- 在其他语言中，您可能更熟悉使用 `=`，来分配
  变量，但GAP 使用 `:=`。

- GAP uses `=` to compare if two things are the same (where other languages might
  use `==`).

- 最后，GAP使用`<>`来检查两件事是否不等价(而不是你以前可能看到的`!=`
  )。

::::::::::::::::::::::::::::::::::::::::::::::::::

空格字符(例如) GAP，
除非它们发生在字符串内，否则空间、标签和回归都微不足道。 例如，上一个输入
可以在没有空格的情况下输入：

```gap
(1+2^64)/(1-2*3*107);
```

```output
-18446744073709551617/641
```

白空间符号常用来格式化更复杂的
更好的可读性。 例如，创建3×3矩阵的以下输入：

```gap
m:=[1,2,3],[4,5,6],[7,8,9]]；
```

```output
[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
```

相反，我们可以用三行写我们的矩阵。 In this case, instead of the full prompt
`gap>`, a partial prompt `>` will be displayed until the user finishes
the input with a semicolon:

```gap
gap> m:=[[ 1, 2, 3 ],
> [ 4, 5, 6 ],
> [ 7, 8, 9 ]]；
```

```output
[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
```

您可以使用 "Display" 来预打印变量，包括此矩阵：

```gap
显示(m)；
```

```output
[ 1、2、3]、
  [ 4、5、6]、
  [ 7、8、9]
```

一般而言，GAP函数，如`LogTo`和`Display`，使用括号调用，
包含一个(可能为空的)参数列表。

:::::::::::::::::::::::::::::::::::::::::  callout

## 函数也是 GAP 对象

检查如果您忘记添加括号，
例如输入 `LogTo;` 和 `Factorial;`
我们将稍后解释这些输出中的差异。

::::::::::::::::::::::::::::::::::::::::::::::::::

以下是调用其他GAP功能的一些例子：

```gap
工厂(100)；
```

```output
933266215443944152681699238856670000715968264381621468\
59296389521759999229929915608941463976156518262532569792082\
7223758251185109168640000000000000000000000000
```

(输出的确切宽度将取决于您的终端设置)，

```gap
a. 决定因素(m)；
```

```output
0
```

和

```gap
因子(2^64-1)；
```

```output
[ 3, 5, 17, 257, 641, 65537, 6700417 ]
```

函数可以各种方式合并，可能是
作为其他函数的参数，例如：
`Filtered` 需要一个列表和一个函数，返回
满足该函数的所有元素。
`IsEventInt`, 毫不奇怪, 检查一个整数是否为偶!

```gap
过滤( [2,9,6,3,4,5], IsEvents;
```

```output
[ 2, 6, 4 ]
```

GAP命令行接口的一个有用的节省时间功能是按下 Tab 键时完成标识符的
。 例如，输入 `Fib` ，然后按
按 Tab 键完成输入 `Fibonacci` ：

```gap
Fibonacci(100);
```

```output
354224848179261915075
```

如果无法完成独特的完成，GAP将尝试执行
部分完成， 第二次按下 Tab 键将显示所有可能的
标识符。 试图以 `GroupHomomorphismByImages`
或 `NaturalHomomorphismByNormalSubgroup` 使用补全。

在 GAP 中命名函数的方式有望帮助您记住甚至猜测书库函数的名称
。 如果变量名包含几个字，那么每个单词的
第一个字母都是大写的(记住GAP 是区分大小写的!)。
关于GAP中使用的命名协议的进一步详情，见
[这里的GAP手册](https://docs.gap-system.org/doc/ref/chap5.html#X81F732457F7BC851)。
在`ALL_CAPITAL_LETTERS`中具有名称的函数是内部函数，不是一般用途的
。 小心使用他们！

重要的是要记住，GAP对案件敏感。 例如，下面的
输入导致一个错误：

```gap
阶梯(100)；
```

```error
错误，变量：'因子'必须有一个值
在 *stdin 第 14 行上没有任何函数*
```

因为GAP库的名称是 `Factorial` 。 使用小写
而不是大写，反之亦然也会影响名称补全。

现在让我们考虑以下问题：对于一个有限的组 _G_，计算其元素的
平均顺序 (也就是说，) 其元素的订单总和
除以该组的订单总和)。 从哪里开始？

输入 `?Group` ，您将看到所有的帮助条目，从`Group`开始：

```output
┌──────────────────────────────────────────────────────────────────────────────┐
│   Choose an entry to view, 'q' for none (or use ?<nr> later):                │
│[1]    AutoDoc (not loaded): @Group                                           │
│[2]    loops (not loaded): group                                              │
│[3]    polycyclic: Group                                                      │
│[4]    RCWA (not loaded): Group                                               │
│[5]    Tutorial: Groups and Homomorphisms                                     │
│[6]    Tutorial: Group Homomorphisms by Images                                │
│[7]    Tutorial: group general mapping                                        │
│[8]    Tutorial: GroupHomomorphismByImages vs. GroupGeneralMappingByImages    │
│[9]    Tutorial: group general mapping single-valued                          │
│[10]   Tutorial: group general mapping total                                  │
│[11]   Reference: Groups                                                      │
│[12]   Reference: Group Elements                                              │
│[13]   Reference: Group Properties                                            │
│[14]   Reference: Group Homomorphisms                                         │
│[15]   Reference: GroupHomomorphismByFunction                                 │
│[16]   Reference: Group Automorphisms                                         │
│[17]   Reference: Groups of Automorphisms                                     │
│[18]   Reference: Group Actions                                               │
│[19]   Reference: Group Products                                              │
│[20]   Reference: Group Libraries                                             │
│ > > >                                                                        │
└─────────────── [ <Up>/<Down> select, <Return> show, q quit ] ────────────────┘
```

您可以使用箭头键向上移动，然后按
打开帮助页面。 此练习请先打开 "教程：Groups and Homomomorphisms"
请注意屏幕底部的导航说明。 首先查看
两个页，然后按 `q` 返回选中菜单。 Next, navigate to
`Reference: Groups` and open it. 在头两个页面内你会找到
函数 `Group` 和提到的 `order` 。

GAP manual comes in several formats: text is good to view in a terminal,
PDF is good for printing and HTML (especially with MathJax support) is
very efficient for exploring with a browser. 如果您在
自己的计算机上运行 GAP ，您可以将帮助查看器设置为默认浏览器。 如果您是
在远程机器上运行GAP，那么(可能) 将无法工作。 (见
`?WriteGapInifile` 关于如何使这个设置永久化：

```gap
SetHelpViewer("浏览器");
```

然后再次求助，看看不同之处！

让我们现在复制从 GAP 引用的第一个示例的
手动章节中的下面输入。 它显示如何创建许可协议，并将值分配给变量
。 这是`Reference：Groups`。 You can select it by typing `?11`, where
you replace `11` with whatever number appears before `Reference: Groups` on your machine.

如果您在终端中查看GAP 文档，您可能会发现它有助于
打开两份GAP。 一个用于阅读文档，一个用于写入代码！

本指南展示GAP如何以循环符号写入的活动，以及
显示与组一起使用的常用函数。 另外，在某些地方，一条线末尾使用了两种半科朗
。 这将阻止GAP显示计算结果。

```gap
a:=(1,2,3);b:=(2,3,4);;
```

接下来，让`G` 成为一个由 `a` 和 `b` 生成的组：

```gap
G:=组(a,b);
```

```output
群组(1,2,3)(2,3,4))
```

我们可以探索`G`及其生成器的一些特性：

```gap
Size(G)；IsAbelian(G)；结构说明(G)；命令(a)；
```

```output
12
false
"A4"
3
```

我们的下一个任务是确定如何获得一份`G'元素及其订单的清单。
输入 `?elements` 并探索帮助主题列表。 检查后，
教程中的条目似乎无关，但
参考手册中的条目是相关的。 它还解释了使用 "AsSSortedList"
和 "AsList" 之间的区别。 因此，这是`G\`的要素清单：

```gap
AsList(G);
```

```output
[ (), (2,3,4), (2,4,3), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4),
  (1,3)(2,4), (1,4,2), (1,4,3), (1,4)(2,3) ]
```

返回的对象是 _列表_。 我们想要将它分配给一个变量
来探索和重新使用。 我们在计算时忘了这样做。
课程，我们可以使用命令行历史来恢复最后一个命令，编辑
并再次呼叫。 但我们将使用 `last ` 作为一个特殊变量
，持有由 GAP返回的最后结果：

```gap
elts:=last;
```

```output
[ (), (2,3,4), (2,4,3), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4),
  (1,3)(2,4), (1,4,2), (1,4,3), (1,4)(2,3) ]
```

这是一个列表。 GAP列表的索引来自1。
以下命令是(希望是!) 自解释：

```gap
gap> elts[1]; elts[3]; Length(els);
```

```output
()
(2,4,3)
12
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 列表不止数组

- 可能包含孔或为空

- 可以动态地改变其长度(使用`Add`、`Append`或直接转让)

- 不需要包含同类型的对象

- 查看更多在 [GAP 教程：列表和记录](https://docs.gap-system.org/doc/tut/chap3.html)

::::::::::::::::::::::::::::::::::::::::::::::::::

GAP中的许多功能都指“设置”。 GAP中的一组只是一个恰好有
无重复、无孔和按顺序排列的元素的列表。 以下是一些例子：

```gap
gap> IsSet([1,3,5]); IsSet([1,5,3]); IsSet([1,3,3]);
```

```output
true
false
false
```

Now let us consider an interesting calculation -- the average order of elements
of `G`. There are many different ways to do this, we will consider a few of them
here.

GAP中的 "for" 循环允许您为收藏的每个成员做一些事情。
"for" 循环的一般形式是：

```gap
用于收藏中的val do
  <something with val>
od;
```

例如，要找到我们的组`G`的平均顺序，我们可以做到。

```gap
s:=0;;
for g in elts do
  s := s + 订单(g);
od;
s/Length(els);
```

```output
31/12
```

实际上，我们只能直接在`G`的元素上循环(一般情况下，GAP
会让你在大多数类型的对象上循环)。 我们必须切换到使用 `Size`
而不是 `Length` ，因为群组没有长度！

```gap
s:=0;;
for g in G do
  s := s + 订单(g);
od;
s/Size(G);
```

```output
31/12
```

还有其他循环方式。 例如，我们可以在一个整数范围内循环,
并接受像一个数组那样的 `elts` ：

```gap
s:=0;;
为i in [ 1 .. Length(elts) ] do
  s = s + 订单(elts[i] );
od;
s/Length(els);
```

```output
31/12
```

然而，往往有更加紧凑的方式去做事。 这里是非常简洁的
方式：

```gap
Sum( els, elts, order ) / 长度( elts );
```

```output
31/12
```

让我们来打破这最后一部分：

- `Order`找到单个逗号的顺序。
- `List(L,F)`提供了一个新的列表，其中函数`F`适用于列表中的每个
  成员。
- `Sum(L)`添加了列表`L`的成员。

:::::::::::::::::::::::::::::::::::::::::  callout

## 哪种办法最好？

比较这些方法。 你想使用哪个？

::::::::::::::::::::::::::::::::::::::::::::::::::

GAP有非常有用的列表操作工具。 我们现在将再举几个例子。

有时，GAP没有我们想要的确切功能。
例如，`NrMovedPoints` 给出了允许移动点的数量，
但是如果我们想要找到移动`4`点的所有可调节点怎么办？ 这是
GAP的箭头标记。 `g -> e` 做了一个新函数，它需要一个参数 `g`,
并返回表达式`e`的值。 以下是一些例子：

- 查找没有固定点的 `G` 的所有元素：

```gap
过滤( elts, g -> NrMovedPoints(g) = 4);
```

```output
[ (1,2)(3,4), (1,3)(2,4), (1,4)(2,3) ]
```

- 在`G`中查找一个允许(1,2)到(2,3)

```gap
第一( elts, g -> (1,2)^g = (2,3) )；
```

```output
(1,2,3)
```

让我们来看看这个(请记住，在GAP permutations 是从左向右乘的！)：

```gap
(1,2,3)^-1*(1,2)*(1,2,3)=(2,3);
```

```output
true
```

- 检查`G`的所有元素是否移动点 1 到 2：

```gap
ForAll( elts, g -> 1^g <> 2 );
```

```output
false
```

- 检查`G`中是否有一个元素移动了两点：

```gap
ForAny( elts, g -> NrMovedPoints(g) = 2 );
```

```output
false
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 使用列表操作从`elts`中选择点2的稳定器和permutation的中央化器(1,2)

- `Filtered( elts, g -> 2^g = 2 );`

- `Filtered( elts, g -> (1,2)^g = (1,2) );`

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 记住，GAP是区分大小写的！
- 如果您看到`错误，变量：`函数名称'必须有一个值'，请不要恐慌。
- 注意变量和功能的名称。
- 使用命令行编辑。
- 使用自动补全而不是输入函数和变量的全名。
- 使用 `?` 和 `??` 查看帮助页面。
- 使用 "SetHelpViewer" 将默认帮助格式设为 HTML
- 使用 `LogTo` 函数保存所有 GAP 输入和输出到文本文件。
- 如果计算需要太长时间，请按 <Control>\-C以打断它。
- 从 GAP 教程中读取"第一次使用 GAP"。

::::::::::::::::::::::::::::::::::::::::::::::::::


