# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# データセットローダ
# CIFAR-10を読み込み
import torch
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms


def get_cifar10_dataloaders(
    batch_size=32,
    num_workers=2,
    data_root="./data"                                          # データ保存先
):
    mean = (0.4914, 0.4822, 0.4465)
    std = (0.2470, 0.2435, 0.2616)

    transform_train = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ])

    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ])

    train_dataset = torchvision.datasets.CIFAR10(
        root=data_root,
        train=True,
        download=True,
        transform=transform_train
    )

    test_dataset = torchvision.datasets.CIFAR10(
        root=data_root,
        train=False,
        download=True,
        transform=transform_test
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True
    )

    return train_loader, test_loader


if __name__ == "__main__":                                      # 動作確認
    train_loader, test_loader = get_cifar10_dataloaders()

    images, labels = next(iter(train_loader))
    print("Train batch image shape:", images.shape)
    print("Train batch label shape:", labels.shape)
