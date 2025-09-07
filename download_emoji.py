#!/usr/bin/env python3
# download_emoji.py
import json, ssl, pathlib, urllib.request, time

# Optional: use certifi for reliable CA bundle (helps on macOS)
try:
    import certifi
    CA_FILE = certifi.where()
except Exception:
    CA_FILE = None

DATA_URLS = [
    "https://cdn.jsdelivr.net/npm/emojibase-data@15/en/data.json",
    "https://unpkg.com/emojibase-data@15/en/data.json",
]

# Map Emojibase numeric group IDs -> our categories
GROUP_ID_MAP = {
    0: "smileys",      # Smileys & Emotion
    1: "people",       # People & Body
    2: "people",       # Component (skin/hair) -> treat as people
    3: "animals",      # Animals & Nature
    4: "food",         # Food & Drink
    5: "travel",       # Travel & Places
    6: "activities",   # Activities
    7: "objects",      # Objects
    8: "symbols",      # Symbols
    9: "flags",        # Flags
}

def ssl_context():
    ctx = ssl.create_default_context()
    if CA_FILE:
        ctx.load_verify_locations(cafile=CA_FILE)
    return ctx

def fetch_json():
    last_err = None
    ctx = ssl_context()
    for url in DATA_URLS:
        for _ in range(2):
            try:
                with urllib.request.urlopen(url, context=ctx, timeout=30) as r:
                    return json.load(r)
            except Exception as e:
                last_err = e
                time.sleep(0.8)
    raise RuntimeError(f"Failed to fetch Emojibase: {last_err}")

def map_group(group, subgroup):
    """
    Accepts numeric or string group/subgroup and returns one of:
    smileys|people|gestures|animals|food|activities|travel|objects|symbols|flags
    """
    # If numeric, use map; if string, normalize
    if isinstance(group, int):
        g = GROUP_ID_MAP.get(group, "objects")
        # We can’t infer 'gestures' from numeric subgroup without a full table,
        # so keep all People (1) as 'people'.
        return g
    # String path
    g = (group or "").lower()
    sg = (subgroup or "")
    sg = sg.lower() if isinstance(sg, str) else str(sg)
    if "smileys" in g: return "smileys"
    if "people"  in g: return "gestures" if "hand" in sg else "people"
    if "gestures" in g: return "gestures"
    if "animals" in g: return "animals"
    if "food"    in g: return "food"
    if "activities" in g: return "activities"
    if "travel"  in g: return "travel"
    if "objects" in g: return "objects"
    if "symbols" in g: return "symbols"
    if "flags"   in g: return "flags"
    return "objects"

def normalize(data):
    out = []
    for e in data:
        emoji = e.get("emoji")
        name  = e.get("label")
        if not emoji or not name:
            continue

        tags = set([name])
        for t in (e.get("tags") or []):
            tags.add(str(t))
        for sc in (e.get("shortcodes") or []):
            tags.add(str(sc).replace("_", " "))

        cat = map_group(e.get("group"), e.get("subgroup"))
        out.append({"e": emoji, "n": name, "c": cat, "k": sorted(tags), "p": 0.5})

        # expand skin tones if present
        for s in (e.get("skins") or []):
            s_emoji = s.get("emoji")
            if s_emoji:
                out.append({
                    "e": s_emoji,
                    "n": name,
                    "c": cat,
                    "k": sorted(tags | {"skin tone"}),
                    "p": 0.49
                })
    return out

def main():
    script_dir = pathlib.Path(__file__).resolve().parent
    out_path = script_dir / "emoji-data.json"
    print("Fetching Emojibase…")
    raw = fetch_json()
    print(f"Fetched {len(raw)} base entries; normalizing…")
    norm = normalize(raw)
    print(f"Writing {len(norm)} emojis to {out_path} …")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(norm, f, ensure_ascii=False, indent=2)
    print("Done.")

if __name__ == "__main__":
    main()

