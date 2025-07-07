---
title: 小群组搜索
teaching: 40
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- 使用小群组库
- A. 设计一个能够相互配合的职能系统

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 模块化编程：将函数集合在一起。
- 如何检查给定订单的所有组的几个曲目

::::::::::::::::::::::::::::::::::::::::::::::::::

在本节中，我们希望发现一些有趣的
属性的非微不足道的组别： 他们元素的平均顺序是整数。

GAP分布包括一些数据库
(例如) 在
[用GAP分发的软件包列表](https://www.gap-system.org/packages/)中搜索“library”一词。
其中之一是
Hans Ulrich Besche、Bettina Eick和Eamonn O'Brien的[小群组图书馆](https://gap-packages.github.io/smallgrp/)。

这个库提供了多种实用工具来确定哪些信息
存储在那里并提交查询以搜索具有所需的
属性。 关键函数是 `SmallGroup`, `AllSmallGroups`,
`NrSmallGroups`, `SmallGroupsInformation` 和 `IdGroup`。 例如：

```output
gap> NrSmallGroups(64);
267
gap> SmallGroupsInformation(64);

  There are 267 groups of order 64.
  They are sorted by their ranks.
     1 is cyclic.
     2 - 54 have rank 2.
     55 - 191 have rank 3.
     192 - 259 have rank 4.
     260 - 266 have rank 5.
     267 is elementary abelian.

  For the selection functions the values of the following attributes
  are precomputed and stored:
     IsAbelian, PClassPGroup, RankPGroup, FrattinifactorSize and
     FrattinifactorId.

  This size belongs to layer 2 of the SmallGroups library.
  IdSmallGroup is available for this size.

gap> G:=SmallGroup(64,2);
<pc group of size 64 with 6 generators>
gap> AllSmallGroups(Size,64,NilpotencyClassOfGroup,5);
[ <pc group of size 64 with 6 generators>, <pc group of size 64 with 6 generators>,
  <pc group of size 64 with 6 generators> ]
gap> List(last,IdGroup);
[ [ 64, 52 ], [ 64, 53 ], [ 64, 54 ] ]
```

我们想要使用我们自己的测试功能，我们将在这里创建，
使用内嵌符号(可用于一个参数的函数)：

```gap
TestOneGroup := G -> IsInt( AvgOrdOfGroup(G) ;
```

正在尝试，例如

```gap
List([TrivialGroup(),Group(1,2)],TestOneGroup);
```

```output
[ true，fals]
```

```gap
gap> AllSmallGroups(Size,24,TestOneGroup,true);
```

```output
[ ]
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 模块化编程在此开始

为什么返回布尔值是这种函数的一个很好的设计决定，
而不是仅仅打印信息或返回一个字符串，如\`YES'？

::::::::::::::::::::::::::::::::::::::::::::::::::

这是测试给定订单所有组的函数的简单例子。
它一次创建一个组，检查想要的财产，并在发现示例后尽快返回
。 否则它返回 `fail` ，这是GAP中一种特殊类型的
布尔变量。

```gap
TestOneOrderEasy := function(n)
local i;
for i in [1..NrSmallGroups(n)] do
  if TestOneGroup( SmallGroup( n, i ) ) then
    return [n,i];
  fi;
od;
return fail;
end;
```

例如，

```gap
TestOneOrderEasy(1);
```

```output
[ 1, 1 ]
```

```gap
TestOneOrderEasy(24);
```

```output
失败
```

:::::::::::::::::::::::::::::::::::::::::  callout

## `AllSmallGroups` 会失去内存 -- 怎么办？

- 在上面的函数中显示的 `[1..NrSmallGroups(n)]` 上使用迭代方式
- 使用`IdsOfAllSmallGroups`来接受与`AllSmallGroups`
  相同的参数，但返回id而不是组。

::::::::::::::::::::::::::::::::::::::::::::::::::

如果您需要
更多地控制计算进度，那么超过`[1..NrSmallGroups(n)]`的迭代会给您带来更大的灵活性。 例如，我们测试函数的下一个版本
会打印关于正在测试的
组数的额外信息。 它还提供测试功能作为一个参数(为什么
你认为这更好了？)

```gap
TestOneOrder := 函数(f,n)
local i, G; A format@@1 for i in [1.. rSmallGroups(n)] do
  Print(n, ":", i, "/", NrSmallGroups(n), "\r");
  G := 小集团( n, i );
  如果f(G) 然后
    Print("\n");
    返回[n,i];
  fi;
od;
Print("\n");
返回失败;
结束;
```

例如，

```gap
TestOneorder(TestOneGroup, 64)；
```

将在计算过程中显示一个变化计数器，然后返回 "失败"：

```output
64:267/267
失败
```

The next step is to integrate `TestOneOrder` into a function which will test
all orders from 2 to `n` and stop as soon as it finds an example of a
group with the average order of an element being an integer:

```gap
TestAllOrders:=f,n)
local i;
for i in [2..n] do
  res:=TestOneorder(f,i)；
  如果res <> 失败，则
    返回；
  fi;
od;
返回失败;
结束;
```

缔约国报告说，有这样一组第105号命令：

```gap
TestAllorders(TestOneGroup,128)；
```

```output
2:1/1
3:1/1
:2/2
5:1/1
6:2/2
7:1/1
8:5/5
...
...
.
100:16/16
101:1/1
102:4/4
103:1/1
104:14/14 
 105:1/2
[ 105, 1 ]
```

要进一步探索，我们可以得到它的 `StructureDescription` (见
[documentation](https://docs.gap-system.org/doc/ref/chap39.html#X87BF1B887C91CA2E)
以解释它所用的符号)：

```gap
G:=小群组(105,1)；AvgOrdOfGroup(G)；结构说明(G)；
```

```output
<pc group of size 105 with 3 generators>
17
"C5 x (C7: C3)"
```

然后将其转换成一个精彩展示的团体，看到其发电机和亲戚：

```gap
H:=SimplifiedFpGroup(Image(IsomorphismFpGroup(G)));
RelatorsOfFpGroup(H);
```

```output
<fp group on the generators [ F1, F2, F3 ]>
[ F1^3, F2^-1*F1^-1*F2*F1, F3^-1*F2^-1*F2^-1*F3*F2, F3^-1*F1*F3*F3^-1^-1^-1*F3*F3^-1, F2^5,
  F3^7 ]
```

现在我们想尝试更大的组别，从第106号命令开始(我们检查
另一组命令105没有这种属性)

```gap
列表(AllSmallGroups(105)，AvgOrdOfGroup)；
```

```output
[ 17, 301/5 ]
```

在稍微修改的情况下，我们添加了一个额外的参数来指定从
开始的订单：

```gap
TestRangeOfOrders:=function(f,n1,n2)
local n, res;
for n in [n1..n2] do
  res:=TestOneOrder(f,n);
  if res <> fail then
    return res;
  fi;
od;
return fail;
end;
```

但我们现在把它叫了

```gap
TestRangeOforders(TestOneGroup,106,256)；
```

and discover that testing 2328 groups of order 128 and additionally 56092 groups
of order 256 already takes too long.

:::::::::::::::::::::::::::::::::::::::::  callout

## 不要恐慌！

您可以按 Ctrl-C一次来打断GAP 然后，GAP将输入
一个间歇循环，由间歇提示`brk>`指定。 You can leave it by
typing `quit;` (beware of pressing Ctrl-C twice within a second -- that will
terminate GAP session completely).

::::::::::::::::::::::::::::::::::::::::::::::::::

这是另一种理论知识帮助远远超过
野蛮武力方法的情况。 If the group is a _p_\-group, then the order of each
conjugacy class of a non-identity element of the group is divisible by _p_;
therefore, the average order of a group element may not be an integer. 因此，
_p_\-groups 可以排除在计算之外。 因此，新版本的代码是

```gap
TestRangeOforders:=f,n1,n2)
本地n,
 [n1..n2]
  如果不是 IsPrimePowerInt(n)，则
     res:=TestOneOrder(f,n)；
     如果res <> 失败，则
       退货；
     fi ;
   fi;
od;
返回失败;
结束;
```

并且使用它，我们能够发现具有相同属性的订单357组：

```gap
gap> TestRangeOforders(TestOneGroup,106,512)；
```

```output
106:2/2
108:45/45
...
350:10/10
351:14/14
352:195/195
354:4/4
355:2/2
356:5/5
357:1/2
[ 357, 1 ]
```

The next function shows even further flexibility: it is variadic, i.e.
it may accept two or more arguments, the first two of which will be assigned to
the variables `f` and `n`, and the rest of which will be available in the list `r`
(this is indicated by `...` after `r`). 第一个参数是测试
函数，第二个参数是检查顺序， 第三和第四个
是该订单的第一组和最后组别的数目，它们应该是
中选中的。 默认情况下，后两者分别等于1和 `NrSmallGroups(n)`
。 此函数还显示如何验证输入和
在无效参数的情况下生成方便用户的错误消息。

此外，此函数展示了如何使用 'Info' 消息，即
可以通过设置相应的`Info`级别来开关。
我们在这里的需要是能够切换
输出的动词级别，而不会有错误的方法走过代码并评论
"Print" 语句进出. 它是通过创建信息类实现的：

```gap
gap> InfoSmallGroupsSearch := NewInfoClass("InfoSmallGroupsSearch");
```

```output
InfoSmallGroups搜索
```

现在可以使用
`Info( InfoSmallGroupsSearch, infolevel, "something" );`
其中`infolevel` 是一个正整数指定了详细的级别。
这个级别可以使用命令
`SetInfoLevel( InfoSmallGroupsSearch, n);`. 在下面的
中查看`Info` 的实际通话：

```gap
TestOneOrderVariadic := 函数 (f,n,r)
local n1, n2, i;

如果不是 [0..2] 中的Length(r) ，则
  Error("参数数必须是2,3或4\n" )；
fi;

if IsFunction(f) through
  Error("第一个参数必须是一个函数\n" );
fi;

if not IsPosInt( n ) then
  Error("第二个参数必须是正整数\n" );
fi;

if IsBound(r[1]) then
  n1:=r[1];
  if not n1 in [1. NrSmallGroups(n)] 然后
    Error("第三个参数，如果存在，必须属于", [1.]。 rSmallGroups(n)], "\n"
  fi;
否则
  n1:=1;
fi;

如果IsBound(r[2]) 然后
  n2:=r[2];
  如果不是[1] n2。 NrSmallGroups(n)] 然后
    Error("第四个参数，如果存在的话，必须属于", [1)。 NrSmallGroups(n)], "\n"
  elif n2 < n1 then
    Error("第四个参数, 如果存在，必须大于或等于第3 \n" ;
  fi;
否则
  n2:=NrSmallGroups(n);
fi;

信息( InfoSmallGroupsSearch, 1,
      "检查组", n1, " ... “，n2，”顺序，n.；
for i in [n1..n2] do
  if InfoLevel( InfoSmallGroupsSearch ) > 1 then
    Print(i, "/", NrSmallGroups(n), "\r";
  fi;
  if f(SmallGroup(n,i)) 然后
    Info( InfoSmallGroupsSearch, 1,
          "发现的计数器：小组( ", n, ", i, " )" ;
    返回[n,i];
  fi;
od;
信息(InfoSmallGroupsSearch, 1,
      "搜索已完成 - 未发现计数采样" );
返回失败;
结束;
```

The following example demonstrates how the output may now be controlled
by switching the info level for `InfoSmallGroupsSearch`:

```output
gap> TestOneOrderVariadic(IsIntegerAverageOrder,24);
fails
gap> SetInfoLevel( InfoSmallGroupsSearch, 1 );
gap> TestOneOrderVariadic(IsIntegerAverageOrder,24);
#I Checking groups 1 . . 24
#I 搜索已完成 - 没有发现计数雷克斯的
失败
gap> TestOneOrderVariadic(IntegerAverageOrder,357)；
#I 检查组 1 。 . 357
#I 发现的计数器： SmallGroup( 357, 1 )
[ 357, 1 ]
gap> SetInfoLevel( InfoSmallGroupsSearch, 0)；
gap> TestOneOrderVariadic(IsIntegerAverageOrder,357)；
[ 357, 1 ]
```

当然，现在这会给测试文件带来一些复杂的问题，即
将实际输出与参考输出进行比较。 为了解决
这个问题，我们将决定在信息级别0运行测试以抑制
所有额外的输出。 因为测试可能已经在
GAP 会话中开始，具有不同的信息级别， 我们将记住此信息等级
以便在测试后还原它：

```output
# 查找具有整数平均顺序的组
gap> INFO_SSS:=InfoLevel(InfoSmallGroupsSearch);;
gap> SetInfoLevel( InfoSmallGroupsSearch, 0);
gap> res:=[];
gap> for n in [1..360] do
> if not IsPrimePowerIntn, than
> t := TestOneOrderVariadic( IsGerAverageOrder, 1,NrSmallGroups(n);
> if t <> failed
> Add(res,t);
> fi;
> fi;
> od;
gap>;
[ [1, 1 ], [ 105, 1 ], [ 357, 1 ]]
gap> SetInfoLevel( InfoSmallGroupsSearch, INFO_SSS);
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 小群组库是否包含具有此属性的其他群组？

- 您可以对拥有此属性的群组的顺序说什么？

- 您能估计检查所有408641062组的1536号命令需要多长时间吗？

- 您可以检查的订单群组数量不超过 2000，
  排除_p_\-groups 和 1536？

- 您是否可以在小群组库
  中找到另一个拥有此属性的群组（订单不等于1536）？

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- 将守则组织为职能。
- 创建一个小集团而不是一个庞大的名单。
- 使用 `SmallGroupsInformation` 可能有助于减少搜索空间。
- GAP不是一种灵丹妙药：理论知识可能比野蛮武力方法有更多的帮助。

::::::::::::::::::::::::::::::::::::::::::::::::::


