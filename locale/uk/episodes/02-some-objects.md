---
title: Ще декілька об'єктів GAP
teaching: 15
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Дивіться приклади типів, які вбудовані в GAP, але можуть бути відсутні в інших системах
- Подивитися приклади арифметики

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Подальші приклади об'єктів та операцій з ними

::::::::::::::::::::::::::::::::::::::::::::::::::

Поки ми виконали три типи типів GAP:

- прості об'єкти, такі як цілі числа, раціональні числа, булеви, перестановки;

- складені об'єкти, такі як _списки_;

- об'єкти з більш складним внутрішнім представленням, такі як групи.

In this section, we will demonstrate some other examples of basic objects
that exist in GAP (the system is extendable, so one can introduce new types
of objects, but this is beyond the scope of this lesson!).

Деякі інші прості об'єкти є плаваючими, лотомікою і скінченними полями елементи:

```gap
1.15; Float(1233456567);
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
-E(3)^2
```

```gap
AsList(GF(2)); Z(5); Z(5)^4;
```

```output
[ 0*Z(2), Z(2)^0 ]
Z(5)
Z(5)^0
```

Ви вже знаєте про списки.
Інший тип складених об'єктів - **записи**. У той час як список містить дані підоб’єктів, індексовані
за їх позиціями у списку, запис містить вкладені об’єкти, які називаються компонентами \*запис
, які індексуються їх іменами. Елементи запису доступні `.`

```gap
date:= rec(year:= 2015, month:= "Новинка", day:= 17);
```

```output
rec( day := 17, місяць := "Новинка", рік := 2015, )
```

```gap
дата.рік;
```

```output
2015
```

```gap
date.time:= rec(hour:= 14, minute:= 55, second:= 12);
```

```output
ректо( година := 14, хвилина := 55, другий := 12)
```

```gap
дата;
```

```output
rec( day := 17, місяць := "Новинка",
  час := rec( година := 14, хвилину := 55, секунду := 12 ), рік := 2015
```

```gap
RecNames(date);
```

```output
[ "час", "рік", "місяць", "день" ]
```

Далі, є **рядки** і **символи**. While strings are printed
specially by GAP, a string is really just a list of characters, and any
function which takes a list will also take a string. Навпаки, символи* це прості об’єкти, такі як цілі числа.

```gap
gap> w:="supercalifragilicexpialociidocious"; Length(w);
```

```output
"supercalifragilisticexpialidocious"
34
```

Рядки позначаються подвійними лапками, а символи по одиницях.

```gap
gap> "s" в w; 's' в w; IsSubset(w,"s"); IsSubset(w,['s','f']); ['c','a','t'] = "Кіт";
```

```output
false
true
true
true

```

Зауважте, що

```gap
gap> PositionSublist(w,"sf"); PositionSublist(w,"fr");
```

```output
fail
10
```

Обережно! Деякі операції можуть створити новий список, а інші -
руйнування. Наприклад:

```gap
gap> SortedList(w); w;
```

```output
"aaacccdeefgiiiiiiillloopprrssstuux"
"supercalifragilisticexpialidocious"
```

але

```gap
gap> Сорт(w); w;
```

```output
"aaacccdeefgiiiiiiillloopprrssstuux"
```

Який лист найбільше зустрічається в "supercalifragilicexpialodidociy"

```gap
gap> c := зібрані (w);
```

```output
[ 'a', 3 ], [ 'c', 3 ], [ 'd', 1 ], ['e', 2 ], [ 'f', 1 ], [ 'g', 1 ],
  [ 'i', 7 ], [ 'l', 3 ], [ 'o', 2 ], [ 'p', 2 ], [ 'r', 2 ], [ 's', 3 ],
  [ 't', 1 ], [ 'u', 2 ], [ 'x', 1 ]
```

```gap
gap> k := Maximum( List( c, v -> v -> v[2] ) ); Filtered( c, v -> v[2] = 7 );
```

```output
7
[ 'i', 7 ]
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Пошук найбільш розповсюджених літер у списку, використовуючи тільки один прохід

Команда

`k := Maximum( список( c, v -> v[2] ) ); Filtered( c, v -> v[2] = 7 );`

iterates over the list `c` twice (in `List` and in `Filtered`), and
it also iterates over another list of the same length as `c` in the call
to `Maximum`. Якщо список довгий, це покриє певну продуктивність
та штрафи за пам'ять. Try to write code that finds the letters that occur most
in `c` without producing an intermediate list.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- GAP має вибірку різних негайних, позиційних та компонентів.
- Список арифметик є дуже гнучким та потужним.
- Такі об'єкти, як списки та записи, корисні для збереження структурованих та пов'язаних даних.

::::::::::::::::::::::::::::::::::::::::::::::::::


