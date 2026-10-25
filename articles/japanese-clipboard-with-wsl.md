---
title: "WSLでclip.exeにパイプした際文字化けしてしまう問題の対策とWSLのファイルをクリップボードにコピーする方法"
emoji: "❓"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["wsl","clip.exe"]
published: true
---
## この記事でわかること
WSLで実行したあるコマンドの出力やファイル全体をwindowsのクリップボードにコピーする方法
例えばcat test.txt|clip.exeというようにclip.exeに渡した場合文字化けしてしまう問題の対処法

## パッケージをインストールできる場合
比較的新しいwslの場合にはwl-clipboardというパッケージが便利です。
```bash
sudo apt install wl-clipboard
```
`wl-copy < test.txt`のように使用でき、windows clipboardに流してくれるため最も良い選択肢です。
## WSLからクリップボードにコピーする方法
wslからはwindowsのclip.exeを呼び出すことでクリップボードにコピーできます。

```powershell-log
PS C:\WINDOWS\System32> CLIP /?

CLIP

説明:
    コマンド ライン ツールの出力を Windows クリップボードにリダイレクトします。
    その出力されたテキストをほかのプログラムに貼り付けることができます。

パラメーター一覧:
    /?                  このヘルプを表示します。

例:
    DIR | CLIP          現在のディレクトリ一覧のコピーを Windows クリップボード
                        に貼り付けます。

    CLIP < README.TXT   readme.txt ファイルのテキストのコピーを Windows
                        クリップボードに貼り付けます。
```
powershellからヘルプ画面を見ると使い方が出てきます。しかし日本語の文書に対して`CLIP < README.TXT`を実行すると文字化けが発生すると思います。
これは日本語版windowsのclip.exeがshift-jisを期待するのにわたるのはUTF-8だからです。

## 文字化けへの対処法

私は`~/.bashrc`に
```
wclip() {
    iconv -t cp932//TRANSLIT//IGNORE | /mnt/c/Windows/System32/clip.exe
}
```
という関数を作っています。
そうすることで`wclip < test.txt`に日本語を渡しても問題なくクリップボードに格納されることを確認できました。

## 残っている課題
ctrl+cではコピーできる絵文字などでも特殊文字として`?`に変換されてしまいます。

## まとめ
ファイルをクリップボードに入れるときは英語ファイルなら`clip.exe < test.txt`や`cat test.txt|clip.exe`
日本語ファイルに対応するには
```
wclip() {
    iconv -t cp932//TRANSLIT//IGNORE | /mnt/c/Windows/System32/clip.exe
}
```
という関数を~/.bashrcに追記して`source ~/.bashrc`を実行またはshellを開きなおした後`wclip < test.txt`や`cat test.txt|wclip`のように使う。

stdoutをパイプしている仕組みなため単一ファイルに限らず、コマンドの出力一般に使えます。
私はLLMに出力を投げる際、多用しています。
