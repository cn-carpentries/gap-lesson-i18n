---
title: Інформація інструктора
permalink: /інструкція/
---

## Усього

- For the first lesson, good to have access to Windows (VM or remote desktop) to
  demonstrate some Windows-specific aspects of working with GAP.

- Перед початком перевірте, чи всі встановили GAP та вміли його запускати.
  Також нагадую, що йому не рекомендується встановлювати в шлях з пробілами, наприклад, в
  "Мої документи".

- Важливо, щоб учні зрозуміли, як працювати з файлами
  , розташованими в різних каталогах. `ChangeDirectoryCurrent` is the function
  from the IO package (requires compulation), which should be available if
  GAP is properly installed (i.e. installed following instructions for the
  workshop). У разі будь-яких проблем, перший крок до виправлення неполадок
  перевірити чи "LoadPackage("io");\` повертає "невдало". Якщо так, то виправити
  для користувачів Windows - ввести повний шлях до файлів. Linux and macOS users
  are less affected as for the, the way how they should start GAP is to
  navigate to the needed directory in the Terminal and start GAP from there.

- Допомога у налаштуванні параметрів терміналу, особливо показувати користувачам Windows, які
  можуть змінювати кольори і шрифти в mintty shell (та, яка починається з розриву
  з прогалини. атт\`).

- Поясніть, як копіювати, вставляти введення і вивід (особливо на Windows).

- Поясніть, як читати сторінки уроків. Вхід GAP є типом без рядка GAP.
  Вивід GAP є синім кольором. Помилки відображаються червоним. Промоти GAP
  не відображаються, якщо це не дійсно необхідно (наприклад, щоб продемонструвати, як працює багаторядковий введення
  ).

- Важливо, що інструктор запускає GAP з опцією «-r», щоб уникнути
  втручатися в власні параметри GAP. . локально встановлені пакунки та
  інший вміст теки `.gap`.

- Щоб використовувати кольоровий запит, коли GAP запущено опцією `-r`, щоб ігнорувати всі налаштування
  , включаючи це (якщо встановлено), виклик `ColorPrompt(true);`.

## [Перша сесія з GAP]({% посилання \_епізоді/01-command-line.md %})

- Зберігайте те, що банер містить інформацію про версію для посилається на GAP чи
  повідомлення про помилки. Вибір пакетів може відрізнятися, але відсутні **IO** та
  **Брауз** пакети вказують на те, що ці та, можливо, деякі інші пакети
  , які потребують компіляції, не були скомпілювані.

- A second call to `LogTo("logfile");` will not open the new file but will report
  that GAP is already logging to another file. In this case, either ignore it if
  you would like to continue logging to the file already in use, or call `LogTo();`
  to close the current log file and then call `LogTo` with an argument to start
  logging to a new file.

- Showing an example of the error with `factorial`, mention that such error
  also happens if e.g. some file has to be read or some package should be loaded
  to define the function.

- Обговоріть чому це погана практика Google для ручного використання GAP, а не
  використання системи допомоги GAP.

- Майте на увазі, що екран допомоги при виборі буде виглядати інакше, якщо пакет **Браузер**
  не буде скомпільовано.

- Поясніть, як перемикатися на HTML версію вручну з підтримкою MathJax.

- Зверніть увагу на різницю між "AsList" і "AsSSortedList".

- Допоможіть подзвонити `WriteGapIniFile` і налаштувати GAP, наприклад, використовувати браузер як
  viewer.

- Demonstrating how to type `Sum( List( elts, Order ) ) / Length( elts );`
  show how to assemble this command using command line editing and moving
  around the line, perhaps executing partial command to see their results,
  instead of typing the whole command from first to last character sequentially.

- Використовуйте Etherpad для голосування за підходи, щоб обчислити середній порядок списку.
  Після цієї ситуації, коли кожен з них може бути кращим за інших.

1. Розв'язання задачі: `Filtered( elts, g -> 2^g = 2 );` і
  `Filtered( elts, g -> (1,2)^g = (1,2) );`.

## [Ще деякі інші об'єкти GAP]({% посилання \_епізоді/02-some-objects.md %})

- Floats, cyclotomics, finite fields elements are not used further in the
  lesson, but we mention them briefly to show that they exist.

- Emphasize that organising complex objects into nested records may
  be more efficient than nested lists.

- Будьте обережні, що `w:="supercalifragilisticexpialidocious"; IsSubset(w,'s');`
  призводить до помилки без методу. This may be a good moment to introduce
  this special kind of error messages.

- For extending GAP with new types of objects, refer to
  [Creating New Objects](https://docs.gap-system.org/doc/ref/chap79.html)
  and [Examples of Extending the System](https://docs.gap-system.org/doc/ref/chap80.html)
  of the GAP Reference Manual.
  Також, [пакет Серця](https://gap-packages.github.io/circle/)
  надає приклад подовження GAP з новими мультиплікативними об'єктами.

1. Розв'язання виклику:
  `r:=c[1]; для i в [2.. ength(c)] виконувати, якщо c[i][2]>r[2] потім r:=c[i]; fi; od; r;`

## [Функції в GAP]({% посилання \_епізоді/03-func.md %})

- Витрачайте деякий час на структуру функції GAP: ключові слова `функція`,
  `local`, `return`, `end`, та інші конструкції мови, які там піддані.

- Скажіть як дослідити цикл перерви при відображенні прикладу з помилкою
  повідомленням.

## [Використання регресійних тестів]({% link \_episodes/01-command-line.md %})(04-testing.html)

- Learners may need help with formatting the test because of misplaced comments
  and/or different formatting of the output.

- Обкладинки створення тестових файлів репродукційно: випадкові vs явні приклади,
  придушує вихід з подвійною крапкою з комою тощо.

- Зверніться до інших параметрів `Тесту`, таких як порівняння виводу до
  пробілів, показуючи прогрес тесту і т.п.

- Згадайте функцію `TestDirectory`, щоб запустити набір тестів.

- Загадка про профілювання та засоби покриття коду.

## [Пошук у невеликих групах]({% зв'язку \_епізодіз/05-small-groups.md %})

- Give an overview of `SmallGroup`, `AllSmallGroups`, `NrSmallGroups` and
  `SmallGroupsInformation` with some examples.

- Обговоріть про те, чому ітерації краще, ніж AllSmallGroups вичерпуючи пам'ять
  (згадайте концепцію об'єктів самонавчання (описується).

- A side question is how to convert a pc group, returned by `SmallGroup`, to
  some other representation, e.g. permutation or fp group.

- Живе кодування є кращим способом навчати більшості функцій
  з цього уроку.

1. Розв'язання задачі:
  `Sum(List(Filtered([1..2000], n -> не IsPrimePowerInt(n),NrSmallGroups)); NrSmallGroups(1536); last;`.
  In addition to `SmallGroup(105,1)` and `SmallGroup(357,1)`, another
  group is `SmallGroup(1785,1)`.

## [Атрибути та методи]({% посилання \_епізоді/06-атрибути.md %})

- Чому не варто заявляти "Рендом" як атрибут?

1. Ідеї для завдання: спробуйте `k:=1` і потім `k:=k+1;n:=2^k;AvgOrdOfCollection(DihedralGroup(n);AvgOrdOfGroup(DihedralGroup(n);time;`.
  Навіть для `k=20`, 1-ша функція займає близько 15s і 2-го - близько 115s
  на MacBook Pro.


