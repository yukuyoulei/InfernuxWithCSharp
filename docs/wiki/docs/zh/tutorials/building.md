---
category: 教程
tags: ["build", "packaging"]
---

# 构建与打包

这个仓库里有两条不同的流程：一种是开发态构建引擎，一种是为 Hub 做分发打包。

## 开发态构建

```bash
conda activate infengine
pip install -r requirements.txt
cmake --preset release
cmake --build --preset release
```

## Hub 打包

- `cmake --build --preset packaging` 生成独立目录版 Hub。
- `cmake --build --preset packaging-installer` 生成图形化 Windows 安装器。

## 文档构建

```bash
conda activate infengine
python docs/wiki/generate_api_docs.py
python -m mkdocs build --clean -f docs/wiki/mkdocs.yml
```
