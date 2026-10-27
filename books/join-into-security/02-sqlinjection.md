---
title: "SQLinjection/SQLインジェクション"
---
## SQLとは
SQLとはデータを表から取得するための言語です。
structured query language(構造化された問い合わせ言語)の略です。
データベースに対して、データ取得や挿入、削除などの問い合わせが行えます。
ちなみに余談ですが、現在のSQLは一般的にチューリング完全です。
## 概念的説明
ユーザーからの入力を*SQL文として解釈することを許し*てしまうこと、すなわち*データを挿入したあとにそれを区別せず構文解析をしている*ことです。
*送信されたデータを信頼してしまっている*ことによって発生しているというのが最も根本的な原因です。

## 具体例
まずは一般的な例です。
```SQL
f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```
このようにSQL文を作ってしまうと`username=' OR 1=1--`という入力だった場合に
```SQL
SELECT * FROM users WHERE username = '' OR 1=1--' AND password = ''
```
という問い合わせ文が作成されます。
`--`はその後ろをコメントアウトすることを表しています。
WHEREが直接的には、users表から一行ずつ取り出し、username='{username}'という式がTrueかどうかを判定し、Trueの場合はその行を返すという処理をしています。
そのためusername = ''はほとんどの場合、すべての行でFalseですが、1=1は常にTrueなためすべての行が返ってしまいます。
## 攻撃の実験(ローカル環境)
[https://github.com/toto1010orange/zenn/blob/main/materials/SQLi.py](https://github.com/toto1010orange/zenn/blob/main/materials/SQLi.py)
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
1.典型:SQLinjectionを起こしてみてください。(HELLO aliceが見えれば正解です)

:::details 解答

 - ブラウザを使った方法
usernameに`' OR 1=1--`と入力し、ログインボタンを押す。

 - shellを使った方法
ターミナル
```bash
curl -X POST http://localhost:8000 -d "username=' OR 1=1--"
```
powershell
```powershell
curl.exe -X POST http://localhost:8000 -d "username=' OR 1=1--"
```

### 解説
A OR True=Trueという文はAにかかわらず常にTrueなためすべての行が返り、一番最初に渡された行であったaliceになりすませました。

:::

2.ちょっと工夫:bobというアカウントになりすましてみましょう(HELLO bobが見えれば正解です)

:::details 解答

 - ブラウザを使った方法
usernameに`bob'--`と入力し、ログインボタンを押す。

 - shellを使った方法
ターミナル
```bash
curl -X POST http://localhost:8000 -d "username=bob'--"
```
powershell
```powershell
curl.exe -X POST http://localhost:8000 -d "username=bob'--"
```
### 解説
usernameがbobである行が返るためbobになりすますことができます。passwordの評価をコメントアウトしているためusernameが一致した行が無条件で返ります。

:::

このコードではエラーの場合の処理を細かく実装していませんが、エラーの種類を悟られないようにするという実装である必要があります。
例えばSQLエラーが出た場合SQLインジェクションが可能であることがわかってしまうなど、エラーから情報を得るというのは一般的なことだからです。
## どのように修正するべきか

脆弱性が生まれている原因は問い合わせ文を組み立てる際、データと構文の区別をしていないこと、SQL文を作ってから構文を評価していることでした。
以下の実装は構文とデータを別々に渡しています。
構文解析のあとデータ挿入を行うことで、SQLインジェクションを防いでいます。
修正したファイルです。
[https://github.com/toto1010orange/zenn/blob/main/materials/SQLinimakenai.py](https://github.com/toto1010orange/zenn/blob/main/materials/SQLinimakenai.py)
構文解析をした後にデータを挿入するため、データが構文解析で評価されないという仕組みです。
サニタイジングなどの方法もありますが、根本的な解決にはならないことが多いため、データと構文を完全に分離するというアプローチをお勧めします。

