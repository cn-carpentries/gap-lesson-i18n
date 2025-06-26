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

Check what happens if you forget to add brackets,
e.g. type `LogTo;` and `Factorial;`
We will explain the differences in these outputs later.

::::::::::::::::::::::::::::::::::::::::::::::::::

Here are some examples of calling other GAP functions:

```gap
Factorial(100);
```

```output
93326215443944152681699238856266700490715968264381621468\
59296389521759999322991560894146397615651828625369792082\
7223758251185210916864000000000000000000000000
```

(the exact width of output will depend on your terminal settings),

```gap
Determinant(m);
```

```output
0
```

and

```gap
Factors(2^64-1);
```

```output
[ 3, 5, 17, 257, 641, 65537, 6700417 ]
```

Functions may be combined in various ways, and may be
used as arguments of other functions, for example, the
`Filtered` function takes a list and a function, returning
all elements of the list which satisfy the function.
`IsEvenInt`, unsurprisingly, checks if an integer is even!

```gap
Filtered( [2,9,6,3,4,5], IsEvenInt);
```

```output
[ 2, 6, 4 ]
```

A useful time-saving feature of the GAP command-line interfaces is completion
of identifiers when the Tab key is pressed. For example, type `Fib` and then
press the Tab key to complete the input to `Fibonacci`:

```gap
Fibonacci(100);
```

```output
354224848179261915075
```

In the case that a unique completion is not possible, GAP will try to perform
partial completion, and pressing the Tab key second time will display all possible
completions of the identifier. Try, for example, to enter `GroupHomomorphismByImages`
or `NaturalHomomorphismByNormalSubgroup` using completion.

The way functions are named in GAP will hopefully help you to memorise or even guess names
of library functions. If a variable name consists of several words then the
first letter of each word is capitalised (remember that GAP is case-sensitive!).
Further details on naming conventions used in GAP are documented
[in the GAP manual here](https://docs.gap-system.org/doc/ref/chap5.html#X81F732457F7BC851).
Functions with names in `ALL_CAPITAL_LETTERS` are internal functions not intended
for general use. Use them with extreme care!

It is important to remember that GAP is case-sensitive. For example, the following
input causes an error:

```gap
factorial(100);
```

```error
Error, Variable: 'factorial' must have a value
not in any function at line 14 of *stdin*
```

because the name of the GAP library function is `Factorial`. Using lowercase
instead of uppercase or vice versa also affects name completion.

Now let's consider the following problem: for a finite group _G_, calculate the
average order of its elements (that is, the sum of orders of its elements divided
by the order of the group). Where to start?

Enter `?Group`, and you will see all help entries, starting with `Group`:

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

You may use arrow keys to move up and down the list, and open help pages by
pressing Return key. For this exercise, open `Tutorial: Groups and Homomorphisms`
first. Note the navigation instructions at the bottom of the screen. Look at
first two pages, then press `q` to return to the selection menu. Next, navigate to
`Reference: Groups` and open it. Within two first pages you will find the
function `Group` and mentioning of `Order`.

GAP manual comes in several formats: text is good to view in a terminal,
PDF is good for printing and HTML (especially with MathJax support) is
very efficient for exploring with a browser. If you are running GAP on your
own computer, you can set the help viewer to the default browser. If you are
running GAP on a remote machine, this (probably) will not work. (see
`?WriteGapIniFile` on how to make this setting permanent):

```gap
SetHelpViewer("browser");
```

After that, invoke the help again, and see the difference!

Let's now copy the following input from the first example of the GAP Reference
manual chapter on groups. It shows how to create permutations, and assign values
to variables. This is `Reference: Groups`. You can select it by typing `?11`, where
you replace `11` with whatever number appears before `Reference: Groups` on your machine.

If you are viewing the GAP documentation in a terminal, you might find it helpful to
open two copies of GAP, one for reading documentation and one for writing code!

This guide shows how permutations in GAP are written in cycle notation, and also
shows common functions which are used with groups. Also, in some places two semi-colons
are used at the end of a line. This stops GAP from showing the result of a computation.

```gap
a:=(1,2,3);;b:=(2,3,4);;
```

Next, let `G` be a group generated by `a` and `b`:

```gap
G:=Group(a,b);
```

```output
Group([ (1,2,3), (2,3,4) ])
```

We may explore some properties of `G` and its generators:

```gap
Size(G); IsAbelian(G); StructureDescription(G); Order(a);
```

```output
12
false
"A4"
3
```

Our next task is to find out how to obtain a list of `G`'s elements and their orders.
Enter `?elements` and explore the list of help topics. After inspection,
the entry from the Tutorial does not seem relevant, but the entry from the
Reference manual is. It also explains the difference between using `AsSSortedList`
and `AsList`. So, this is the list of elements of `G`:

```gap
AsList(G);
```

```output
[ (), (2,3,4), (2,4,3), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4),
  (1,3)(2,4), (1,4,2), (1,4,3), (1,4)(2,3) ]
```

The returned object is a _list_. We would like to assign it to a variable
to explore and reuse. We forgot to do it when we were calculating it. Of
course, we may use the command line history to restore the last command, edit
it and call again. But instead, we will use `last` which is a special variable
holding the last result returned by GAP:

```gap
elts:=last;
```

```output
[ (), (2,3,4), (2,4,3), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4),
  (1,3)(2,4), (1,4,2), (1,4,3), (1,4)(2,3) ]
```

This is a list. Lists in GAP are indexed from 1.
The following commands are (hopefully!) self-explanatory:

```gap
gap> elts[1]; elts[3]; Length(elts);
```

```output
()
(2,4,3)
12
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Lists are more than arrays

- May contain holes or be empty

- May dynamically change their length (with `Add`, `Append` or direct assigment)

- Not required to contain objects of the same type

- See more in [GAP Tutorial: Lists and Records](https://docs.gap-system.org/doc/tut/chap3.html)

::::::::::::::::::::::::::::::::::::::::::::::::::

Many functions in GAP refer to `Set`s. A set in GAP is just a list that happens to have
no repetitions, no holes, and elements in increasing order. Here are some examples:

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

A `for` loop in GAP allows you to do something for every member of a collection.
The general form of a `for` loop is:

```gap
for val in collection do
  <something with val>
od;
```

For example, to find the average order of our group `G` we can do.

```gap
s:=0;;
for g in elts do
  s := s + Order(g);
od;
s/Length(elts);
```

```output
31/12
```

Actually, we can just directly loop over the elements of `G` (in general GAP
will let you loop over most types of object). We have to switch to using `Size`
instead of `Length`, as groups don't have a length!

```gap
s:=0;;
for g in G do
  s := s + Order(g);
od;
s/Size(G);
```

```output
31/12
```

There are other ways of looping. For example, we can instead loop over a range of integers,
and accept `elts` like an array:

```gap
s:=0;;
for i in [ 1 .. Length(elts) ] do
  s := s + Order( elts[i] );
od;
s/Length(elts);
```

```output
31/12
```

However, often there are more compact ways of doing things. Here is a very
short way:

```gap
Sum( List( elts, Order ) ) / Length( elts );
```

```output
31/12
```

Let's break this last part down:

- `Order` finds the order of a single permutation.
- `List(L,F)` makes a new list where the function `F` is applied to each
  member of the list `L`.
- `Sum(L)` adds up the members of a list `L`.

:::::::::::::::::::::::::::::::::::::::::  callout

## Which approach is best?

Compare these approaches. Which one would you prefer to use?

::::::::::::::::::::::::::::::::::::::::::::::::::

GAP has very helpful list manipulation tools. We will now show a few more examples.

Sometimes, GAP does not have the exact function we want.
For example, `NrMovedPoints` gives the number of moved points of a permutation,
but what if we want to find all permutations which move `4` points? This is where
GAP's arrow notation comes in. `g -> e` makes a new function which takes one argument `g`,
and returns the value of the expression `e`. Here are some examples:

- finding all elements of `G` with no fixed points:

```gap
Filtered( elts, g -> NrMovedPoints(g) = 4 );
```

```output
[ (1,2)(3,4), (1,3)(2,4), (1,4)(2,3) ]
```

- finding a permutation in `G` that conjugates (1,2) to (2,3)

```gap
First( elts, g -> (1,2)^g = (2,3) );
```

```output
(1,2,3)
```

Let's check this (remember that in GAP permutations are multiplied from left to right!):

```gap
(1,2,3)^-1*(1,2)*(1,2,3)=(2,3);
```

```output
true
```

- checking whether all elements of `G` move the point 1 to 2:

```gap
ForAll( elts, g -> 1^g <> 2 );
```

```output
false
```

- checking whether there is an element in `G` which moves exactly two points:

```gap
ForAny( elts, g -> NrMovedPoints(g) = 2 );
```

```output
false
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Use list operations to select from `elts` the stabiliser of the point 2 and the centraliser of the permutation (1,2)

- `Filtered( elts, g -> 2^g = 2 );`

- `Filtered( elts, g -> (1,2)^g = (1,2) );`

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Remember that GAP is case-sensitive!
- Do not panic if you see `Error, Variable: 'FuncName' must have a value`.
- Care about names of variables and functions.
- Use command line editing.
- Use autocompletion instead of typing names of functions and variables in full.
- Use `?` and `??` to view help pages.
- Set the default help format to HTML using `SetHelpViewer`.
- Use the `LogTo` function to save all GAP input and output into a text file.
- If calculation takes too long, press <Control>\-C to interrupt it.
- Read 'A First Session with GAP' from the GAP Tutorial.

::::::::::::::::::::::::::::::::::::::::::::::::::


