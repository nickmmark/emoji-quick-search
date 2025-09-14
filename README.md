# emoji-quick-search

## 🔍️ purpose
Finding the right emoji or symbol is a pain! For example if you are looking for "dead" the traditional search gives you 😵, 💀, and ☠️ but not 🪦. If you search for "anatomical" you get 🫀 but NOT 🫁. Additionally, it can be a pain to find certain scientific characters (∇, ∉, °F, ℤ, etc). 
I wanted a better, smarter, faster, and more cross-indexed search for emoji and characters. So I built one.

## ⚙️ implementation
Find and copy the exact emoji or scientific symbol you need—instantly. 
Type to filter, click (or press Enter) to copy. Zero backend. Works from any static host.

Try it out [here](https://nickmmark.github.io/emoji-quick-search/).

### highlights
* fast search: token index + fuzzy fallback (prefix + substring).
* copy with one click (with clipboard fallback for older browsers).
* categories & Recents: filter by pill
* enlarged with hover
* Flexible data loading:
  * emoji-data.json in the same folder (default)
  * absolute /emoji-data.json fallback
  * built-in remotes (your GitHub raw + jsDelivr mirror)
* no server code: just static files

### JSON data schema
Data Format

The app uses a compact schema encoded in a JSON:

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


## 🪪 License
* Freely available under an MIT License 

