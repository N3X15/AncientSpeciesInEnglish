# Ancient Species in English

![](About/Preview.png)

This mod provides a quick and dirty Japanese to English translation for the Ancient Species mod by Haduki and Heli, which adds "Weeb Half Elves" and "Weeb Ancient Elves" (their words, not mine) to the game.

* It does *NOT* replace their mod, but uses the built-in translation features of RimWorld to add the translated strings. 
* No other content is added, removed, or modified (the thumbnail is just for laughs).
* I do not know how to read Japanese, but I know enough to be dangerous with Google Translate.

Therefore, this mod REQUIRES Ancient Species (https://steamcommunity.com/sharedfiles/filedetails/?id=2154569778).

## BUG REPORTS

I don't keep track of Steam, so you should use our GitHub.

1. Go to our GitHub issue tracker (https://github.com/N3X15/AncientSpeciesInEnglish/issues).
2. BEFORE YOU GO ANY FURTHER: Search for your problem FIRST.  It's likely been reported already. Duplicate reports will be closed.
3. Create a bug report.

## Corrections/Contributions

You are welcome to submit bug reports or pull requests to our GitHub: https://github.com/N3X15/AncientSpeciesInEnglish

## Load Order

This mod should be loaded after Ancient Species.

## NOTES/LEGAL

* I am not Japanese, so the translations won't be precise.  English idioms, metaphors, and phrases will be worked into the text to attempt to convey the same meaning as the original, but I may be wrong in places.  Be patient, I am stupid.
* The original dataset was made with RimTrans, which is dead as of 2020 and broken.  I may miss some translation keys in newer structures. I plan on making my own version of RimTrans, eventually.  Maybe.
* Mods can break your game.  While I do the best I can, I am not liable if this mod causes something bad to happen to your save, game, computer, or sanity.
* Downloading this mod from places other than Steam and our GitHub places you at risk of downloading bad things onto your computer.
* The Ancient Species Mod is ©2020-2022 Haduki.  This mod's author is not associated with nor (currently) condoned by Haduki or their team.
* The Ancient Species in English (AS/En) mod is ©2022 AS/En Contributors.  This content and it's source code is available to you under the MIT Open Source License. This means you can fork and re-upload without my permission, but you are required to give me credit somewhere when you do so.
* Haduki is permitted to copy this translation into their mod, as long as credit is given.

## Dev Stuff

### Prerequisites

1. Install Python >= 3.6 for your OS.
2. `pip install -U poetry`
3. `poetry install --no-root`

### Building a Release Package

```shell
python devtools/PACKAGE.py --rebuild
```

You will see a bunch of console spam as a minimal set of files are built, then a folder called `dist` will appear, followed by a ZIP plopped into the root of this directory.

* `dist/` holds the files that were thrown into the zip
* `Ancient_Species_in_English.zip` is the packaged files in an LZMA ZIP archive.