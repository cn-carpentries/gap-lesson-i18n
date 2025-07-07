---
title: GAP中的函数
teaching: 40
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- 使用命令行进行原型
- 创建函数
- 从文件读取 GAP 代码

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 函数作为重新使用代码的方式

::::::::::::::::::::::::::::::::::::::::::::::::::

只是为了提醒我们注意我们的任务：为了一个有限的小组 _G_， 我们想要计算
其元素的平均顺序(即： 其元素
的订单总和除以该组的订单)。

我们首先采取一种非常直截了当的做法，对有关群体的所有内容进行反复反复反复的
：

```gap
S:=SymmetricGroup(10);
```

```output
Sym( [ 1 .. 10 ] )
```

```gap
sum:=0;
```

```output
0
```

```gap
为 g in S do
  和 := 和 + 订单；
od；
sum/Size(S)；
```

```output
39020911/3628800
```

现在假定我们想要保存这个GAP代码片段，然后
为其他一些组重复这个计算方法。 We may even reformat it to fit
it into one line and use a double semicolon to suppress the output of `sum`:

```gap
sum:=0;;对于S do sum:= 和+ 订单;od;sum/Size(S);
```

```output
39020911/3628800
```

现在我们可以轻松地复制并将其粘贴到我们下次需要的全球行动纲领会议上。
But here we see the first inconvenience: the code expects that the group in question
must be stored in a variable named `S`, so either we have to reset `S` each
time, or we need to edit the code:

```gap
S:=AlternatingGroup(10)；
```

```output
Alt( [ 1 ... 10 ] )
```

```gap
sum:=0;;对于S do sum:= 和+ 订单;od;sum/Size(S);
```

```output
2587393/259200
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 这仅适用于快速的原型

- 可能意外复制并粘贴代码的一部分，
  不完整的输入可能会触发中断循环；
- 甚至更危险：人们可能会忘记在新的
  计算之前将 'sum' 重置为 0 并获得不正确的结果；
- 该组可能有一个不同的变量名称，所以代码必须更改
  ；
- **是最后的，但不是最少：** 当GAP 代码粘贴到解释器中，它会被直线评估为
  。 If you have a long file with many commands, and a syntax error is
  in line _N_, this error will be reported only when GAP completes
  the evaluation of all preceding lines, and that might be quite time-consuming.

::::::::::::::::::::::::::::::::::::::::::::::::::

That is why we need to give our GAP code more structure by organising it
into functions:

- 函数先解析，后来可能被调用；
- 任何**语法**错误将在解析阶段被检测到，而不是在调用
  时被检测到；
- functions may have local variables, and this prevents them
  being accidentally overwritten just because of reusing the same name of the
  variable to store something else.

以下函数使用一个参数 `G` 并计算元素的平均顺序

```gap
AvgOrdOfGroup := 函数(G)
局部总和；
sum := 0；
用于G do
  和 := 和 + 订单；
od；
退还苏姆/Size(G)；
结束
```

```output
函数 (G ) ... 结束
```

现在我们可以将它应用到另一个小组，将该小组作为一个理由：

```gap
A:=AlternatingGroup(10)；AvgOrdOfGroup(A)；时间；
```

```output
Alt( [ 1 ... 10 ]
2587393/259200
837
```

上面的示例也演示了 `time` - 这是存储上次命令所花费的
CPU 时间的变量。

因此，我们现在可以创建新组，并重新使用 `AvgOrdOfGroup` 来计算它们在同一GAP 会话中的元素的平均
顺序。 Our next goal is to make it
reusable for calculations in future sessions.

Using a text editor (for example, the one that you may have used for previous
Software Carpentry lessons), create a text file called `avgord.g` containing
the following function code and comments (a good chance to practise using them!):

```gap
###################################################################
#
# AvgOrdOfGroup(G)
#
# 计算G元素的平均顺序 其中，G意味着
# 是一个组，但事实上可能是任何包含
# 乘数顺序
#
AvgOrdOfGroup := function(G)
local sum, g;
和 := 0;
G do
  和 := 和 + 订单;
od;
return sum/Size(G);
结束
```

现在开始一个新的 GAP 会话并创建另一个小组，例如`MathieuGroup(11)`：

```gap
M11：=MathieuGroup(11)；
```

```output
群组(1,2,3,4,5,6,7,8,9,10,11)(3,7,11)(4,10,56)])
```

很明显，`AvgOrdOfGroup` 在本次会议上没有定义，因此尝试
调用此函数会导致错误：

```gap
AvgOrdOfGroup(M11);
```

```error
错误，变量: 'AvgOrdOfGroup' 必须有一个值
在 *stdin 第 2 行上没有任何函数*
```

要可用，首先应该使用函数`Read`加载它。 在
下，我们假定文件在当前目录中，所以不需要路径。

```gap
读取("avgord.g")；
```

这将文件加载到GAP中，并且函数`AvgOrdOfGroup` 现在是
可用的：

```gap
AvgOrdOfGroup(M11);
```

```output
53131/7920
```

在这个使用 `Read`， 一个新的 GAP 会话已经开始，以明确
在 `Read` 通话之前不存在`AvgOrdOfGroup` 并且从文件中加载了
。 然而，仍然存在着这种情况。 一个函数类似的文件可以在同一个GAP 会话中读取多次
次(稍后你会看到重新读取
文件更复杂的情况)。 调用 `Read` 再次执行正在读取的文件
中的所有代码。 This means that if the code of the function has been modified, and
it has no errors (but possibly has warnings), the function will be
overwritten. **永远不要忽略警告！**

例如，让我们编辑文件并替换行

```gap
返回sum/Size(G)；
```

通过故意语法错误的行：

```gap
返回 Float(sum/SizeG)；
```

现在读取此文件

```gap
读取("avgord.g")；
```

并且您将看到一个错误消息：

```error
语法错误：) 预期在 avgord.g 第 7 行
返回 Float(sum/Size(G)；
^。
```

由于出现错误，我们会话中的`AvgOrdOfGroup`函数不是
重新定义。 并保持与上次成功阅读相同的版本：

```gap
Print(AvgOrdOfGroup)；
```

```output
函数 (G )
    为G do
        和 := 和 + 订单 (g )；
    od；
    退还金额 / Size( G )；
结束
```

现在通过添加缺失的结尾括号来纠正错误，
再次读取文件并重新计算`M11`元素的平均顺序：

```gap
Read("avgord.g");
AvgOrdOfGroup(M11);
```

```output
6.70846
```

现在让我们看到一个_警告_的例子。 因为它只是一个警告，它将为
重新定义函数，这可能会导致一些意外结果。 To see what
could happen, first edit the file to roll back the change in the type of the
result (so it will return a rational instead of a float), and then comment
out two lines as follows:

```gap
AvgOrdOfGroup := 函数(G)
# 本地总和, g;
# 总和 := 0;
用于G do
  和 := 和 + 订单；
od；
退还苏姆/Size(G)；
结束
```

现在，当你阅读该文件时，你会看到警告：

```gap
读取("avgord.g")；
```

```error
Syntax error: warning: unbound global variable in avgord.g line 4
for g in G do
       ^
Syntax error: warning: unbound global variable in avgord.g line 5
  sum := sum + Order(g);
       ^
Syntax error: warning: unbound global variable in avgord.g line 5
  sum := sum + Order(g);
             ^
Syntax error: warning: unbound global variable in avgord.g line 7
return sum/Size(G);
          ^
```

这些警告意味着，因为`g` 和 `sum` 没有被声明为 `local`
变量， 当被调用的
函数时，GAP将期望它们成为全局变量。 因为他们在 `Read`
被调用时不存在，所以显示了警告。 However, if they happened to exist
by that time, there would be no warning, and any call to `AvgOrdOfGroup` would
overwrite them! 这表明
声明本地变量是多么重要。 让我们稍微了解一下
发生了什么：

The function is now redefined, as we can see from its output (or can
inspect with `PageSource(AvgOrdOfGroup)` which will also display any comments):

```gap
Print(AvgOrdOfGroup)；
```

```output
函数 (G )
    为G do
        和 := 和 + 订单 (g )；
    od；
    退还金额 / Size( G )；
结束
```

但试图运行它会导致中断循环：

```gap
AvgOrdOfGroup(M11);
```

```error
Error, Variable: 'sum' must have an assigned value in
  sum := sum + Order( g ); called from
<function "AvgOrdOfGroup">( <arguments> )
 called from read-eval loop at line 24 of *stdin*
you can 'return;' after assigning a value
brk>
```

你可以使用 'quit;' 退出那里。

下一步发生的情况说明事情可能发生错误：

```gap
sum:=2^64; g:=[1];
```

```output
18446744073799551616
[ 1 ]
```

```gap
AvgOrdOfGroup(M11);
```

```output
18446744073709604747/7920
```

```gap
总和；g;
```

```output
1844674407309604747
(1,2)(3,10,5,6,8,9)(4,7,11)
```

Now, before reading the next part of the lesson, please
revert the last change by uncommenting the two commented lines, so that
you have initial version of `AvgOrdOfGroup` in the file `avgord.g` again:

```gap
AvgOrdOfGroup := 函数(G)
局部总和；
sum := 0；
用于G do
  和 := 和 + 订单；
od；
退还苏姆/Size(G)；
结束
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 路径

- 重要的是要知道如何在所有运行
  系统中指定文件路径，以及在哪里找到您的主页和当前目录。

- 非常有用的是知道
  激活路径和文件名补全，按两四次按Esc键。

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 命令行对原型输入很好；函数对重复计算很好。
- 信息函数名称和注释将使代码更易于自身和其他人阅读。
- 请注意未申报的本地变量！

::::::::::::::::::::::::::::::::::::::::::::::::::


