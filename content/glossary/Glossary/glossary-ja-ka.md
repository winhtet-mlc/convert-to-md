+++
title = "用語集（か行）"
weight = "3"
+++


## か

## き

### 共分散

- 読み: きょうぶんさん
- 英語での表現: covariance
- Tags: 確率・統計

確率分布やデータの特徴を表す指標の一つで、[平均](../glossary-ja-ha#平均)を中心として複数の確率変数やカラムの値がどのようにばらつくかの傾向を示すもの。確率変数 \\(X, Y\\) の平均をそれぞれ \\(\\mu\_X, \\mu\_Y\\) としたとき、 \\(X, Y\\) の共分散を

\\[
\\sigma\_{X Y} = \\mathrm{Cov} ( X , Y ) = \\mathrm{E} [ ( X - \\mu\_X ) ( Y - \\mu\_Y ) ]
\\]

で定める。特に、自分自身との共分散 \\(\\mathrm{Cov} ( X , Y )\\) は[分散](../glossary-ja-ha#分散) \\(\\mathrm{V} [ X ]\\) に一致する。データ \\(\\{ ( X\_1, Y\_1 ), \\ldots, ( X\_n, Y\_n ) \\}\\) について、 \\(\\{ X\_i \\}, \\{ Y\_i \\}\\) の標本平均をそれぞれ \\(\\bar{X}, \\bar{Y}\\) としたとき、このデータの標本共分散 (sample covariance) は

\\[
\\frac{1}{n} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ( Y\_i - \\bar{Y} )
\\]

を指すこともあれば、 \\(n\\) の代わりに \\(n - 1\\) で除した

\\[
\\frac{1}{n - 1} \\sum\_{i=1}^n ( X\_i - \\bar{X} ) ( Y\_i - \\bar{Y} )
\\]


を指すこともある。 \\(( X\_i, Y\_i )\\) の組が独立同分布のとき、後者の標本分散は元の分布の共分散の不偏推定量になっており、これゆえ特に不偏（標本）共分散とも呼ばれる。

## く

## け

## こ
