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
Epoch [1/3] Train Loss: 1.7763, Train Acc: 0.3358 | Test Loss: 1.5829, Test Acc: 0.4190 | Time: 52.1s
Epoch [2/3] Train Loss: 1.5171, Train Acc: 0.4412 | Test Loss: 1.3934, Test Acc: 0.4892 | Time: 65.6s
Epoch [3/3] Train Loss: 1.3809, Train Acc: 0.4956 | Test Loss: 1.3101, Test Acc: 0.5200 | Time: 53.9s
============================================================
Running experiment with patch size = 8
============================================================
Using device: cpu
Files already downloaded and verified
Files already downloaded and verified
Patch size: 8
Number of parameters: 81226
Epoch [1/3] Train Loss: 1.8561, Train Acc: 0.3143 | Test Loss: 1.6937, Test Acc: 0.3768 | Time: 24.6s
Epoch [2/3] Train Loss: 1.6700, Train Acc: 0.3851 | Test Loss: 1.5805, Test Acc: 0.4241 | Time: 24.8s
Epoch [3/3] Train Loss: 1.5572, Train Acc: 0.4308 | Test Loss: 1.4485, Test Acc: 0.4768 | Time: 24.3s
============================================================
Running experiment with patch size = 16
============================================================
Using device: cpu
Files already downloaded and verified
Files already downloaded and verified
Patch size: 16
Number of parameters: 117322
Epoch [1/3] Train Loss: 1.8728, Train Acc: 0.3203 | Test Loss: 1.7420, Test Acc: 0.3681 | Time: 20.3s
Epoch [2/3] Train Loss: 1.7544, Train Acc: 0.3635 | Test Loss: 1.6523, Test Acc: 0.4070 | Time: 20.5s
Epoch [3/3] Train Loss: 1.6991, Train Acc: 0.3842 | Test Loss: 1.6517, Test Acc: 0.3996 | Time: 20.7s

============================================================
Final Results (Patch Size vs Test Accuracy)
============================================================
Patch Size  4 : Test Accuracy = 0.5200
Patch Size  8 : Test Accuracy = 0.4768
Patch Size 16 : Test Accuracy = 0.3996
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