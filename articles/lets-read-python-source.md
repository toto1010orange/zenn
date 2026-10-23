---
title: "pythonのソースコードを読んでみよう"
emoji: "🐍"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [python]
published: false
---
## Pythonのソースコード
[https://github.com/python/cpython](https://github.com/python/cpython)
これはcpythonというインタープリタのソースコードです。
今回はこの中のthis.pyについて見てみたいと思います。
## import this
pythonで
```python
import this
```
を実行するかshellで
```bash
python3 -c "import this"
```
を実行してみてください。
するとthe zen of python(pythonの禅)から始まるpythonの設計思想についてのpython開発者の言葉が出てくると思います。
これを題材にpythonのソースコードを読むという体験をしたいと思います。

## ソースコードを読んでみよう！

[https://github.com/python/cpython/blob/main/Lib/this.py](https://github.com/python/cpython/blob/main/Lib/this.py)
import thisを実行したときこのthis.pyが呼び出されます。

```python
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
```
以上のコードが見られると思います。
実はrot13という仕組みを使って難読化されています。
sの部分を飛ばして下の部分に注目しましょう。
