---
title: 讨论情况
permalink: /discusses/
---

## GAP初学者的10个提示

1. **请记住，GAP是区分大小写的！** 这意味着`ABC`、`Abc`和`abc`
  是三种不同的标识符。 调用`SymmetricGroup(3)` 工作, 但
  `Symmetricgroup(3)` 会导致错误。

2. 错误消息 **`错误， 变量: '函数名称' 必须有一个值"** 在
    函数调用中通常指向函数名称中的输入(见前一个提示),
    或一些必须预先使用 [**`LoadPackage\`**](https://docs.gap-system.org/doc/ref/chap76.html#X79B373A77B29D1F5 ]加载的软件包。

3. **Do not hesitate to use longer and more informative variable names where
  appropriate.** For example, `x` looks perfectly suitable for `List([1..10], x -> x^2)`,
  while `ConClassesReps` may be more informative than just `x` for a list of
  representatives of conjugacy classes of a group.

4. **Use command line editing:** scroll the history of commands and navigate within
  the command line using arrow keys to edit it.

5. \*\*使用自动补全而不是输入函数和变量的全名。 \*
  输入标识符的初始部分，然后按下 "<Tab>"。 如果它能够完成独特的完成，它将是
  。 如果没有，您可以再次按下<Tab>
  查看所有可能的建议。

6. **要查看帮助页面，请使用 `?` 和 `?` 命令**。 This will search not only
  in the GAP manuals, but also in the manuals of all GAP packages available
  in your GAP installation.

7. **Set default help format to HTML.** Use
  [**`SetHelpViewer`**](https://docs.gap-system.org/doc/ref/chap2.html#X87C1BFB2826488B0)
  to view it with your preferred browser.

8. \*\*使用 [**`LogTo`**](https://docs.gap-system.org/doc/ref/chap9.html#X79813A6686894960)
  将所有 GAP 输入和输出保存到文本文件中。\*\*它应该在
  计算之前而不是之后调用！

9. **如果计算需要太长时间，按下 `<Control>-C` 来中断它**。
  然后输入退出；离开休息循环。

10. **从 GAP 教程读取[与GAP一起的第一次会话](https://docs.gap-system.org/doc/tut/chap2.html)**

## 在 GAP 写入程序

- 在命令行中直接计算对象勘探和原型，
  然后考虑如何组织您的代码，使其可以重新使用。

- 使用 [**`LogTo`**](https://docs.gap-system.org/doc/ref/chap9.html#X79813A6686894960)
  保存输入和输出到日志文件，然后您可以在文本编辑器中进行编辑。

- 在文本文件中保存代码并使用
  [**`Read`**](https://docs.gap-system.org/doc/ref/chap9.html#X8373AC6B7D5F9167)
  加载它们。 查找一些高级文本编辑器来编辑这些文件。

- 将你的代码模块组织成函数并可复用。

- 在代码中写下评论 - 这将有助于您在一段时间后返回它。

- Understand [break loops](https://docs.gap-system.org/doc/ref/chap6.html#X8593B49F8705B486):
  you may [explore variables](https://docs.gap-system.org/doc/ref/chap6.html#X7EE5CF2C8419F061)
  on the current break level and use
  [**`Where`**](https://docs.gap-system.org/doc/ref/chap6.html#X7A7FFA2B7C1EF5A3)
  to show the last commands before the error occurred.

- Use [preferences mechanism](https://docs.gap-system.org/doc/ref/chap3.html#X7FD66F977A3B02DF)
  to customise GAP, for example, to set help viewer to HTML or to make command line history available
  after quitting GAP in the next GAP session.

- 理解计算背后的理论：理论上的改进可以提高
  的性能，远远超过仍在进行暴力计算的高度优化的代码。

- 实现算法，不要忘记角子案例。 例如，实现
  是一个微不足道的组还是一个身份元素？

- 不要依赖GAP函数返回结果的特定顺序，除非此
  有文件记录。 For example, dependently on the method, it may be not guaranteed
  that conjugacy classes or irreducible characters are listed in some particular
  order, or that the first element in their list is the conjugacy class of an identity
  element or the trivial character.

- 不要再询问，因为这可能涉及性能问题。
  例如：

  - 如果该财产是（元素或
    子群组的）婚姻类的不变财产， 你可能只想看一看婚姻类的代表
    。

  - 如果您对一个收藏的元素列表感兴趣，没有一个
    特定顺序，请使用 `AsList` 而不是 `AsSSortedList` 。

  - 不计算所有子组的婚姻类，如果： 您是
    只对普通或最大子组感兴趣——有特殊的
    方法来计算它们。

  - If you are looking for _p_\-subgroups, first you may calculate
    a Sylow _p_\-subgroup of a group, and then look at its subgroups
    and their conjugates.

  - 代表权事项：可能值得将一个组从fp group
    转换为异构无主pc组或独占组，以使用更快的方法。

- [常见问题] (https://www.gap-system.org/faq/) 获取更多提示。

## 保持联系

- 订阅\*\*[GAP论坛](https://www.gap-system.org/forum/)\*\*。

- 如果您需要帮助，请在这三个选项中选择以下问题：

  - 在 [GAP 论坛](https://www.gap-system.org/forum/) 中提出问题

  - 发送他们到 [GAP Support](https://www.gap-system.org/issues/)

  - 将它们发布在[数学问号\&A 站点](https://math.stackexchange.com/questions/tagged/gap?sort=frequent&pageSize=50)

## 为GAP贡献

- If you think that you've found a bug: please
  [create an issue on GitHub](https://github.com/gap-system/gap/issues) or
  report it by email to [GAP Support](https://www.gap-system.org/issues/).

- 如果您使用GAP，请引用GAP。 这有助于社区增长，
  ，这将有助于您的回报。
  [此页面](https://www.gap-system.org/cite/)
  建议如何引用GAP。 和函数
  [**`Cite`**](https://docs.gap-system.org/doc/ref/chap76.html#X79637D9A7B1AD7F7)
  将有助于为所使用的 GAP 同一版本生成引文样本。

- 考虑与其他人分享您的 GAP 发展动态，从通过
  分享您的代码到将它组织成一个 GAP 包。 已提交用于重新分配
  并可选择用于重置。

- 有助于进一步发展这一经验教训。

## 提示和方法

- 这是从 shell 脚本调用GAP 的简单方法。 创建名为 `check-one-order.sh` 的 shell
  脚本，包含以下内容：

```gap
#!/bin/sh

gap -r -b -q avgord.g << EOI
TestOneOrderEasy( $1 );
quit;
EOI
```

并使用`chmod u+x check-on-order.sh`来执行它。 现在你可以调用
，如下所示：

```gap
$./检查一个订单.sh 24
```

```output
失败
```

```gap
$ ./chec-on-order.sh 105
```

```output
[ 105, 1 ]
```

- 读取数据文件

GAP可以使用 "Read" 从代码中读取任何有效的 GAP 输入。 The contents will
be read and evaluated in the main read-evaluate-print loop, but the results will
not printed. 有时你可能想要将文件内容作为一个函数
并返回这个函数 - 为此目的，你可能发现`ReadAsFunction`是有用的。
But what to do if you have some a data file coming from other source, and it is
not a valid GAP input? 有时，您可能会控制导出
数据的工具，并且可能会调整它以生成 GAP 输入文件。 But where to look
if this option is not possible?

`ReadCSV( filename[, nohead][, separator] )` reads a file in a CSV (comma
separated values) format and returns its entries as a list of records
(see [documentation](https://docs.gap-system.org/doc/ref/chap10.html#X848DD7DC79363341)).
文件第一行的条目将用于记录组件的名称
(空白将被翻译成下划线)。
还可以指出第一行包含数据而不是
字段名，并且指定了一个自定义分隔符。 反之，`PrintCSV`
可能用于输出 CSV 文件。

若要以字符串读取任意(二进制或文本)文件，请使用 GAPDoc 包提供的 `StringFile`
函数(见
[documentation](https://docs.gap-system.org/pkg/gapdoc/doc/chap6.html#X7E14D32181FBC3C3))。
它将返回作为字符串的文件内容。
在此之后， 您可以使用各种字符串操纵工具(见
[字符串和字符](https://docs.gap-system.org/doc/ref/chap27.html)
在 GAP 参考手册中以您需要的方式处理它。 GAPDoc package
also provides the `FileString` function which writes the content of a string
into a file.

如果您需要通过行来组织读/写，而不是读或
来一次写整个文件/字符串， 我们建议查看IO 包
提供的功能
(见 [documentation](https://docs.gap-system.org/pkg/io/doc/chap4.html)) 。
特别是在`IO_ReadLine`和`IO_WriteLine`中。


