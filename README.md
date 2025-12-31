# advanced_vison2025
* 2025年アドバンスドビジョンの課題作成で使用したリポジトリ．
## Vision Transformerに対するパッチサイズの違いによる性能比較

[![test](https://github.com/harus860723/advanced_vison2025/actions/workflows/test.yml/badge.svg)](https://github.com/harus860723/advanced_vison2025/actions/workflows/test.yml)

### 概要
* 本実験では，Vision Transformer(Vit)を用いて画像のパッチサイズを変更した場合の分類性能を比較することを目的としている．
* Vitは入力画像を小さなパッチに分割し，それらをトークンとしてTransformer入力するモデルである．
* 実験では，CIFAR-10データセットの画像に対してパッチサイズを変更して，それぞれの性能比較を行う．
* パッチサイズは，4，8，16，で実験を行った．
* テストデータ全体のうち正しく分類できた画像の割合である，テスト制度をそれぞれ出力する．

### 実行方法
#### 準備
* 実行環境を整える．
    * Python3
    * Pytorch
    * torchvison
* cloneコマンドを使用しリポジトリをインストールする．
```
$ git clone https://github.com/harus860723/advanced_vison2025.git
```

#### 実行
* 実行用のスクリプトを実行する．
```
$ python3 main.py
```
* データセットのロードと学習が実行される．

#### 実行結果
* 以下のような結果が表示される．
```
============================================================
Final Results (Patch Size vs Test Accuracy)
============================================================
Patch Size  4 : Test Accuracy = 0.5291
Patch Size  8 : Test Accuracy = 0.4718
Patch Size 16 : Test Accuracy = 0.3991
```

### システム構成
* システムの構成を以下に示す．
```
├── main.py                     # 実行用スクリプト
├── models/                     
│   └── vit_custom.py           # Vitモデルの定義
├── datasets/                   
│   └── dataset_loader.py       #データセットローダ(CIFAR-10を読み込み)
├── train.py                    #学習と評価
```

### モデルの説明
#### Vison Transformerの定義
* PatchEmbeddingクラスで入力を分割し，埋め込みベクトルへ変換する．
* 入力画像は以下のように表す．
* 画像はN個のパッチに分割される．
    * B: バッチサイズ
    * C: チャンネル数(RGB)
    * H: 画像の高さ
    * W: 画像の幅
    * P: パッチサイズ
```math
\begin{align}
x ∈ R^{B × C × H × W} (C = 3, H = W = 32)
\end{align}
```
```math
\begin{align}
N = \Biggl(\frac{H}{P}\Biggl)^2
\end{align}
```
* 1つの画像パッチの線形埋め込み．
    * xp: 入力画像の各パッチ
    * WE: 重み行列
    * bE: バイアス
    * zp: パッチ埋め込み
```math
\begin{align}
z_p = W_E x_p + b_E
\end{align}
```
* VisionTransformerクラスで，CLSトークンを用いた画像分類を行う．
* 分類用にCLSトークンを導入し，トークン列の先頭に追加する．
* Z0がTransformer-encoderに入力される．
    * zcls: CLSトークン
    * N: パッチ数
    * Epos: 位置埋め込み
```math
\begin{align}
Z' = [z_{cls}; z_1; ...; z_N]
\end{align}
```
```math
\begin{align}
Z_0 = Z' + E_{pos}
\end{align}
```

* Self-Attentionの式
    * Z: 入力トークン列
    * WQ, WK, WV: 学習パラメータ
```math
\begin{align}
Q = W_Q Z,  K = W_k Z,  V = W_V Z
\end{align}
```
```math
\begin{align}
\text{Attention}(Q, K, V)\text{softmax}\Biggl(\frac{QK^T}{\sqrt{D}}\Biggl)V
\end{align}
```
* vit_custom.pyで実装される．

#### データセットローダ
* torchvisionを用いてCIFAR-10の読み込みを行う．
* CIFAR-10について．
    * 画像サイズ: 32×32ピクセル
    * チャネル数: 3(RGB)
    * クラス数: 10
    * 学習用画像: 50000
    * テスト用画像: 10000
* CIFAR-10は飛行機や自動車，鳥などの10種類の物体画像から構成される画像分類用データセットである．
* dataset_loader.pyで実装される．

#### 学習と評価処理
* モデルの生成，学習処理，テストデータによる性能評価を行う．
* パッチサイズ4，8，16についてそれぞれ学習を行う．
    * 損失関数: Cross Entropy Loss
* 学習終了後に最終的なテスト制度(Test Accuracy)を返す．
* テスト制度は，テストデータ全体のうち正しく分類できた画像の割合である．
* train.pyで実装される．

#### 実行用スクリプト
* 複数のパッチサイズを指定し，順に実験を実行する．
* パッチサイズとテスト制度(Test Accuacy)の対応関係を一覧で表示する．
* main.pyで実装される．

### 実験結果
* Vitにおいて画像のパッチサイズの違いが分類性能に与える影響を調査するため，パッチサイズごとのテスト制度の比較実験を行った．
* 実行用のスクリプトを実行した場合の学習のログについて説明する．
* パッチサイズの4の時の学習結果を下に示す．
* データセットがダウンロードされていない場合は，/dataが作成される．
```
============================================================
Running experiment with patch size = 4
============================================================
Using device: cpu
Downloading https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz to ./data/cifar-10-python.tar.gz
100.0%
Extracting ./data/cifar-10-python.tar.gz to ./data
Files already downloaded and verified
Patch size: 4
Number of parameters: 75082
Epoch [1/3] Train Loss: 1.7527, Train Acc: 0.3445 | Test Loss: 1.5686, Test Acc: 0.4153 | Time: 59.9s
Epoch [2/3] Train Loss: 1.4960, Train Acc: 0.4518 | Test Loss: 1.3916, Test Acc: 0.4903 | Time: 53.3s
Epoch [3/3] Train Loss: 1.3650, Train Acc: 0.4984 | Test Loss: 1.2971, Test Acc: 0.5291 | Time: 56.2s
```
* 今回の実験は低スペックのCPUのみで行ったため，epoch数やバッチサイズなどのパラメータを低く設定している．
* パッチサイズの8の時の学習結果を下に示す．
```
============================================================
Running experiment with patch size = 8
============================================================
Using device: cpu
Files already downloaded and verified
Files already downloaded and verified
Patch size: 8
Number of parameters: 81226
Epoch [1/3] Train Loss: 1.8530, Train Acc: 0.3151 | Test Loss: 1.7026, Test Acc: 0.3747 | Time: 25.5s
Epoch [2/3] Train Loss: 1.6620, Train Acc: 0.3898 | Test Loss: 1.5724, Test Acc: 0.4247 | Time: 26.0s
Epoch [3/3] Train Loss: 1.5478, Train Acc: 0.4316 | Test Loss: 1.4658, Test Acc: 0.4718 | Time: 24.5s
```
* パッチサイズの16の時の学習結果を下に示す．
```
============================================================
Running experiment with patch size = 16
============================================================
Using device: cpu
Files already downloaded and verified
Files already downloaded and verified
Patch size: 16
Number of parameters: 117322
Epoch [1/3] Train Loss: 1.8802, Train Acc: 0.3146 | Test Loss: 1.7572, Test Acc: 0.3668 | Time: 20.1s
Epoch [2/3] Train Loss: 1.7721, Train Acc: 0.3610 | Test Loss: 1.6941, Test Acc: 0.3937 | Time: 20.1s
Epoch [3/3] Train Loss: 1.7157, Train Acc: 0.3809 | Test Loss: 1.6663, Test Acc: 0.3991 | Time: 20.1s
```
* 最終的な実行結果の，パッチサイズに対するテスト制度を下に示す．
```
============================================================
Final Results (Patch Size vs Test Accuracy)
============================================================
Patch Size  4 : Test Accuracy = 0.5291
Patch Size  8 : Test Accuracy = 0.4718
Patch Size 16 : Test Accuracy = 0.3991
```
* 実験結果から，パッチサイズが大きくなるにつれて精度が低下していることがわかる。
* パッチサイズが小さいほど画像の局所的な情報を細かく保持できるためと考えられる．
* Vitにおいて，CIFAR-10の画像で実験を行った結果から，パッチサイズが小さいほど高い分類精度が得られることが確認できた．

## 使用ライブラリ
* Python3
    * テスト済み: 3.9~3.11
* Vision Transfomer
* Pytorch
* torchvison

## 使用コーパス
* CIFAR-10 Dataset

## テスト環境
* Ubuntu

## 参考文献
* [Dosovitskiy et al., An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale, ICLR 2021](https://arxiv.org/abs/2010.11929)
* [torchvision.datasets.CIFAR10](https://docs.pytorch.org/vision/master/generated/torchvision.datasets.CIFAR10.html)

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再領布および使用が許可される．

* このコードは，ロボットシステム学の授業で使用したスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものである．
    * [ryuichiueda/slides_marp/advanced_vision/](https://github.com/ryuichiueda/slides_marp/tree/master/advanced_vision)
	* [ryuichiueda/slides_marp/robosys_2025/](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)

© 2025 Haruki Matsushita