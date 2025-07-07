---
title: 使用回归测试
teaching: 40
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- 能够创建和运行测试文件
- 了解如何识别和解释测试差异和运行时回归。
- 了解如何调整测试以检查随机算法
- 学习“让它对错，然后使它更快”概念

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- B. 禁毒驱动的发展

::::::::::::::::::::::::::::::::::::::::::::::::::

`AvgOrdOfGroup`的代码非常简单，任何东西都不可能有错误的
By iterating over the group instead of creating a list of its elements,
it avoids running out of memory
(calling `AsList(SymmetricGroup(11))` already results in exceeding the permitted
memory). 尽管如此，计算仍然需要时间，需要几分钟的
来计算`对称组(11)`的
元素的平均顺序。 But at least we are confident that it is
correct.

现在我们想使用我们从群组理论上了解的一些
理论事实来编写这个功能的更好版本。 We may put
`avgord.g` under version control to revert changes if need be;
we may create a new function to keep the old one around and compare the
results of both; but this could be made even more efficient if we
use **regression testing**: this is the term for testing based on
rerunning previously completed tests to check that new changes do not
impact their correctness or worsen their performance.

首先，我们需要创建一个 **测试文件** 。 The test file looks
exactly like a GAP session, so it is easy to create it by copying and
pasting a GAP session with all GAP prompts, inputs and outputs into a
text file (a test file could be also created from a log file with a
GAP session recorded with the help of `LogTo`). During the test, GAP will
run all inputs from the test file, compare the outputs with those in the test
file and report any differences.

GAP 测试文件只是文本文件，但通常的做法是用扩展`.tst`命名
它们。 Now create the file `avgord.tst` in the current directory (to
avoid typing the full path) with the following content:

```gap
# 组元素平均顺序测试

# 许可组
gap> S:=对称组(9);
符号 ( [ 1 .
gap> AvgOrdOfGroup(S)；
3291487/362880
```

正如你所看到的那样，测试文件可能包含注释，某些规则指定
它们可以放置在哪里， 因为我们应该能够区分测试文件中的注释
和 GAP 输出以 '#' 开始。 为此目的，
行在以`#`开头的测试文件的开头， 和一条空行
连同一条或多条开头的行被视为评论。
所有其他行都被解释为先前GAP输入的GAP输出。

要运行测试，需要使用函数 `Test` (见
[documentation](https://docs.gap-system.org/doc/ref/chap7.html#X87712F9D8732193C)。
例如(假设函数`AvgOrdOfGroup`已加载)：

```gap
测试("avgord.tst");
```

```output
true
```

在这种情况下，`Test`报告没有出入，返回`true`，所以我们
认为测试已经通过了。

我们将不涉及在这里撰写一套良好和全面的试验材料。
我们也不会覆盖`Test`函数的各种选项，允许我们使用 为
示例，忽略输出格式中的差异 或显示测试的进度
，因为这些都在其文件中作了说明。

相反，我们现在将添加更多的小组。 st\`, 以证明
代码也适用于其他类型的组 并显示测试文件中包含命令的
的各种方式：

```gap
# 组元素平均顺序测试

# 许可组
gap> S:=对称组(9);
符号 ( [ 1 ...
gap> AvgOrdOfGroup(S)；
3291487/36280

# pc group
gap> D：=DihedralGroup(512)；
<pc group of size 512 with 9 generators>
gap> AvgOrdOfGroup(D)；
44203/512
gap> G:=TrivialGroup();# 压制输出
gap> AvgOrdOfGroup(G);
1

# fp group
gap> F:=FreeGroup("a","b");
<free group on the generators [ a, b ]>
gap> G:=F/ParseRelators(GeneratorsOfGroup(F),"a^8=b^2=1, b^-1ab=a^-1")；
<fp group on the generators [ a, b ]>
gap> IsFinite(G)；
true
gap> AvgOrdOfGroup(G)；
59/16

# 有限矩阵组的整数
gap> AvgOrdOfGroup( Group( [[[0,-1],[1,0]] );
11/4

# 有限字段上的矩阵组
gap> AvgOrdOfGroup(SL(2.5))；
221/40
```

让我们再次测试扩展版本的测试，并检查它是否起作用：

```gap
测试("avgord.tst");
```

```output
true
```

现在我们将努力改进执行工作。 当然，元素
的顺序是一组元素的一种未婚夫妻。 所以我们只需要
知道婚姻各类要素及其代表。 The
following code, which we add into `avgord.g`, reads into GAP and redefines
`AvgOrdOfGroup` without any syntax errors:

```gap
AvgOrdOfGroup := function(G)
local cc, sum, c;
cc:=ConjugacyClasses(G);
sum:=0;
cc do
  ump:= 和 + Order( Representative) * Size(cc);
od;
return sum/Size(G);
end
```

但当我们运行测试时，这会令人吃惊！

```gap
读取("avgord.g");
测试("avgord.tst");
```

```output
########> Avgord中的Diff st, 第 6 行:
# 输入:
AvgOrdOfGroup(S)；
# 预期输出：
3291487/362880
# 但发现：
11/672
########
##########> 相差于avgord。 St, 第12行：
# 输入为：
AvgOrdOfGroup(D)；
# 预期的输出：
44203/512
# 但发现：
2862481/512
######
##########> 不同于avgord。 st, 第 23行：
# 输入：
AvgOrdOfGroup(G)；
# 预期的输出：
59/16
# 但发现：
189/16
########
##########> 严重情况下的Diff。 St, 第 29行：
# 输入：
AvgOrdOfGroup(SL(2.5))；
# 预期输出：
221/40
# 但发现：
69/20
#######
false
```

事实上，我们打了一种打字（故意），将“Size(c)”改为“Size(cc)”。
正确的版本当然应该如下所示：

```gap
AvgOrdOfGroup := function(G)
local cc, sum, c;
cc:=ConjugacyClasses(G);
sum:=0;
cc do
  summary:= sum + Order( Representative) * Size(c);
od;
return sum/Size(G);
end
```

现在我们将在 `avgord.g` 中修复这个问题，并再次阅读和测试它以检查
测试是否正常。

```gap
读取("avgord.g");
测试("avgord.tst");
```

```output
true
```

因此，方法“使它正确，然后使它更快”帮助在引入后立即检测到一个 bug
。

:::::::::::::::::::::::::::::::::::::::: keypoints

- 通过复制和粘贴GAP会话来创建测试文件是容易的。
- 编写一套良好和全面的试验套件需要作出一些努力。
- 把它变得对了，然后让它变得更快！

::::::::::::::::::::::::::::::::::::::::::::::::::


