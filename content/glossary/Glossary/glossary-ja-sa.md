+++
title = "用語集（さ行）"
weight = "4"
+++


## さ

### 最小値

- 読み: さいしょうち
- 英語での表現: minimum
- Tags: 確率・統計

データの特徴を表す指標の一つで、データ  \\(\\{ X\_1, \\ldots, X\_n \\}\\) の中で最も小さい値

\\[
\\min\_{1 \\le i \\le n} X\_i
\\] 

のことを指す。

### 最大値

- 読み: さいだいち
- 英語での表現: maximum
- Tags: 確率・統計

データの特徴を表す指標の一つで、データ  \\(\\{ X\_1, \\ldots, X\_n \\}\\) の中で最も大きい値

\\[
\\max\_{1 \\le i \\le n} X\_i
\\] 

のことを指す。

### 最頻値

- 読み: さいひんち
- 英語での表現: mode
- Tags: 確率・統計

確率分布やデータの特徴を表す指標の一つで、その分布やデータで最も多く出現する値のこと。確率変数 \\(X\\) が連続分布に従う場合はその確率密度関数が、離散分布に従う場合はその確率質量関数がそれぞれ最大値を取る値を \\(X\\) の最頻値という。データ \\(\\{ X\_1, \\ldots, X\_n \\}\\) については、その中で最も多く出現する値（複数ある場合がある）をそのデータの最頻値という。

## し

### 順位相関係数

- 読み: じゅんいそうかんけいすう
- 英語での表現: rank correlation coefficient
- Tags: 確率・統計

データの特徴を表す指標の一つで、複数のカラムの値が順位の意味でどのようにばらつくかの傾向を示すもの。Spearmanの順位相関係数 (Spearman rank correlation coefficient, Spearman's rho) とKendallの順位相関係数（Kendall rank correlation coefficient, Kendall's tau) の2つがよく用いられる。以下ではSpearmanの順位相関係数について述べる。

データ \\(\\{ ( X\_1, Y\_1 ), \\ldots, ( X\_n, Y\_n ) \\}\\) について、それぞれの \\(\\{ X\_i \\}, \\{ Y\_i \\}\\) 内での順位を \\(\\{ ( R\_1, Q\_1 ), \\ldots, ( R\_n, Q\_n ) \\}\\) とする。ただし、複数の値が同順になる場合はそれらの値に全て対応する中間の順位を割り振る（例えば \\(X\_1, \\ldots, X\_4\\) が全て「3位タイ」であるとき、 \\(Q\_1 = \\cdots = Q\_4 = \\frac{3 + 4 + 5 + 6}{4} = 4.5\\) とする）。このとき、Spearmanの順位相関係数を

\\[
r\_S = \\frac{\\sum\_{i = 1}^n (R\_i - \\bar{R} ) ( Q\_i - \\bar{Q} )}{\\sqrt{\\sum\_{i = 1}^n ( R\_i - \\bar{R} ) ^2} \\sqrt{\\sum\_{i = 1}^n ( Q\_i - \\bar{Q} ) ^2}}
\\]

で定める。ここで \\(\\bar{R}, \\bar{Q}\\) はそれぞれ \\(\\{ R\_i \\}, \\{ Q\_i \\}\\) の標本平均とする。これは標本の順位 \\(\\{ (R\_i, Q\_i) \\}\\) についての[Pearsonの積率相関係数](#相関係数)であるが、 \\(\\{ (X\_i, Y\_i) \\}\\) に対する通常の（Pearsonの）相関係数が両者の線形の関係しか捉えられないのに対し、（Spearmanの）順位相関係数は両者の単調な関係を捉えることができる。なお、標本の中に同順の値が存在しないときは

\\[
r\_S = 1 - \\frac{6 \\sum\_{i = 1}^n ( R\_i - Q\_i ) ^2}{n ( n^2 - 1 )}
\\]

と簡単に計算できる。



関連項目

- [相関係数](#相関係数): Pearsonの積率相関係数

## す

## せ

### 尖度

- 読み: せんど
- 英語での表現: kurtosis
- Tags: 確率・統計

確率分布やデータの特徴を表す指標の一つで、[平均](../glossary-ja-ha/#平均)を中心とした分布の尖り具合の程度を示すもの。確率変数 \\(X\\) の平均を \\(\\mu\\)、[標準偏差](../glossary-ja-ha/#標準偏差)を \\(\\sigma\\) としたとき、 \\(X\\) の尖度を

\\[
\\mathrm{Kurt} [ X ] = \\frac{\\mathrm{E} [ ( X - \\mu ) ^4 ]}{\\sigma^4}
\\]

で定める。この定義において正規分布の尖度は3であり、尖度が3より小さい値を取る場合は正規分布より尖っていない（裾の重い）、逆に3より大きい値を取る場合は正規分布より尖っている（裾の軽い）分布であるとそれぞれ考えられる。このため

\\[
\\mathrm{Kurt} [ X ] - 3 = \\frac{\\mathrm{E} [ ( X - \\mu ) ^4 ]}{\\sigma^4} - 3
\\] 

は過剰尖度 (excess kurtosis) と呼ばれ、またこの値を尖度と定義する場合もある。データ \\(\\{ X\_1, \\ldots, X\_n \\}\\) の平均を \\(\\bar{X}\\)、[不偏分散](../glossary-ja-ha/#分散)を \\(s^2\\) とすると、データの過剰尖度はモーメントの推定値から

\\[
\\gamma\_2 = \\frac{\\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ^4}{s^4} - 3
\\]

や、キュムラントの推定値から

\\[
G\_2 = \\frac{( n - 1 ) ( n + 1 )}{( n - 2 ) ( n - 3 )} \\frac{\\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ^4}{\\left( \\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ^2 \\right) ^2} - \\frac{3 ( n - 1 ) ^2}{( n - 2 ) ( n - 3 )}
\\]

とそれぞれ計算される。

## そ

### 相関係数

- 読み: そうかんけいすう
- 英語での表現: correlation coefficient
- Tags: 確率・統計

確率分布やデータの特徴を表す指標の一つで、複数の確率変数やカラムの値がどのようにばらつくかの傾向を示すもの。いくつかの定義があるが、一般にはPearsonの積率相関係数 (Pearson correlation coefficient) のことを指す。確率変数 \\(X, Y\\) の[標準偏差](../glossary-ja-ha/#標準偏差)をそれぞれ \\(\\sigma\_X, \\sigma\_Y\\)、[共分散](../glossary-ja-ka/#共分散)を \\(\\mathrm{Cov} ( X, Y )\\) としたとき、 \\(X, Y\\) の相関係数を

\\[
\\rho\_{X Y} = \\frac{\\mathrm{Cov} ( X , Y )}{\\sigma\_X \\sigma\_Y}
\\]

で定める。相関係数 \\(\\rho\_{X Y}\\) は \\(-1 \\le \\rho\_{X Y} \\le 1\\) をみたす。相関係数の値に対する解釈は

- \\(\\rho\_{X Y}\\) が正の値をとるとき、 \\(X\\) の値が増加すると対応する \\(Y\\) の値も増加する傾向にある
- \\(\\rho\_{X Y}\\) が負の値をとるとき、 \\(X\\) の値が増加すると対応する \\(Y\\) の値は減少する傾向にある
- \\(| \\rho\_{X Y} |\\) の値が \\(1\\) に近い程、 \\(( X, Y )\\) の組は直線状に分布する傾向にある

などがある。データ \\(\\{ ( X\_1, Y\_1 ), \\ldots, ( X\_n, Y\_n ) \\}\\) について、 \\(\\{ X\_i \\}, \\{ Y\_i \\}\\) の[標本平均](../glossary-ja-ha/#平均)をそれぞれ \\(\\bar{X}, \\bar{Y}\\) 、（不偏）標本標準偏差をそれぞれ \\(s\_X, s\_Y\\) 、（不偏）標本共分散を \\(s\_{X Y}\\) としたとき、このデータの標本相関係数 (sample correlation coefficient) を

\\[
r\_{X Y} = \\frac{s\_{X Y}}{s\_X s\_Y} = \\frac{\\sum\_{i = 1}^n ( X\_i - \\bar{X} ) ( Y\_i - \\bar{Y} )}{\\sqrt{\\sum\_{i = 1}^n ( X\_i - \\bar{X} ) ^2} \\sqrt{\\sum\_{i = 1}^n ( Y\_i - \\bar{Y} ) ^2}}
\\]

で定める。なお、これはデータの従う確率分布の相関係数の不偏推定量にはなっていない。


関連項目

- [順位相関係数](#順位相関係数)
