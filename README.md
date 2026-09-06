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
- [BRAWL STARS SOUND](https://studyplayings.web.app/brawl-stars-sound.html)
- [PINBALL VS ZOMBIE](https://studyplayings.web.app/pinball-vs-zombie.html)
- [SCARY BABY YELLOW GAME](https://quizverses.pages.dev/scary-baby-yellow-game.html)
- [STEAM SORTER](https://studyplayings.web.app/steam-sorter.html)
- [SNIPER ELITE 3D](https://thequizzone.pages.dev/sniper-elite-3d.html)
- [CATEGORY BOARDGAMES](https://thelearnquesters.pages.dev/category-boardgames.html)
- [SPACE SURVIVOR](https://studyquesthub.web.app/space-survivor.html)
- [BUBBLE SHOOTER PANDA BLAST](https://studyplayings.web.app/bubble-shooter-panda-blast.html)
- [SCARY BANBAN ESCAPE](https://studyplayings.web.app/scary-banban-escape.html)
- [MOTO CABBIE SIMULATOR](https://quizverses.github.io/moto-cabbie-simulator.html)
- [FROGTASTIC MARBLE ADVENTURE](https://studyplayings.web.app/frogtastic-marble-adventure.html)
- [KUNG FU LITTLE ANIMALS](https://quizverses-9d2f2.web.app/kung-fu-little-animals.html)
- [CLASH CROWD GAME](https://studyplayings.web.app/clash-crowd-game.html)
- [OFFICE GOLF](https://studyplayings.web.app/office-golf.html)
- [ZOMBIES BATTLE FOR SURVIVAL](https://studyplaying.github.io/zombies-battle-for-survival.html)
- [COFFEE CRAZE SORTING GAME](https://studyplayings.web.app/coffee-craze-sorting-game.html)
- [HOTEL FEVER TYCOON](https://quizverses-9d2f2.web.app/hotel-fever-tycoon.html)
- [HOME RUSH THE FISH WAR](https://studyquests.pages.dev/home-rush-the-fish-war.html)
- [CATEGORY HUB](https://learnquester.pages.dev/category-hub.html)
- [SPACEBAR CLICKER](https://learnquesters.pages.dev/spacebar-clicker.html)
- [ZOMBIE TERMINATOR](https://learnquesters.pages.dev/zombie-terminator.html)
- [BAD EGG](https://thelearnquester.web.app/bad-egg.html)
- [TERMS](https://studyquesthub.web.app/terms.html)
- [STICKMAN ARMY THE DEFENDERS](https://studyquests.github.io/stickman-army-the-defenders.html)
- [TURNFIGHT COM UAP](https://studyplayings.web.app/turnfight-com-uap.html)
- [FROGGA](https://quizverses-9d2f2.web.app/frogga.html)
- [DINO DIGG](https://studyquesthub.web.app/dino-digg.html)
- [MOUNTAIN BUS DRIVER](https://quizverses.github.io/mountain-bus-driver.html)
- [RAGDOLL SHOW THROW BREAK AND DESTROY](https://studyplayings.web.app/ragdoll-show-throw-break-and-destroy.html)
- [EYE ART PERFECT MAKEUP ARTIST](https://studyquests.github.io/eye-art-perfect-makeup-artist.html)
- [FLAG MASTER WORLD FLAGS QUIZ](https://studyplayings.web.app/flag-master-world-flags-quiz.html)
- [BATTLE OF PIRATE CARIBBEAN BATTLE](https://studyquests.github.io/battle-of-pirate-caribbean-battle.html)
- [TOY RUMBLE 3D](https://studyquests.github.io/toy-rumble-3d.html)
- [BELOTE 3IN1](https://quizverses.github.io/belote-3in1.html)
- [IDLE BANK](https://learnquesters.pages.dev/idle-bank.html)
- [BEST CLASSIC FREECELL SOLITAIRE](https://studyquests.github.io/best-classic-freecell-solitaire.html)
- [CATEGORY ARENA254](https://studyplayings.web.app/category-arena254.html)
- [COLOR 3D BUMP IT UP](https://quizverses-9d2f2.web.app/color-3d-bump-it-up.html)
- [CATEGORY BIKE 3](https://thelearnquesters.pages.dev/category-bike-3.html)
- [GOING BALLS ADVENTURE 2](https://studyquests.github.io/going-balls-adventure-2.html)
- [STICKMAN IN SPACE](https://studyquests.github.io/stickman-in-space.html)
- [IDLE AIRPORT CEO](https://thelearnquester.web.app/idle-airport-ceo.html)
- [MONSTER DASH](https://studyplayings.web.app/monster-dash.html)
- [CATEGORY SOCCER 2](https://learnquesters.pages.dev/category-soccer-2.html)
- [FARMER RUSH IDLE FARM GAME](https://studyplaying.github.io/farmer-rush-idle-farm-game.html)
- [REAL RACING 3D](https://thelearnquester.web.app/real-racing-3d.html)
- [CATEGORY SPACE](https://learnquesters.pages.dev/category-space.html)
- [ASMR WATER VS FIRE](https://studyquesthub.web.app/asmr-water-vs-fire.html)
- [WATERPARK SORT](https://studyquests.github.io/waterpark-sort.html)
- [SNOWBOARD GAME PARTY](https://thelearnquester.web.app/snowboard-game-party.html)
- [FAMILY TREE EMOJI](https://studyquests.github.io/family-tree-emoji.html)
- [CATEGORY BATTLE524](https://studyplaying.github.io/category-battle524.html)
- [MERGE WAR](https://learnquesters.pages.dev/merge-war.html)
- [ACE CAR RACING](https://studyplayings.web.app/ace-car-racing.html)
- [ARCHER LEGEND](https://studyquesthub.web.app/archer-legend.html)
- [CATEGORY PIXEL313](https://thelearnquester.web.app/category-pixel313.html)
- [SCARY TEACHER 3D RETURNS](https://studyquests.github.io/scary-teacher-3d-returns.html)
- [CUBE CONNECT](https://studyplayings.web.app/cube-connect.html)
- [OFFROAD ISLAND](https://studyquests.github.io/offroad-island.html)
- [HAPPY BLOCKS](https://learnquesters.pages.dev/happy-blocks.html)
- [DRAW TO HOME 3D](https://studyquests.github.io/draw-to-home-3d.html)
- [BRAINROT BRIDGE RACE 3D](https://studyquests.pages.dev/brainrot-bridge-race-3d.html)
- [THE BODYGUARD](https://quizverses.pages.dev/the-bodyguard.html)
- [UNCLE HIT PUNCH THE DUMMY](https://studyplayings.web.app/uncle-hit-punch-the-dummy.html)
- [KINGDOM PUZZLES](https://studyquests.github.io/kingdom-puzzles.html)
- [CHRISTMAS FIND THE DIFFERENCES](https://thelearnquester.web.app/christmas-find-the-differences.html)
- [DINOSAUR SHIFTING RUN](https://thelearnquester.web.app/dinosaur-shifting-run.html)
- [CATEGORY SIDE SCROLLING184](https://studyquests.github.io/category-side-scrolling184.html)
- [SCREW JAM FUN PUZZLE GAME](https://quizverses.pages.dev/screw-jam-fun-puzzle-game.html)
- [CATEGORY FLASH](https://studyplayings.web.app/category-flash.html)
- [BRICK MATCH](https://studyplayings.web.app/brick-match.html)
- [CATEGORY THINKY 2](https://thelearnquester.web.app/category-thinky-2.html)
- [IDLE AIRPORT CEO](https://studyplayings.web.app/idle-airport-ceo.html)
- [IDLE BATHROOM EMPIRE TYCOON](https://studyplayings.web.app/idle-bathroom-empire-tycoon.html)
- [ASMR PET TREATMENT](https://studyplaying.github.io/asmr-pet-treatment.html)
- [CUTE CRAFT LAB](https://studyquests.github.io/cute-craft-lab.html)
- [DEEP FISHING](https://quizverses.pages.dev/deep-fishing.html)
- [CATEGORY SOLITAIRE](https://thelearnquester.web.app/category-solitaire.html)
- [INDEX9](https://quizverses.pages.dev/index9.html)
- [STICKMAN JUMP](https://quizverses-9d2f2.web.app/stickman-jump.html)
- [SHELTER SECURITY GATEKEEPER SIMULATOR](https://thelearnquester.web.app/shelter-security-gatekeeper-simulator.html)
- [BOMB HEAD HOT POTATO](https://learnquesters.pages.dev/bomb-head-hot-potato.html)
- [INDEX20](https://thelearnquesters.pages.dev/index20.html)
- [SERIOUS HEAD 2](https://studyquests.pages.dev/serious-head-2.html)
- [BACKWOODS](https://quizverses-9d2f2.web.app/backwoods.html)
- [INDEX15](https://studyplayings.web.app/index15.html)
- [WORLD CUP SOCCER CAPS](https://quizverses.github.io/world-cup-soccer-caps.html)
- [STEAL A FISH](https://studyquests.github.io/steal-a-fish.html)
- [CAR PARKING MASTER 3D REAL DRIVING SIMULATOR](https://quizverses.github.io/car-parking-master-3d-real-driving-simulator.html)
- [SPRUNKI LINK](https://thelearnquester.web.app/sprunki-link.html)
- [PUZZLE FEVER](https://studyquests.pages.dev/puzzle-fever.html)
- [OBBY PRISON CRAFT ESCAPE](https://learnquesters.pages.dev/obby-prison-craft-escape.html)
- [JELLY MATH 3D](https://quizverses-9d2f2.web.app/jelly-math-3d.html)
- [ITALIAN BRAINROT DRAG MERGE PUZZLE](https://studyplayings.web.app/italian-brainrot-drag-merge-puzzle.html)
- [AGARIO](https://studyquests.pages.dev/agario.html)
- [MERGE FRUIT](https://learnquesters.pages.dev/merge-fruit.html)
- [CATEGORY INCREMENTAL388](https://quizverses.github.io/category-incremental388.html)
- [TRADING GAMES PLAYTIME](https://thelearnquester.web.app/trading-games-playtime.html)
- [MALL ANOMALY](https://studyquesthub.web.app/mall-anomaly.html)
- [FOOD JAM](https://quizverses.pages.dev/food-jam.html)
- [MERGE FLOWERS](https://studyplayings.web.app/merge-flowers.html)
- [CATEGORY BATTLE ROYALE25](https://studyplayings.web.app/category-battle-royale25.html)
- [COLOR SCREW RESCUE PUZZLE](https://studyplayings.web.app/color-screw-rescue-puzzle.html)
- [GUMMY MERGE](https://studyquests.pages.dev/gummy-merge.html)
- [BUBBLE SHOOTER WONDERS OF EGYPT](https://studyplaying.github.io/bubble-shooter-wonders-of-egypt.html)
- [PRIVACY](https://brainquests.onrender.com/privacy.html)
- [BRICK MATCH](https://learnquesters.pages.dev/brick-match.html)
- [SUMMER SPOTLIGHT DIFFERENCES](https://studyplayings.web.app/summer-spotlight-differences.html)
- [LIMITED DEFENSE](https://thelearnquester.web.app/limited-defense.html)
- [CATEGORY MAKEUP51](https://studyplayings.web.app/category-makeup51.html)
- [INDEX27](https://thelearnquesters.pages.dev/index27.html)
- [SIGMA BOY MUSICAL CLICKER](https://thelearnquester.web.app/sigma-boy-musical-clicker.html)
- [JELLY RUN 2048](https://quizverses.github.io/jelly-run-2048.html)
- [VICE CITY DRIVER](https://quizverses.github.io/vice-city-driver.html)
- [CATEGORY STRATEGY](https://thelearnquester.web.app/category-strategy.html)
- [XYTRIAN RUNNER](https://studyquests.github.io/xytrian-runner.html)
- [TUNNEL ROAD](https://studyquests.pages.dev/tunnel-road.html)
- [ZIG SNAKE](https://studyquests.github.io/zig-snake.html)
- [HERO STORY MONSTERS CROSSING](https://studyplayings.web.app/hero-story-monsters-crossing.html)
- [LIVE STAR DOLL DRESS UP](https://thelearnquester.web.app/live-star-doll-dress-up.html)
- [TILEMAN IO](https://learnquesters.pages.dev/tileman-io.html)
- [CUTE SHEEP SKYBLOCK](https://learnquesters.pages.dev/cute-sheep-skyblock.html)
- [DEMOLITION DERBY DERBY](https://studyquests.github.io/demolition-derby-derby.html)
- [MAHJONG CONNECT FISH WORLD](https://thelearnquester.web.app/mahjong-connect-fish-world.html)
- [CATEGORY CARTOON76](https://studyplayings.web.app/category-cartoon76.html)
- [PRACTICE ON ME](https://quizverses.github.io/practice-on-me.html)
- [MINETAP MERGE CLICKER](https://studyquesthub.web.app/minetap-merge-clicker.html)
- [CATEGORY BALL175](https://studyplayings.web.app/category-ball175.html)
- [TEACHER SIMULATOR](https://quizverses.pages.dev/teacher-simulator.html)
- [AVATAR LIFE MY TOWN](https://quizverses.pages.dev/avatar-life-my-town.html)
