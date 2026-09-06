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
- [CATEGORY HERO72](https://quizverses.github.io/category-hero72.html)
- [CANDY CHAIN MASTER](https://iskillquest.pages.dev/candy-chain-master.html)
- [BUBBLE SHOOTER TEMPLE JEWELS](https://themindplay.pages.dev/bubble-shooter-temple-jewels.html)
- [CATEGORY MINECRAFT](https://studyplaying.github.io/category-minecraft.html)
- [CATEGORY CAN T STOP PLAYING212](https://iskillquest.pages.dev/category-can-t-stop-playing212.html)
- [RAMP CAR JUMPING](https://themindplaying.web.app/ramp-car-jumping.html)
- [BUBBLE SHOOTER VINTAGE](https://themindplay.pages.dev/bubble-shooter-vintage.html)
- [HOME RUSH THE FISH WAR](https://thelearnquesters.pages.dev/home-rush-the-fish-war.html)
- [FARMER RUSH IDLE FARM GAME](https://studyplaying.github.io/farmer-rush-idle-farm-game.html)
- [CATEGORY BUBBLE SHOOTER27](https://studyquesthub.web.app/category-bubble-shooter27.html)
- [DREAM RESTAURANT 3D](https://theskillquest.pages.dev/dream-restaurant-3d.html)
- [STOCKINGS DILEMMA](https://theskillquest.pages.dev/stockings-dilemma.html)
- [CATEGORY AGILITY](https://iskillquest.pages.dev/category-agility.html)
- [GOO GOO GAGA CLICKER](https://theskillquest.pages.dev/goo-goo-gaga-clicker.html)
- [STICK KILL 3D](https://theskillquest.pages.dev/stick-kill-3d.html)
- [WALKERS ATTACK](https://themindplays.pages.dev/walkers-attack.html)
- [CATEGORY DISCORD](https://iskillplay.web.app/category-discord.html)
- [2 PLAYER GAMES KIDS KITCHEN](https://studyplayings.pages.dev/2-player-games-kids-kitchen.html)
- [CATEGORY CAT](https://studyquests.github.io/category-cat.html)
- [MOTO ROAD RASH 3D 2](https://studyquesthub.web.app/moto-road-rash-3d-2.html)
- [GEOMETRY SUBZERO](https://skillplay.github.io/geometry-subzero.html)
- [CATEGORY BUSINESS135](https://iskillplay.web.app/category-business135.html)
- [NG FLOW LINES](https://skillplay.github.io/ng-flow-lines.html)
- [MERGE PIXEL](https://themindplays.pages.dev/merge-pixel.html)
- [CATEGORY CARDS](https://themindplays.pages.dev/category-cards.html)
- [SAKURA BRANCH](https://themindplaying.web.app/sakura-branch.html)
- [CATEGORY IDLE445](https://iskillplay.web.app/category-idle445.html)
- [GAS STATION JUNKYARD TYCOON](https://skillplay.github.io/gas-station-junkyard-tycoon.html)
- [PARKING FRENZY](https://theskillquest.pages.dev/parking-frenzy.html)
- [JEWELRY IDLE](https://theskillquest.pages.dev/jewelry-idle.html)
- [CONTACT](https://studyquesthub.web.app/contact.html)
- [CATEGORY UNBLOCKEDGAMES](https://studyquests.github.io/category-unblockedgames.html)
- [KINDER GARDEN](https://themindplaying.web.app/kinder-garden.html)
- [SWORDEDIO SPIN AND RUB](https://studyquests.github.io/swordedio-spin-and-rub.html)
- [DAILY CHESS PUZZLE](https://themindskillplayplay.pages.dev/daily-chess-puzzle.html)
- [CATEGORY BOOKMARKLETS](https://iskillquest.pages.dev/category-bookmarklets.html)
- [CATEGORY AVOID](https://iskillquest.pages.dev/category-avoid.html)
- [LORENZO THE RUNNER](https://theskillquest.pages.dev/lorenzo-the-runner.html)
- [INDEX28](https://themindplays.pages.dev/index28.html)
- [ANIMAL BASKETBALL](https://theskillquest.pages.dev/animal-basketball.html)
- [PATH ICE](https://iskillplay.web.app/path-ice.html)
- [FIND THE CAT CAT SEARCH](https://studyquesthub.web.app/find-the-cat-cat-search.html)
- [WORD MINE](https://themindplay.pages.dev/word-mine.html)
- [STACKTRIS 2048](https://quizverses.pages.dev/stacktris-2048.html)
- [SAND BLAST](https://themindplay.pages.dev/sand-blast.html)
- [CATEGORY GROW GAMES](https://studyplayings.web.app/category-grow-games.html)
- [CATEGORY BUBBLE SHOOTER](https://studyplayings.web.app/category-bubble-shooter.html)
- [GRID BLAST](https://thelearnquester.web.app/grid-blast.html)
- [OFFROAD JEEP GAME SIMULATOR](https://learnquester.github.io/offroad-jeep-game-simulator.html)
- [CROSS THE ROAD](https://themindplay.pages.dev/cross-the-road.html)
- [LIPSTICK COLLECTOR RUN](https://learnquester.github.io/lipstick-collector-run.html)
- [ESCAPE ROOM MYSTERY KEY](https://studyplayings.pages.dev/escape-room-mystery-key.html)
- [WORLDCRAFT 3](https://skillplay.github.io/worldcraft-3.html)
- [CUNNING GINGER](https://themindplays.pages.dev/cunning-ginger.html)
- [HEXA ARROWS PUZZLE](https://quizverses.pages.dev/hexa-arrows-puzzle.html)
- [STRIPED FRUIT WATERMELON LAND](https://themindskillplayplay.pages.dev/striped-fruit-watermelon-land.html)
- [LITTLE ALCHEMY](https://quizverses-9d2f2.web.app/little-alchemy.html)
- [CAT CUT](https://theskillquest.pages.dev/cat-cut.html)
- [ROBBIE BECOME A BEAST](https://studyquesthub.web.app/robbie-become-a-beast.html)
- [MATH WALL SIMULATOR](https://iskillquest.pages.dev/math-wall-simulator.html)
- [EMOJI DROP THEMES](https://iskillquest.pages.dev/emoji-drop-themes.html)
- [ROMANTIC MATCH TACTICS](https://themindskillplayplay.pages.dev/romantic-match-tactics.html)
- [BATTLE OF TANK STEEL](https://themindplays.pages.dev/battle-of-tank-steel.html)
- [CATEGORY PUZZLE 4](https://themindplaying.web.app/category-puzzle-4.html)
- [BRICK BREAKER CHIPI CHIPI CHAPA CHAPA CAT](https://skillplay.github.io/brick-breaker-chipi-chipi-chapa-chapa-cat.html)
- [KAWAII CLAW MERGE](https://studyplayings.web.app/kawaii-claw-merge.html)
- [CATEGORY DIRT BIKE](https://skillplay.github.io/category-dirt-bike.html)
- [PHOTO BLOCK JOURNEY](https://skillplay.github.io/photo-block-journey.html)
- [SOKOBAN PUSH THE BOX](https://themindplay.github.io/sokoban-push-the-box.html)
- [CATEGORY PUZZLE 5](https://themindplay.pages.dev/category-puzzle-5.html)
- [CATEGORY TOWER DEFENSE118](https://quizverses.pages.dev/category-tower-defense118.html)
- [DOLPHIN COUPLE UNDERWATER DRESS UP](https://themindplay.pages.dev/dolphin-couple-underwater-dress-up.html)
- [BLOCK DROPPING MERGE](https://skillplay.github.io/block-dropping-merge.html)
- [ESCAPE ROOM MYSTERY KEY](https://studyquesthub.web.app/escape-room-mystery-key.html)
- [STEAMPUNK TOWER BUILDER](https://skillplay.github.io/steampunk-tower-builder.html)
- [IDLE INVENTOR](https://studyquesthub.web.app/idle-inventor.html)
- [MAD DASH](https://studyplayings.pages.dev/mad-dash.html)
- [ITALIAN BRAINROT QUIZ](https://iskillquest.pages.dev/italian-brainrot-quiz.html)
- [CATEGORY BASKETBALL32](https://themindplay.github.io/category-basketball32.html)
- [GLUTTONY](https://studyquesthub.web.app/gluttony.html)
- [CATEGORY BATTLE ROYALE](https://iskillquest.pages.dev/category-battle-royale.html)
- [ITALIAN BRAINROT SURVIVE PARKOUR](https://iskillquest.pages.dev/italian-brainrot-survive-parkour.html)
- [MERGE MASTER](https://studyquesthub.web.app/merge-master.html)
- [OFFROAD CLIMB 4X4](https://themindplaying.web.app/offroad-climb-4x4.html)
- [ZOMBIE EEASTER BUNNIES](https://quizverses-9d2f2.web.app/zombie-eeaster-bunnies.html)
- [QUBE 2048 ELF](https://themindskillplayplay.pages.dev/qube-2048-elf.html)
- [MEMORY MATCH MAGIC](https://thelearnquester.web.app/memory-match-magic.html)
- [INDEX3](https://studyquesthub.web.app/index3.html)
- [ASMR MAKEOVER MAKEUP STUDIO](https://studyplayings.pages.dev/asmr-makeover-makeup-studio.html)
- [ROBLO X ZOMBIE](https://themindplays.pages.dev/roblo-x-zombie.html)
- [OKAY](https://skillplay.github.io/okay.html)
- [BITGOBLINS RPG SIMULATOR](https://themindplaying.web.app/bitgoblins-rpg-simulator.html)
- [GOLF ORBIT](https://iskillquest.pages.dev/golf-orbit.html)
- [DINOSAUR CARDS](https://studyplayings.web.app/dinosaur-cards.html)
- [CATEGORY UNBLOCKER](https://quizverses.pages.dev/category-unblocker.html)
- [ULTIMATE BRAINROT CLICKER](https://themindplaying.web.app/ultimate-brainrot-clicker.html)
- [PLANE CHASE](https://themindplaying.web.app/plane-chase.html)
- [LEGEND OF FIREBALL](https://learnquester.github.io/legend-of-fireball.html)
- [DAILY JEWELS BLITZ MAHJONG](https://themindplay.pages.dev/daily-jewels-blitz-mahjong.html)
- [FARM TRIPLE MATCH](https://theskillquest.pages.dev/farm-triple-match.html)
- [ENERGY CLICKER](https://studyquesthub.web.app/energy-clicker.html)
- [SEAT JAM 3D](https://studyplayings.pages.dev/seat-jam-3d.html)
- [CUT THE ROPE TIME TRAVEL](https://iskillquest.pages.dev/cut-the-rope-time-travel.html)
- [SITEMAP](https://learnquester.github.io/sitemap.html)
- [OVERTIDE IO](https://themindskillplayplay.pages.dev/overtide-io.html)
- [CHICKEN BANANA QUEST](https://themindplay.github.io/chicken-banana-quest.html)
- [HEXA BLOCK HONEY CELLS](https://iskillquest.pages.dev/hexa-block-honey-cells.html)
- [CATEGORY BATTLE ROYALE GAMES](https://iskillquest.pages.dev/category-battle-royale-games.html)
- [BRAINROT BOING BOING MERGE](https://studyplayings.web.app/brainrot-boing-boing-merge.html)
- [ROPE STITCH PUZZLE](https://iskillquest.pages.dev/rope-stitch-puzzle.html)
- [CATEGORY PUZZLE 4](https://themindplay.pages.dev/category-puzzle-4.html)
- [WAVE DASH GEOMETRY ARROW](https://studyplayings.pages.dev/wave-dash-geometry-arrow.html)
- [CATEGORY HUB](https://themindplays.pages.dev/category-hub.html)
- [CATEGORY BIKE 3](https://themindplays.pages.dev/category-bike-3.html)
- [COLOR MAZE](https://theskillquest.pages.dev/color-maze.html)
- [CATEGORY RESTAURANT64](https://learnquester.github.io/category-restaurant64.html)
- [CATEGORY MOBILE2 112](https://thelearnquester.web.app/category-mobile2-112.html)
- [MATH QUEST](https://studyplayings.pages.dev/math-quest.html)
- [CATEGORY CUTE62](https://skillplay.github.io/category-cute62.html)
- [ALPHABET MERGE AND FIGHT](https://theskillquest.pages.dev/alphabet-merge-and-fight.html)
- [MINI GOLF BATTLE](https://studyplayings.web.app/mini-golf-battle.html)
- [ROBLO X ZOMBIE](https://iskillplay.web.app/roblo-x-zombie.html)
- [INDEX28](https://iskillquest.pages.dev/index28.html)
- [WORD STARS](https://learnquester.github.io/word-stars.html)
- [CATEGORY MATCH 3117](https://themindplay.github.io/category-match-3117.html)
- [BACK 2 SCHOOL MAKEOVER](https://studyplayings.pages.dev/back-2-school-makeover.html)
- [PURRFECT PUZZLE](https://themindplay.pages.dev/purrfect-puzzle.html)
- [RESCUE SHARP TURN](https://studyquesthub.web.app/rescue-sharp-turn.html)
- [CAR FACTORY FOR KIDS](https://theskillquest.pages.dev/car-factory-for-kids.html)
- [STICKMAN DUO ESCAPE THE TOMB](https://themindskillplayplay.pages.dev/stickman-duo-escape-the-tomb.html)
