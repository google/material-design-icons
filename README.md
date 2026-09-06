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
- [MAKEUP STACK](https://themindzone.pages.dev/makeup-stack.html)
- [SUPER NINJA BALLOON](https://quizverses-9d2f2.web.app/super-ninja-balloon.html)
- [EXCAVATOR SIMULATOR 3D](https://learnquester.github.io/excavator-simulator-3d.html)
- [COMBINE PICKAXES](https://studyplayings.pages.dev/combine-pickaxes.html)
- [SOLITAIRE QUEST](https://studyplayings.pages.dev/solitaire-quest.html)
- [PUMPKIN CATCHER](https://studyplayings.web.app/pumpkin-catcher.html)
- [ISLAND BATTLE 3D](https://studyplayings.pages.dev/island-battle-3d.html)
- [SWEET BUSINESS OF CATS CAKES](https://learnquester.github.io/sweet-business-of-cats-cakes.html)
- [DOGGO JUMP](https://studyplayings.web.app/doggo-jump.html)
- [CATEGORY RAGDOLL57](https://studyquests.github.io/category-ragdoll57.html)
- [TOPSY TURVY](https://learnquester.github.io/topsy-turvy.html)
- [GUMMY MERGE](https://learnquester.github.io/gummy-merge.html)
- [2020 CONNECT](https://learnquester.github.io/2020-connect.html)
- [BFFS Y2K FASHION](https://quizverses-9d2f2.web.app/bffs-y2k-fashion.html)
- [SCREW PUZZLE](https://learnquester.github.io/screw-puzzle.html)
- [COLOR DOTS CHALLENGE](https://studyplayings.pages.dev/color-dots-challenge.html)
- [LABUBU DOLL MUKBANG ASMR UNBLOCKED](https://studyplayings.web.app/labubu-doll-mukbang-asmr-unblocked.html)
- [CARS MERGE](https://studyquests.github.io/cars-merge.html)
- [GRANNYS CLASSROOM NIGHTMARE](https://learnquester.github.io/grannys-classroom-nightmare.html)
- [BUBBLE SHOOTER SPINNER POP](https://quizverses-9d2f2.web.app/bubble-shooter-spinner-pop.html)
- [CATEGORY CAT](https://studyquests.github.io/category-cat.html)
- [RED STICKMAN VS CRAFTMANS 2](https://studyquests.github.io/red-stickman-vs-craftmans-2.html)
- [TRAFFIC JAM HOP ON](https://quizverses.github.io/traffic-jam-hop-on.html)
- [CATEGORY INTERSTELLARUNBLOCKER](https://learnquester.github.io/category-interstellarunblocker.html)
- [MONSTER SCHOOL 2](https://quizverses-9d2f2.web.app/monster-school-2.html)
- [PHONE CASE DIY 5](https://quizverses-9d2f2.web.app/phone-case-diy-5.html)
- [CURSED TREASURE 11 2](https://quizverses.github.io/cursed-treasure-11-2.html)
- [IDLE ARCHEOLOGY](https://studyplayings.web.app/idle-archeology.html)
- [ZUMBA STORY](https://quizverses-9d2f2.web.app/zumba-story.html)
- [OHPEACH IT](https://quizverses.github.io/ohpeach-it.html)
- [CATEGORY MAKEUP51](https://studyquests.github.io/category-makeup51.html)
- [CINEMA EMPIRE IDLE TYCOON](https://learnquester.github.io/cinema-empire-idle-tycoon.html)
- [SHANGHAI CHEF](https://quizverses.github.io/shanghai-chef.html)
- [CUBATORIA MERGE 2048](https://quizverses-9d2f2.web.app/cubatoria-merge-2048.html)
- [SUGAR HEROES](https://learnquester.github.io/sugar-heroes.html)
- [ANNOYING BOSS PUNCH GAME](https://studyplayings.web.app/annoying-boss-punch-game.html)
- [COLOR COCKTAIL](https://learnquester.github.io/color-cocktail.html)
- [PALKOVIL THE WAY HOME](https://learnquester.github.io/palkovil-the-way-home.html)
- [CATEGORY SURVIVAL](https://thelearnquester.web.app/category-survival.html)
- [CATEGORY GITHUB IO](https://studyquests.github.io/category-github-io.html)
- [SUPER STAR ANIMAL SALON](https://quizverses.pages.dev/super-star-animal-salon.html)
- [BACKGAMMON DUEL](https://studyplayings.web.app/backgammon-duel.html)
- [NINJA BAMBOO ASSASSIN](https://learnquester.github.io/ninja-bamboo-assassin.html)
- [ITALIAN BRAINROT FIND THE STARS](https://quizverses.github.io/italian-brainrot-find-the-stars.html)
- [CATEGORY INTERSTELLAR](https://thelearnquester.web.app/category-interstellar.html)
- [MEGA FALL RAGDOLL SIMULATOR](https://studyquesthub.web.app/mega-fall-ragdoll-simulator.html)
- [CATEGORY DESTROY256](https://thelearnquester.web.app/category-destroy256.html)
- [MONSTER DUELIST](https://studyquesthub.web.app/monster-duelist.html)
- [SAVE MY HERO](https://quizverses.pages.dev/save-my-hero.html)
- [CATEGORY RACING DRIVING](https://quizverses.pages.dev/category-racing-driving.html)
- [CATEGORY GROW99](https://learnquester.github.io/category-grow99.html)
- [IDLE BARBER SHOP](https://quizverses.pages.dev/idle-barber-shop.html)
- [DRAW CLIMB RACE THE ULTIMATE HILL CLIMBING CHALLENGE](https://quizverses.github.io/draw-climb-race-the-ultimate-hill-climbing-challenge.html)
- [MAHJONG SLIDE PUZZLE](https://quizverses.github.io/mahjong-slide-puzzle.html)
- [POP PARTY SUIKA WATERMELON](https://studyplayings.web.app/pop-party-suika-watermelon.html)
- [FISH EAT GROW MEGA](https://studyplayings.pages.dev/fish-eat-grow-mega.html)
- [FRUITE SWIPE](https://quizverses-9d2f2.web.app/fruite-swipe.html)
- [MUSHROOM BLOCKS](https://studyplayings.pages.dev/mushroom-blocks.html)
- [MERGE PLANETS](https://studyplayings.pages.dev/merge-planets.html)
- [CATEGORY HORROR 2](https://thelearnquester.web.app/category-horror-2.html)
- [VEGAMIX DA VINCI PUZZLES](https://studyplayings.web.app/vegamix-da-vinci-puzzles.html)
- [HOOK MASTER MAFIA CITY](https://quizverses.pages.dev/hook-master-mafia-city.html)
- [CLEAN THE FLOOR](https://quizverses.pages.dev/clean-the-floor.html)
- [ANGRY FLAPPY](https://quizverses.github.io/angry-flappy.html)
- [SAVE SEAFOOD](https://studyplayings.pages.dev/save-seafood.html)
- [BRAIN FIND CAN YOU FIND IT](https://quizverses.github.io/brain-find-can-you-find-it.html)
- [ROBOCARPOLI](https://studyplayings.pages.dev/robocarpoli.html)
- [100 DOORS PUZZLE BOX](https://quizverses.github.io/100-doors-puzzle-box.html)
- [HIGH SPEED CRAZY BIKE](https://studyplayings.web.app/high-speed-crazy-bike.html)
- [GOBATTLEIO](https://quizverses-9d2f2.web.app/gobattleio.html)
- [CATEGORY FIGHTING](https://learnquester.github.io/category-fighting.html)
- [CATEGORY SHOOTER](https://studyquests.github.io/category-shooter.html)
- [WATERMELON MERGE](https://studyplayings.web.app/watermelon-merge.html)
- [KNEE CASE SIMULATOR](https://studyplayings.pages.dev/knee-case-simulator.html)
- [TIC TAC TOE MERGE](https://quizverses.github.io/tic-tac-toe-merge.html)
- [CATEGORY SANDBOX](https://studyquests.github.io/category-sandbox.html)
- [SMARTLE](https://studyplayings.web.app/smartle.html)
- [IDLE AIRPORT CEO](https://studyquests.github.io/idle-airport-ceo.html)
- [CATEGORY STICKMAN175](https://quizverses-9d2f2.web.app/category-stickman175.html)
- [CATEGORY DRAWING](https://thelearnquester.web.app/category-drawing.html)
- [CATEGORY LIGHTSPEED FILTER](https://thelearnquester.web.app/category-lightspeed-filter.html)
- [CATEGORY RESTAURANT64](https://studyquesthub.web.app/category-restaurant64.html)
- [BRICKS BALLS BREAKER](https://quizverses.pages.dev/bricks-balls-breaker.html)
- [ARROW COUNT MASTER](https://studyplayings.pages.dev/arrow-count-master.html)
- [2048 DROP MERGE](https://quizverses.github.io/2048-drop-merge.html)
- [WORD GAME 2026](https://learnquester.github.io/word-game-2026.html)
- [FASHION WORLD SIMULATOR](https://quizverses.github.io/fashion-world-simulator.html)
- [INDEX19](https://studyquesthub.web.app/index19.html)
- [ARROW COUNT MASTER](https://learnquester.github.io/arrow-count-master.html)
- [OIL DIGGING](https://studyplayings.pages.dev/oil-digging.html)
- [EPIC STUNTS PVP 3D](https://studyplayings.web.app/epic-stunts-pvp-3d.html)
- [INCREDIBLE KIDS DENTIST](https://quizverses.github.io/incredible-kids-dentist.html)
- [NUMBER MERGE 10](https://studyplayings.web.app/number-merge-10.html)
- [CATEGORY CAR376](https://studyquesthub.web.app/category-car376.html)
- [WONDERS OF EGYPT MATCH](https://quizverses.pages.dev/wonders-of-egypt-match.html)
- [SUPERHEROES AND THE WAND](https://studyquesthub.web.app/superheroes-and-the-wand.html)
- [CATEGORY UNBLOCKED WEBSITE](https://quizverses-9d2f2.web.app/category-unblocked-website.html)
- [SCREW JAM FUN PUZZLE GAME](https://quizverses.pages.dev/screw-jam-fun-puzzle-game.html)
- [BUS JAM ESCAPE](https://quizverses-9d2f2.web.app/bus-jam-escape.html)
- [ASMR MAKEOVER MAKEUP STUDIO](https://studyplayings.pages.dev/asmr-makeover-makeup-studio.html)
- [KITTY MATCH 3 PUZZLE GAME](https://studyplayings.pages.dev/kitty-match-3-puzzle-game.html)
- [INDEX3](https://thelearnquester.web.app/index3.html)
- [NUMBER RUSH](https://studyplayings.pages.dev/number-rush.html)
- [BRAIN CHALLENGE](https://quizverses.pages.dev/brain-challenge.html)
- [SLIME FARM](https://studyplayings.pages.dev/slime-farm.html)
- [TOW N GO](https://studyquesthub.web.app/tow-n-go.html)
- [HORROR FOREST BEAR](https://quizverses.pages.dev/horror-forest-bear.html)
- [FISH KINGDOM](https://studyplayings.pages.dev/fish-kingdom.html)
- [NUTS STACK SORT NUTS BOLTS](https://studyplayings.web.app/nuts-stack-sort-nuts-bolts.html)
- [CATEGORY DRESS UP 2](https://thelearnquester.web.app/category-dress-up-2.html)
- [PEOPLE PLAYGROUND 3D](https://studyplayings.pages.dev/people-playground-3d.html)
- [CATEGORY FASHION](https://learnquester.github.io/category-fashion.html)
- [MUSTANG CITY DRIVER](https://studyplayings.web.app/mustang-city-driver.html)
- [4 HEXA](https://quizverses-9d2f2.web.app/4-hexa.html)
- [INDEX17](https://studyplayings.web.app/index17.html)
- [GEOMETRY LITE](https://quizverses.github.io/geometry-lite.html)
- [SOLITAIRE EMPEROR SECRETS OF FATE](https://quizverses.github.io/solitaire-emperor-secrets-of-fate.html)
- [CITY BIKE RACING CHAMPION](https://quizverses-9d2f2.web.app/city-bike-racing-champion.html)
- [OFFICE ESCAPE TO DATE](https://studyplayings.pages.dev/office-escape-to-date.html)
- [IDLE BATHROOM EMPIRE TYCOON](https://studyquests.pages.dev/idle-bathroom-empire-tycoon.html)
- [GRANDMA RECIPE RAMEN](https://quizverses-9d2f2.web.app/grandma-recipe-ramen.html)
- [CAR CARE REPAIR DUDU MECHANIC](https://quizverses.pages.dev/car-care-repair-dudu-mechanic.html)
- [WORDS FROM WORDS](https://quizverses.github.io/words-from-words.html)
- [MATH RUNNER](https://studyquests.pages.dev/math-runner.html)
- [FAT CAT LIFE](https://studyquests.pages.dev/fat-cat-life.html)
- [LOVE TILE TRIO](https://learnquester.github.io/love-tile-trio.html)
- [WINTER GIFTS](https://studyquests.pages.dev/winter-gifts.html)
- [PARKING FURY 3D BEACH CITY 2](https://quizverses.github.io/parking-fury-3d-beach-city-2.html)
- [RACING PINBALL](https://learnquester.github.io/racing-pinball.html)
- [BR BR PATAPIM OBBY CHALLENGE](https://studyquests.pages.dev/br-br-patapim-obby-challenge.html)
