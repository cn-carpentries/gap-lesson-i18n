---
title: Використовуються регресійні тести
teaching: 40
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Створення і запуск тестових файлів
- Розумить, як можна визначити та інтерпретувати розбіжності та регресії стаціонару
- Зрозумійте як налаштувати тести, щоб перевірити випадкові алгоритми
- Дізнайтеся, як "Зроби це правильним, а потім зробити концепцію швидкого "

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Керована тестами розробка

::::::::::::::::::::::::::::::::::::::::::::::::::

The code of `AvgOrdOfGroup` is very simple, and nothing could possibly go wrong
with it. By iterating over the group instead of creating a list of its elements,
it avoids running out of memory
(calling `AsList(SymmetricGroup(11))` already results in exceeding the permitted
memory). Однак, обчислення все ще потребує часу, за декілька хвилин
потрібно було обчислити середній порядок
елемента `Симетричної групи (11)`. But at least we are confident that it is
correct.

Now we would like to write a better version of this function using some
theoretical facts we know from Group Theory. We may put
`avgord.g` under version control to revert changes if need be;
we may create a new function to keep the old one around and compare the
results of both; but this could be made even more efficient if we
use **regression testing**: this is the term for testing based on
rerunning previously completed tests to check that new changes do not
impact their correctness or worsen their performance.

Для початку нам потрібно створити **тестовий файл**. The test file looks
exactly like a GAP session, so it is easy to create it by copying and
pasting a GAP session with all GAP prompts, inputs and outputs into a
text file (a test file could be also created from a log file with a
GAP session recorded with the help of `LogTo`). During the test, GAP will
run all inputs from the test file, compare the outputs with those in the test
file and report any differences.

GAP test files are just text files, but the common practice is to name
them with the extension `.tst`. Now create the file `avgord.tst` in the current directory (to
avoid typing the full path) with the following content:

```gap
# тестів за середній порядок елемента групи

# permutation group
gap> S:=SymmetricGroup(9);
Sym( [ 1 . 9] )
gap> AvgOrdOfGroup(S);
3291487/362880
```

Як бачите, у файлі з тестами містяться коментарі, які визначають
, де вони можуть бути розміщені, тому що ви зможете розрізняти коментарі
у тестовому файлі від виходу GAP почався з `#`. For that purpose,
lines at the beginning of the test file that start with `#`, and one empty line
together with one or more lines starting with `#`, are considered as comments.
Усі інші лінії інтерпретуються як вихід GAP з попереднього введення GAP.

Щоб запустити тест, використайте функцію `Тест` (див.
[documentation](https://docs.gap-system.org/doc/ref/chap7.html#X87712F9D8732193C).
Наприклад, (якщо припустити, що функція "AvgOrdOfGroup" вже завантажена):

```gap
Тест("avgord.tst");
```

```output
істина
```

In this case, `Test` reported no discrepancies and returned `true`, so we
conclude that the test has passed.

We will not cover the topic of writing a good and comprehensive test suite here,
nor will we cover the various options of the `Test` function, allowing us, for
example, to ignore differences in the output formatting, or to display the progress
of the test, as these are described in its documentation.

Натомість ми додамо більше груп, щоб "відмовитися. st\`, щоб продемонструвати, що
код також працює з іншими групами, і щоб показати різні способи
поєднання команд у тестовому файлі:

```gap
# tests for average order of a group element

# permutation group
gap> S:=SymmetricGroup(9);
Sym( [ 1 .. 9 ] )
gap> AvgOrdOfGroup(S);
3291487/362880

# pc group
gap> D:=DihedralGroup(512);
<pc group of size 512 with 9 generators>
gap> AvgOrdOfGroup(D);
44203/512
gap> G:=TrivialGroup();; # suppress output
gap> AvgOrdOfGroup(G);
1

# fp group
gap> F:=FreeGroup("a","b");
<free group on the generators [ a, b ]>
gap> G:=F/ParseRelators(GeneratorsOfGroup(F),"a^8=b^2=1, b^-1ab=a^-1");
<fp group on the generators [ a, b ]>
gap> IsFinite(G);
true
gap> AvgOrdOfGroup(G);
59/16

# finite matrix group over integers
gap> AvgOrdOfGroup( Group( [[0,-1],[1,0]] ) );
11/4

# matrix group over a finite field
gap> AvgOrdOfGroup(SL(2,5));
221/40
```

Давайте перевіримо розширену версію тесту ще раз і перевіримо, чи вона працює:

```gap
Тест("avgord.tst");
```

```output
істина
```

Тепер ми будемо працювати над кращою реалізацією. Of course, the order of an element
is an invariant of a conjugacy class of elements of a group, so we need only to
know the orders of conjugacy classes of elements and their representatives.
наступний код, який ми додаємо в `avgord.g`, читається в GAP і змінює визначення
`AvgOrdOfGroup` без жодних синтаксичних помилок:

```gap
AvgOrdOfGroup := function(G)
local cc, сума, c;
c:=ConjugacyClasses(G);
sum:=0;
for c in cc do
  sum := sum + Замовлення ( Представник (c) * Розмір (c);
od;
return sum/Size(G);
end;
```

але коли ми будемо запускати тест, ось буде сюрприз!

```gap
Read("avgord.g");
Test("avgord.tst");
```

```output
########> Diff in avgord.tst, line 6:
# Input is:
AvgOrdOfGroup(S);
# Expected output:
3291487/362880
# But found:
11/672
########
########> Diff in avgord.tst, line 12:
# Input is:
AvgOrdOfGroup(D);
# Expected output:
44203/512
# But found:
2862481/512
########
########> Diff in avgord.tst, line 23:
# Input is:
AvgOrdOfGroup(G);
# Expected output:
59/16
# But found:
189/16
########
########> Diff in avgord.tst, line 29:
# Input is:
AvgOrdOfGroup(SL(2,5));
# Expected output:
221/40
# But found:
69/20
########
false
```

Дійсно, ми зробили typo (навмисне) і замінили `Розмір(c)` розміром `Size(cc)`.
Правильна версія, звичайно, повинна виглядати наступним чином:

```gap
AvgOrdOfGroup := function(G)
local cc, сума, c;
c:=ConjugacyClasses(G);
sum:=0;
for c in cc do
  sum := sum + Замовлення ( Представник (c) * Розмір (c);
od;
return sum/Size(G);
end;
```

Тепер ми виправимо це в `avgord.g`, і знову прочитайте і протестуємо знов, щоб переконатися, що
тести виконані правильно.

```gap
Read("avgord.g");
Test("avgord.tst");
```

```output
істина
```

Таким чином, підхід 'Зроби це правильним, а потім зробити його швидкою' допоміг виявити помилку
відразу після того, як він був представлений.

:::::::::::::::::::::::::::::::::::::::: keypoints

- Створення файла тестів легке шляхом копіювання та вставки сеансу GAP.
- Написання доброго і всебічного тестового набори вимагає деяких зусиль.
- Зробіть це правильно, а потім робіть це швидше!

::::::::::::::::::::::::::::::::::::::::::::::::::


