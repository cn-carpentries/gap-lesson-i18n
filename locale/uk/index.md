---
site: канальний папір::sandpaper_site
---

[GAP](https://www.gap-system.org) is a system for discrete computational algebra,
with particular emphasis on Computational Group Theory. GAP provides a
programming language, a library of thousands of functions implementing algebraic
algorithms written in the GAP language as well as large data libraries of algebraic
objects, for example the [Small Groups Library](https://gap-packages.github.io/smallgrp/)
which contains, among others, all 423 164 062 groups of order at most 2000 except 1024.

Цей урок дає вступ до GAP. Він зосереджений навколо загального завдання
пошуку в бібліотеці дрібних груп для цікавих прикладів і підприкладів,
та конкретна проблема дослідження, в якій ми будемо зацікавлені - це \*\*знайти
приклади нетривіальних груп, так що середній порядок їх елементів є цілим числом \*\*.

The lesson will lead the learner along the path from working in the GAP command
line and exploring algebraic objects interactively to saving the GAP code into
files, creating functions and regression tests, and further to performing
comprehensive search and extending the system by adding new attributes.

По цьому шляху учень стане знайомий з:

- базові конструкції мови програмування GAP,

- способи пошуку необхідної інформації в системі GAP та

- хороші практики проектування коду GAP у складних програмах.

::::::::::::::::::::::::::::::::::::::::::  prereq

## Передумови

The lesson is oriented on learners possessing the minimal theoretical
background (at least at the level of an undergraduate group theory course)
and willing to learn how concepts from abstract algebra may be
explored using computational tools.
Необхідний попередній досвід роботи з GAP.

Learners only need to understand the concepts of files and directories
(including home and working directories) and know how to start GAP.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  checklist

## Приготуватися

1. У домашньому каталозі створіть новий каталог під назвою "avgord".
2. Запустити GAP:

- для Linux і macOS, відкрийте термінал і викличте `path-to-your-gap-installation/gap-4.X.Y/gap`
  (редагувати шлях, як необхідний);
- on Windows, start GAP using the Start menu or a desktop shortcut
  created after GAP installation.

3. Встановіть поточний каталог в `avgord`:

- on Linux and macOS, call `ChangeDirectoryCurrent("/Users/username/avgord");`
  (edit the path as necessary; remember to type the full path to your home
  directory instead of `~`).
- для Windows, викличте `ChangeDirectoryCurrent("C:/Users/username/avgord");`
  (редагувати шлях, як це необхідно; не забудьте використовувати `/` замість `\`);

4. Переконайтеся, що ваш поточний каталог налаштовано правильно: виклик `DirectoryCurrent();`
  і перевірте, що шлях у вихідних точках розташований у каталозі `avgord`.

::::::::::::::::::::::::::::::::::::::::::::::::::


