---
title: "WSLでclip.exeにパイプした際文字化けしてしまう問題の対策とWSLのファイルをクリップボードにコピーする方法"
emoji: "❓"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["wsl","clip.exe"]
published: false
---
## この記事でわかること
WSLで実行したあるコマンドの出力やファイル全体をwindowsのクリップボードにコピーする方法
例えばcat test.txt|clip.exeというようにclip.exeに渡した場合文字化けしてしまう問題の対処法

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
## 文字化けの対処法

