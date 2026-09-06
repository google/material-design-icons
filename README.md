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
- [THIEF STICK PUZZLE MAN ESCAPE](https://themindzone.pages.dev/thief-stick-puzzle-man-escape.html)
- [CALL OF THE JUNGLE ANIMAL EVOLUTION](https://thelearnquester.web.app/call-of-the-jungle-animal-evolution.html)
- [TYPE SPRINT](https://studyplayings.web.app/type-sprint.html)
- [NEON BLAST](https://studyplaying.github.io/neon-blast.html)
- [WORDS WITH PROF WISELY](https://quizverses.github.io/words-with-prof-wisely.html)
- [CATEGORY IO](https://skillplay.github.io/category-io.html)
- [CATEGORY MAKEUP51](https://thequizzone.pages.dev/category-makeup51.html)
- [WORM ESCAPE](https://studyplayings.pages.dev/worm-escape.html)
- [PANDA DASH AUTO SHOOTING](https://iskillquest.pages.dev/panda-dash-auto-shooting.html)
- [CATEGORY PUZZLE](https://iskillquest.pages.dev/category-puzzle.html)
- [CATEGORY CAR](https://skillplay.github.io/category-car.html)
- [SNAKES](https://theskillquest.pages.dev/snakes.html)
- [STEAL BRAINROT EGGS](https://quizverses.github.io/steal-brainrot-eggs.html)
- [TWILIGHT SOLITAIRE TRIPEAKS](https://studyquests.github.io/twilight-solitaire-tripeaks.html)
- [BRILLIANT JEWELS](https://learnquesters.pages.dev/brilliant-jewels.html)
- [CATEGORY FUN MAKEUP GAMES](https://iskillquest.pages.dev/category-fun-makeup-games.html)
- [FISH FEEDING](https://studyplayings.pages.dev/fish-feeding.html)
- [BLOCK DODGER](https://learnquesters.pages.dev/block-dodger.html)
- [POPPY PLAYER PUZZLE](https://themindplays.pages.dev/poppy-player-puzzle.html)
- [LETTERS MATCH](https://themindplay.pages.dev/letters-match.html)
- [MAHJONG AT HOME SCANDINAVIAN EDITION](https://learnquesters.pages.dev/mahjong-at-home-scandinavian-edition.html)
- [TIDY MASTER SATISFEEL ASMR](https://themindplaying.web.app/tidy-master-satisfeel-asmr.html)
- [BLOCKPUZZLE COLOR BLAST](https://learnquester.github.io/blockpuzzle-color-blast.html)
- [BILLIARD DIAMOND CHALLENGE](https://themindskillplayplay.pages.dev/billiard-diamond-challenge.html)
- [COIN STACK UP](https://learnquesters.pages.dev/coin-stack-up.html)
- [CATEGORY AGILITY 3](https://iskillquest.pages.dev/category-agility-3.html)
- [INDEX38](https://iskillplay.web.app/index38.html)
- [ONLINE PORTAL](https://quizverses.github.io/)
- [INDEX8](https://studyquests.github.io/index8.html)
- [CATEGORY EDUCATIONAL25](https://thelearnquesters.pages.dev/category-educational25.html)
- [CATEGORY DRIFTING116](https://iskillquest.pages.dev/category-drifting116.html)
- [CATEGORY CASUAL969](https://iskillquest.pages.dev/category-casual969.html)
- [ARMY COMMANDER CRAFT](https://studyquesthub.web.app/army-commander-craft.html)
- [FISH SHOOTING FISH HUNTER](https://quizverses.pages.dev/fish-shooting-fish-hunter.html)
- [CATEGORY DRESS UP](https://quizverses-9d2f2.web.app/category-dress-up.html)
- [TRICKY ARROW 2](https://skillplay.github.io/tricky-arrow-2.html)
- [CATEGORY MERGE](https://learnquesters.pages.dev/category-merge.html)
- [CATEGORY DRESS UP97](https://learnquester.pages.dev/category-dress-up97.html)
- [CATEGORY DRESS UP](https://themindplay.pages.dev/category-dress-up.html)
- [INDEX7](https://learnquester.github.io/index7.html)
- [OBBY PRISON CRAFT ESCAPE](https://iskillplay.web.app/obby-prison-craft-escape.html)
- [CATEGORY GITHUB IO](https://iskillquest.pages.dev/category-github-io.html)
- [IDLE HOTEL EMPIRE](https://learnquester.pages.dev/idle-hotel-empire.html)
- [CATEGORY FOOD](https://learnquester.github.io/category-food.html)
- [ELLIE AND FRIENDS GET READY FOR FIRST DATE](https://studyquesthub.web.app/ellie-and-friends-get-ready-for-first-date.html)
- [INDEX27](https://themindplays.pages.dev/index27.html)
- [CAR STUNT RACING 3D](https://skillplay.github.io/car-stunt-racing-3d.html)
- [CHALLENGER CITY DRIVER](https://studyplayings.web.app/challenger-city-driver.html)
- [CATEGORY OBSTACLE299](https://quizverses.github.io/category-obstacle299.html)
- [OBBY GYM SIMULATOR ESCAPE](https://iskillquest.pages.dev/obby-gym-simulator-escape.html)
- [STEAL BRAINROT MONSTERS](https://themindplay.github.io/steal-brainrot-monsters.html)
- [2 PLAYER BATTLE](https://themindskillplayplay.pages.dev/2-player-battle.html)
- [TAP GO DELUXE](https://quizverses.pages.dev/tap-go-deluxe.html)
- [CATEGORY 3 PLAYER26](https://iskillquest.pages.dev/category-3-player26.html)
- [GRANDMA WITH MACHINE GUN APOCALYPSIS](https://themindplaying.web.app/grandma-with-machine-gun-apocalypsis.html)
- [MY PERFECT YEAR PLANNER](https://learnquesters.pages.dev/my-perfect-year-planner.html)
- [CATEGORY CAR](https://themindplay.github.io/category-car.html)
- [TSUNAMI BRAINROTS ONLINE](https://quizverses-9d2f2.web.app/tsunami-brainrots-online.html)
- [CRAFT MAN VS GIANT TNT](https://studyplayings.web.app/craft-man-vs-giant-tnt.html)
- [CATEGORY FREE DRESS UP GAMES](https://themindplay.github.io/category-free-dress-up-games.html)
- [CATEGORY MAHJONG 2](https://learnquesters.pages.dev/category-mahjong-2.html)
- [CATEGORY PUZZLE 3](https://studyplayings.web.app/category-puzzle-3.html)
- [CATEGORY IDLE445](https://themindplay.github.io/category-idle445.html)
- [GUN RUSH](https://learnquester.pages.dev/gun-rush.html)
- [OVERPROTECTIVE BOYFRIEND](https://themindplaying.web.app/overprotective-boyfriend.html)
- [UNBLOCK IT ATLANTIS](https://quizverses.github.io/unblock-it-atlantis.html)
- [ARCHERY RAGDOLL](https://themindplaying.web.app/archery-ragdoll.html)
- [PUSH THE FROG](https://themindskillplayplay.pages.dev/push-the-frog.html)
- [GARDEN TALES MAHJONG 2](https://themindplaying.web.app/garden-tales-mahjong-2.html)
- [TRI PEAKS EMERLAND SOLITAIRE](https://quizverses-9d2f2.web.app/tri-peaks-emerland-solitaire.html)
- [KISS O NECK](https://themindplaying.web.app/kiss-o-neck.html)
- [ASMR BEAUTY TREATMENT](https://quizverses-9d2f2.web.app/asmr-beauty-treatment.html)
- [CATEGORY CASUAL](https://iskillquest.pages.dev/category-casual.html)
- [CATEGORY FOOD95](https://iskillquest.pages.dev/category-food95.html)
- [CATEGORY BASKETBALL 2](https://skillplay.github.io/category-basketball-2.html)
- [CATEGORY BIKE](https://thelearnquesters.pages.dev/category-bike.html)
- [OFFROAD ISLAND](https://studyplayings.web.app/offroad-island.html)
- [DOODLE FOOTBALL](https://studyquests.github.io/doodle-football.html)
- [CATEGORY EDUCATIONAL](https://learnquesters.pages.dev/category-educational.html)
- [CATEGORY JIGSAW](https://themindplay.github.io/category-jigsaw.html)
- [CATEGORY AVOID295](https://studyquests.pages.dev/category-avoid295.html)
- [DOGGO DROP](https://quizverses-9d2f2.web.app/doggo-drop.html)
- [GREATSWORD V3](https://quizverses-9d2f2.web.app/greatsword-v3.html)
- [HIDE SEEK GO AND FIND](https://themindskillplayplay.pages.dev/hide-seek-go-and-find.html)
- [CATEGORY 3D1 371](https://iskillquest.pages.dev/category-3d1-371.html)
- [CATEGORY MERGE](https://skillplay.github.io/category-merge.html)
- [CATEGORY ART](https://iskillquest.pages.dev/category-art.html)
- [ROBYBOX SPACE STATION WAREHOUSE](https://studyplaying.github.io/robybox-space-station-warehouse.html)
- [MATH QUEST](https://quizverses.github.io/math-quest.html)
- [CATEGORY FLASH 2](https://iskillquest.pages.dev/category-flash-2.html)
- [CATEGORY CLASSIC98](https://skillplay.github.io/category-classic98.html)
- [CATEGORY BRAIN261](https://iskillquest.pages.dev/category-brain261.html)
- [CATEGORY BATTLESHIP19](https://iskillquest.pages.dev/category-battleship19.html)
- [DIRTY MONEY THE RICH GET RICH](https://themindskillplayplay.pages.dev/dirty-money-the-rich-get-rich.html)
- [CATEGORY TURN BASED30](https://themindplay.github.io/category-turn-based30.html)
- [CITYQUEST](https://themindskillplayplay.pages.dev/cityquest.html)
- [COLOR NUTS BOLTS PUZZLE](https://studyquests.github.io/color-nuts-bolts-puzzle.html)
- [CATEGORY HALLOWEEN45](https://themindplay.github.io/category-halloween45.html)
- [CATEGORY THINKY](https://theskillquest.pages.dev/category-thinky.html)
- [CATEGORY MOBILE2 095](https://learnquester.pages.dev/category-mobile2-095.html)
- [GLOSSY BUBBLES CHALLENGE](https://studyplayings.web.app/glossy-bubbles-challenge.html)
- [CATEGORY CASUAL971](https://skillplay.github.io/category-casual971.html)
- [SUPERWINGS SUBWAY](https://themindzone.pages.dev/superwings-subway.html)
- [QUIZ X](https://quizverses.github.io/quiz-x.html)
- [PIXEL PATH](https://studyquests.github.io/pixel-path.html)
- [OBBY RESCUE MISSION](https://theskillquest.pages.dev/obby-rescue-mission.html)
- [CATEGORY RACING DRIVING 3](https://studyquests.github.io/category-racing-driving-3.html)
- [CATEGORY PREMIUM PERKS71](https://quizverses.pages.dev/category-premium-perks71.html)
- [STICKMAN TEAM DETROIT](https://themindskillplayplay.pages.dev/stickman-team-detroit.html)
- [SITEMAP](https://theskillquest.pages.dev/sitemap.html)
- [TOCA AVATAR MY HOSPITAL](https://studyquesthub.web.app/toca-avatar-my-hospital.html)
- [ESCAPE AGAIN](https://themindskillplayplay.pages.dev/escape-again.html)
- [DEEP FISHING](https://quizverses.pages.dev/deep-fishing.html)
- [CATEGORY LOVE](https://theskillquest.pages.dev/category-love.html)
- [CATEGORY RPG GAMES](https://theskillquest.pages.dev/category-rpg-games.html)
- [BOUNCE DUNK BASKETBALL](https://studyquests.github.io/bounce-dunk-basketball.html)
- [CATEGORY BOOKMARKLETS](https://iskillquest.pages.dev/category-bookmarklets.html)
- [CATEGORY SPORTS](https://learnquester.pages.dev/category-sports.html)
- [CATEGORY FLASH](https://theskillquest.pages.dev/category-flash.html)
- [SWEET BUSINESS OF CATS CAKES](https://themindplays.pages.dev/sweet-business-of-cats-cakes.html)
- [CATEGORY ADVENTURE 3](https://skillplay.github.io/category-adventure-3.html)
- [3D ACRYLIC NAIL NAIL ART GAME](https://quizverses-9d2f2.web.app/3d-acrylic-nail-nail-art-game.html)
- [DTA BEST THIEF](https://themindplays.pages.dev/dta-best-thief.html)
- [SAVE THE CATS BUBBLE SHOOTER](https://quizverses.github.io/save-the-cats-bubble-shooter.html)
- [INCOWORD](https://themindplaying.web.app/incoword.html)
- [BATTLESHIP](https://quizverses-9d2f2.web.app/battleship.html)
- [FREECELL](https://studyquests.github.io/freecell.html)
- [SUPER FOOTBALL FEVER](https://studyquests.github.io/super-football-fever.html)
- [CATEGORY PUZZLE 5](https://learnquesters.pages.dev/category-puzzle-5.html)
- [COLOR NONOGRAM PUZZLE](https://skillplay.github.io/color-nonogram-puzzle.html)
