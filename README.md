# day3-for-range
Day 3 of Python basics: practicing for loops, exploring range() quirks, and formatting with f-strings. Python基礎3日目：for文とrange()の挙動、f-stringによる整形

## Day3: forループとrange()の文化摩擦ログ

- Pythonは「要素直渡し文化」。インデックスは必要なときだけ呼び出す。
- `enumerate()` は番号札を渡してくれる係。`start`で表示番号だけ変えられる。
- `range()` は終了値を含まない文化。C系経験者は最初に摩擦を感じやすい。
- ステップ指定や負数ステップは直感的だが、慣れが必要。
- `range(len(...))` はインデックス文化の救済策。ただしPython流では非推奨。
