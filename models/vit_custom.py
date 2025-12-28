# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
# Vitモデルの定義
# パッチサイズの可変
# パッチサイズを引数で切り替え
import torch
import torch.nn as nn


class PatchEmbedding(nn.Module):                # 画像をパッチに分割，埋め込みに変換
    def __init__(
        self, 
        embed_dim,                              # 各パッチを表すベクトルの次元数
        img_size=32,                            # 入力画像の縦横サイズ
        patch_size=8,                           # 1パッチの縦横サイズ
        in_channels=3                           # 入力チャネル数
        
        ):
        super().__init__()

        assert img_size % patch_size == 0

        self.img_size = img_size
        self.patch_size = patch_size
        self.num_patches = (img_size // patch_size) ** 2

        self.proj = nn.Conv2d(
            in_channels,
            embed_dim,
            kernel_size=patch_size,
            stride=patch_size
        )

    def forward(self, x):                       # 入力x:(B, C, H, W)
        x = self.proj(x)                        # パッチ化と埋め込み
        x = x.flatten(2)                        # 平坦化
        x = x.transpose(1, 2)                   # 軸の入れ替え
        return x


class VisionTransformer(nn.Module):             # CLSトークンを用いて画像分類
    def __init__(
        self,
        embed_dim,
        depth,
        num_heads,
        mlp_dim,
        img_size=32,
        patch_size=8,
        in_channels=3,
        num_classes=10,
        dropout=0.1
    ):
        super().__init__()

        self.patch_embed = PatchEmbedding(
            img_size=img_size,
            patch_size=patch_size,
            in_channels=in_channels,
            embed_dim=embed_dim
        )

        num_patches = self.patch_embed.num_patches

        self.cls_token = nn.Parameter(torch.zeros(1, 1, embed_dim)) # CLSトークン

        self.pos_embed = nn.Parameter(                              # 位置埋め込み
            torch.zeros(1, num_patches + 1, embed_dim)
        )

        self.pos_dropout = nn.Dropout(dropout)

        encoder_layer = nn.TransformerEncoderLayer(                 # transformer encoder
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=mlp_dim,
            dropout=dropout,
            activation="gelu",
            batch_first=True
        )

        self.encoder = nn.TransformerEncoder(
            encoder_layer,
            num_layers=depth
        )

        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)

        self._init_weights()

    def _init_weights(self):
        nn.init.trunc_normal_(self.pos_embed, std=0.02)
        nn.init.trunc_normal_(self.cls_token, std=0.02)

    def forward(self, x):
        B = x.size(0)

        x = self.patch_embed(x)

        cls_tokens = self.cls_token.expand(B, -1, -1)
        x = torch.cat((cls_tokens, x), dim=1)

        x = x + self.pos_embed
        x = self.pos_dropout(x)

        x = self.encoder(x)

        cls_output = x[:, 0]
        cls_output = self.norm(cls_output)

        out = self.head(cls_output)
        return out
