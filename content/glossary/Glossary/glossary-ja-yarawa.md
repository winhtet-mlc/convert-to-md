+++
title = "用語集（や・ら・わ行）"
weight = "9"
+++


## や

## ゆ

## よ

## ら

## り

## る

## れ

## ろ

## わ

### 歪度

- 読み: わいど
- 英語での表現: skewness
- Tags: 確率・統計

確率分布やデータの特徴を表す指標の一つで、[平均](../glossary-ja-ha#平均)を中心とした分布の非対称性の程度を示すもの。確率変数 \\(X\\) の平均を \\(\\mu\\)、[標準偏差](../glossary-ja-ha#標準偏差)を \\(\\sigma\\) としたとき、 \\(X\\) の歪度を

\\[
\\mathrm{Skew} [ X ] = \\frac{\\mathrm{E} [ ( X - \\mu ) ^3 ]}{\\sigma^3}
\\]

で定める。歪度が負の値を取る場合は分布が実軸上で平均より小さい向きに、逆に正の値を取る場合は平均より大きい向きにそれぞれ偏っていると考えられる。データ \\(\\{ X\_1, \\ldots, X\_n \\}\\) の平均を \\(\\bar{X}\\)、[不偏分散](../glossary-ja-ha#分散)を \\(s^2\\) とすると、データの歪度はモーメントの推定値から

\\[
\\gamma\_1 = \\frac{\\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ^3}{s^3}
\\]

や、キュムラントの推定値から

\\[
G\_1 = \\frac{\\sqrt{n ( n - 1 )}}{n - 2} \\frac{\\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ^3}{\\left( \\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ^2 \\right) ^\\frac{3}{2}}
\\]

とそれぞれ計算される。
