---
title: 设置
permalink: /setup/
---

## 窗口

从 [GAP 下载页面](https://www.gap-system.org/Releases/),
下载`.exe` 安装程序并双击文件来运行它。
When you are asked for the installation path, note that it should
not contain spaces. For example, you may install GAP 4.X.Y in `C:\gap-4.X.Y`
(default), `D:\gap-4.X.Y` or `C:\Math\GAP\gap-4.X.Y`, but you must not
install it in a directory such as `C:\Program Files\gap-4.X.Y` or
`C:\Users\alice\My Documents\gap-4.X.Y`.

## macOS

On macOS, you need to install GAP from source as explained
at the [GAP Downloads page](https://www.gap-system.org/Releases/).
下载其中一个存档，解包后在未打包的目录下运行
`./configure && make` 。 Then change to the
`pkg` subdirectory and call `../bin/BuildPackages.sh` to run the
script which will build most of the packages that require compilation
(provided sufficiently many libraries, headers and tools are available).

或者，您也可以使用 [Homebrew](https://brew.sh/ 安装GAP。
安装Homebrew后，按照
[GAP Homebrew tap](https://github.com/gap-system/homebrew-gap)的说明操作。

## Linux

在 Linux 上，您需要按照
[GAP 下载页面](https://www.gap-system.org/Releases/)的解释从源安装GAP。
下载其中一个存档，解包后在未打包的目录下运行
`./configure && make` 。 Then change to the
`pkg` subdirectory and call `../bin/BuildPackages.sh` to run the
script which will build most of the packages that require compilation
(provided sufficiently many libraries, headers and tools are available).


