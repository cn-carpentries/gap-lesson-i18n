---
title: Пошук у маленьких групах
teaching: 40
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Використовується невеличка бібліотека груп
- Створення системи функцій, що підходять під комплекс

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Модульне програмування: з'єднайте функції разом
- Як перевірити деякі гіпотези за всі групи заданого порядку

::::::::::::::::::::::::::::::::::::::::::::::::::

In this section, we wish to discover some non-trivial groups with an interesting
property: namely, that the average order of their elements is an integer.

Розподіл GAP включає в себе кількість бібліотек даних
(наприклад, пошук слова "бібліотека" в
[список пакетів, розподілених GAP](https://www.gap-system.org/packages/)).
One of them is the [Small Groups Library](https://gap-packages.github.io/smallgrp/) by
Hans Ulrich Besche, Bettina Eick and Eamonn O'Brien.

This library provides various utilities to determine which information
is stored there and submit queries to search for groups with desired
properties. Основні функції - це `дрібна група!`, `AllSmallGroups`,
`NrSmallGroups`, `SmallGroupsInformation` та `IdGroup`. Наприклад:

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

Хотілося б скористатися нашою власною функцією тестування, яку ми створимо тут,
використовуючи вбудований запис (доступно для одноаргументних функцій):

```gap
TestOneGroup := G -> IsInt( AvgOrdOfGroup(G) );
```

Намагатися, наприклад,

```gap
Список ([TrivialGroup(),Group(((1,2))],TestOneGroup);
```

```output
[ true, false ]
```

```gap
gap> AllSmallGroups(Розмір, 24,TestOneGroup,true);
```

```output
[ ]
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Модульне програмування починається тут

Чому повертають булеві хороше конструктивне рішення для таких функцій,
замість того, щоб просто друкувати інформацію або повертати рядок, такий як "YES"?

::::::::::::::::::::::::::::::::::::::::::::::::::

Це простий приклад функції, яка тестує всі групи заданого замовлення.
It creates one group at a time, checks the desired property, and returns as soon
as an example is discovered. В іншому випадку він повертає "збій", який є спеціальним видом
логічної змінної в GAP.

```gap
TestOneOrderEasy := function(n)
local i ;
для i в [1.. rsmallGroups(n)] виконати
  якщо TestOneGroup(SmallGroup(n, i) то
    return [n,i];
  fi;
od;
повернутий з ладу;
закінчено;
```

Наприклад,

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
невдача
```

:::::::::::::::::::::::::::::::::::::::::  callout

## `AllSmallGroups` бракує пам'яті - що робити?

- Використовуйте ітерацію над `[1..NrSmallGroups(n)]` як показано в функції вище
- Use `IdsOfAllSmallGroups` which accepts same arguments as `AllSmallGroups`
  but returns ids instead of groups.

::::::::::::::::::::::::::::::::::::::::::::::::::

Iterating over `[1..NrSmallGroups(n)]` gives you more flexibility if you need
more control over the progress of calculation. Наприклад, наступна версія
нашої тестової функції друкує додаткову інформацію про кількість тестової групи
. It also supplies the testing function as an argument (why do
you think this is better?).

```gap
TestOneOrder := function(f,n)
local i, G;
для i в [1. rSmallGroups(n)] виконати
  Print(n, ":", i, "/", NrSmallGroups(n), "\r");
  G := Малювати Групу ( n, i );
  якщо f(G), то
    Друк ("\n");
    повертає [n,i];
  fi;
od;
Print("\n");
повернення невдачі;
завершується;
```

Наприклад,

```gap
Тестування OneOrder(TestOneGroup,64);
```

буде показано лічильник зміни під час розрахунку, потім повернути "не вдалось":

```output
64:267/267
fail
```

Наступним кроком буде інтегрувати "TestOneOrder" у функцію, яка перевіряє
усі замовлення від 2 до `n` і зупиняється, як тільки вона знайде приклад групи
з середнім порядком елемента є цілим:

```gap
TestAllOrders:=function(f,n)
local i, res;
for i in [2..n] do
  res:=TestOneOrder(f,i);
  if res <> fail then
    return res;
  fi;
od;
return fail;
end;
```

Вони повідомляють, що існує така група порядку 105:

```gap
Тестувати AllOrders(TestOneGroup,128);
```

```output
2:1/1
3:1/1
4:2/2
5:1/1
6:2/2
7:1/1
8:5/5
...
...
...
100:16/16
101:1/1
102:4/4
103:1/1
104:14/14
105:1/2
[ 105, 1 ]
```

Щоб вивчити його далі, ми можемо отримати його `StructureDescription` (див.
[documentation](https://docs.gap-system.org/doc/ref/chap39.html#X87BF1B887C91CA2E)
для пояснення позначення, яке він використовує):

```gap
G:=SmallGroup(105,1); AvgOrdOfGroup(); Оптимізація(G);
```

```output
<pc group of size 105 with 3 generators>
17
"C5 x (C7 : C3)"
```

а потім перетворити її в кінцеву особу, щоб побачити її генератори і реляторів:

```gap
H:=SimplifiedFpGroup(Image(IsomorphismFpGroup(G)));
RelatorsOfFpGroup(H);
```

```output
<fp group on the generators [ F1, F2, F3 ]>
[F1^3, F2^-1*F1^-1*F2*F2*F1, F3^-1*F3*F3*F2, F3^-1*F1^-1^-1*F3*F3^-1*F3^-1, F3^-1, F2^5,
  F3^7 ]
```

Now we want to try larger groups, starting from order 106 (we check that
the other group of order 105 possesses no such property)

```gap
Список (AllSmallGroups(105),AvgOrdOfGroup);
```

```output
[ 17, 301/5 ]
```

With a little modification, we add an extra argument specifying the order from
which to start:

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

Але зараз ми називаємо це

```gap
Тестування RangeOfOrders(TestOneGroup,106,256);
```

and discover that testing 2328 groups of order 128 and additionally 56092 groups
of order 256 already takes too long.

:::::::::::::::::::::::::::::::::::::::::  callout

## Не панікуйте!

Ви можете перервати GAP, натиснувши Ctrl-C один раз. Після цього GAP потрапить до
циклу перерви, визначений запитом `brk>`. You can leave it by
typing `quit;` (beware of pressing Ctrl-C twice within a second -- that will
terminate GAP session completely).

::::::::::::::::::::::::::::::::::::::::::::::::::

This is another situation where theoretical knowledge helps much more than the
brute-force approach. If the group is a _p_\-group, then the order of each
conjugacy class of a non-identity element of the group is divisible by _p_;
therefore, the average order of a group element may not be an integer. Тому
_p_\-групи можуть бути виключені з розрахунків. Так, є нова версія коду

```gap
TestRangeOfOrders:=function(f,n1,n2)
local n, res;
for n in [n1..n2] do
  if not IsPrimePowerInt(n) then
     res:=TestOneOrder(f,n);
     if res <> fail then
       return res;
     fi;
   fi;
od;
return fail;
end;
```

і використовуючи це, ми можемо відкрити групу замовлення 357 з тією самою власністю:

```gap
gap> TestRangeOfOrders(TestOneGroup,106,512);
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
(this is indicated by `...` after `r`). The first argument is the testing
function, the second is the order to check, and the third and the fourth
are the numbers of the first and last groups of this order that should be
checked. By default, the last two are equal to 1 and `NrSmallGroups(n)`
respectively. Ця функція також показує, як підтвердити введені дані і дані
повертають повідомлення про помилки, зрозумілі для користувача в разі невірних аргументів.

Крім того, ця функція демонструє, як використовувати повідомлення `Info`, які
можна увімкнути і вимкнути шляхом встановлення відповідного рівня `Info`. Необхідний
, з яким ми звернулись сюди, можна переключити рівні вербiльності
на вивід без помилки-орієнтованого підходу в коді та коментування
`Print` команд через і на вулиці. Це досягається шляхом створення інформаційного класу:

```gap
gap> InfoSmallGroupsSearch := NewInfoClass("InfoSmallGroupsSearch");
```

```output
Пошук інфофофографічних груп
```

Now instead of `Print("something");` one could use
`Info( InfoSmallGroupsSearch, infolevel, "something" );`
where `infolevel` is a positive integer specifying the level of verbosity.
Цей рівень можна змінити на `n`, використовуючи команду
`SetInfoLevel( InfoSmallGroupsSearch, n);`. Дивіться реальні виклики `Info` в
код нижче:

```gap
TestOneOrderVariadic := function(f,n,r...)
local n1, n2, i;

if not Length(r) in [0..2] then
  Error("The number of arguments must be 2,3 or 4\n" );
fi;

if not IsFunction( f ) then
  Error("The first argument must be a function\n" );
fi;

if not IsPosInt( n ) then
  Error("The second argument must be a positive integer\n" );
fi;

if IsBound(r[1]) then
  n1:=r[1];
  if not n1 in [1..NrSmallGroups(n)] then
    Error("The 3rd argument, if present, must belong to ", [1..NrSmallGroups(n)], "\n" );
  fi;
else
  n1:=1;
fi;

if IsBound(r[2]) then
  n2:=r[2];
  if not n2 in [1..NrSmallGroups(n)] then
    Error("The 4th argument, if present, must belong to ", [1..NrSmallGroups(n)], "\n" );
  elif n2 < n1 then
    Error("The 4th argument, if present, must be greater or equal to the 3rd \n" );
  fi;
else
  n2:=NrSmallGroups(n);
fi;

Info( InfoSmallGroupsSearch, 1,
      "Checking groups ", n1, " ... ", n2, " of order ", n );
for i in [n1..n2] do
  if InfoLevel( InfoSmallGroupsSearch ) > 1 then
    Print(i, "/", NrSmallGroups(n), "\r");
  fi;
  if f(SmallGroup(n,i)) then
    Info( InfoSmallGroupsSearch, 1,
          "Discovered counterexample: SmallGroup( ", n, ", ", i, " )" );
    return [n,i];
  fi;
od;
Info( InfoSmallGroupsSearch, 1,
      "Search completed - no counterexample discovered" );
return fail;
end;
```

The following example demonstrates how the output may now be controlled
by switching the info level for `InfoSmallGroupsSearch`:

```output
gap> TestOneOrderVariadic(IsIntegerAverageOrder,24);
fail
gap> SetInfoLevel( InfoSmallGroupsSearch, 1 );
gap> TestOneOrderVariadic(IsIntegerAverageOrder,24);
#I  Checking groups 1 ... 15 of order 24
#I  Search completed - no counterexample discovered
fail
gap> TestOneOrderVariadic(IsIntegerAverageOrder,357);
#I  Checking groups 1 ... 2 of order 357
#I  Discovered counterexample: SmallGroup( 357, 1 )
[ 357, 1 ]
gap> SetInfoLevel( InfoSmallGroupsSearch, 0);
gap> TestOneOrderVariadic(IsIntegerAverageOrder,357);
[ 357, 1 ]
```

Of course, this now introduces some complication for the test file,
which compares the actual output with the reference output. To resolve
this problem, we will decide to run the tests at info level 0 to suppress
all additional outputs. Оскільки тести могли бути запущені в
сеанс GAP з іншим рівнем інформації, ми будемо пам'ятати що рівень інформації
щоб відновити її після тесту:

```output
# Finding groups with integer average order
gap> INFO_SSS:=InfoLevel(InfoSmallGroupsSearch);;
gap> SetInfoLevel( InfoSmallGroupsSearch, 0);
gap> res:=[];;
gap> for n in [1..360] do
>      if not IsPrimePowerInt(n) then
>        t := TestOneOrderVariadic( IsIntegerAverageOrder,n,1,NrSmallGroups(n) );
>        if t <> fail then
>          Add(res,t);
>        fi;
>      fi;
>    od;
gap> res;
[ [ 1, 1 ], [ 105, 1 ], [ 357, 1 ] ]
gap> SetInfoLevel( InfoSmallGroupsSearch, INFO_SSS);
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Чи міститься в бібліотеці дрібних груп інша група з цією властивістю?

- Що можна сказати про порядок груп з цією властивістю?

- Чи можете ви підрахувати, скільки часу буде потрібно для перевірки всіх 408641062 груп по порядку 1536?

- How many groups of order not higher than 2000 might you be able to check,
  excluding _p_\-groups and those of order 1536?

- Can you find another group with this property in the Small Groups Library
  (of order not equal to 1536)?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Організуйте код у функції.
- Створюйте невеликі групи одна за одною, замість того, щоб виробляти величезний список з них.
- Використання `SmallGroupsInformation` може допомогти зменшити простір пошуку.
- GAP не є магічним інструментом: теоретичні знання можуть допомогти набагато більше, ніж підхід жорстокої сили.

::::::::::::::::::::::::::::::::::::::::::::::::::


