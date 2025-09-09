# emoji-quick-search

### purpose
Finding the right emoji or symbol is a pain! I need a better and more cross-indexes search when I'm looking for character I need. So I built one.

### implementation
Find and copy the exact emoji or scientific symbol you need—instantly.
Type to filter, click (or press Enter) to copy. Zero backend. Works from any static host.

#### Highlights
* Blazing-fast search: token index + fuzzy fallback (prefix + substring).
* One click to copy (with clipboard fallback for older browsers).
* Categories & Recents: filter by pill; auto-save your last uses.
* Hover enlarge: glyph zooms on hover/focus (respects prefers-reduced-motion).
* Black/white high-contrast theme: tuned for visibility.
* Flexible data loading:
  * emoji-data.json in the same folder (default)
  * absolute /emoji-data.json fallback
  * ?data=… query param override
  * remembered URL in localStorage
  * built-in remotes (your GitHub raw + jsDelivr mirror)
* No server code: just static files.

#### Date schema
Data Format

The app accepts a compact schema (preferred) and can normalize common alternatives:

```
Preferred (compact)
{
  "e": "😀",
  "n": "grinning face",
  "c": "smileys",
  "k": ["smile","happy","grin","joy","face"],
  "p": 0.95
}
```

* e: emoji/symbol (string)
* n: human-readable name
* c: category one of smileys|people|gestures|animals|food|activities|travel|objects|symbols|flags
* k: keywords/tags (array of strings)
* p: optional popularity/boost (0..1, default 0.5)


#### Search App


