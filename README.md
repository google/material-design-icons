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
- [LABUBA HALLOWEEN INFESTATION](https://themindplay.pages.dev/labuba-halloween-infestation.html)
- [CATEGORY DIFFICULT81](https://thelearnquesters.pages.dev/category-difficult81.html)
- [HIDDEN OBJECTS ISLAND](https://studyplayings.web.app/hidden-objects-island.html)
- [QUIZ X](https://quizverses.github.io/quiz-x.html)
- [CATEGORY BALL175](https://studyplayings.web.app/category-ball175.html)
- [CATEGORY BATTLE](https://studyplayings.web.app/category-battle.html)
- [CATEGORY STICKMAN175](https://studyplayings.pages.dev/category-stickman175.html)
- [CANDY CRUNCH SUGAR ESCAPE](https://studyplaying.github.io/candy-crunch-sugar-escape.html)
- [CATEGORY BATTLE](https://studyquests.pages.dev/category-battle.html)
- [LINK FLOW](https://learnquester.github.io/link-flow.html)
- [SORT WORKS NUTS ORDER](https://studyplayings.web.app/sort-works-nuts-order.html)
- [4 COLORS CARD MANIA](https://studyquests.github.io/4-colors-card-mania.html)
- [HAPPY JUMP](https://studyquests.github.io/happy-jump.html)
- [DOOMSDAY SURVIVAL RPG SHOOTER](https://studyquests.github.io/doomsday-survival-rpg-shooter.html)
- [POPCATS MERGE THE CATS](https://studyquests.github.io/popcats-merge-the-cats.html)
- [PRACTICE ON ME](https://studyquests.github.io/practice-on-me.html)
- [COLLECT HONEY PUZZLE](https://thelearnquester.web.app/collect-honey-puzzle.html)
- [ADDICTION SOLITAIRE](https://learnquester.github.io/addiction-solitaire.html)
- [IDLE AIRPORT CEO](https://thelearnquester.web.app/idle-airport-ceo.html)
- [MINE SLASH](https://iskillquest.pages.dev/mine-slash.html)
- [CATEGORY SCHOOL](https://learnquester.github.io/category-school.html)
- [CATEGORY CAR](https://thelearnquester.web.app/category-car.html)
- [SKINFLUENCER BEAUTY ROUTINE](https://iskillquest.pages.dev/skinfluencer-beauty-routine.html)
- [ARROW SORTING](https://iskillquest.pages.dev/arrow-sorting.html)
- [SUMMER TRIPLE MAHJONG](https://studyquests.github.io/summer-triple-mahjong.html)
- [CHALLENGE YOUR FRIENDS](https://themindplays.pages.dev/challenge-your-friends.html)
- [HIDDEN OBJECTS CRIME SCENE](https://iskillquest.pages.dev/hidden-objects-crime-scene.html)
- [CATEGORY EDUCATIONAL](https://studyplaying.github.io/category-educational.html)
- [CATEGORY STRATEGY 2](https://thelearnquester.web.app/category-strategy-2.html)
- [DEVIL DASH](https://studyplaying.github.io/devil-dash.html)
- [CATEGORY BUBBLE SHOOTER](https://studyplayings.web.app/category-bubble-shooter.html)
- [FISH STORY 3](https://themindplays.pages.dev/fish-story-3.html)
- [CATEGORY RAGDOLL57](https://studyplayings.web.app/category-ragdoll57.html)
- [DONT PANIC DUDE](https://iskillquest.pages.dev/dont-panic-dude.html)
- [PRINCESS RUN 3D](https://studyplayings.pages.dev/princess-run-3d.html)
- [AUTO NINJA](https://studyquests.github.io/auto-ninja.html)
- [MERGE WAR](https://themindplays.pages.dev/merge-war.html)
- [BASKETBALL STARS 2026](https://studyplayings.pages.dev/basketball-stars-2026.html)
- [MEME WARS](https://studyplayings.pages.dev/meme-wars.html)
- [IDLE BARBER SHOP](https://iskillquest.pages.dev/idle-barber-shop.html)
- [RAGDOLL FOOTBALL 2 PLAYERS](https://studyplayings.web.app/ragdoll-football-2-players.html)
- [ANIME COUPLE AVATAR MAKER](https://iskillquest.pages.dev/anime-couple-avatar-maker.html)
- [LAMPHEAD](https://studyquests.github.io/lamphead.html)
- [BUBBLE PLOPPER](https://skillplay.github.io/bubble-plopper.html)
- [CATEGORY 2D1 070](https://studyplaying.github.io/category-2d1-070.html)
- [CONNECT THE DOTS COLOR LINES](https://studyplayings.pages.dev/connect-the-dots-color-lines.html)
- [ULTIMATE YATZY](https://iskillquest.pages.dev/ultimate-yatzy.html)
- [PUSH THE FROG](https://studyquesthub.web.app/push-the-frog.html)
- [ROBIN HOOD ARCHER](https://studyquesthub.web.app/robin-hood-archer.html)
- [CATEGORY ART32](https://themindplays.pages.dev/category-art32.html)
- [ULTIMATE PLANTS TD](https://themindskillplayplay.pages.dev/ultimate-plants-td.html)
- [WORDS MATCH](https://studyplaying.github.io/words-match.html)
- [ULTIMATE ROBO DUEL 3D](https://iskillquest.pages.dev/ultimate-robo-duel-3d.html)
- [CATEGORY MOUSE1 707](https://studyplayings.web.app/category-mouse1-707.html)
- [SUPER HERO TYCOON](https://iskillquest.pages.dev/super-hero-tycoon.html)
- [TAP BLOCK PUZZLE SMASH GAME](https://skillplay.github.io/tap-block-puzzle-smash-game.html)
- [CATEGORY UNBLOCKED GAMES](https://iskillquest.pages.dev/category-unblocked-games.html)
- [PRACTICE ON ME](https://studyquesthub.web.app/practice-on-me.html)
- [FRUIT BALLS JUICY FUSION](https://studyquesthub.web.app/fruit-balls-juicy-fusion.html)
- [CATEGORY STICKMAN](https://studyplayings.web.app/category-stickman.html)
- [LORENZO THE RUNNER](https://iskillquest.pages.dev/lorenzo-the-runner.html)
- [POWERFUL PUNCH](https://iskillquest.pages.dev/powerful-punch.html)
- [HEX PLANET IDLE](https://studyquesthub.web.app/hex-planet-idle.html)
- [ICOLORCOIN SORT PUZZLE](https://iskillquest.pages.dev/icolorcoin-sort-puzzle.html)
- [CATEGORY WAR GAME](https://themindplays.pages.dev/category-war-game.html)
- [FLIP KNIFE](https://iskillquest.pages.dev/flip-knife.html)
- [FROGGA](https://skillplay.github.io/frogga.html)
- [LADDER MASTER COLOR RUN](https://studyquests.github.io/ladder-master-color-run.html)
- [CATEGORY COLOR197](https://studyplayings.pages.dev/category-color197.html)
- [HYPER NURSE HOSPITAL GAMES](https://studyplaying.github.io/hyper-nurse-hospital-games.html)
- [CATEGORY MANAGEMENT209](https://studyplayings.pages.dev/category-management209.html)
- [EYE ATTACK TOILET MONSTER WAR](https://studyquests.pages.dev/eye-attack-toilet-monster-war.html)
- [CATEGORY GUN238](https://studyplaying.github.io/category-gun238.html)
- [CATEGORY STICKMAN175](https://themindplays.pages.dev/category-stickman175.html)
- [CATEGORY IBOSS](https://studyplaying.github.io/category-iboss.html)
- [CATEGORY MOUSE1 697](https://thelearnquester.web.app/category-mouse1-697.html)
- [CATEGORY CAR 2](https://studyplayings.web.app/category-car-2.html)
- [CATEGORY CUTE](https://themindplays.pages.dev/category-cute.html)
- [CATEGORY SPOT THE DIFFERENCE](https://iskillquest.pages.dev/category-spot-the-difference.html)
- [CATEGORY SOLITAIRE](https://iskillplay.web.app/category-solitaire.html)
- [OFFROAD JEEP GAME SIMULATOR](https://studyplayings.pages.dev/offroad-jeep-game-simulator.html)
- [HEXA TILE TRIO](https://skillplay.github.io/hexa-tile-trio.html)
- [CATEGORY RACING DRIVING 3](https://themindplays.pages.dev/category-racing-driving-3.html)
- [LABUBU ADVENTURE](https://iskillquest.pages.dev/labubu-adventure.html)
- [CATEGORY BUBBLE SHOOTER](https://thelearnquester.web.app/category-bubble-shooter.html)
- [RESIDENT EVIL PURGE OPERATION](https://skillplay.github.io/resident-evil-purge-operation.html)
- [CATEGORY TANK](https://studyplayings.web.app/category-tank.html)
- [SAND BLOCK BLAST](https://studyquests.github.io/sand-block-blast.html)
- [OFFICE SOLITAIRE](https://studyquests.github.io/office-solitaire.html)
- [GYM MUSCLE MERGE TYCOON](https://iskillquest.pages.dev/gym-muscle-merge-tycoon.html)
- [FARM VS ZOMBIES](https://thelearnquester.web.app/farm-vs-zombies.html)
- [EUROPE AT WAR](https://studyplayings.web.app/europe-at-war.html)
- [ANIME DOLL DIY COSPLAY GIRL](https://skillplay.github.io/anime-doll-diy-cosplay-girl.html)
- [VENETIAN LOVE AFFAIR](https://iskillquest.pages.dev/venetian-love-affair.html)
- [MIND GAMES FOR 2 3 4 PLAYER](https://iskillquest.pages.dev/mind-games-for-2-3-4-player.html)
- [SANDBOX ISLAND WAR](https://iskillplay.web.app/sandbox-island-war.html)
- [CATEGORY TOWER DEFENSE](https://iskillquest.pages.dev/category-tower-defense.html)
- [SUMMER CONNECT](https://thelearnquester.web.app/summer-connect.html)
- [FOOD SORT PUZZLE](https://studyplayings.web.app/food-sort-puzzle.html)
- [PUZZLE BLOCKS FILL IT COMPLETELY](https://iskillquest.pages.dev/puzzle-blocks-fill-it-completely.html)
- [PARKOUR BLOCK 6](https://iskillquest.pages.dev/parkour-block-6.html)
- [MONSTER MERGE LEGENDS ALIVE](https://iskillquest.pages.dev/monster-merge-legends-alive.html)
- [TANK STRIKE WASTELAND ROGUE](https://iskillquest.pages.dev/tank-strike-wasteland-rogue.html)
- [CATEGORY IO](https://studyplayings.pages.dev/category-io.html)
- [TOWER OF HELL OBBY BLOX](https://studyplaying.github.io/tower-of-hell-obby-blox.html)
- [BITGOBLINS RPG SIMULATOR](https://studyplaying.github.io/bitgoblins-rpg-simulator.html)
- [FIGHT TO THE END](https://iskillquest.pages.dev/fight-to-the-end.html)
- [TOSS THE RING](https://studyplayings.pages.dev/toss-the-ring.html)
- [SCREW PUZZLE](https://iskillquest.pages.dev/screw-puzzle.html)
- [BOLTS AND NUTS PUZZLE](https://studyplaying.github.io/bolts-and-nuts-puzzle.html)
- [DREAM PET HOTEL](https://skillplay.github.io/dream-pet-hotel.html)
- [SPIDER EVOLUTION](https://themindskillplayplay.pages.dev/spider-evolution.html)
- [STICKMAN ZOMBIE VS STICKMAN HERO](https://thelearnquester.web.app/stickman-zombie-vs-stickman-hero.html)
- [CATEGORY GOGUARDIAN](https://themindplays.pages.dev/category-goguardian.html)
- [BFFS GOLDEN HOUR](https://iskillquest.pages.dev/bffs-golden-hour.html)
- [COLOR IT IN 3D](https://iskillquest.pages.dev/color-it-in-3d.html)
- [KABOOM MINER](https://iskillquest.pages.dev/kaboom-miner.html)
- [CATEGORY CLASSIC98](https://studyplaying.github.io/category-classic98.html)
- [BACKROOMS AMONG IMPOSTOR ROLLING GIANT](https://studyplaying.github.io/backrooms-among-impostor-rolling-giant.html)
- [WILD RACE MASTER 3D](https://iskillquest.pages.dev/wild-race-master-3d.html)
- [THEO MORINIS MAGICAL RESORT](https://iskillplay.web.app/theo-morinis-magical-resort.html)
- [JUNGLE MATCH ADVENTURES](https://studyplaying.github.io/jungle-match-adventures.html)
- [CATEGORY CASUAL 9](https://themindplays.pages.dev/category-casual-9.html)
- [RICH CHOICE RUN](https://iskillquest.pages.dev/rich-choice-run.html)
- [PARTY GAMES MINI SHOOTER BATTLE](https://iskillquest.pages.dev/party-games-mini-shooter-battle.html)
- [STICKMAN DUO ESCAPE THE TOMB](https://themindskillplayplay.pages.dev/stickman-duo-escape-the-tomb.html)
- [CARNAGE BATTLE ARENA](https://studyplayings.pages.dev/carnage-battle-arena.html)
- [CATEGORY CUTE](https://iskillplay.web.app/category-cute.html)
- [ARROW SLIDE PUZZLE](https://studyquesthub.web.app/arrow-slide-puzzle.html)
- [CATEGORY AVOID295](https://themindplays.pages.dev/category-avoid295.html)
