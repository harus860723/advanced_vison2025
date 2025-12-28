# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# 学習と評価
import argparse
import time
import os
import torch
import torch.nn as nn
import torch.optim as optim
from models.vit_custom import VisionTransformer
from datasets.dataset_loader import get_cifar10_dataloaders


def train_one_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    
    for images, labels in dataloader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()

    epoch_loss = running_loss / total
    epoch_acc = correct / total

    return epoch_loss, epoch_acc


def evaluate(model, dataloader, criterion, device):         # testデータ性能評価
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in dataloader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)

            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

    epoch_loss = running_loss / total
    epoch_acc = correct / total

    return epoch_loss, epoch_acc


def main(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)                          # GPUがなければCPUを使用

    if os.environ.get("CI") == "true":
        print("CI mode: lightweight structural check")

        model = VisionTransformer(
            img_size=32,
            patch_size=args.patch_size,
            num_classes=10,
            embed_dim=64,
            depth=2,
            num_heads=2,
            mlp_dim=128
        ).to(device)

        dummy = torch.randn(2, 3, 32, 32).to(device)
        out = model(dummy)

        assert out.shape == (2, 10)
        print("CI check passed")
        return 0.0


    train_loader, test_loader = get_cifar10_dataloaders(    # Data Loader生成
        batch_size=args.batch_size
    )

    model = VisionTransformer(                              # Vitモデル生成
        img_size=32,
        patch_size=args.patch_size,
        num_classes=10,
        embed_dim=64,
        depth=2,
        num_heads=2,
        mlp_dim=128
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr)

    print(f"Patch size: {args.patch_size}")
    print(f"Number of parameters: {sum(p.numel() for p in model.parameters())}")

    for epoch in range(args.epochs):
        start_time = time.time()

        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer, device
        )
        test_loss, test_acc = evaluate(
            model, test_loader, criterion, device
        )

        elapsed = time.time() - start_time

        print(
            f"Epoch [{epoch+1}/{args.epochs}] "
            f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f} | "
            f"Test Loss: {test_loss:.4f}, Test Acc: {test_acc:.4f} | "
            f"Time: {elapsed:.1f}s"
        )

    return test_acc                                         #test accuracyを返す


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch_size", type=int, default=8)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-3)

    args = parser.parse_args()

    main(args)
