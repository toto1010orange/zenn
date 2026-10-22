---
title: "pipが使えない環境でパッケージをインストールする方法"
emoji: "📦"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [pip,linux]
published: true
---

最近のlinux osでは
```bash
└─$ pip install matplotlib
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

というようにエラーが出て依存関係を守ろうとすることが多いと思います。
強制的にインストールすることはできますが少し怖いですよね。

ということで今回は、pipが使えない場合の私が実践している対処法について解説していきます。

#### 一つ目
まず実はaptなどのパッケージ管理ツールでもインストールすることができるという場合があります。
```bash
apt search python3-{パッケージ名}
apt install python3-{パッケージ名}
```
{パッケージ名}をインストールしたいパッケージ名に置き換えてください。
AIに聞いても大丈夫です。

#### 二つ目
pipxを使う方法です。
ただしこの方法はCLIツール専用でありコマンドとして呼び出すことはできますが、importして使用することはできません。importすることを想定している場合次のvenvを使う方法が適切です。
##### 導入方法
```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
source ~/.bashrc #zshの場合はsource ~/.zshrcを実行してください
```

pipxではシステムのpython(通常は/usr/bin/python)を壊さず、パッケージをインストールすることができます。使い方はpipとほぼ同じです。
またpipx listでリスティングしたりpipx uninstallが用意されていたりなど便利な点が多くあります。
#### 三つ目
最後に紹介する方法がvenvを使う方法です。

##### 導入方法
```bash
python3 -m venv ~/venv
source ~/venv/bin/activate
```
エラーが出る場合
```bash
sudo apt install python3-full #または python3-venv
```
を実行してから再度実行してみてください
この状態ではpipが`/usr/bin/pip`ではなく`~/venv/bin/pip`を指すようになるのでpipを実行することができます。ただし毎回パッケージ使用前にactivateをしなければいけないのがこの問題の対処のみを目的とする場合に使いにくいところです。
また、無効化したいときは
```bash
deactivate
```
を実行します。
プロジェクトごとに依存関係を完全に分離できるというメリットがあります。(これが本来の目的です)
#### 最後に
`--break-system-packages`というオプションを付けることで強制的にインストールすることができます。
ただしOS自体にpythonが使われているため最悪の場合OSが動作しなくなってしまう場合があります。実際そのような事例が後を絶たないことからディストリビューションを提供されている方々はpipを触れないように変更したわけですからあまり推奨はしません。
