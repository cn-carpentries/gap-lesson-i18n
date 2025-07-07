---
title: Функції в GAP
teaching: 40
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Використання командного рядка для прототипу
- Створення функцій
- Читання GAP коду з файлу

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Функції як спосіб повторного використання коду

::::::::::::::::::::::::::::::::::::::::::::::::::

Нагадаємо нам про наше завдання: скінченну групу _G_, ми хотіли б обчислити
середній порядок її елементів (тобто сума замовлень її елементів
поділена на порядок групи).

We begin with a very straightforward approach, iterating
over all elements of the group in question:

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
для g в S робити
  сума := sum + Замовлення (g);
od;
sum/Size(S);
```

```output
39020911/3628800
```

Тепер припустимо, що ми хотіли б зберегти цей фрагмент коду GAP, а потім
повторити це обчислення для деяких інших груп. We may even reformat it to fit
it into one line and use a double semicolon to suppress the output of `sum`:

```gap
sum:=0;; для g в S сума := sum + замовлення(g); od; sum/Size(S);
```

```output
39020911/3628800
```

Тепер ми можемо легко копіювати та вставити це до сеансу GAP наступного разу при потребі.
But here we see the first inconvenience: the code expects that the group in question
must be stored in a variable named `S`, so either we have to reset `S` each
time, or we need to edit the code:

```gap
S:=Альтернативна Група(10);
```

```output
Alt( [ 1 .. 10 ] )
```

```gap
sum:=0;; для g в S сума := sum + замовлення(g); od; sum/Size(S);
```

```output
2587393/259200
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Це працює лише для швидкого створення прототипів

- випадково копіювати і вставити тільки частину коду, а
  неповне введення може викликати цикл перерви;
- ще більше небезпеки: можна було забути скинути `sum` до нуля перед новим
  розрахунок та отримати неправильні результати;
- група, що ставиться під сумнів іншу назву змінної, так що код
  повинен бути змінений;
- **last, but not least:** when GAP code is pasted into the interpreter, it is evaluated line
  by line. If you have a long file with many commands, and a syntax error is
  in line _N_, this error will be reported only when GAP completes
  the evaluation of all preceding lines, and that might be quite time-consuming.

::::::::::::::::::::::::::::::::::::::::::::::::::

That is why we need to give our GAP code more structure by organising it
into functions:

- функції обробляються в першу чергу і можуть викликатись пізніше;
- any **syntax** errors will be detected in the parsing stage, and not at the time
  of the call;
- функції можуть мати локальні змінні, і це запобігає випадковому перезаписуванню їх
  після повторного використання змінної
  для зберігання чогось іншого.

Ця функція приймає аргумент `G` і обчислює середній порядок
його елементів:

```gap
AvgOrdOfGroup := function(G)
локальна сума, g;
сума := 0;
для g in G do
  sum := sum + замовлення(g);
od;
return sum/Size(G);
end;
```

```output
функція( Г) ... кінець
```

Тепер ми можемо застосувати її до іншої групи, передавши групу в якості аргумента:

```gap
A:=Альтернативні Group(10); AvgOrdOfGroup(A); час;
```

```output
Alt( [ 1 .. 10 ] )
2587393/259200
837
```

The example above also demonstrates `time` -- this is the variable which stores
the CPU time in milliseconds spent by the last command.

Thus, we may now create new groups and reuse `AvgOrdOfGroup` to calculate the average
order of their elements in the same GAP session. Our next goal is to make it
reusable for calculations in future sessions.

Використовуючи текстовий редактор (наприклад, той, який ви могли використовувати для попередніх
програм Carpentry lesson), створити текстовий файл під назвою "avgord. \`, що містить
наступний код функції і коментарі (хороший шанс практикуватися з використанням них!):

```gap
#####################################################################
#
# AvgOrdOfGroup(G)
#
# Calculating the average order of an element of G, where G meant to
# be a group but in fact may be any collection of objects having
# multiplicative order
#
AvgOrdOfGroup := function(G)
local sum, g;
sum := 0;
for g in G do
  sum := sum + Order(g);
od;
return sum/Size(G);
end;
```

Тепер створіть новий сеанс GAP та створіть іншу групу, наприклад, `MathieuGroup(11)`:

```gap
M11:=MathieuGroup(11);
```

```output
Група ([ (1,2,3,4,5,6,7,8,9,10,11), (3,7,11,8)(4,10,5,6)
```

Clearly, `AvgOrdOfGroup` is not defined in this session, so an attempt to
call this function results in an error:

```gap
AvgOrdOfGroup(M11);
```

```error
Помилка, змінна: 'AvgOrdOfGroup' повинно мати значення
у будь-якій функції на рядку 2 *stdin*
```

Для доступності, спершу потрібно завантажити за допомогою функції `Read`. Below
we assume that the file is in the current directory, so no path is needed.

```gap
Читання ("avgord.g");
```

This loads the file into GAP, and the function `AvgOrdOfGroup` is now
available:

```gap
AvgOrdOfGroup(M11);
```

```output
53131/7920
```

В цьому прикладі використання `Read`, нову сесію GAP було запущено, щоб очистити
, що параметр `AvgOrdOfGroup` не існував до дзвінка `Read` і був завантажений
з файлу. Проте, файл з такою функцією, як це, може бути прочитаний кілька
в одному сеансі GAP (пізніше ви побачите випадки при повторному читанні файлу
є більш складним). Виклик `Read` знову виконує весь код в файлі
. This means that if the code of the function has been modified, and
it has no errors (but possibly has warnings), the function will be
overwritten. **Ніколи не ігноруйте попередження!**

Наприклад, давайте змінимо файл і замінимо рядок

```gap
сума повертає/Розмір(G);
```

за лінією з уточненою помилкою синтаксису:

```gap
повернути Float(sum/Size(G);
```

Прочитати файл допомогою

```gap
Читання ("avgord.g");
```

і ви побачите повідомлення про помилку:

```error
Синтаксична помилка: очікується в avgord.g рядок 7
повертати Float(sum/Size(G);
^
```

Since there was an error, the `AvgOrdOfGroup` function in our session was not
redefined, and remains the same as last time it was successfully read:

```gap
Друк (AvgOrdOfGroup);
```

```output
функція ( G )
    для g in G сума
        := sum + замовлення( g);
    od;
    return sum / Розмір ( G );
кінець
```

Now correct the error by adding the missing closing bracket,
read the file again and recalculate the average order of an element for `M11`:

```gap
Read("avgord.g");
AvgOrdOfGroup(M11);
```

```output
6.70846
```

Тепер давайте розглянемо приклад _попередження_. Since it is only a warning, it will
redefine the function, and this may cause some unexpected result. To see what
could happen, first edit the file to roll back the change in the type of the
result (so it will return a rational instead of a float), and then comment
out two lines as follows:

```gap
AvgOrdOfGroup := function(G)
# локальна сума, g;
# сума:= 0;
для g in G do
  sum := sum + замовлення(g);
od;
return sum/Size(G);
end;
```

Тепер, коли ви прочитали файл, ви побачите попередження:

```gap
Читання ("avgord.g");
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

Ці попередження означають, що оскільки `g` і `sum` не оголошені як `local`
змінні, GAP очікує, що вони будуть глобальними змінними в той час, коли
буде викликана функція. Оскільки після виклику `Read`
вони не існували, було показано попередження. However, if they happened to exist
by that time, there would be no warning, and any call to `AvgOrdOfGroup` would
overwrite them! This shows how important it is to
declare local variables. Let us investigate what happened in slightly
more detail:

The function is now redefined, as we can see from its output (or can
inspect with `PageSource(AvgOrdOfGroup)` which will also display any comments):

```gap
Друк (AvgOrdOfGroup);
```

```output
функція ( G )
    для g in G сума
        := sum + замовлення( g);
    od;
    return sum / Розмір ( G );
кінець
```

але спроба запустити його в результаті в циклі перери:

```gap
AvgOrdOfGroup(M11);
```

```error
Помилка, Змінна : 'sum' повинна мати призначене значення в
  sum := sum + замовлення( g ); дзвонимо з
<function "AvgOrdOfGroup">( <arguments> )
 викликано з циклу "читання-eval у рядку 24 *stdin*
Ви можете "return; після призначення значення
brk>
```

що ви можете закрити, використовуючи `quit;`.

Далі ми демонструємо, як все може піти не так:

```gap
sum:=2^64; g:=[1];
```

```output
18446744073709551616
[ 1 ]
```

```gap
AvgOrdOfGroup(M11);
```

```output
18446744073709604747/7920
```

```gap
сума; г;
```

```output
18446744073709604747
(1,2)(3,10,5,6,8,9)(4,7,11)
```

Now, before reading the next part of the lesson, please
revert the last change by uncommenting the two commented lines, so that
you have initial version of `AvgOrdOfGroup` in the file `avgord.g` again:

```gap
AvgOrdOfGroup := function(G)
локальна сума, g;
сума := 0;
для g in G do
  sum := sum + замовлення(g);
od;
return sum/Size(G);
end;
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Шляхи

- It is important to know how to specify paths to files in all operating
  systems and where to find your home and current directory.

- It is useful to know that path and filename completion is activated by
  pressing Esc two or four times.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Командний рядок підходить для прототипу; функції корисні для повторюваних розрахунків.
- Інформаційні імена функцій та коментарі зроблять код більш читабельним для вашого майбутнього та для інших.
- Остерігайтеся неоголошених місцевих змінних!

::::::::::::::::::::::::::::::::::::::::::::::::::


