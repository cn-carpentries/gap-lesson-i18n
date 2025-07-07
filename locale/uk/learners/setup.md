---
title: Установка
permalink: /setup/
---

## Вікна

From the [GAP Downloads page](https://www.gap-system.org/Releases/),
download the `.exe` installer and double click on the file to run it.
When you are asked for the installation path, note that it should
not contain spaces. For example, you may install GAP 4.X.Y in `C:\gap-4.X.Y`
(default), `D:\gap-4.X.Y` or `C:\Math\GAP\gap-4.X.Y`, but you must not
install it in a directory such as `C:\Program Files\gap-4.X.Y` or
`C:\Users\alice\My Documents\gap-4.X.Y`.

## macOS

На macOS, вам необхідно встановити GAP з джерела, як пояснено
на [сторінці завантаження GAP](https://www.gap-system.org/Releases/).
Завантажте один із наданих там архівів, розпакуйте його та запустіть
`./configure && make` в розпакованій теці. Then change to the
`pkg` subdirectory and call `../bin/BuildPackages.sh` to run the
script which will build most of the packages that require compilation
(provided sufficiently many libraries, headers and tools are available).

Крім того, ви також можете встановити GAP за допомогою [Homebrew](https://brew.sh/).
Після встановлення Homebrew, слідуйте інструкціям
[GAP Homebrew tap](https://github.com/gap-system/homebrew-gap).

## Linux

На Linux, ви повинні встановити GAP з джерела, як пояснено на
[сторінка завантаження GAP](https://www.gap-system.org/Releases/).
Завантажте один із наданих там архівів, розпакуйте його та запустіть
`./configure && make` в розпакованій теці. Then change to the
`pkg` subdirectory and call `../bin/BuildPackages.sh` to run the
script which will build most of the packages that require compilation
(provided sufficiently many libraries, headers and tools are available).


