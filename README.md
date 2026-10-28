<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/witching-hour-theme/main/assets/icon.png" alt="Witching Hour Theme logo" width="128">
</p>

<h1 align="center">Witching Hour Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.witching-hour-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-C25A1E?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-A8D06A?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-E8722A?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/witching-hour-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

Pumpkin cream by day, charcoal violet by night. Four colours do the work: pumpkin orange, slime green, blood red and candle yellow, on paper in the light variant and on a dark violet in the dark one.

白天是南瓜奶油纸，夜里是炭紫。四个颜色撑起整套：南瓜橙、毒绿、血红与烛黄；浅色版铺在纸色上，深色版沉进炭紫里。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Witching Hour Theme Light](https://raw.githubusercontent.com/vaxicy/witching-hour-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Witching Hour Theme Dark](https://raw.githubusercontent.com/vaxicy/witching-hour-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FBF3E4` pumpkin cream | `#1E1626` charcoal violet |
| Foreground | `#2A1C33` plum ink | `#F2EDE4` ghost white |
| Muted text / placeholders | `#8A7A80` | `#9A8AA4` |
| Side bar | `#FFF9EE` | `#221A2C` |
| Panel / terminal | `#FCF5E8` | `#241C2E` |
| Title bar | `#F6C08A` with `#3A2430` text | `#171020` with `#D8CFC4` text |
| Tab bar / inactive tab | `#F3E8D6` | `#241C2E` |
| Active tab / indicator | `#3A2430` text, `#C25A1E` top border | `#F6F0EA` text, `#E8722A` top border |
| Activity bar | `#F5E7D3` with `#8A4A28` icons | `#1A1322` with `#C9A8B0` icons |
| Status bar | `#4A2C5A` with `#F6F0EA` text | `#4A2C5A` with `#F2E8EE` text |
| Selection | `#F7DCC2` | `#3E2A4E` |
| Current line | `#FBF5E8` | `#2A2036` |
| Borders | `#E9DCC6` | `#3A2C46` |
| Indent guides | `#EDE0C8` | `#332641` |
| Button | `#C25A1E` with white text (hover `#B0472A`) | `#E8722A` with `#1E1626` text (hover `#F08542`) |
| Badge | `#4A2C5A` with white text | `#A8D06A` with `#1E1626` text |
| Cursor | `#C25A1E` | `#E8722A` |
| Links | `#B0472A` | `#A8D06A` |
| Errors / warnings | `#B0303F` / `#9A6A1E` | `#E88A96` / `#E8C66A` |
| Git added / modified / deleted | `#5E7A2E` / `#9A6A1E` / `#B0303F` | `#A8D06A` / `#E8C66A` / `#E88A96` |

Pumpkin `#E8722A`, slime `#A8D06A`, blood `#B0303F`, candle `#E8C66A` and charcoal `#1E1626` carry both variants, so a file still reads as "witching hour" after switching.

南瓜橙 `#E8722A`、毒绿 `#A8D06A`、血红 `#B0303F`、烛黄 `#E8C66A` 与炭紫 `#1E1626` 贯穿明暗两版，切换后整个文件还是同一个午夜。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#8A7A80` | `#8A7A96` |
| Keywords / storage | `#B0472A` | `#E8722A` |
| Strings | `#5E7A2E` | `#A8D06A` |
| Functions / methods | `#9A6A1E` | `#E8C66A` |
| Types / classes | `#6B4A8A` | `#C9A0E0` |
| Numbers / constants | `#9A2F3E` | `#E88A96` |
| Variables | `#2A1C33` | `#F2EDE4` |
| Parameters | `#5E4A50` | `#C9BCC8` |
| Properties | `#9A6A1E` | `#E8C66A` |
| Operators | `#7A6A70` | `#B9A8C4` |
| Punctuation | `#8A7A80` | `#8A7A96` |
| HTML tags | `#B0472A` | `#E8722A` |
| Attribute names | `#9A2F3E` | `#E88A96` |
| Regex | `#9A6A1E` | `#DCC48A` |
| Escape characters | `#9A2F3E` | `#EFD0A8` |

Semantic highlighting is enabled, so variables, parameters, properties, functions and types follow the same mapping in TypeScript, JavaScript, Go, Rust and Python.

已开启语义高亮，TypeScript、JavaScript、Go、Rust 与 Python 里的变量、参数、属性、函数与类型都会落到同一套配色。

## Install / 安装

1. 打开扩展面板 `Ctrl+Shift+X`。
2. 搜索 **Witching Hour Theme** 并安装。
3. 按 `Ctrl+K Ctrl+T`，选择 `Witching Hour Theme Light` 或 `Witching Hour Theme Dark`。

也可以用命令行安装：

```bash
code --install-extension lilinhuang.witching-hour-theme
```

## Build from source / 本地构建

```bash
py -3 scripts/build-theme.py       # regenerate both theme JSON files
py -3 scripts/generate-icon.py     # export assets/icon.png from the selected logo
py -3 scripts/capture-real-screenshots.py   # real VS Code screenshots
```

## License / 许可证

Non-Commercial License — free for personal, educational and non-commercial use. See [LICENSE](https://github.com/vaxicy/witching-hour-theme/blob/main/LICENSE).

非商业许可证：个人、教育与非商业用途免费使用，详见 LICENSE。
