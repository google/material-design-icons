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
- [BASKET SWAP](https://studyquests.github.io/basket-swap.html)
- [KICK THE NOOBIK 3D](https://studyplayings.web.app/kick-the-noobik-3d.html)
- [CATEGORY CASUAL](https://studyquests.github.io/category-casual.html)
- [YUMMY TALES 4](https://learnquesters.pages.dev/yummy-tales-4.html)
- [CATEGORY PREMIUM PERKS71](https://thelearnquesters.pages.dev/category-premium-perks71.html)
- [CATEGORY SIDE SCROLLING184](https://thelearnquesters.pages.dev/category-side-scrolling184.html)
- [WORDLING DAILY WORD CHALLENGE](https://theskillquest.pages.dev/wordling-daily-word-challenge.html)
- [HERITAGE MAHJONG CLASSIC](https://learnquesters.pages.dev/heritage-mahjong-classic.html)
- [CATEGORY MAKEUP](https://thelearnquesters.pages.dev/category-makeup.html)
- [TERMS](https://thelearnquesters.pages.dev/terms.html)
- [CATEGORY CASUAL 8](https://thelearnquesters.pages.dev/category-casual-8.html)
- [CATEGORY COLLECT600](https://thelearnquesters.pages.dev/category-collect600.html)
- [ORGANIZER MASTER](https://thequizzone.pages.dev/organizer-master.html)
- [CATEGORY BATTLE ROYALE25](https://thelearnquesters.pages.dev/category-battle-royale25.html)
- [TAP AWAY](https://thelearnquesters.pages.dev/tap-away.html)
- [CANDY POP MANIA](https://learnquesters.pages.dev/candy-pop-mania.html)
- [BLOCK TEAM DEATHMATCH](https://thequizzone.pages.dev/block-team-deathmatch.html)
- [CATEGORY HUNTING16](https://thelearnquesters.pages.dev/category-hunting16.html)
- [CANDY CHAIN MASTER](https://learnquesters.pages.dev/candy-chain-master.html)
- [CATEGORY AGILITY](https://thelearnquesters.pages.dev/category-agility.html)
- [ANTS EMPIRE EVOLVE SIM](https://thelearnquesters.pages.dev/ants-empire-evolve-sim.html)
- [YUMMY TALES 4](https://thelearnquesters.pages.dev/yummy-tales-4.html)
- [PERFECT CAKE MAKER](https://thelearnquesters.pages.dev/perfect-cake-maker.html)
- [FREE HOOPS](https://learnquesters.pages.dev/free-hoops.html)
- [RACE TIME](https://thelearnquesters.pages.dev/race-time.html)
- [OMEGA LAYERS](https://learnquesters.pages.dev/omega-layers.html)
- [MERGE BLOCKS 2048 STYLE](https://thequizzone.pages.dev/merge-blocks-2048-style.html)
- [IDLE MERGE CAR AND RACE](https://thequizzone.pages.dev/idle-merge-car-and-race.html)
- [SPEEDRUN PLATFORMER](https://thelearnquesters.pages.dev/speedrun-platformer.html)
- [SUDOKU CLASSIC DAILY BRAIN PUZZLE](https://thequizzone.pages.dev/sudoku-classic-daily-brain-puzzle.html)
- [CATEGORY QUIZ](https://thelearnquesters.pages.dev/category-quiz.html)
- [ROBOT TERMINATOR T REX](https://thequizzone.pages.dev/robot-terminator-t-rex.html)
- [THE COUNTERFEIT BANK](https://learnquesters.pages.dev/the-counterfeit-bank.html)
- [CATEGORY CAR 3](https://thelearnquesters.pages.dev/category-car-3.html)
- [CATEGORY CAR](https://thelearnquesters.pages.dev/category-car.html)
- [THE WALL](https://learnquesters.pages.dev/the-wall.html)
- [ROOM SORT FLOOR PLAN](https://learnquesters.pages.dev/room-sort-floor-plan.html)
- [POTION MERGE WITCH](https://learnquesters.pages.dev/potion-merge-witch.html)
- [CATEGORY LOGIC538](https://thelearnquesters.pages.dev/category-logic538.html)
- [HOME PIN 1](https://learnquesters.pages.dev/home-pin-1.html)
- [CATEGORY CASUAL971](https://thelearnquesters.pages.dev/category-casual971.html)
- [DUNGEON MASTER CULT CRAFT](https://thelearnquesters.pages.dev/dungeon-master-cult-craft.html)
- [ROBBY BOMBERMAN](https://thequizzone.pages.dev/robby-bomberman.html)
- [CATEGORY ANIMAL216](https://thelearnquesters.pages.dev/category-animal216.html)
- [ARROW PUZZLE](https://thequizzone.pages.dev/arrow-puzzle.html)
- [PIRATES MATCH THE LOST TREASURE](https://thelearnquesters.pages.dev/pirates-match-the-lost-treasure.html)
- [KIRKA IO](https://thelearnquesters.pages.dev/kirka-io.html)
- [PANDA LU TREEHOUSE](https://thelearnquesters.pages.dev/panda-lu-treehouse.html)
- [DRUNK MAN 3D](https://thelearnquesters.pages.dev/drunk-man-3d.html)
- [ARCHERS RANDOM](https://studyquests.pages.dev/archers-random.html)
- [CALL OF THE JUNGLE ANIMAL EVOLUTION](https://thequizzone.pages.dev/call-of-the-jungle-animal-evolution.html)
- [SERIOUS HEAD](https://studyplaying.github.io/serious-head.html)
- [GIANT CROWD IO HOUSE CAPTURE](https://quizverses.pages.dev/giant-crowd-io-house-capture.html)
- [MATCH 3D PUZZLE SAGA](https://thequizzone.pages.dev/match-3d-puzzle-saga.html)
- [MINI SCRAPBOOK PAPER](https://learnquesters.pages.dev/mini-scrapbook-paper.html)
- [CUNNING GINGER](https://learnquesters.pages.dev/cunning-ginger.html)
- [MURDER CASE CLUE 3D](https://studyplaying.github.io/murder-case-clue-3d.html)
- [CATEGORY CASUAL 10](https://thelearnquesters.pages.dev/category-casual-10.html)
- [WENDY SOFT GIRL MAKEUP](https://learnquesters.pages.dev/wendy-soft-girl-makeup.html)
- [ZOMBIE OUTBREAK SURVIVE](https://studyquesthub.web.app/zombie-outbreak-survive.html)
- [DAN THE MAN](https://studyplaying.github.io/dan-the-man.html)
- [BLOCK UP](https://quizverses.pages.dev/block-up.html)
- [CATEGORY SNAKE](https://thelearnquesters.pages.dev/category-snake.html)
- [SCHOOL TEACHER SIMULATOR](https://studyplaying.github.io/school-teacher-simulator.html)
- [GEOMETRY DASH MAZE MAPS](https://studyplaying.github.io/geometry-dash-maze-maps.html)
- [CATEGORY FLASH 3](https://thelearnquesters.pages.dev/category-flash-3.html)
- [CAT VS GRANNY CAT SIMULATOR](https://learnquesters.pages.dev/cat-vs-granny-cat-simulator.html)
- [BLACK JUMP](https://learnquesters.pages.dev/black-jump.html)
- [ARROW ESCAPE](https://thelearnquesters.pages.dev/arrow-escape.html)
- [CATEGORY CLASSIC98](https://studyplayings.web.app/category-classic98.html)
- [CATEGORY FREE RAGDOLL GAMES](https://thelearnquesters.pages.dev/category-free-ragdoll-games.html)
- [SNOW ROAD PUZZLE](https://learnquesters.pages.dev/snow-road-puzzle.html)
- [CATEGORY SNAKE](https://learnquesters.pages.dev/category-snake.html)
- [HEXA TILE TRIO](https://thelearnquesters.pages.dev/hexa-tile-trio.html)
- [CLASSIC LABYRINTH 3D MAZE](https://studyplaying.github.io/classic-labyrinth-3d-maze.html)
- [AFRICAN PRINCESSES STYLE ISLAND](https://learnquester.pages.dev/african-princesses-style-island.html)
- [CATEGORY JIGSAW](https://thelearnquesters.pages.dev/category-jigsaw.html)
- [TOYTOPIA](https://learnquesters.pages.dev/toytopia.html)
- [CATEGORY RPG80](https://thelearnquesters.pages.dev/category-rpg80.html)
- [CATEGORY FREE RAGDOLL GAMES](https://studyplayings.web.app/category-free-ragdoll-games.html)
- [CATEGORY HALLOWEEN45](https://studyquests.github.io/category-halloween45.html)
- [CATEGORY CASUAL 8](https://studyplayings.pages.dev/category-casual-8.html)
- [CATEGORY SURVIVAL366](https://learnquesters.pages.dev/category-survival366.html)
- [CATEGORY PUZZLE 3](https://studyquests.github.io/category-puzzle-3.html)
- [DRIVE RACE CRASH](https://learnquesters.pages.dev/drive-race-crash.html)
- [HOSPITAL SURGEON DOCTOR GAME](https://studyplaying.github.io/hospital-surgeon-doctor-game.html)
- [VIRTUAL NEKO KITTY COLLECTOR](https://learnquester.pages.dev/virtual-neko-kitty-collector.html)
- [MAHJONG TILE CLUB](https://quizverses.github.io/mahjong-tile-club.html)
- [CATEGORY POOL 3](https://thelearnquesters.pages.dev/category-pool-3.html)
- [MANYUNYA SAVING THE PRINCESS](https://learnquesters.pages.dev/manyunya-saving-the-princess.html)
- [VALENTINE S DAY COUPLE DATE](https://studyplayings.pages.dev/valentine-s-day-couple-date.html)
- [CATEGORY FPS GAMES](https://studyplayings.web.app/category-fps-games.html)
- [SPRUNKI MONSTER MUSIC BEATS](https://learnquesters.pages.dev/sprunki-monster-music-beats.html)
- [DADDY RABBIT](https://thequizzone.pages.dev/daddy-rabbit.html)
- [NUMBER MERGE 10](https://studyplayings.web.app/number-merge-10.html)
- [RACE TIME](https://learnquester.github.io/race-time.html)
- [EASTERN STAR VS CITY STYLE ICON](https://thequizzone.pages.dev/eastern-star-vs-city-style-icon.html)
- [INDEX7](https://learnquesters.pages.dev/index7.html)
- [CATEGORY MINECRAFT](https://studyplayings.web.app/category-minecraft.html)
- [COLOR BLOCK JAM](https://thequizzone.pages.dev/color-block-jam.html)
- [TERMS](https://cryptotify9.onrender.com/terms.html)
- [TOSS THE RING](https://studyplaying.github.io/toss-the-ring.html)
- [SNAKE 2048](https://studyplaying.github.io/snake-2048.html)
- [COLLEGE GIRLS TEAM MAKEOVER](https://learnquesters.pages.dev/college-girls-team-makeover.html)
- [PARK FEVER](https://learnquesters.pages.dev/park-fever.html)
- [GRILL IT ALL](https://learnquester.github.io/grill-it-all.html)
- [BEAT MUSIC BATTLE](https://studyplaying.github.io/beat-music-battle.html)
- [CATEGORY ARENA254](https://thelearnquesters.pages.dev/category-arena254.html)
- [CHECKERS DELUXE EDITION](https://thequizzone.pages.dev/checkers-deluxe-edition.html)
- [INDEX5](https://learnquesters.pages.dev/index5.html)
- [CATEGORY BRAIN260](https://studyplayings.pages.dev/category-brain260.html)
- [HIDDEN OBJECTS LOST ISLAND 2](https://learnquester.pages.dev/hidden-objects-lost-island-2.html)
- [STICKMAN DISMOUNT SIMULATOR](https://thequizzone.pages.dev/stickman-dismount-simulator.html)
- [FOOD SORT PUZZLE](https://studyplayings.web.app/food-sort-puzzle.html)
- [CATEGORY SECURLY](https://thelearnquester.web.app/category-securly.html)
- [PYRAMID SOLITAIRE ANCIENT EGYPT](https://thequizzone.pages.dev/pyramid-solitaire-ancient-egypt.html)
- [MAGNETIC PULL](https://thelearnquesters.pages.dev/magnetic-pull.html)
- [BUBBLE SHOOTER VINTAGE](https://thelearnquesters.pages.dev/bubble-shooter-vintage.html)
- [GLAMOUR BEACHLIFE](https://studyquests.github.io/glamour-beachlife.html)
- [DONT PANIC DUDE](https://thequizzone.pages.dev/dont-panic-dude.html)
- [CRAZY SCREW KING](https://learnquesters.pages.dev/crazy-screw-king.html)
- [BLOONS SURVIVALIO](https://thelearnquesters.pages.dev/bloons-survivalio.html)
- [DOOMSDAY TOWER DEFENSE](https://learnquesters.pages.dev/doomsday-tower-defense.html)
- [HYPER NURSE HOSPITAL GAMES](https://quizverses.github.io/hyper-nurse-hospital-games.html)
- [TONY ARCHER](https://thequizzone.pages.dev/tony-archer.html)
- [CATEGORY DIFFICULT81](https://studyplayings.pages.dev/category-difficult81.html)
- [WATERPARK SORT](https://studyquesthub.web.app/waterpark-sort.html)
- [STICKMAN ROCKET](https://quizverses.github.io/stickman-rocket.html)
- [SHADOW FIGHTER](https://thelearnquesters.pages.dev/shadow-fighter.html)
- [SHIP FISH](https://learnquester.pages.dev/ship-fish.html)
