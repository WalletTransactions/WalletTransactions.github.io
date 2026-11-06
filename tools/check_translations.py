#!/usr/bin/env python3
"""Сверяет docs/<locale>/ с языком по умолчанию (docs/ru/).

Непереведённую страницу сайт молча показывает по-русски (fallback_to_default),
поэтому пропуски видны только здесь. Пишет предупреждения в формате GitHub
Actions; с --strict завершается кодом 1, если что-то не переведено.
"""
import pathlib
import sys

DEFAULT = "ru"
docs = pathlib.Path(__file__).resolve().parent.parent / "docs"


def pages(locale: str) -> set[str]:
    root = docs / locale
    return {p.relative_to(root).as_posix() for p in root.rglob("*.md")}


base = pages(DEFAULT)
problems = 0
for loc_dir in sorted(p for p in docs.iterdir() if p.is_dir() and p.name != DEFAULT):
    have = pages(loc_dir.name)
    for page in sorted(base - have):
        print(f"::warning file=docs/{DEFAULT}/{page}::нет перевода на '{loc_dir.name}'")
        problems += 1
    for page in sorted(have - base):
        print(f"::warning file=docs/{loc_dir.name}/{page}::нет оригинала в '{DEFAULT}'")
        problems += 1
    print(f"{loc_dir.name}: {len(have & base)}/{len(base)} страниц")

sys.exit(1 if problems and "--strict" in sys.argv else 0)
