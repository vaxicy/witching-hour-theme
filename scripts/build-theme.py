# -*- coding: utf-8 -*-
"""Build the Witching Hour Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "witching-hour-theme"
SLUG = "witching-hour"
DISPLAY = "Witching Hour Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/witching-hour-theme"

UI = {
    "foreground": ("#2A1C33", "#F2EDE4"),
    "editor.foreground": ("#2A1C33", "#F2EDE4"),
    "terminal.foreground": ("#2A1C33", "#F2EDE4"),
    "input.foreground": ("#3A2430", "#F7F2EA"),
    "dropdown.foreground": ("#3A2430", "#F7F2EA"),
    "quickInput.foreground": ("#3A2430", "#F7F2EA"),
    "editorWidget.foreground": ("#3A2430", "#F7F2EA"),
    "editorHoverWidget.foreground": ("#3A2430", "#F7F2EA"),
    "editorSuggestWidget.foreground": ("#3A2430", "#F7F2EA"),
    "notifications.foreground": ("#3A2430", "#F7F2EA"),
    "descriptionForeground": ("#8A7A80", "#9A8AA4"),
    "input.placeholderForeground": ("#8A7A80", "#9A8AA4"),
    "focusBorder": ("#C25A1E", "#A8D06A"),
    "inputOption.activeBorder": ("#B0472A", "#E8722A"),
    "input.border": ("#E9DCC6", "#3A2C46"),
    "dropdown.border": ("#E9DCC6", "#3A2C46"),
    "editor.background": ("#FBF3E4", "#1E1626"),
    "tab.activeBackground": ("#FBF3E4", "#1E1626"),
    "titleBar.activeBackground": ("#F6C08A", "#171020"),
    "titleBar.activeForeground": ("#3A2430", "#D8CFC4"),
    "titleBar.inactiveBackground": ("#F8D2A8", "#1F1728"),
    "titleBar.inactiveForeground": ("#7A6058", "#8A7A96"),
    "activityBar.background": ("#F5E7D3", "#1A1322"),
    "activityBar.foreground": ("#8A4A28", "#C9A8B0"),
    "activityBar.activeBorder": ("#C25A1E", "#E8722A"),
    "activityBar.inactiveForeground": ("#B09A8A", "#6E5F78"),
    "sideBar.background": ("#FFF9EE", "#221A2C"),
    "sideBar.foreground": ("#4A3040", "#E0D6CC"),
    "sideBarSectionHeader.background": ("#F7EDDC", "#2A2036"),
    "sideBarSectionHeader.foreground": ("#563A48", "#EBE1D8"),
    "panel.background": ("#FCF5E8", "#241C2E"),
    "terminal.background": ("#FCF5E8", "#241C2E"),
    "panel.border": ("#E9DCC6", "#3A2C46"),
    "editorGroup.border": ("#E9DCC6", "#3A2C46"),
    "tab.border": ("#E9DCC6", "#3A2C46"),
    "sideBar.border": ("#E9DCC6", "#3A2C46"),
    "titleBar.border": ("#E9DCC6", "#3A2C46"),
    "statusBar.background": ("#4A2C5A", "#4A2C5A"),
    "statusBar.noFolderBackground": ("#4A2C5A", "#4A2C5A"),
    "statusBar.foreground": ("#F6F0EA", "#F2E8EE"),
    "statusBar.noFolderForeground": ("#F6F0EA", "#F2E8EE"),
    "statusBarItem.hoverBackground": ("#5A3A6C", "#5F3C72"),
    "statusBar.debuggingBackground": ("#B0472A", "#9A3E28"),
    "statusBar.debuggingForeground": ("#FFF4EC", "#F7E6DC"),
    "editorGroupHeader.tabsBackground": ("#F3E8D6", "#241C2E"),
    "tab.inactiveBackground": ("#F3E8D6", "#241C2E"),
    "tab.activeForeground": ("#3A2430", "#F6F0EA"),
    "tab.activeBorderTop": ("#C25A1E", "#E8722A"),
    "tab.inactiveForeground": ("#8A7A80", "#8A7A96"),
    "tab.hoverBackground": ("#F8EEDC", "#2A2036"),
    "tab.activeModifiedBorder": ("#5E7A2E", "#A8D06A"),
    "tab.inactiveModifiedBorder": ("#5E7A2E", "#A8D06A"),
    "list.hoverBackground": ("#FAF0DE", "#2A2036"),
    "list.activeSelectionBackground": ("#F7DCC2", "#3E2A4E"),
    "editorSuggestWidget.selectedBackground": ("#F7DCC2", "#3E2A4E"),
    "list.activeSelectionForeground": ("#3A2430", "#F6F0EA"),
    "list.inactiveSelectionForeground": ("#3A2430", "#F6F0EA"),
    "editorSuggestWidget.selectedForeground": ("#3A2430", "#F6F0EA"),
    "list.inactiveSelectionBackground": ("#FAE8D4", "#35253F"),
    "list.highlightForeground": ("#B0472A", "#A8D06A"),
    "list.focusHighlightForeground": ("#B0472A", "#A8D06A"),
    "tree.indentGuidesStroke": ("#EADCC4", "#3A2C46"),
    "editorLineNumber.foreground": ("#B29E90", "#6E5F78"),
    "editorLineNumber.activeForeground": ("#B0472A", "#E8722A"),
    "editor.lineHighlightBackground": ("#FBF5E8", "#2A2036"),
    "editor.lineHighlightBorder": ("#F3E6CE", "#35253F"),
    "editorCursor.foreground": ("#C25A1E", "#E8722A"),
    "selection.background": ("#F7DCC2", "#3E2A4E"),
    "editor.selectionBackground": ("#F7DCC2", "#3E2A4E"),
    "terminal.selectionBackground": ("#F7DCC2", "#3E2A4E"),
    "editor.inactiveSelectionBackground": ("#FAE8D4", "#35253F"),
    "editor.wordHighlightBackground": ("#F7DCC280", "#6E4A8080"),
    "editor.wordHighlightStrongBackground": ("#F7DCC280", "#6E4A8080"),
    "editor.selectionHighlightBackground": ("#F7DCC266", "#6E4A8066"),
    "editor.findMatchHighlightBackground": ("#F2E2B0", "#4A3A5C"),
    "editor.findMatchBackground": ("#E9CE86", "#5A4468"),
    "editor.findMatchBorder": ("#B0472A", "#E8C66A"),
    "editorBracketMatch.background": ("#F8ECDA", "#35253F"),
    "editorBracketMatch.border": ("#C25A1E", "#E8722A"),
    "editorIndentGuide.background1": ("#EDE0C8", "#332641"),
    "editorIndentGuide.activeBackground1": ("#C4AC94", "#6E5F78"),
    "editorWhitespace.foreground": ("#EADCC4", "#3A2C46"),
    "editorRuler.foreground": ("#F8EFDD", "#2A2036"),
    "textLink.foreground": ("#B0472A", "#A8D06A"),
    "textLink.activeForeground": ("#8A3A22", "#C9E88A"),
    "editorLink.activeForeground": ("#8A3A22", "#C9E88A"),
    "quickInput.background": ("#FFFDF7", "#2A2036"),
    "editorHoverWidget.background": ("#FFFDF7", "#2A2036"),
    "notifications.background": ("#FFFDF7", "#2A2036"),
    "input.background": ("#FFFFFF", "#221A2C"),
    "dropdown.background": ("#FFFFFF", "#221A2C"),
    "editorWidget.background": ("#FFFDF7", "#2A2036"),
    "editorSuggestWidget.background": ("#FFFDF7", "#2A2036"),
    "editorWidget.border": ("#E9DCC6", "#443250"),
    "editorHoverWidget.border": ("#E9DCC6", "#443250"),
    "editorSuggestWidget.border": ("#E9DCC6", "#443250"),
    "notifications.border": ("#E9DCC6", "#443250"),
    "button.background": ("#C25A1E", "#E8722A"),
    "button.foreground": ("#FFFFFF", "#1E1626"),
    "button.hoverBackground": ("#B0472A", "#F08542"),
    "button.secondaryBackground": ("#F7EDDC", "#35253F"),
    "button.secondaryForeground": ("#4A3040", "#EBE1D8"),
    "button.secondaryHoverBackground": ("#EFE0C8", "#3E2A4E"),
    "badge.background": ("#4A2C5A", "#A8D06A"),
    "activityBarBadge.background": ("#4A2C5A", "#A8D06A"),
    "badge.foreground": ("#FFFFFF", "#1E1626"),
    "activityBarBadge.foreground": ("#FFFFFF", "#1E1626"),
    "scrollbarSlider.background": ("#B29E9066", "#9A8AA488"),
    "scrollbarSlider.hoverBackground": ("#9E8A7C99", "#B0A0BA99"),
    "scrollbarSlider.activeBackground": ("#88766A99", "#A8D06A99"),
    "errorForeground": ("#B0303F", "#E88A96"),
    "editorError.foreground": ("#B0303F", "#E88A96"),
    "problemsErrorIcon.foreground": ("#B0303F", "#E88A96"),
    "gitDecoration.deletedResourceForeground": ("#B0303F", "#E88A96"),
    "editorGutter.deletedBackground": ("#B0303F", "#E88A96"),
    "editorWarning.foreground": ("#9A6A1E", "#E8C66A"),
    "problemsWarningIcon.foreground": ("#9A6A1E", "#E8C66A"),
    "editorInfo.foreground": ("#5E7A2E", "#A8D06A"),
    "problemsInfoIcon.foreground": ("#5E7A2E", "#A8D06A"),
    "gitDecoration.addedResourceForeground": ("#5E7A2E", "#A8D06A"),
    "gitDecoration.untrackedResourceForeground": ("#5E7A2E", "#A8D06A"),
    "editorGutter.addedBackground": ("#5E7A2E", "#A8D06A"),
    "gitDecoration.modifiedResourceForeground": ("#9A6A1E", "#E8C66A"),
    "editorGutter.modifiedBackground": ("#9A6A1E", "#E8C66A"),
    "diffEditor.insertedTextBackground": ("#E2EACAAA", "#3E2A4E66"),
    "diffEditor.removedTextBackground": ("#F2DCDEAA", "#5E2E3E66"),
    "diffEditor.insertedLineBackground": ("#E2EACA66", "#3E2A4E44"),
    "diffEditor.removedLineBackground": ("#F2DCDE66", "#5E2E3E44"),
    "terminal.ansiBlack": ("#2A1C33", "#241C2E"),
    "terminal.ansiRed": ("#B0303F", "#E88A96"),
    "terminal.ansiGreen": ("#5E7A2E", "#A8D06A"),
    "terminal.ansiYellow": ("#9A6A1E", "#E8C66A"),
    "terminal.ansiBlue": ("#4A5E8A", "#A8B8E8"),
    "terminal.ansiMagenta": ("#6B4A8A", "#C9A0E0"),
    "terminal.ansiCyan": ("#4A7A72", "#A8D4C8"),
    "terminal.ansiWhite": ("#8A7A80", "#E0D6CC"),
    "terminal.ansiBrightBlack": ("#6E5F68", "#8A7A96"),
    "terminal.ansiBrightRed": ("#C94A58", "#F7B0BA"),
    "terminal.ansiBrightGreen": ("#7A9A46", "#C9E88A"),
    "terminal.ansiBrightYellow": ("#B08234", "#F7DCA0"),
    "terminal.ansiBrightBlue": ("#5E729E", "#C4D0F0"),
    "terminal.ansiBrightMagenta": ("#8260A4", "#DCC4F0"),
    "terminal.ansiBrightCyan": ("#5E8E86", "#C4E4DC"),
    "terminal.ansiBrightWhite": ("#3A2430", "#F7F2EA"),
}

TOKENS = [
    ("comment", ("#8A7A80", "#8A7A96"), "italic"),
    (("keyword", "storage"), ("#B0472A", "#E8722A"), None),
    ("string", ("#5E7A2E", "#A8D06A"), None),
    (("entity.name.function", "support.function"), ("#9A6A1E", "#E8C66A"), None),
    (("entity.name.type", "support.type", "support.class"), ("#6B4A8A", "#C9A0E0"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#9A2F3E", "#E88A96"), None),
    ("variable", ("#2A1C33", "#F2EDE4"), None),
    ("variable.parameter", ("#5E4A50", "#C9BCC8"), None),
    (("variable.other.property", "support.variable.property"), ("#9A6A1E", "#E8C66A"), None),
    ("keyword.operator", ("#7A6A70", "#B9A8C4"), None),
    ("punctuation", ("#8A7A80", "#8A7A96"), None),
    ("entity.name.tag", ("#B0472A", "#E8722A"), None),
    ("entity.other.attribute-name", ("#9A2F3E", "#E88A96"), None),
    ("string.regexp", ("#9A6A1E", "#DCC48A"), None),
    ("constant.character.escape", ("#9A2F3E", "#EFD0A8"), None),
    ("markup.heading", ("#3A2430", "#F7F2EA"), "bold"),
    ("markup.bold", ("#3A2430", "#F7F2EA"), "bold"),
    ("markup.italic", ("#3A2430", "#F7F2EA"), "italic"),
    ("invalid", ("#B0303F", "#E88A96"), None),
]

SEMANTIC = {
    "variable": "#2A1C33|#F2EDE4",
    "parameter": "#5E4A50|#C9BCC8",
    "property": "#9A6A1E|#E8C66A",
    "function": "#9A6A1E|#E8C66A",
    "method": "#9A6A1E|#E8C66A",
    "type": "#6B4A8A|#C9A0E0",
    "class": "#6B4A8A|#C9A0E0",
    "interface": "#6B4A8A|#C9A0E0",
    "variable.readonly": "#9A2F3E|#E88A96",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "Pumpkin cream by day and a charcoal violet night: an orange, slime green and blood red palette for late sessions.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "halloween", "pumpkin"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#1E1626", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
