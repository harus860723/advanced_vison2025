# advanced_vison2025
* アドバンスドビジョンの課題作成で使用したリポジトリ
# 

##
```
├── main.py
├── models/
│   └── vit_custom.py
├── datasets/
│   └── dataset_loader.py
├── train.py
```
## 実行ログ
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

============================================================
Final Results (Patch Size vs Test Accuracy)
============================================================
Patch Size  4 : Test Accuracy = 0.5291
Patch Size  8 : Test Accuracy = 0.4718
Patch Size 16 : Test Accuracy = 0.3991
```

## 使用ライブラリ
* Vision Transfomer
* Pytorch

## 使用コーパス
* CIFAR-10 Dataset

## 参考文献
* [Dosovitskiy et al., An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale, ICLR 2021](https://arxiv.org/abs/2010.11929)
* [torchvision.datasets.CIFAR10](https://docs.pytorch.org/vision/master/generated/torchvision.datasets.CIFAR10.html)
## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再領布および使用が許可される．

* このコードは，ロボットシステム学の授業で使用したスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものである．
	* [ryuichiueda/slides_marp/robosys_2025/](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)

© 2025 Haruki Matsushita