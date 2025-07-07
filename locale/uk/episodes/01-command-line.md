---
title: Перша сесія з GAP
teaching: 30
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Підказки в економії часу
- Використання системи довідки GAP
- Основні об'єкти та конструкції мови GAP

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Робота з командним рядком GAP

::::::::::::::::::::::::::::::::::::::::::::::::::

Якщо GAP встановлено правильно, ви можете запустити його. Exactly how
you start GAP will depend on your operating system and how you installed
GAP. GAP починається з _банера_ відображення інформації про версію
системи і завантажених компонентів, і потім відображає командний рядок
`gap>`, наприклад:

```output
 ┌───────┐   GAP 4.9.2 of 04-Jul-2018
 │  GAP  │   https://www.gap-system.org
 └───────┘   Architecture: x86_64-apple-darwin16.7.0-default64
 Configuration:  gmp 6.1.2, readline
 Loading the library and packages ...
 Packages:   AClib 1.3, Alnuth 3.1.0, AtlasRep 1.5.1, AutPGrp 1.9,
             Browse 1.8.8, CRISP 1.4.4, Cryst 4.1.17, CrystCat 1.1.8,
             CTblLib 1.2.2, FactInt 1.6.2, FGA 1.4.0, GAPDoc 1.6.1, IO 4.5.1,
             IRREDSOL 1.4, LAGUNA 3.9.0, Polenta 1.3.8, Polycyclic 2.14,
             PrimGrp 3.3.1, RadiRoot 2.8, ResClasses 4.7.1, SmallGrp 1.3,
             Sophus 1.24, SpinSym 1.5, TomLib 1.2.6, TransGrp 2.0.2,
             utils 0.54
 Try '??help' for help. See also '?copyright', '?cite' and '?authors'
gap>
```

Щоб залишити GAP, введіть `quit;` в запиті GAP. Пам'ятайте, що всі команди GAP,
, включаючи поточну, повинні бути завершені з комою! Вступайте з категорії
`quit;`, щоб залишити GAP, а потім розпочати нову сесію GAP. Before continuing, you
may wish to enter the following command to display GAP prompts and user inputs
in different colours:

```gap
 ColorPrompt(true);
```

Найпростіший спосіб почати спроби GAP це як калькулятор:

```gap
( 1 + 2^32 ) / (1 - 2*3*107 );
```

```output
-6700417
```

If you want to record what you did in a GAP session, so you can look over it
later, you can enable logging with the `LogTo` function, like this.

```gap
ЛогTo("gap-intro.log");
```

This will create a file file `gap-intro.log` in the current directory which
will contain all subsequent input and output that appears on your terminal.
Щоб зупинити журнал, ви можете викликати `LogTo` без аргументів, як в `LogTo();`,
або залишити GAP. Note that `LogTo` blanks the file before starting, if it
already exists!

It can be useful to leave some comments in the log file in case you
return to it in the future. Коментар в GAP починається з символу `#` і
продовжує до кінця рядка. You can enter the following after the
GAP prompt:

```gap
# GAP програмний урок Carpentry
```

після натиснення кнопки повернення GAP відобразить новий запит, але коментар
буде записано до файлу журналу.

Журнал записує все взаємодію з GAP, яка трапляється після дзвінка
в "Увійти" , але не раніше. We can repeat our calculation from above
if we want to record it as well. Instead of retyping it, we will use the Up and Down
arrow keys to scroll the _command line history_. Repeat this until you see
the formula again, then press Return (the location of the cursor in the command
line does not matter):

```gap
( 1 + 2^32 ) / (1 - 2*3*107 );
```

```output
-6700417
```

Ви також можете редагувати існуючі команди. Press Up once more, and then use the
Left and Right arrow keys, Delete or Backspace to edit it and replace
32 by 64 (some other useful shortcuts are
Ctrl-A and Ctrl-E to move the cursor to the beginning and end of the
line, respectively). Now press the Return key (at any position of the
cursor in the command line):

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

If you want to store a value for later use, you can assign it to a name
using `:=`

```gap
всесвіт := 6*7;
```

:::::::::::::::::::::::::::::::::::::::::  callout

## `:=`, `=` і `<>`

- In other languages you might be more familiar with using `=`, to assign
  variables, but GAP uses `:=`.

- GAP uses `=` to compare if two things are the same (where other languages might
  use `==`).

- Нарешті, GAP використовує `<>` щоб перевірити, чи два речі не дорівнюють (замість `!=`
  ви, можливо, бачили раніше).

::::::::::::::::::::::::::::::::::::::::::::::::::

Символи пробілу (напр. Космії, Табори і Повернення) незначні в GAP,
, крім випадків, якщо вони зустрічаються у рядку. Наприклад,
попередній вхід може типізуватися без пробілів:

```gap
(1+2^64)/(1-2*3*107);
```

```output
-18446744073709551617/641
```

Символи пробілів часто використовуються для більш складного форматування команд
кращої читання. Наприклад, наступний вхід створює матрицю 3×3:

```gap
м:=[[1,2,3],[4,5,6],[7,8,9]];
```

```output
[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
```

Ми замість цього можемо написати свою матрицю на 3 лінії. У такому випадку, замість повного запиту
`gap>`, попередній запит `>` відображатиметься до тих пір, поки користувач не завершить поле
введення крапкою з комою:

```gap
gap> m:=[1, 2, 3],
> [ 4, 5, 6 ],
> [ 7, 8, 9 ]];
```

```output
[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
```

Ви можете використовувати `Display` для красивих змінних, включаючи цей матриця:

```gap
Відображення(м);
```

```output
[ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
```

В загальних функціях GAP, такі як `LogTo` і `Display` викликаються за допомогою дужок,
який містить (можливо порожній) список аргументів.

:::::::::::::::::::::::::::::::::::::::::  callout

## Функції - це також об'єкти GAP

Перевірте що станеться, якщо ви забудете додати дужки,
наприклад, тип "LogTo;" і "Factorial;\`
Ми пояснимо різницю у цих виходах пізніше.

::::::::::::::::::::::::::::::::::::::::::::::::::

Ось деякі приклади виклику інших функцій GAP:

```gap
Factorial(100);
```

```output
93326215443944152681699238856266700490715968264381621468\
5929638952175999932299158941463976156518369792082\
72237582511852109160000000000000000000000
```

(точна ширина виходу буде залежати від ваших терміналів),

```gap
Визначник (м);
```

```output
0
```

та

```gap
Факторс(2^64-1);
```

```output
[ 3, 5, 17, 257, 641, 65537, 6700417 ]
```

Functions may be combined in various ways, and may be
used as arguments of other functions, for example, the
`Filtered` function takes a list and a function, returning
all elements of the list which satisfy the function.
`ІЄвенінт`, не дивно, перевіряє, чи є ціле число парним!

```gap
Фільтрація ( [2,9,6,3,4,5], Євелет);
```

```output
[ 2, 6, 4 ]
```

Корисна функція збереження часу інтерфейсів командного рядка GAP завершена
ідентифікаторів при натисканні кнопки Tab . Наприклад, введіть `Fib` і потім
натисніть клавішу вкладки, щоб завершити введення даних до `Fibonacci`:

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

Функції названі в GAP, сподіваюся, допоможуть вам запам"ятати або навіть вгадати імена
функцій бібліотеки. If a variable name consists of several words then the
first letter of each word is capitalised (remember that GAP is case-sensitive!).
Further details on naming conventions used in GAP are documented
[in the GAP manual here](https://docs.gap-system.org/doc/ref/chap5.html#X81F732457F7BC851).
Functions with names in `ALL_CAPITAL_LETTERS` are internal functions not intended
for general use. Користуйтеся ними з крайньою турботою!

Важливо пам'ятати, що GAP чутливий до регістру. Наприклад, наступний
введення викликає помилку:

```gap
факторіал(100);
```

```error
Помилка, змінна: 'factorial' повинно мати значення
у будь-якій функції на рядку 14 стадії *
```

тому що ім'я функції бібліотеки GAP "Factorial". Використання маленького регістру
замість верхнього або навпаки впливає на заповнення імен.

Now let's consider the following problem: for a finite group _G_, calculate the
average order of its elements (that is, the sum of orders of its elements divided
by the order of the group). З чого почати?

Введіть `?Group`, і ви побачите всі допоміжні входи, починаючи з `Group`:

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

Можна використовувати клавіші зі стрілками для переміщення вгору і вниз по списку і відкривати сторінки довідки
натиснувши клавішу повернення. Для цієї вправи відкрийте `Посібник: групи та гомоморфізми
першими. Зверніть увагу на навігаційні інструкції в нижній частині екрану. Look at
first two pages, then press `q`to return to the selection menu. Далі, перейдіть по місту`Посилання: Групи' і відкрийте його. Within two first pages you will find the
function `Group` and mentioning of `Order`.

Підручник GAP має декілька форматів: текст можна переглянути в терміналі,
PDF хороший для друку та HTML (особливо для підтримки MathJax),
є дуже ефективним для вивчення з браузером. If you are running GAP on your
own computer, you can set the help viewer to the default browser. If you are
running GAP on a remote machine, this (probably) will not work. (дивіться
`?WriteGapIniFile` як зробити цей параметр постійним):

```gap
SetHelpViewer("browser");
```

Після цього, викликайте допомогу знову, і дивіться різницю!

Let's now copy the following input from the first example of the GAP Reference
manual chapter on groups. Він показує як створити перестановки і призначити значення
змінним. Це "Посилання: Групи". Ви можете обрати його, набравши `?11`, де
ви заміните `11` на будь-який номер, що з'являється перед `Посиланням: Групи` на вашому машині.

If you are viewing the GAP documentation in a terminal, you might find it helpful to
open two copies of GAP, one for reading documentation and one for writing code!

Ця інструкція показує, як перестановки в GAP записуються в нотації циклу, а також
показує загальні функції, які використовуються в групах. Також в деяких місцях два півдвокрапки
використовуються в кінці лінії. Це зупиняє GAP показати, як результат обчислення.

```gap
a:=(1,2,3);;b:=(2,3,4);;
```

Далі, нехай `G` буде групою, створеною `a` і `b`:

```gap
G:=Group(a,b);
```

```output
Група ([ (1, 2,3), (2,3,4) ])
```

Ми можемо досліджувати деякі властивості `G` і його генераторів:

```gap
Розмір(G); IsAbelian(G); Структура Опису (G); Ордер();
```

```output
12
false
"A4"
3
```

Наше наступне завдання - дізнатися, як отримати список "Г" та їх замовлень.
Введіть `?elements` та дослідіть список тем допомоги. Після перевірки,
запис з посібника не є актуальним, але запис з довідника
"Документації A". Він також пояснює різницю між використанням `AsSSortedList`
та `AsList`. Ось список елементів `G`:

```gap
AsList(G);
```

```output
[ (), (2,3,4), (2,4,3), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4),
  (1,3)(2,4), (1,4,2), (1,4,2), (1,4)(2,3) ]
```

Повернений об'єкт - _список_. Ми хотіли б призначити його змінній
для дослідження і повторного використання. Ми забули зробити це, коли підрахували. Of
course, we may use the command line history to restore the last command, edit
it and call again. Натомість ми будемо використовувати `last`, який є спеціальною змінною
що тримає останній результат, який повернув GAP:

```gap
elts:=last;
```

```output
[ (), (2,3,4), (2,4,3), (1,2)(3,4), (1,2,3), (1,2,4), (1,3,2), (1,3,4),
  (1,3)(2,4), (1,4,2), (1,4,2), (1,4)(2,3) ]
```

Це перелік. Списки в GAP індексовані з 1.
Наступні команди (надію!) самопояснення:

```gap
gap> ельфи[1]; elts[3]; Length(elts);
```

```output
()
(2,4,3)
12
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Списки більше за масиви

- Може містити отвори або бути пустим

- Може динамічно змінити їх довжину (за допомогою `Додати`, `Додатку` або прямого призначення)

- Не потрібно містити об'єкти одного типу

- See more in [GAP Tutorial: Lists and Records](https://docs.gap-system.org/doc/tut/chap3.html)

::::::::::::::::::::::::::::::::::::::::::::::::::

Багато функцій в GAP посилаються на \`Встановити'. A set in GAP is just a list that happens to have
no repetitions, no holes, and elements in increasing order. Ось кілька прикладів:

```gap
gap> IsSet([1,3,5]); IsSet([1,5,3]); IsSet([1,3,3]);
```

```output
true
false
false
```

Тепер розгляньмо цікавий розрахунок - середній порядок елементів
"Г". Є багато різних способів зробити це, ми розглянемо деякі з них
тут.

Цикл `for` в GAP дозволяє вам щось зробити для кожного члена колекції.
Загальна форма циклу `for`:

```gap
для val у колекції
  <something with val>
od;
```

Наприклад, щоб знайти середній порядок нашої групи `G` ми можемо це зробити.

```gap
s:=0;;
for g в elts do
  s := s + Замовлення (g);
od;
s/Length(elts);
```

```output
31/12
```

Насправді, ми можемо напряму по елементах `G` (у загальному GAP
дозволить вам цикл на більшість типів об'єкта). We have to switch to using `Size`
instead of `Length`, as groups don't have a length!

```gap
s:=0;;
для g in G виконати
  s := s + Замовлення (g);
od;
s/Size(G);
```

```output
31/12
```

Є й інші способи повторення питань. Наприклад, ми можемо працювати над діапазоном цілих чисел,
і приймати `elts` як масив:

```gap
s:=0;;
для i в [ 1. довжиною (elts) ] зробити
  s := s + Замовлення ( elts[i] );
od;
s/Length(elts);
```

```output
31/12
```

Проте, часто трапляються більш компактні способи щось робити. Here is a very
short way:

```gap
Сума ( список, порядок) / довжина( elts );
```

```output
31/12
```

Давайте розберемо останню частину:

- `Замовлення` знаходить порядок однієї перестановки.
- `List(L,F)` створює новий список, коли функція `F` застосовується до кожного з
  членів списку "L".
- `Sum(L)` додає до списку `L`.

:::::::::::::::::::::::::::::::::::::::::  callout

## Який підхід найкращий?

Порівняйте ці підходи. Який з них ви надаєте перевагу використати?

::::::::::::::::::::::::::::::::::::::::::::::::::

GAP має дуже корисні засоби керування списком. Тепер ми розглянемо ще кілька прикладів.

Іноді GAP не має точної функції, яку ми хочемо.
For example, `NrMovedPoints` gives the number of moved points of a permutation,
but what if we want to find all permutations which move `4` points? This is where
GAP's arrow notation comes in. `g -> e` створює нову функцію, яка приймає один аргумент `g`,
і повертає значення виразу `e`. Ось кілька прикладів:

- пошук всіх елементів `G` без фіксованих точок:

```gap
Filtered( elts, g -> NrMovedPoints(g) = 4 );
```

```output
[ (1,2)(3,4), (1,3)(2,4), (1,4)(2,3) ]
```

- знайти перестановку в `G`, яка з'єднується (1,2) до (2,3)

```gap
Перша(elts, g -> (1,2)^g = (2,3) );
```

```output
(1,2,3)
```

Давайте перевіримо (пам'ятайте, що в районі GAP перемножилися ліворуч праворуч!):

```gap
(1,2,3)^-1*(1,2)*(1,2,3)=(2,3);
```

```output
істина
```

- перевіряє, чи всі елементи `G` переміщують точку з 1 до 2:

```gap
ForAll( elts, g -> 1^g <> 2 );
```

```output
хибність
```

- перевірка чи є елемент у "G", який рухається рівно до двох пунктів:

```gap
ForAny( elts, g -> NrMovedPoints(g) = 2 );
```

```output
хибність
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Використовуйте список операцій, щоб вибрати "ельсів" зі стабілізатора точки 2 і централізатора перестановки (1,2)

- `Filtered( elts, g -> 2^g = 2 );`

- `Filtered( elts, g -> (1,2)^g = (1,2) );`

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Пам'ятайте, що GAP чутлива до регістру!
- Не панічно якщо бачите `Помилку, змінна: 'FuncName' повинна мати значення`.
- Купіть імена змінних і функцій.
- Використовуйте редагування командного рядка.
- Використовувати автодоповнення замість введення імен функцій і змінних в повному обсязі.
- Використовуйте `?` та `??` для перегляду сторінок довідки.
- Встановіть формат довідки за замовчуванням у HTML за допомогою `SetHelpViewer`.
- Використовуйте функцію `LogTo`, щоб зберегти всі дані GAP і вивести в текстовий файл.
- Якщо розрахунок триває занадто довго, натисніть <Control>\-C для переривання його.
- Читайте "Перша сесія з GAP" з посібника GAP.

::::::::::::::::::::::::::::::::::::::::::::::::::


