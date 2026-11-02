# pgy763.github.io

个人站点，用 GitHub Pages 托管：<https://pgy763.github.io/>

纯静态 HTML，没有构建步骤 —— 改完直接推，Pages 从 `main` 分支根目录发布。

## 页面上有什么

| 文件 | 内容 |
| --- | --- |
| `index.html` | 入口页：三块卡片（接入手册 / 踩坑手册 / 完整项目）+「从哪开始」的四条路径 |
| `story.html` | 案例页：这三份内容各自为什么长成这样、验证到什么程度、哪些结论被代码纠正过 |
| `prompting.html` | 2026-08 写的一篇提示词工程科普长文，存档 |
| `404.html` | 站内任意不存在的路径都会落到这里 |
| `favicon.svg` / `og.png` | 标签页图标 / 分享卡片（1200×630，`tools/gen_og.py` 生成） |

## 顺手记一下

- 用户站点必须叫 `<用户名>.github.io`，否则只能挂在 `/<仓库名>/` 下面
- 这个页面刻意没引入任何前端框架和外部字体：首屏就是文字，弱网也能打开
- 深色模式跟随系统（`prefers-color-scheme`），没有手动开关
- `og.png` 用 PIL + 微软雅黑生成，改文案后重跑 `python tools/gen_og.py` 即可
