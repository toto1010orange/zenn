---
title: "式と文の違い"
emoji: "🧩"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["数学","プログラミング"]
published: false
---
## はじめに
1+1を1に1を足すことだと思っていませんか？もしその場合、その認識は間違っているかもしれません。

数学やプログラミングが苦手な人は式に対するイメージが正しくないという印象があります。
そのためこの記事を通して式とは何かというイメージを正しく持っていただきたいと思います。

## 式と文の違い
結論を一行でいうと**文は処理、式は値であるという違い**です。
pythonでosをimportする場合で例えます。
`import this`という文はimportする、pythonではthis.pyを実行するという処理です。
`__import__("this")`という式はimportしたthisモジュールそのものです。
2つのコマンドを比較してみます。
```
└─$ python3 -c "import this"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
というようにこちらはthis.pyで定義されている処理が実行されています。this.pyは特殊ですが通常はこの処理は関数を使えるようにするという処理が返ります。
一方で
```
└─$ python3 -c "print(__import__('this'))"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
<module 'this' from '/usr/lib/python3.14/this.py'>
```
というようにこちらは`__import__("this")`は`<module 'this' from '/usr/lib/python3.14/this.py'>`というオブジェクトになっています。つまり式の場合はthis.pyを実行したあとのオブジェクトが返ります。

※　一般にいう式を文として解釈する言語もあります。
## 式という意識を正しく持つことの数学教育的意義
式はある処理を実行した後のオブジェクトです。例えば`1+1`という式なら2というオブジェクトだということです。一方でadd 1 1という文は一般的にレジスタに2を置くという処理ですよね。
この感覚がない場合に、数学の方程式などで、右辺=左辺なら両辺に同じ処理をしても等式は崩れないという方則を本当の意味で理解することができません。
例えば$2x^2-3x+1=x^2+2x-5$の左辺$2x^2-3x+1$を
```
xを二乗したものに2をかけたものからxを3倍したものに1をたす
```
という処理という風に捉えてしまうと両辺に同じものを足してなぜ等価性が崩れないのか理解できない場合があります。
しかし本来は
```
xを二乗したものに2をかけたものからxを3倍したものに1をたした結果
```
という意味を表しています。
処理の順序はわかりにくいです。しかし処理の結果は値なので**その外で扱われる際の順序**という概念はありません。
そのため方程式の原理やもっと難解な式でもより容易に理解できます。
## まとめ
式は値、文は処理である。
