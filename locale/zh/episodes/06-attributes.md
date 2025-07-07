---
title: 属性和方法
teaching: 40
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 声明属性
- 安装方法
- 理解方法选择
- 使用调试工具

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 如何在 GAP 对象中记录信息

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## 哪个函数更快？

尝试重复计算 `AvgOrdOfGroup(M11)` 和 `AvgOrdOfCollection(M11)`
并比较运行时间。 对于`M11`的新副本和已经观察到此参数的
的副本执行此操作。 你观察了什么？

::::::::::::::::::::::::::::::::::::::::::::::::::

Of course, for any given group the average order of its elements needs to
be calculated only once, as the next time it will return the same value.
然而，正如我们从下面的运行时所看到的那样，每个新调用的 `AvgOrdOfGroup`
将再次重复相同的计算，但运行时间略有不同：

```gap
A:=AlternatingGroup(10)；
```

```output
Alt( [ 1 ... 10 ] )
```

```gap
AvgOrdOfCollection(A)；时间(A)；
```

```output
2587393/259200
8226
2587393/259200
8118
```

In the last example, the group in question was the same -- we haven't
constructed another copy of `AlternatingGroup(10)`; however, the result
of the calculation was not stored in `A`.

如果您需要重新使用此值，一个选项可以是将其存储在一些
变量中， 但你应该小心匹配这种变量
和相应的组别，代码可能会变得相当复杂的
并且无法读取。 On the other hand, GAP has the notion of an _attribute_ -- a
data structure that is used to accumulate information that an object learns about itself
during its lifetime. 请考虑以下示例：

```gap
G:=Group(1,3,4,5,5,6,7,8,9,10,11),(3,7,11,8)(4,10,5,6));
gap> NrConjugacyClasses(G);time;NrConjugacyClasses(G);time;；
```

```output
组(1,2,3,4,5,6,7,7,8,9,10,11)(3,7,11)(4,10,5,6))
10
39
10
0
```

In this case, the group `G` has 10 conjugacy classes, and it took 39 ms to
establish that in the first call. 由于
结果保存在`G`中，因为“NrConjugacyClasses”是一个属性，因此第二次调用的成本为零：

```gap
NrConjugacyClasses；
```

```output
<Attribute "NrConjugacyClasses">
```

我们现在的目标是学习如何创建自己的属性。

既然我们已经有一个
进行计算的函数 `AvgOrdOfCollection` ，那么将其转换为
属性的最简单方式如下：

```gap
AverageOrder := NewAttribute("AverageOrder", IsCollection);
安装方法( AverageOrder, "for a collection", [IsCollection], AvgOrdOfCollection);
```

在这个示例中，我们首先声明了`IsCollection`类别中的
对象的属性`AverageOrder` ， 然后安装函数
`AvgOrdOfCollection` 作为此属性的方法。 我们现在可以调用
，而不是调用 AvgOrdOfCollection`，我们现在可以调用 `AverageOrder\` 。

现在我们可以检查是否以零成本执行同一个参数
的 `AverageOrder` 后来的通话。 在此示例中，时间将从超过
16 秒减少为零：

```gap
S:=对称群组(10)；AverageOrder(S)；时间(AverageOrder(S)；时间；
```

```output
39020911/3628800
16445
39020911/3628800
0
```

You may wonder why we have declared the operation for a collection and not only
for a group, and why we have installed the inefficient `AvgOrdOfCollection`.
毕竟，我们已经发展了更有效的“AvgOrdOfGroup”。

想一想你想要能够计算一个平均订单
的组和一个包含具有乘法
订单的对象的列表中。 你可能像我们所做的那样，对每个情况都有一个特殊的功能。 If it
could happen that you don't know in advance the type of the object in question,
you may add checks into the code and dispatch to a suitable function. This could
quickly become complicated if you have several different functions for various
types of objects. 反之，属性是一堆函数，称为
_方法_ 和 GAP的 _方法选择_ 将根据所有参数的类型选择最有效的方法
。

为了说明这一点，我们现在将为一个组安装一个 `AverageOrder` 方法：

```gap
安装方法 ( AverageOrder, [IsGroup], AvgOrdOfGroup)；
```

如果你将它应用到一个已经计算了 `AverageOrder` 的组中，那么就不会发生任何
，因为GAP 将使用存储的值。 然而，对于一个新创建的小组，
这个新方法将被调用：

```gap
S:=对称群组(10)；AverageOrder(S)；时间(AverageOrder(S)；时间；
```

```output
39020911/3628800
26
39020911/3628800
0
```

:::::::::::::::::::::::::::::::::::::::::  callout

## 什么方法被调用

- 尝试调用 `AverageOrder` 来获取不是组
  的集合(组元素列表和/或组元素的征服类)。

- 调试工具，如`TraceMethods`，可能有助于您看到被调用的方法是
  。

- `ApplicableMethod` 与 `PageSource` 相结合，可能会指向您的
  指向所有的源代码。

::::::::::::::::::::::::::::::::::::::::::::::::::

_财产_是一种布尔值属性。 它可以使用 `NewProperty` 创建

```gap
IsIntegerAverageOrder := NewProperty("IsIntegerAverageOrder", IsCollection);
```

现在我们将安装 IsIntegerAverageOrder\` 收藏的方法。
观察到从来没有必要先创建
函数然后将其安装为方法。 以下方法安装
后创建一个新函数作为其参数之一：

```gap
安装方法 ( IsIntegerAverageOrder,
  "用于收藏",
  [IsCollection],
  coll -> IsInt( AverageOrder( coll )
);
```

请注意，因为`AverageOrder` 是一个属性，因此它将注意选择
是最合适的方法。

:::::::::::::::::::::::::::::::::::::::::  callout

## 这种方法是否总是存在？

否。 "No-method-found" is a special kind of error, and there are tools to
investigate such errors: see `?ShowArguments`, `?ShowDetails`, `?ShowMethods`
and `?ShowOtherMethods`.

::::::::::::::::::::::::::::::::::::::::::::::::::

The following calculation shows that despite our success with calculating
the average order for large permutation groups via conjugacy classes of
elements, for pc groups from the Small Groups Library it could be faster
to iterate over their elements than to calculate conjugacy classes:

```gap
l:=列表([1..1000],i->小组(1536,i);; List(l,AvgOrdOfGroup);;时间;
```

```output
56231
```

```gap
l:=列表([1..1000],i->小组(1536,i);; List(l,AvgOrdCollection);;时间;
```

```output
9141
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 不要恐慌！

- 安装一个 `IsPcGroup` 方法来迭代组元素
  ，而不是计算组的征服类。

- 评估其可行性的实际范围。 您能找到一个 pc 组的示例
  在该组中，迭代速度慢于计算夫妻之间的类？

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- _定位_对象在其生命期内可能会积累关于自己的信息。
- 这意味着下次以零成本检索所储存的信息。
- _Methods_ 是各种函数。GAP的_方法选择_ 将根据所有参数的类型选择最有效的方法。
- “找不到方法”是一种特殊错误，使用有用的调试工具帮助理解它。

::::::::::::::::::::::::::::::::::::::::::::::::::


