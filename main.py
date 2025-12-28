# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# パッチサイズ比較実験
# 実行用スクリプト
import argparse
from collections import OrderedDict
import torch
from train import main as train_main


def run_experiments(args):# 複数のパッチサイズ実験
    results = OrderedDict()

    patch_sizes = args.patch_sizes

    if args.test_mode:
        patch_sizes = [args.patch_sizes[0]]

    for patch_size in args.patch_sizes:
        print("=" * 60)
        print(f"Running experiment with patch size = {patch_size}")
        print("=" * 60)

        exp_args = argparse.Namespace(
            patch_size=patch_size,
            epochs=1 if args.test_mode else args.epochs,
            batch_size=2 if args.test_mode else args.batch_size,
            lr=args.lr
        )

        test_acc = train_main(exp_args)

        results[patch_size] = test_acc

    print("\n" + "=" * 60)
    print("Final Results (Patch Size vs Test Accuracy)")
    print("=" * 60)

    for patch_size, acc in results.items():
        print(f"Patch Size {patch_size:>2d} : Test Accuracy = {acc:.4f}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--patch_sizes",
        type=int,
        nargs="+",
        default=[4, 8, 16],
        help="List of patch sizes to compare"
        "--test_mode",
        action="store_true",
        help="Run very small test for CI"
    
    )
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-3)

    args = parser.parse_args()

    run_experiments(args)
