---
title: "SQLinjection/SQLインジェクション"
---
## SQLとは
SQLとはデータを表から取得するための言語です。
structured query language(構造化された問い合わせ言語)の略です。
## 概念的説明
ユーザーからの入力を含んだ*SQL文を組み立てた後に問い合わせ*てしまうことが原因です。
世の脆弱性はほとんどが*送信されたデータを信頼してしまっていること*や*処理の順番が意識できていない*ことによって発生しているということも知っておいていただきたいです。

## 具体例
まずは一般的な例です。
```SQL
f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```
このようにSQL文を作ってしまうと`username=a , password=' OR 1=1;--`という入力だった場合に
```SQL
SELECT * FROM users WHERE username = 'a' AND password = '' OR 1=1;--'
```
という問い合わせ文が作成されます。
`--`はその後ろを無視する、`;`は処理を閉じる意味です。
WHERE以降の部分に注目すると一見aという人の行(レコード)が返るように見えますが実はすべての行が返ってしまいます。
なぜならANDの方がORより先に実行されるからです。ここで誤解をしていた方はやはり`元のテンプレート文と完成したSQL文を切り離して考えられていない`のではないでしょうか。ちなみに私も最初は誤解していました。

## 攻撃の実験(ローカル環境)
[以下のコードをダウンロードしてください](https://github.com/toto1010orange/zenn/blob/main/materials/SQLi.py)
コードをコピーして適当なファイル名で保存してもらえれば結構です。ただし念のため拡張子は.pyでお願いします。

ちなみにこのコードはLLM(gemini)に作成してもらいました。
練習問題です。AIに聞いてしまうと簡単にわかってしまうので自分で考えることを推奨します。

### 準備
保存したファイルをpythonで実行して、[実験サイト](http://localhost:8000)にアクセスしてみてください。
:::message alert
今回の実験サイトはあなたのPC上だけで動いていますが、そうでない外部のサイト等に対するアクセスの試み、またふざけて攻撃文字列を打つなどの行為を行うと
 - [不正アクセス行為の禁止等に関する法律](https://laws.e-gov.go.jp/law/411AC0000000128)上の違法行為に該当する可能性があります。
 - WAF(web application firewall)や、fuzzing検知を伴うアクセス制御機能などによって当該webサイトへのアクセスが不可能になる可能性があります。
:::
1.SQLinjectionを起こしてみてください。(hello aliceが見えれば正解です)

:::details 解答

UI(user interface)を使った
usernameには適当な文字列、passwordには`' OR 1=1;--`を入力し、ログインボタンを押す。

shellを使った解答
```bash
curl -X POST http://localhost:8000 -d "username=a&password=' OR 1=1;--"
```
```powershell
curl.exe -X POST http://localhost:8000 -d "username=a&password=' OR 1=1;--"
```

:::

2.bobというアカウントになりすましてみましょう
