---
title: Обговорення
permalink: /discuss/
---

## Десять гінтів для початківців GAP

1. **Пам'ятайте, що GAP чутливий до регістру!** Це означає, що "ABC", "Abc" і "abc"* три різні ідентифікатори. Виклик на `SymmetricGroup(3)` працює, але
    `Symmetricgroup(3)` викличе помилку.

2. An error message **`"Error, Variable: 'FuncName' must have a value"`** in a
  function call usually points to a typo in the function name (see the previous hint),
  or to some package that must be loaded in advance using
  [**`LoadPackage`**](https://docs.gap-system.org/doc/ref/chap76.html#X79B373A77B29D1F5).

3. \*\*Не вагатися у використанні довших і більш інформативних змінних, де
  підходять. \* Наприклад, `x` абсолютно підходить для `Список ([1..10], x -> x^2)`,
  , а `ConClassesReps` може бути більш інформативним, ніж просто `x` для списку
  представників кон'югантних класів групи.

4. **Використовуйте редагування командного рядка:** прокрутіть історію команд і переміщайтеся всередині
  командний рядок за допомогою клавіш зі стрілками для редагування.

5. \*\*Використовувати автодоповнення замість введення назви функцій та змінних в повному обсязі. \*
  Введіть початкову частину ідентифікатору, а потім натисніть `<Tab>`. It will be
  completed if its unique completion is possible. If not, you may press `<Tab>`
  again to see all possible suggestions.

6. **Для перегляду сторінок довідки, використовуйте `?` та `?` команди**. This will search not only
  in the GAP manuals, but also in the manuals of all GAP packages available
  in your GAP installation.

7. **Встановіть формат довідки за замовчуванням у HTML.** Використовуйте
  [**`SetHelpViewer`**](https://docs.gap-system.org/doc/ref/chap2.html#X87C1BFB2826488B0)
  , щоб переглянути його в бажаному браузері.

8. **Use [**`LogTo`**](https://docs.gap-system.org/doc/ref/chap9.html#X79813A6686894960)
  to save all GAP input and output into a text file.** It should be called before
  calculations, not after!

9. **If the calculation takes too long, press `<Control>-C` to interrupt it**.
  Введіть наступне; для того, щоб залишити петлю зупинок.

10. **Прочитайте [Перша сесія з GAP](https://docs.gap-system.org/doc/tut/chap2.html)**
  з посібника GAP.

## Письмо програми в GAP

- Використовуйте прямі розрахунки в командному рядку для розвідки та прототипізації об'єктів,
  потім подумайте як організувати свій код, щоб він став знову придатним.

- Використовуйте [**`LogTo`**](https://docs.gap-system.org/doc/ref/chap9.html#X79813A6686894960)
  для збереження даних і виходів до log-файлу, який потім ви можете редагувати в текстовому редакторі.

- Save code in text files and use
  [**`Read`**](https://docs.gap-system.org/doc/ref/chap9.html#X8373AC6B7D5F9167)
  to load them. Знайдіть якийсь розширений текстовий редактор для редагування цих файлів.

- Зробіть ваш код модульним та повторно придатним для використання, організувавши його у функціях.

- Пишіть коментарі в коді - це допоможе вам, коли ви повернетеся до нього через деякий час.

- Understand [break loops](https://docs.gap-system.org/doc/ref/chap6.html#X8593B49F8705B486):
  you may [explore variables](https://docs.gap-system.org/doc/ref/chap6.html#X7EE5CF2C8419F061)
  on the current break level and use
  [**`Where`**](https://docs.gap-system.org/doc/ref/chap6.html#X7A7FFA2B7C1EF5A3)
  to show the last commands before the error occurred.

- Use [preferences mechanism](https://docs.gap-system.org/doc/ref/chap3.html#X7FD66F977A3B02DF)
  to customise GAP, for example, to set help viewer to HTML or to make command line history available
  after quitting GAP in the next GAP session.

- Understand the theory behind calculations: theoretical improvements could improve
  the performance much more than highly optimised code which still does a brute-force calculation.

- Реалізація алгоритмів не забувайте про кут справи. Наприклад, чи працює реалізація
  для тривіальної групи чи елементу особи?

- Do not rely that GAP functions return results in a particular order, unless this
  is documented. Наприклад, залежить від методу, можливо не гарантувати
  перераховані класи кон'югації або незначні символи в одному замовленні
  або що перший елемент у списку - це клас кон'югантності
  елемента або тривіальний символ.

- Не запитувати більше, ніж потрібно, оскільки це може мати наслідки для продуктивності.
  Наприклад:

  - Якщо властивість є інваріант класу кон'югації (елементів
    підгрупи), вас може зацікавити тільки перегляд представників
    занять кон'югатими.

  - If you are interested in a list of elements of a collection, without a
    particular order, use `AsList` instead of `AsSSortedList`.

  - Do not calculate conjugacy classes of all subgroups, if e.g. you are
    interested only in normal or maximal subgroups - there are special
    methods to compute them.

  - Якщо ви шукаєте _p_\-підгрупи, спочатку можете обчислити
    силову _p_\-підгрупу групи, а потім подивіться на їх підгрупи
    та їх піджонати.

  - Представлення мають значення: він може бути вартий перетворення групи з fp групи
    в ізоморфну групу або групу прав для використання швидших методів.

- Переглядайте [GAP Frequently Asked Questions](https://www.gap-system.org/faq/) для подальших отримувачів.

## Залишайтеся на зв'язку

- Підпишіться на **[Форум доступу GAP](https://www.gap-system.org/forum/)**.

- Якщо вам потрібна допомога, оберіть один з цих трьох варіантів, залежно від питання:

  - ask questions in the [GAP Forum](https://www.gap-system.org/forum/)

  - send them to the [GAP Support](https://www.gap-system.org/issues/)

  - розміщувати їх у [математичний Q\&A сайті](https://math.stackexchange.com/questions/tagged/gap?sort=frequent&pageSize=50)

## Внесок у GAP

- Якщо ви думаєте, що ви знайшли помилку: будь ласка,
  [створити проблему на GitHub](https://github.com/gap-system/gap/issuesчи
  повідомлять про це електронною поштою в [підтримку GAP](https://www.gap-system.org/issues/).

- Будь ласка, встановіть GAP, якщо ви його використовуєте. Це допоможе спільноті рости,
  і це допоможе вам у зворотному напрямку.
  [This page](https://www.gap-system.org/cite/)
  suggests how to cite GAP, and the function
  [**`Cite`**](https://docs.gap-system.org/doc/ref/chap76.html#X79637D9A7B1AD7F7)
  will help to generate citation sample for precisely the same version of GAP that is used.

- Consider sharing your GAP developments with others, from sharing your code by
  available means to organising it into a GAP package, submitted for the redistribution
  with GAP and optionally for the refereeing.

- Зробити внесок у подальший розвиток самого цього уроку.

## Поради та хитрощі

- Це простий підхід до дзвінка GAP з shell сценарій. Створіть скрипт
  під назвою `check-one-order.sh` з наступним змістом:

```gap
#!/bin/sh

gap -r -b -q avgord.g << EOI
TestOneOrderEasy( $1 );
quit;
EOI
```

і зробіть його виконуваним за допомогою `chmod u+x check-one-order.sh`. Now you may call
it as follows:

```gap
$ ./контрольне одне замовлення 24
```

```output
невдача
```

```gap
$ ./check-one-order.sh 105
```

```output
[ 105, 1 ]
```

- Читання файлів даних

GAP може прочитати будь-які дійсні дані GAP з коду, використовуючи `Read`. The contents will
be read and evaluated in the main read-evaluate-print loop, but the results will
not printed. Іноді може захотіти прочитати вміст файлу як функцію
і повернути цю функцію - можна використати для цього типу `ReadAsFunction`.
Але що робити, якщо у вас є деякі дані, які надходять з іншого джерела, і це
не дійсне введення GAP? Іноді ви можете контролювати інструмент, який експортує
дані і може мати можливість налаштувати їх для генерації файлу введення GAP. But where to look
if this option is not possible?

`ReadCSV( filename[, nohead][, розділювач ])` читає файл у форматі CSV (через кому
і повертає його записи, як список записів
(див. [documentation](https://docs.gap-system.org/doc/ref/chap10.html#X848DD7DC79363341)).
Записи першого рядка файлу будуть використовуватися в іменах
компонентів запису (ярлики будуть перекладені в підкреслення).
Можна також вказати, що перший рядок містить дані замість
імена полів та також вказано користувацький роздільник. І навпаки, `PrintCSV`
може використовуватися для виводу файлів CSV.

To read arbitrary (binary or text) files as strings, use the `StringFile`
function provided by the GAPDoc package (see
[documentation](https://docs.gap-system.org/pkg/gapdoc/doc/chap6.html#X7E14D32181FBC3C3)).
Це поверне вміст файлу як рядок.
Після цього, ви можете використовувати різні інструменти керування рядками (див.
[Рядки і символів](https://docs.gap-system.org/doc/ref/chap27.html)
в посиланні на GAP вручну), щоб опрацювати це у потрібний вам спосіб. GAPDoc package
also provides the `FileString` function which writes the content of a string
into a file.

If you need to organise reading/writing line by line, instead of reading or
writing the whole file/string at once, we suggest to look at the functionality
provided by the IO package
(see [documentation](https://docs.gap-system.org/pkg/io/doc/chap4.html)),
in particular at `IO_ReadLine` and `IO_WriteLine`.


