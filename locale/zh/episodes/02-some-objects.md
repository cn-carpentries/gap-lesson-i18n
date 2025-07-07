---
title: 更多的 GAP 对象
teaching: 15
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- 查看内置的 GAP 类型，但在其他系统可能缺失的实例
- 查看列表数学示例

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- 与它们一起进行的物体和操作的其他实例

::::::::::::::::::::::::::::::::::::::::::::::::::

到目前为止，我们遇到了三种类型的全球行动纲领：

- 简单对象，如整数、基本原理、布尔值、超值；

- a. 复合对象，如_列表_；

- 具有更复杂的内部代表性的对象，例如群组。

在本节中，我们将演示GAP中存在的一些基本对象
的其他示例(系统可以扩展) 这样就可以引入新类型的
对象，但这超出了这个课程的范围！)。

其他一些简单的物体是浮质、环形和有限的野外元素：

```gap
1.15; Float(1232/34567)；
```

```output
1.15
0.000356423
```

```gap
E(4); E(4)^2; E(6);
```

```output
E(4)
-1
E(3)^2
```

```gap
AsList(GF(2)); Z(5); Z(5)^4;
```

```output
[ 0*Z(2), Z(2)^0 ]
Z(5)
Z(5)^0
```

您已经知道的列表。
另一种复合对象是 **records**。 列表中包含按列表中位置索引的
子对象。 记录包含子对象，名为 \*record
components \*，它们被他们的名字编入索引。 记录元素使用`.`访问

```gap
date:= rec(year:= 2015, month:= "Nov", day:= 17)；
```

```output
rec( day := 17, month := "Nov", year := 2015 )
```

```gap
年份；
```

```output
2015
```

```gap
date.time:= receiv(小时:= 14分钟:= 55, second:= 12)；
```

```output
rec( hour:= 14分钟, := 55, second := 12)
```

```gap
日期；
```

```output
rec( day := 17, month := "Nov",
  time := rec( hour:= 14, mine := 55, second := 12), year := 2015 )
```

```gap
RecNames(date);
```

```output
[ "time", "year", "month", "day" ]
```

接下来，有 **strings** 和 **characters** 。 当字符串由GAP特别打印出
时，字符串实际上只是一个字符列表， 和任何带有列表的
函数也会使用一个字符串。 相比之下，字符
是像整数这样简单的对象。

```gap
gap> w:="超校准脆弱过期"; Length(w);
```

```output
"supercalifragilisticexpialidocious"
34
```

字符串用双引号和单个字符表示。

```gap
gap> "s" in w; IsSubset(w,"s"); IsSubset(w,['s','f']); ['c','a','t'] = "cat";
```

```output
false
true
true
true
true
```

请注意：

```gap
gap> PositionSublist(w,"sf"); PositionSublist(w,"fr");
```

```output
失败
10
```

小心！ 一些操作可能会创建一个新的列表，而其他操作则是
毁灭性的。 例如：

```gap
gap> SortedList(w); w;
```

```output
"aaacccdeefgiiiiiiillloopprrssstuux"
"supercalifragilisticexpialidocious"
```

不适用

```gap
gap> Sort(w)；w;
```

```output
"aaacccdeefgiiiiiiillloopprrssstuux"
```

最常见的“超校准过期”中出现哪一封信？

```gap
gap> c := 收集(w)；
```

```output
[ 'a', 3], [ 'c', 3], [ 'd', 1], [ 'e', 2], [ 'f', ] 1], [ 'g', 1],
  [ 'i', 7], [ 'l', 3], [ 'o', 2], [ 'p', 2], [ 'r', 2], [ 's', 3],
  [ 't', 1 ], [ 'u', 2 ], [ 'x', 1 ]
```

```gap
gap> k := Maximum( List( c, v -> v[2] ) ); Filtered( c, v -> v[2] = 7 );
```

```output
7
[ [ ', 7 ]
```

:::::::::::::::::::::::::::::::::::::::  challenge

## 只使用一个通道在列表中找到最常见的字母 (s)

命令

`k := Maximum( List( c, v -> v[2] ) ); Filtered( c, v -> v[2] = 7 );`

在列表`c`上迭代两次(在 `List` 和 `Filtered`), 和
它也会在调用
到`Maximum` 的相同长度的另一个列表上重复。 如果该列表长，这将会对某些性能进行
和内存惩罚。 尝试写代码，找出大部分
出现在`c`中，而不生成中间列表。

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- GAP有大量的眼前、位置和组件物体。
- 清单的算术非常灵活和有力。
- 像列表和记录这样的对象可以保存结构化和相关的数据。

::::::::::::::::::::::::::::::::::::::::::::::::::


