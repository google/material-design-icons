## Material Symbols / Material Icons

These are two different official icon sets from Google, using the same underlying designs. Material Symbols is the current set, introduced in April 2022, built on variable font technology. Material Icons is the classic set, but no longer updated. More details below.

The icons can be browsed in a more user-friendly way at https://fonts.google.com/icons. Use the popdown menu near top left to choose between the two sets; Material Symbols is the default.

The icons are designed under the [material design guidelines](https://material.io/guidelines/).

## Icon Requests

We’d love to support your icon needs! Please submit your request here on GitHub as an issue.

Please note that Google Fonts does not accept user submissions of finished icon designs! There are fairly strict  guidelines for Material icons, plus Google has upstream source files from which this repo is generated. Therefore, Google does not accept pull requests for icon files (whether new icon suggestions, or fixes for existing icons). Concepts are appreciated—just don’t design SVGs and submit them via pull request.

However, users are perfectly welcome to point at outside files or images as examples—for the kind of thing they want, but they won’t just be taken “as is.” This works especially well if you have multiple examples for a single icon, to help us understand the “essence” of the idea.

> For example, there is a fairly universal conceptual logo/icon for “agender,” so if you were proposing Google add an agender icon in the Material style, either mentioning that, or pointing at https://www.google.com/search?q=agender+icon would be a helpful tip.

### Third-party logos

Currently, Google does not include 3rd-party logos among the Material Symbols or Material Icons due to legal reasons. Some 3rd-party logos that were included in the past have since been removed.

## npm Packages

Google does not currently maintain the npm package for this repo, past v3 (2016). However, user @marella is hosting the following. He tells us these are automatically updated and published using GitHub Actions. Note: Google does **not** monitor or vet these packages.

### [material-symbols](https://github.com/marella/material-symbols/tree/main/material-symbols#readme) [![npm](https://img.shields.io/npm/v/material-symbols)](https://www.npmjs.com/package/material-symbols) [![install size](https://packagephobia.com/badge?p=material-symbols)](https://packagephobia.com/result?p=material-symbols)

- Only WOFF2 variable fonts and CSS for Material Symbols
- Includes outlined, rounded, and sharp icons and all variations of fill, weight, grade, and optical size
- Supports Sass

### [material-icons](https://github.com/marella/material-icons#readme) [![npm](https://img.shields.io/npm/v/material-icons)](https://www.npmjs.com/package/material-icons) [![install size](https://packagephobia.com/badge?p=material-icons)](https://packagephobia.com/result?p=material-icons) [![Downloads](https://img.shields.io/npm/dm/material-icons)](https://www.npmjs.com/package/material-icons)

- Only WOFF2, WOFF fonts and CSS
- Includes outlined, round, sharp and two-tone icons
- Supports Sass

### [@material-design-icons/font](https://github.com/marella/material-design-icons/tree/main/font#readme) [![npm (scoped)](https://img.shields.io/npm/v/@material-design-icons/font)](https://www.npmjs.com/package/@material-design-icons/font) [![install size](https://packagephobia.com/badge?p=@material-design-icons/font)](https://packagephobia.com/result?p=@material-design-icons/font)

- Only WOFF2 fonts and CSS
- Lighter version of `material-icons` package
- Doesn't support [older browsers](https://caniuse.com/woff2) such as Internet Explorer because of dropping WOFF (v1)

### [@material-design-icons/svg](https://github.com/marella/material-design-icons/tree/main/svg#readme) [![npm (scoped)](https://img.shields.io/npm/v/@material-design-icons/svg)](https://www.npmjs.com/package/@material-design-icons/svg) [![install size](https://packagephobia.com/badge?p=@material-design-icons/svg)](https://packagephobia.com/result?p=@material-design-icons/svg)

- Only SVGs
- Optimizes SVGs using SVGO

## Material Symbols

These newer icons can be browsed in a more user-friendly way at https://fonts.google.com/icons. Use the popdown menu near top left to choose between the two sets; Material Symbols is the default.

These icons were built/designed as variable fonts first (based on the 24 px designs from Material Icons). There are three separate Material Symbols variable fonts, which also have static icons available (but those do not have all the variations available, as that would be hundreds of styles):
- Outlined
- Rounded
- Sharp
- Note that although there is no separate Filled font, the Fill axis allows access to filled styles, in all three fonts. It can also be manipulated for an animated fill effect, to indicate user selection.

Each of the fonts has these design axes, which can be varied in CSS, or in many more modern design apps:
- Optical Size (opsz) from 20 to 48 px. The default is 24.
- Weight from 100 (Thin) to 700 (Bold). Regular is 400.
- Grade from -50 to 200. The default is 0 (zero). -50 is suggested for reversed contrast (e.g. white icons on black background)
- Fill from 0 to 100. The default is 0 (zero).

The following directories in this repo contain specifically Material Symbols (not Material Icons) content:
- symbols
- variablefont

What is currently _not_ available in Material Symbols?
- only the 20 and 24 px versions are designed with perfect pixel-grid alignment
- the only pre-made fonts are the variable fonts
- there are no two-tone icons

## Material Icons

The icons can be browsed in a more user-friendly way at https://fonts.google.com/icons?icon.set=Material+Icons

These classic icons are available in five distinct styles:
- Outlined
- Filled (the font version is just called Material Icons, as this is the oldest style)
- Rounded
- Sharp
- Two tone

The following directories in this repo contain specifically Material Icons (not Material Symbols) content:
- android
- font
- ios
- png
- src

What is currently _not_ available in Material Icons?
- variable fonts
- weights other than Regular
- grades other than Regular
- a means to animate Fill transitions
- new icons (since updates were halted in 2022)

## Material Icons update history

### 4.0.0 Update
* 2020 Aug 31
* Restructured repository, updated assets.

### 3.0.1 Update
* 2016 Sep 01
* Changed license in package.json.
* Added missing device symbol sprites.

### 3.0.0 Update
* 2016 Aug 25
* License change to Apache 2.0!

### 2.0
* 2016 May 28

## Getting Started

Read the [developer guide](https://developers.google.com/fonts/docs/material_icons) on how to use the material design icons in your project.

### Using a font

The `font` and `variablefont` folders contain pre-generated font files that can be included in a project. This is especially convenient for the web; however, it is generally better to link to the web font hosted on Google Fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Material+Icons"
      rel="stylesheet">
```

```html
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined"
      rel="stylesheet">
```
Read more on [Material Symbols](https://developers.google.com/fonts/docs/material_symbols/) or [Material Icons](https://developers.google.com/fonts/docs/material_icons/) in the Google Fonts developer guide.


## License

We have made these icons available for you to incorporate into your products under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt). Feel free to remix and re-share these icons and documentation in your products.
We'd love attribution in your app's *about* screen, but it's not required.


## 🌐 Web Resources & Interactive Index
- [UNSCREW THEM ALL](https://quizverses.github.io/unscrew-them-all.html)
- [BREAK BEAT](https://iskillquest.pages.dev/break-beat.html)
- [CHICKEN WARS MERGE GUNS](https://quizverses.github.io/chicken-wars-merge-guns.html)
- [BLOCK UP](https://quizverses.pages.dev/block-up.html)
- [CATEGORY MONSTER](https://studyplaying.github.io/category-monster.html)
- [BLACK PINK CHRISTMAS CONCERT](https://studyplayings.pages.dev/black-pink-christmas-concert.html)
- [CATEGORY ROGUELIKE38](https://studyquesthub.web.app/category-roguelike38.html)
- [SNAKE HUNTER](https://quizverses.pages.dev/snake-hunter.html)
- [COIN MERGE MACHINE](https://studyquests.github.io/coin-merge-machine.html)
- [BLOCK CRAFT 3D SCHOOL](https://studyplaying.github.io/block-craft-3d-school.html)
- [CATEGORY MAHJONG](https://quizverses.github.io/category-mahjong.html)
- [LOVE TILE TRIO](https://quizverses.pages.dev/love-tile-trio.html)
- [CATEGORY IDLE GAMES](https://studyquests.github.io/category-idle-games.html)
- [CATEGORY SNAKE](https://studyquests.github.io/category-snake.html)
- [SPIN THRU](https://studyplaying.github.io/spin-thru.html)
- [KNEE CASE SIMULATOR](https://studyplaying.github.io/knee-case-simulator.html)
- [TRAVEL WITH ME ASMR EDITION](https://studyplaying.github.io/travel-with-me-asmr-edition.html)
- [DOGGI](https://studyquests.github.io/doggi.html)
- [PULL THE PIN FISH RESCUE](https://quizverses.github.io/pull-the-pin-fish-rescue.html)
- [COLOR JAM 3D](https://studyplayings.pages.dev/color-jam-3d.html)
- [CATEGORY AVOID](https://learnquester.github.io/category-avoid.html)
- [FRUIT CANDY MERGE](https://quizverses.github.io/fruit-candy-merge.html)
- [CATEGORY MATCH 3 2](https://studyquests.github.io/category-match-3-2.html)
- [TRICKY CASTLE](https://studyplaying.github.io/tricky-castle.html)
- [STICKMAN HALLOWEEN SURVIVE](https://studyplayings.web.app/stickman-halloween-survive.html)
- [GOLF ORBIT](https://quizverses.pages.dev/golf-orbit.html)
- [BLOCK BLAST JEWEL PUZZLE](https://studyplaying.github.io/block-blast-jewel-puzzle.html)
- [FARM MATCH SEASONS 2](https://quizverses.pages.dev/farm-match-seasons-2.html)
- [HELP ME TRICKY BRAIN PUZZLES](https://studyplaying.github.io/help-me-tricky-brain-puzzles.html)
- [HEXAMATCH](https://studyplayings.pages.dev/hexamatch.html)
- [VARIETY MECHA](https://studyplaying.github.io/variety-mecha.html)
- [AROUND ELBRUS](https://studyquests.github.io/around-elbrus.html)
- [BACK 2 SCHOOL MAKEOVER](https://studyplayings.pages.dev/back-2-school-makeover.html)
- [BLOCK ESCAPE](https://quizverses.github.io/block-escape.html)
- [SUDOBLOCK DAILY](https://learnquester.github.io/sudoblock-daily.html)
- [WOODY TAP BLOCK](https://quizverses.pages.dev/woody-tap-block.html)
- [BRUTALMANIA IO](https://studyplaying.github.io/brutalmania-io.html)
- [MERGE FRUIT TIME](https://studyplayings.web.app/merge-fruit-time.html)
- [CATEGORY HORROR 2](https://studyquests.github.io/category-horror-2.html)
- [CATEGORY BASKETBALL](https://quizverses.github.io/category-basketball.html)
- [CATEGORY STICKMAN175](https://studyquests.github.io/category-stickman175.html)
- [CLEAN THE FLOOR](https://learnquester.github.io/clean-the-floor.html)
- [CATEGORY SIDE SCROLLING184](https://studyquests.github.io/category-side-scrolling184.html)
- [DRAW BRIDGE CHALLENGE](https://quizverses.pages.dev/draw-bridge-challenge.html)
- [SHADOWMAN RUNNER](https://studyplayings.pages.dev/shadowman-runner.html)
- [CATEGORY DESTROY256](https://studyplayings.web.app/category-destroy256.html)
- [BLAST CUBES](https://quizverses.pages.dev/blast-cubes.html)
- [CATEGORY WORLD CUP17](https://studyquests.github.io/category-world-cup17.html)
- [TOSS THE RING](https://studyplayings.pages.dev/toss-the-ring.html)
- [SQUID ESCAPE BUT BLOCKWORLD](https://studyplaying.github.io/squid-escape-but-blockworld.html)
- [ANGRY CITY SMASHER](https://studyplaying.github.io/angry-city-smasher.html)
- [CATEGORY RUNNING107](https://studyplaying.github.io/category-running107.html)
- [CATEGORY SNAKE40](https://studyplaying.github.io/category-snake40.html)
- [DAILY JEWELS BLITZ MAHJONG](https://studyplaying.github.io/daily-jewels-blitz-mahjong.html)
- [KALULU TANHULU ASMR MUKBANG](https://quizverses.pages.dev/kalulu-tanhulu-asmr-mukbang.html)
- [CATEGORY MMO25](https://studyquests.github.io/category-mmo25.html)
- [INDEX14](https://studyplayings.web.app/index14.html)
- [HARD ROCK ZOMBIE TRUCK](https://quizverses.github.io/hard-rock-zombie-truck.html)
- [BLOCKS BREAKER](https://quizverses.pages.dev/blocks-breaker.html)
- [ONE HERO](https://studyplayings.pages.dev/one-hero.html)
- [CATEGORY BIKE 2](https://thelearnquester.web.app/category-bike-2.html)
- [SHELF SHIFT MATCH](https://studyquests.pages.dev/shelf-shift-match.html)
- [CATEGORY DIRT BIKE18](https://studyquests.pages.dev/category-dirt-bike18.html)
- [HORROR MINECRAFT PARTYTIME](https://quizverses.pages.dev/horror-minecraft-partytime.html)
- [CATEGORY 2D1 070](https://learnquester.github.io/category-2d1-070.html)
- [CATEGORY CASUAL971](https://thelearnquester.web.app/category-casual971.html)
- [PUZZLE PLAY](https://studyplayings.pages.dev/puzzle-play.html)
- [INDEX11](https://thelearnquester.web.app/index11.html)
- [MATCH 3D PUZZLE SAGA](https://quizverses.github.io/match-3d-puzzle-saga.html)
- [BLADE FORGE 3D](https://learnquester.github.io/blade-forge-3d.html)
- [MUSHROOM FEVER MATCH 3](https://quizverses.github.io/mushroom-fever-match-3.html)
- [CATEGORY BOARDGAMES](https://studyplayings.web.app/category-boardgames.html)
- [ROPE SORTING](https://quizverses.github.io/rope-sorting.html)
- [GUN RUSH](https://quizverses.pages.dev/gun-rush.html)
- [CATEGORY MINECRAFT81](https://studyquests.github.io/category-minecraft81.html)
- [CATEGORY GUN238](https://thelearnquester.web.app/category-gun238.html)
- [PRINCESS RESCUE SAVE GIRL](https://studyplayings.pages.dev/princess-rescue-save-girl.html)
- [SPACE SURVIVAL RAINBOW FRIENDS MONSTER](https://studyplayings.pages.dev/space-survival-rainbow-friends-monster.html)
- [CATEGORY AVOID295](https://learnquester.github.io/category-avoid295.html)
- [CUTE SHEEP SKYBLOCK](https://quizverses.pages.dev/cute-sheep-skyblock.html)
- [VEGAMIX DA VINCI PUZZLES](https://quizverses.pages.dev/vegamix-da-vinci-puzzles.html)
- [BACKROOMS SKIBIDI TERRORS](https://studyquests.pages.dev/backrooms-skibidi-terrors.html)
- [CATEGORY BLOCK91](https://studyplayings.web.app/category-block91.html)
- [CATEGORY MATCH 3 2](https://studyquests.pages.dev/category-match-3-2.html)
- [OBBY GYM SIMULATOR ESCAPE](https://quizverses.pages.dev/obby-gym-simulator-escape.html)
- [BUS JAM](https://studyquests.pages.dev/bus-jam.html)
- [CATEGORY TURN BASED30](https://studyquests.github.io/category-turn-based30.html)
- [POPPY PLAYTIME 3 GAME](https://quizverses.pages.dev/poppy-playtime-3-game.html)
- [SPOTDIFFERS](https://studyplayings.pages.dev/spotdiffers.html)
- [SPIN SPIN](https://studyplayings.pages.dev/spin-spin.html)
- [WORLDCRAFT 3](https://studyplayings.pages.dev/worldcraft-3.html)
- [ONLINE PORTAL](https://brainquests.pages.dev/)
- [METAXIS](https://studyplayings.pages.dev/metaxis.html)
- [SOLITAIRE QUEST](https://studyplayings.pages.dev/solitaire-quest.html)
- [CAT CHAOS SIMULATOR](https://quizverses.pages.dev/cat-chaos-simulator.html)
- [FIND THE SPRUNKI](https://studyquests.pages.dev/find-the-sprunki.html)
- [SITEMAP](https://brainquests.pages.dev/sitemap.html)
- [PURSUIT RAMPAGE](https://studyquests.pages.dev/pursuit-rampage.html)
- [CATEGORY PIXEL313](https://studyquests.github.io/category-pixel313.html)
- [CATEGORY INTERSTELLARUNBLOCKER](https://studyquests.github.io/category-interstellarunblocker.html)
- [INDEX10](https://quizverses.pages.dev/index10.html)
- [SAVE THE DADDY](https://quizverses-9d2f2.web.app/save-the-daddy.html)
- [TRAFFIC ESCAPE PUZZLE](https://studyplayings.pages.dev/traffic-escape-puzzle.html)
- [MAZE CRAZE](https://studyplayings.pages.dev/maze-craze.html)
- [CATEGORY MAHJONG37](https://thelearnquester.web.app/category-mahjong37.html)
- [CATEGORY MAHJONG37](https://studyquests.github.io/category-mahjong37.html)
- [CATEGORY MATCH 3117](https://studyquesthub.web.app/category-match-3117.html)
- [V AND N PIZZA COOKING GAME](https://studyquests.github.io/v-and-n-pizza-cooking-game.html)
- [INDEX19](https://studyplayings.web.app/index19.html)
- [STICKMAN MINERS WARS](https://studyquests.pages.dev/stickman-miners-wars.html)
- [PRIVACY](https://brainquests.pages.dev/privacy.html)
- [CAR PARKING STUNT GAMES 2024](https://studyquesthub.web.app/car-parking-stunt-games-2024.html)
- [BOARD KINGS BOARD DICE](https://studyplayings.web.app/board-kings-board-dice.html)
- [TERMS](https://brainquests.pages.dev/terms.html)
- [PONGOAL](https://quizverses.pages.dev/pongoal.html)
- [FILL SORT PUZZLE](https://learnquester.github.io/fill-sort-puzzle.html)
- [FLYING BILL](https://studyquesthub.web.app/flying-bill.html)
- [SNIPER FOR BRAINROT](https://quizverses.pages.dev/sniper-for-brainrot.html)
- [CATEGORY SCRATCH17](https://studyplaying.github.io/category-scratch17.html)
- [CATEGORY CARTOON76](https://studyplayings.pages.dev/category-cartoon76.html)
- [GIRLFRIEND FROM HELL](https://studyquests.pages.dev/girlfriend-from-hell.html)
- [LAST STANDING](https://studyquesthub.web.app/last-standing.html)
- [THE COUNTERFEIT BANK](https://studyquests.pages.dev/the-counterfeit-bank.html)
- [CATEGORY BIKE](https://quizverses.pages.dev/category-bike.html)
- [HIDDEN OBJECT EMILYS CASE](https://learnquester.github.io/hidden-object-emilys-case.html)
- [K WEDDING DREAM](https://quizverses.github.io/k-wedding-dream.html)
- [CRYPTO GALS TIKTOK FASHION](https://studyplayings.pages.dev/crypto-gals-tiktok-fashion.html)
- [CATEGORY WATER39](https://studyquests.pages.dev/category-water39.html)
- [INDEX14](https://quizverses.pages.dev/index14.html)
- [CATEGORY EDUCATIONAL](https://studyquests.github.io/category-educational.html)
