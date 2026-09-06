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
- [AUTO NINJA](https://studyquests.github.io/auto-ninja.html)
- [ANGRY FLAPPY](https://iskillquest.pages.dev/angry-flappy.html)
- [CAKE LINK MASTER](https://studyplayings.web.app/cake-link-master.html)
- [SNOW RIDER 3D NOSTALGIA](https://studyplaying.github.io/snow-rider-3d-nostalgia.html)
- [CELEBRITY SPRING MANICURE DESIGN](https://learnquester.github.io/celebrity-spring-manicure-design.html)
- [PRINCESSES AT HORROR SCHOOL](https://quizverses.github.io/princesses-at-horror-school.html)
- [MEOW BLOCK COLOR COLLECT](https://studyplayings.pages.dev/meow-block-color-collect.html)
- [LATUTU HOLIDAY GIFT HUNT](https://studyplayings.pages.dev/latutu-holiday-gift-hunt.html)
- [HAPPY FARM THE CROP](https://quizverses.github.io/happy-farm-the-crop.html)
- [PRIVACY](https://brainquests-fb2c5.web.app/privacy.html)
- [WORLD WAR BROTHERS WW2](https://studyplayings.web.app/world-war-brothers-ww2.html)
- [ONLINE PORTAL](https://brainquests.netlify.app/)
- [THE ZOMBIE HOUSE](https://quizverses.github.io/the-zombie-house.html)
- [HIGH SPEED CRAZY BIKE](https://studyplayings.web.app/high-speed-crazy-bike.html)
- [TINY FIGHTER UNSTOPPABLE RUN](https://quizverses.github.io/tiny-fighter-unstoppable-run.html)
- [INDEX17](https://quizverses.github.io/index17.html)
- [CATEGORY MAHJONG 2](https://studyplayings.pages.dev/category-mahjong-2.html)
- [HAPPY FARM THE CROP](https://studyplaying.github.io/happy-farm-the-crop.html)
- [CRAZY BUNNIES](https://quizverses.github.io/crazy-bunnies.html)
- [BLOCK PARKOUR TRIALS](https://quizverses.github.io/block-parkour-trials.html)
- [ONLINE PORTAL](https://brainquests.github.io/)
- [COLLECT BRAINROT ARENA](https://studyplayings.web.app/collect-brainrot-arena.html)
- [FILL THE BOTTLE](https://studyplayings.pages.dev/fill-the-bottle.html)
- [HORROR MINECRAFT PARTYTIME](https://studyplaying.github.io/horror-minecraft-partytime.html)
- [CIRCUIT MASTER](https://studyplaying.github.io/circuit-master.html)
- [DRESS PRINCESS](https://quizverses.github.io/dress-princess.html)
- [FURY ROAD ZOMBIE CRASH](https://studyplayings.pages.dev/fury-road-zombie-crash.html)
- [SUSHI PUZZLE](https://studyplaying.github.io/sushi-puzzle.html)
- [SITEMAP](https://cryptotify.github.io/sitemap.html)
- [THE ROMAN EMPIRE COLOSSEUM](https://studyplaying.github.io/the-roman-empire-colosseum.html)
- [SUPER TANK WRESTLE](https://studyplaying.github.io/super-tank-wrestle.html)
- [RACING BALL ADVENTURE](https://studyplaying.github.io/racing-ball-adventure.html)
- [MANYUNYA SAVING THE PRINCESS](https://quizverses.github.io/manyunya-saving-the-princess.html)
- [CATEGORY CASUAL 3](https://studyplayings.pages.dev/category-casual-3.html)
- [BOUNCEPOP QUEST](https://studyplayings.pages.dev/bouncepop-quest.html)
- [APPLE WORM](https://quizverses-9d2f2.web.app/apple-worm.html)
- [ZOMBIES WEAPON MERGE 4](https://studyplaying.github.io/zombies-weapon-merge-4.html)
- [GOO SLIME JUMP](https://quizverses.github.io/goo-slime-jump.html)
- [M5 CITY DRIVER](https://studyplayings.web.app/m5-city-driver.html)
- [CATEGORY MATCH 3117](https://quizverses-9d2f2.web.app/category-match-3117.html)
- [SCREW COLOR SORTING MASTER](https://quizverses.github.io/screw-color-sorting-master.html)
- [CATEGORY FREE](https://quizverses-9d2f2.web.app/category-free.html)
- [MINE SWEEPER](https://studyplayings.pages.dev/mine-sweeper.html)
- [TERMS](https://cryptotify.pages.dev/terms.html)
- [FRUIT KING MERGE](https://quizverses.github.io/fruit-king-merge.html)
- [SAVE THE CROP](https://studyplaying.github.io/save-the-crop.html)
- [GUN EVOLUTION](https://quizverses.github.io/gun-evolution.html)
- [BALL PAINT 3D](https://quizverses-9d2f2.web.app/ball-paint-3d.html)
- [WORD SEARCH UNIVERSE ANIMALS](https://quizverses.github.io/word-search-universe-animals.html)
- [CATEGORY BLOODY29](https://quizverses.github.io/category-bloody29.html)
- [WAVE CHIC OCEAN FASHION FRENZY](https://quizverses-9d2f2.web.app/wave-chic-ocean-fashion-frenzy.html)
- [CATEGORY CONTROLLER 2](https://studyplayings.pages.dev/category-controller-2.html)
- [BUBBLE SHOOTER PRO 4](https://studyplayings.web.app/bubble-shooter-pro-4.html)
- [DRAWING SQUARES](https://studyplaying.github.io/drawing-squares.html)
- [CATEGORY MANAGEMENT](https://studyplayings.pages.dev/category-management.html)
- [GRANDMAS LAST STAND](https://studyplaying.github.io/grandmas-last-stand.html)
- [BLACK PINK HALLOWEEN CONCERT](https://quizverses-9d2f2.web.app/black-pink-halloween-concert.html)
- [GARAGE MASTER NUTS AND BOLTS](https://studyplaying.github.io/garage-master-nuts-and-bolts.html)
- [BEARS VS ART](https://studyplaying.github.io/bears-vs-art.html)
- [FIND THE CAT CAT SEARCH](https://studyplaying.github.io/find-the-cat-cat-search.html)
- [TOW N GO](https://quizverses.github.io/tow-n-go.html)
- [CATEGORY FOOTBALL](https://quizverses-9d2f2.web.app/category-football.html)
- [CATEGORY FASHION](https://quizverses.github.io/category-fashion.html)
- [ROYAL REBELLION PUNK MAGIC](https://studyplayings.pages.dev/royal-rebellion-punk-magic.html)
- [PING PONG AIR](https://studyplaying.github.io/ping-pong-air.html)
- [CAKE LINK MASTER](https://studyplaying.github.io/cake-link-master.html)
- [BONNIE FITNESS FRENZY](https://quizverses.github.io/bonnie-fitness-frenzy.html)
- [GRIDDLERS DELUXE](https://studyplaying.github.io/griddlers-deluxe.html)
- [STEAL BRAINROT DUEL](https://quizverses-9d2f2.web.app/steal-brainrot-duel.html)
- [MARBLE SORT](https://studyplaying.github.io/marble-sort.html)
- [CATEGORY ADVENTURE 3](https://quizverses-9d2f2.web.app/category-adventure-3.html)
- [BULLET SUPERHERO](https://studyplayings.web.app/bullet-superhero.html)
- [HIDDEN PAINT 3D](https://studyplayings.pages.dev/hidden-paint-3d.html)
- [RUN NOW](https://quizverses-9d2f2.web.app/run-now.html)
- [MONEY CHASER CITY PARKOUR GAME](https://quizverses.github.io/money-chaser-city-parkour-game.html)
- [FISH SHOOTING FISH HUNTER](https://studyplayings.web.app/fish-shooting-fish-hunter.html)
- [SITEMAP](https://cryptotify.vercel.app/sitemap.html)
- [SNOWFLIGHT](https://studyplayings.web.app/snowflight.html)
- [CATEGORY BATTLE ROYALE25](https://quizverses.github.io/category-battle-royale25.html)
- [BLOCK PIXELS](https://studyplaying.github.io/block-pixels.html)
- [SQUID GAME CRAFT RUNNER](https://quizverses-9d2f2.web.app/squid-game-craft-runner.html)
- [BUS JAM ESCAPE](https://quizverses-9d2f2.web.app/bus-jam-escape.html)
- [GIRLFRIEND FROM HELL](https://quizverses.github.io/girlfriend-from-hell.html)
- [CATEGORY CASUAL 13](https://quizverses.github.io/category-casual-13.html)
- [HAPPY TOWN](https://quizverses.github.io/happy-town.html)
- [CATEGORY CAR 3](https://quizverses.github.io/category-car-3.html)
- [HORROR ESCAPE GRANNY ROOM](https://studyplayings.web.app/horror-escape-granny-room.html)
- [HEAD JUMP](https://quizverses.github.io/head-jump.html)
- [BRUTALMANIA IO](https://quizverses.github.io/brutalmania-io.html)
- [BOYFRIEND FOR HIRE](https://quizverses-9d2f2.web.app/boyfriend-for-hire.html)
- [SAVE BABY CAPYBARAS PULL PIN](https://quizverses-9d2f2.web.app/save-baby-capybaras-pull-pin.html)
- [RESCUE RIFT](https://quizverses.github.io/rescue-rift.html)
- [MAZOO](https://studyplayings.web.app/mazoo.html)
- [ANTISTRESS SIMULATOR OF SEQUINS DIY](https://quizverses.github.io/antistress-simulator-of-sequins-diy.html)
- [SHOTTING BALLS](https://quizverses.github.io/shotting-balls.html)
- [BOWLING STARS](https://quizverses.github.io/bowling-stars.html)
- [MUSHROOM BLOCKS](https://studyplayings.pages.dev/mushroom-blocks.html)
- [LEVEL EATEN](https://studyplaying.github.io/level-eaten.html)
- [TRAVEL WITH ME ASMR EDITION](https://studyplaying.github.io/travel-with-me-asmr-edition.html)
- [MEMOJI](https://studyplayings.web.app/memoji.html)
- [MERGE WAR](https://quizverses.github.io/merge-war.html)
- [STACK UP](https://studyplayings.pages.dev/stack-up.html)
- [DESERT ROVER SURVIVAL](https://studyplaying.github.io/desert-rover-survival.html)
- [MINICRAFT WINTERBLOCK](https://studyplayings.pages.dev/minicraft-winterblock.html)
- [SERIOUS HEAD 2](https://quizverses-9d2f2.web.app/serious-head-2.html)
- [PAPA BUZJA](https://studyplaying.github.io/papa-buzja.html)
- [SOLAR SMASH](https://studyplayings.pages.dev/solar-smash.html)
- [TANKS](https://studyplayings.web.app/tanks.html)
- [CATEGORY CUTE62](https://quizverses-9d2f2.web.app/category-cute62.html)
- [OBBY VS ZOMBIES](https://studyplayings.web.app/obby-vs-zombies.html)
- [MAGIC SORT](https://quizverses.github.io/magic-sort.html)
- [SANTA GO](https://quizverses.github.io/santa-go.html)
- [CATEGORY FPS175](https://quizverses-9d2f2.web.app/category-fps175.html)
- [CUPIDS STORY LOVE ARCHER BOW](https://quizverses-9d2f2.web.app/cupids-story-love-archer-bow.html)
- [TIMEWARRIORS](https://studyplaying.github.io/timewarriors.html)
- [IDLE ANIMAL ANATOMY](https://studyplayings.pages.dev/idle-animal-anatomy.html)
- [CATEGORY AGILITY](https://quizverses.github.io/category-agility.html)
- [CATEGORY MOBILE2 112](https://studyplayings.web.app/category-mobile2-112.html)
- [CUBE TO HOLE PUZZLE](https://quizverses-9d2f2.web.app/cube-to-hole-puzzle.html)
- [CHARGER CITY DRIVER](https://quizverses.github.io/charger-city-driver.html)
- [TANK ATTACK 5](https://quizverses.github.io/tank-attack-5.html)
- [CATEGORY DESTROY256](https://studyplayings.pages.dev/category-destroy256.html)
- [TAP TO COLOR PAINTING BOOK](https://studyplaying.github.io/tap-to-color-painting-book.html)
- [CATEGORY ARENA255](https://quizverses.github.io/category-arena255.html)
- [KNIT BEARS](https://studyplaying.github.io/knit-bears.html)
- [CATEGORY OBSTACLE](https://quizverses-9d2f2.web.app/category-obstacle.html)
- [CATEGORY DESTROY](https://studyplayings.pages.dev/category-destroy.html)
- [321 CHOOSE THE DIFFERENT](https://studyplaying.github.io/321-choose-the-different.html)
- [VOLLEY BEAN](https://quizverses-9d2f2.web.app/volley-bean.html)
- [MY LITTLE CAR WASH](https://quizverses.github.io/my-little-car-wash.html)
