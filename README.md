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
- [SWEET AND FRUITY MAKEUP](https://studyquests.pages.dev/sweet-and-fruity-makeup.html)
- [POOL MERGE MANIA](https://iskillquest.pages.dev/pool-merge-mania.html)
- [CATEGORY MAHJONG 2](https://studyplaying.github.io/category-mahjong-2.html)
- [MR DUDE KING OF THE HILL](https://studyquests.pages.dev/mr-dude-king-of-the-hill.html)
- [RED STICKMAN VS CRAFTMANS](https://studyplaying.github.io/red-stickman-vs-craftmans.html)
- [GUN BUILDER](https://studyplaying.github.io/gun-builder.html)
- [TILE HEXA SORT](https://studyplaying.github.io/tile-hexa-sort.html)
- [CATEGORY CASUAL 8](https://studyplaying.github.io/category-casual-8.html)
- [CATEGORY IBOSS](https://studyplaying.github.io/category-iboss.html)
- [CATEGORY IO](https://studyquests.pages.dev/category-io.html)
- [SAFARI STORY MAHJONG](https://studyplaying.github.io/safari-story-mahjong.html)
- [CATEGORY MAHJONG](https://studyquests.pages.dev/category-mahjong.html)
- [INDEX25](https://studyplaying.github.io/index25.html)
- [CATEGORY DEEP IMMERSIVE24](https://studyplayings.pages.dev/category-deep-immersive24.html)
- [CATEGORY MINECRAFT](https://studyplaying.github.io/category-minecraft.html)
- [HUMAN EVOLUTION RUN](https://studyplayings.pages.dev/human-evolution-run.html)
- [EXTREME REAL CAR DRIVING 2025](https://studyplaying.github.io/extreme-real-car-driving-2025.html)
- [STACK TOWER PRO](https://studyplayings.pages.dev/stack-tower-pro.html)
- [CATEGORY IDLE448](https://studyplayings.pages.dev/category-idle448.html)
- [MINI GAMES RELAX COLLECTION 2](https://studyplaying.github.io/mini-games-relax-collection-2.html)
- [COLORSFORMS](https://studyplaying.github.io/colorsforms.html)
- [TERMS](https://studyplayings.web.app/terms.html)
- [IDLE MONEY FACTORY](https://studyplayings.pages.dev/idle-money-factory.html)
- [MATCH 3D PUZZLE SAGA](https://studyplaying.github.io/match-3d-puzzle-saga.html)
- [MOJO EMOJI](https://learnquester.github.io/mojo-emoji.html)
- [CATEGORY STICKMAN](https://learnquester.github.io/category-stickman.html)
- [BEARS VS ART](https://studyplaying.github.io/bears-vs-art.html)
- [HALLOWEEN STICKMAN](https://studyplaying.github.io/halloween-stickman.html)
- [MOTOR TOUR](https://studyplaying.github.io/motor-tour.html)
- [SHELF SWEEP](https://learnquester.github.io/shelf-sweep.html)
- [CATEGORY HORDE SURVIVAL67](https://studyplaying.github.io/category-horde-survival67.html)
- [CATEGORY DIRT BIKE](https://studyquests.pages.dev/category-dirt-bike.html)
- [SAVE THE CROP](https://studyplaying.github.io/save-the-crop.html)
- [CHAIN CUBE 2048 3D MERGE GAME](https://studyplaying.github.io/chain-cube-2048-3d-merge-game.html)
- [CATEGORY DEFENSE](https://studyplaying.github.io/category-defense.html)
- [MAGIC FOREST MERGE THE SECRETS](https://studyplaying.github.io/magic-forest-merge-the-secrets.html)
- [CATEGORY STICKMAN](https://thelearnquester.web.app/category-stickman.html)
- [ITALIAN BRAINROT OBBY PARKOUR](https://studyplaying.github.io/italian-brainrot-obby-parkour.html)
- [CATEGORY BRAIN260](https://studyplaying.github.io/category-brain260.html)
- [MATCH FIND 3D](https://learnquester.github.io/match-find-3d.html)
- [CARS MERGE](https://studyplayings.web.app/cars-merge.html)
- [HOT COLD WINTER STYLE](https://studyplaying.github.io/hot-cold-winter-style.html)
- [CATEGORY LINKS](https://thelearnquester.web.app/category-links.html)
- [CATEGORY RACING DRIVING](https://learnquester.github.io/category-racing-driving.html)
- [MATCH MASTER](https://studyquesthub.web.app/match-master.html)
- [MUSHROOM BLOCKS](https://studyplayings.pages.dev/mushroom-blocks.html)
- [MY DINOSAUR LAND](https://studyplayings.pages.dev/my-dinosaur-land.html)
- [INDEX19](https://studyplayings.pages.dev/index19.html)
- [MONSTER GIRLS BACK TO SCHOOL](https://studyplayings.web.app/monster-girls-back-to-school.html)
- [CATEGORY MATCH 3117](https://learnquester.github.io/category-match-3117.html)
- [CATEGORY MAGIC46](https://learnquester.github.io/category-magic46.html)
- [AGENT SQUAD](https://studyquests.pages.dev/agent-squad.html)
- [BALLOON POP FRENZY](https://studyplayings.web.app/balloon-pop-frenzy.html)
- [NOOB FUN FISHING](https://learnquester.github.io/noob-fun-fishing.html)
- [MANSION STORY MATCH](https://studyplayings.web.app/mansion-story-match.html)
- [SOKOBAN PUZZLE GAME](https://studyplayings.web.app/sokoban-puzzle-game.html)
- [DINO SIMULATOR CITY ATTACK](https://studyplayings.web.app/dino-simulator-city-attack.html)
- [CATEGORY EXPLOIT](https://thelearnquester.web.app/category-exploit.html)
- [GOLDEN FRONTIER](https://studyplayings.pages.dev/golden-frontier.html)
- [CATEGORY TANK58](https://studyplayings.pages.dev/category-tank58.html)
- [HEXANAUT IO](https://quizverses.github.io/hexanaut-io.html)
- [DUSTY MAZE HUNTER](https://quizverses.github.io/dusty-maze-hunter.html)
- [BLOCK UP](https://quizverses.github.io/block-up.html)
- [CATEGORY MISSION207](https://studyquesthub.web.app/category-mission207.html)
- [MY LITTLE CAR WASH](https://quizverses.github.io/my-little-car-wash.html)
- [DOMINO ADVENTURE](https://quizverses-9d2f2.web.app/domino-adventure.html)
- [PUZZLE BLOCKS](https://studyplaying.github.io/puzzle-blocks.html)
- [TURNFIGHT COM UAP](https://studyplayings.pages.dev/turnfight-com-uap.html)
- [SERIOUS HEAD 2](https://quizverses-9d2f2.web.app/serious-head-2.html)
- [GO CHICKEN GO](https://learnquester.github.io/go-chicken-go.html)
- [GEOMETRY ARROW 2](https://learnquester.github.io/geometry-arrow-2.html)
- [VR WORLD](https://quizverses-9d2f2.web.app/vr-world.html)
- [INDEX11](https://studyplayings.pages.dev/index11.html)
- [MAGIC BEAUTY MAKEUP](https://quizverses.github.io/magic-beauty-makeup.html)
- [CUBE DROP PUZZLE](https://quizverses-9d2f2.web.app/cube-drop-puzzle.html)
- [CATEGORY UNBLOCKED GAMES](https://quizverses.pages.dev/category-unblocked-games.html)
- [BUBBLE SHOOTER PANDA BLAST](https://quizverses.github.io/bubble-shooter-panda-blast.html)
- [OHPEACH IT](https://quizverses.github.io/ohpeach-it.html)
- [CATEGORY BOARDGAMES](https://quizverses.pages.dev/category-boardgames.html)
- [THRILL ROLLER COASTER](https://quizverses.github.io/thrill-roller-coaster.html)
- [HOTGEAR](https://studyplaying.github.io/hotgear.html)
- [WARCALL IO](https://quizverses.github.io/warcall-io.html)
- [FURY TANKS](https://quizverses.github.io/fury-tanks.html)
- [FARM BLAST](https://quizverses.github.io/farm-blast.html)
- [CATEGORY MAKEUP51](https://quizverses.pages.dev/category-makeup51.html)
- [MOTO ATTACK BIKE RACING](https://quizverses.github.io/moto-attack-bike-racing.html)
- [CAR CARE REPAIR DUDU MECHANIC](https://studyplaying.github.io/car-care-repair-dudu-mechanic.html)
- [POP PARTY SUIKA WATERMELON](https://studyplayings.web.app/pop-party-suika-watermelon.html)
- [HEXAGON](https://studyplaying.github.io/hexagon.html)
- [IMAGE CROSSWORD](https://learnquester.github.io/image-crossword.html)
- [CRAZY BUNNIES](https://quizverses.github.io/crazy-bunnies.html)
- [CATEGORY LOGIC538](https://quizverses.pages.dev/category-logic538.html)
- [HARLEY LEARNS TO LOVE](https://studyquests.pages.dev/harley-learns-to-love.html)
- [PANDA LU TREEHOUSE](https://studyplaying.github.io/panda-lu-treehouse.html)
- [CATEGORY SPORTS](https://quizverses.pages.dev/category-sports.html)
- [CATEGORY BASKETBALL](https://quizverses.github.io/category-basketball.html)
- [SUDOKU MASTER](https://learnquester.github.io/sudoku-master.html)
- [MAHJONG MAGIC ISLANDS](https://learnquester.github.io/mahjong-magic-islands.html)
- [BOOM STICK BAZOOKA](https://quizverses.github.io/boom-stick-bazooka.html)
- [MIND GAMBIT](https://quizverses.github.io/mind-gambit.html)
- [MERGE FLOWERS](https://studyplayings.web.app/merge-flowers.html)
- [CATEGORY PIXEL313](https://quizverses.pages.dev/category-pixel313.html)
- [CATEGORY DESTROY256](https://studyquests.pages.dev/category-destroy256.html)
- [SUM MASTER](https://quizverses.github.io/sum-master.html)
- [THE ROMAN EMPIRE COLOSSEUM](https://quizverses.github.io/the-roman-empire-colosseum.html)
- [CRAZY BAR BRAWL](https://studyquests.github.io/crazy-bar-brawl.html)
- [JOURNEY OF ESCAPE](https://studyplaying.github.io/journey-of-escape.html)
- [LUCY ALL SEASON FASHIONINSTA](https://quizverses.github.io/lucy-all-season-fashioninsta.html)
- [CATEGORY CAN T STOP PLAYING212](https://studyquests.pages.dev/category-can-t-stop-playing212.html)
- [BANK ROBBERY ESCAPE](https://quizverses.github.io/bank-robbery-escape.html)
- [CATEGORY RACING DRIVING 2](https://quizverses.pages.dev/category-racing-driving-2.html)
- [PYRAMIDZ2](https://studyplaying.github.io/pyramidz2.html)
- [HAPPY FARM THE CROP](https://quizverses.pages.dev/happy-farm-the-crop.html)
- [100 ROOMS ESCAPE](https://studyplayings.web.app/100-rooms-escape.html)
- [OBBY CARDS THE LEGEND HUNT](https://studyplaying.github.io/obby-cards-the-legend-hunt.html)
- [CATEGORY PREMIUM PERKS71](https://learnquester.github.io/category-premium-perks71.html)
- [PIN MASTER](https://studyquests.pages.dev/pin-master.html)
- [DEEP FISHING](https://quizverses.pages.dev/deep-fishing.html)
- [HALLOWEEN MATCH TRIO](https://quizverses.pages.dev/halloween-match-trio.html)
- [CATEGORY BATTLE524](https://thelearnquester.web.app/category-battle524.html)
- [MOTORCYCLE RACER ROAD MAYHEM](https://quizverses.pages.dev/motorcycle-racer-road-mayhem.html)
- [CATEGORY YOUTUBE](https://learnquester.github.io/category-youtube.html)
- [CATEGORY SIDE SCROLLING184](https://quizverses.pages.dev/category-side-scrolling184.html)
- [CATEGORY BIKE 2](https://studyplayings.pages.dev/category-bike-2.html)
- [TILEMAN IO](https://studyplaying.github.io/tileman-io.html)
- [DINOSAUR CARDS](https://studyplayings.web.app/dinosaur-cards.html)
- [JINN DASH](https://quizverses.pages.dev/jinn-dash.html)
- [BUILD AND RUN](https://studyplaying.github.io/build-and-run.html)
- [UNCLE HIT PUNCH THE DUMMY](https://studyplayings.web.app/uncle-hit-punch-the-dummy.html)
- [MR RECKLESS CAR CHASE SIMULATOR](https://quizverses.pages.dev/mr-reckless-car-chase-simulator.html)
