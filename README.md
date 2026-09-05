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
- [NITRO SPEED 2 UNDERGROUND](https://studyquests.pages.dev/nitro-speed-2-underground.html)
- [WORD SOLITAIRE](https://thequizzone.pages.dev/word-solitaire.html)
- [SKATING PARK](https://quizverses-9d2f2.web.app/skating-park.html)
- [ELEMENTAL GLOVES MAGIC POWER](https://quizverses.github.io/elemental-gloves-magic-power.html)
- [CATEGORY RUNNING107](https://quizverses-9d2f2.web.app/category-running107.html)
- [CATEGORY BUILDING182](https://quizverses.pages.dev/category-building182.html)
- [CATEGORY BUBBLE SHOOTER](https://quizverses.pages.dev/category-bubble-shooter.html)
- [DRUNK BUT NOT WASTED KNIGHT](https://quizverses-9d2f2.web.app/drunk-but-not-wasted-knight.html)
- [CRAZY BUBBLE BREAKER](https://quizverses-9d2f2.web.app/crazy-bubble-breaker.html)
- [BLACK PINK HALLOWEEN CONCERT](https://quizverses-9d2f2.web.app/black-pink-halloween-concert.html)
- [2048 MERGE CIRCLE](https://quizverses-9d2f2.web.app/2048-merge-circle.html)
- [CATEGORY HUNTING16](https://quizverses.github.io/category-hunting16.html)
- [CATEGORY MEDIEVAL15](https://quizverses.pages.dev/category-medieval15.html)
- [CATEGORY FREE RAGDOLL GAMES](https://studyquests.github.io/category-free-ragdoll-games.html)
- [PIXEL SHOOT](https://studyquests.github.io/pixel-shoot.html)
- [SNIPER 3D ZOMBIE](https://studyquests.github.io/sniper-3d-zombie.html)
- [CATEGORY SIMULATION](https://studyquests.github.io/category-simulation.html)
- [VEX HYPER DASH](https://quizverses.github.io/vex-hyper-dash.html)
- [CATEGORY WEB PROXY](https://studyquests.github.io/category-web-proxy.html)
- [STICKMAN IN SPACE](https://studyquests.github.io/stickman-in-space.html)
- [TILE FARM STORY MATCHING GAME](https://quizverses.github.io/tile-farm-story-matching-game.html)
- [CATEGORY BATTLE GAMES](https://quizverses.github.io/category-battle-games.html)
- [CATEGORY PUZZLE](https://quizverses-9d2f2.web.app/category-puzzle.html)
- [CATEGORY SECURLY BYPASS](https://studyquests.github.io/category-securly-bypass.html)
- [ONLINE PORTAL](https://cryptotify.github.io/)
- [SUPER TANK WRESTLE](https://quizverses.pages.dev/super-tank-wrestle.html)
- [CATEGORY UNBLOCKED](https://studyquests.github.io/category-unblocked.html)
- [TERMS](https://studyquests.github.io/terms.html)
- [CUTE SHEEP SKYBLOCK](https://studyquests.github.io/cute-sheep-skyblock.html)
- [CATEGORY FOOTBALL](https://studyquests.github.io/category-football.html)
- [ROPE SORTING](https://studyquests.github.io/rope-sorting.html)
- [SITEMAP](https://cryptotify9.onrender.com/sitemap.html)
- [K POP HUNTER FASHION](https://quizverses.github.io/k-pop-hunter-fashion.html)
- [INDEX6](https://quizverses.github.io/index6.html)
- [NEW YEAR MAKEUP TRENDS](https://studyquests.github.io/new-year-makeup-trends.html)
- [SNAP FIX](https://studyquests.github.io/snap-fix.html)
- [BALLPOINT](https://quizverses-9d2f2.web.app/ballpoint.html)
- [PRIVACY](https://cryptotify9.onrender.com/privacy.html)
- [PRIVACY](https://cryptotify.pages.dev/privacy.html)
- [BLOXORZ BLOCK PUZZLE 3D](https://quizverses.github.io/bloxorz-block-puzzle-3d.html)
- [INDEX11](https://quizverses.pages.dev/index11.html)
- [PRIVACY](https://cryptotify.vercel.app/privacy.html)
- [CATEGORY GUN238](https://studyquests.github.io/category-gun238.html)
- [INDEX3](https://quizverses.github.io/index3.html)
- [NEKOS ADVENTURE](https://studyquests.github.io/nekos-adventure.html)
- [PLANE CRASH RAGDOLL SIMULATOR](https://studyquests.github.io/plane-crash-ragdoll-simulator.html)
- [IMPOSTOR AMONG SPACE](https://studyquests.github.io/impostor-among-space.html)
- [MART PUZZLE SHOPPING SORT](https://quizverses.github.io/mart-puzzle-shopping-sort.html)
- [INDEX5](https://quizverses.github.io/index5.html)
- [BOLTS AND NUTS PUZZLE](https://quizverses.github.io/bolts-and-nuts-puzzle.html)
- [LAST TO LEAVE CIRCLE OBBY](https://studyquests.github.io/last-to-leave-circle-obby.html)
- [BROOMCRAFT MYSTIC EVASION](https://studyquests.github.io/broomcraft-mystic-evasion.html)
- [GIN RUMMY](https://quizverses.github.io/gin-rummy.html)
- [ZOMBIE DEFENSE WAR](https://studyquests.github.io/zombie-defense-war.html)
- [CATEGORY HALLOWEEN45](https://studyquests.github.io/category-halloween45.html)
- [CATEGORY CASUAL 8](https://quizverses-9d2f2.web.app/category-casual-8.html)
- [ANTISTRESS SIMULATOR OF SEQUINS DIY](https://studyquests.github.io/antistress-simulator-of-sequins-diy.html)
- [CATEGORY ADVENTURE 3](https://studyquests.github.io/category-adventure-3.html)
- [TERMS](https://cryptotify9.onrender.com/terms.html)
- [SITEMAP](https://cryptotify.netlify.app/sitemap.html)
- [INDEX8](https://quizverses.github.io/index8.html)
- [DEAD FACES CLONE ONLINE](https://studyquests.github.io/dead-faces-clone-online.html)
- [TERMS](https://cryptotify.github.io/terms.html)
- [CATEGORY RAGDOLL57](https://studyquests.github.io/category-ragdoll57.html)
- [VOLLEY BEAN](https://studyquests.github.io/volley-bean.html)
- [CHAMPIONS FC](https://studyplaying.github.io/champions-fc.html)
- [CATEGORY TOP DOWN251](https://quizverses-9d2f2.web.app/category-top-down251.html)
- [SOCCER DUEL](https://quizverses-9d2f2.web.app/soccer-duel.html)
- [TILE FRUITS](https://studyquests.github.io/tile-fruits.html)
- [TERMS](https://cryptotify.pages.dev/terms.html)
- [WORD SEARCH WITH HINTS](https://studyquests.github.io/word-search-with-hints.html)
- [CATEGORY THINKY 2](https://studyquesthub.web.app/category-thinky-2.html)
- [CATEGORY MATCH 3 2](https://studyplaying.github.io/category-match-3-2.html)
- [EMOJI FRENZY](https://studyquesthub.web.app/emoji-frenzy.html)
- [SLINGER BLOCK](https://studyquesthub.web.app/slinger-block.html)
- [SISYPHUS SIMULATOR](https://studyquests.github.io/sisyphus-simulator.html)
- [CATEGORY MOUSE1 707](https://quizverses-9d2f2.web.app/category-mouse1-707.html)
- [INDEX21](https://studyquests.github.io/index21.html)
- [TERMS](https://brainquests.onrender.com/terms.html)
- [HIDDEN OBJECTS](https://studyquests.github.io/hidden-objects.html)
- [MINI SHOOTERS](https://quizverses-9d2f2.web.app/mini-shooters.html)
- [LOOP SURVIVORS ZOMBIE CITY](https://studyquests.pages.dev/loop-survivors-zombie-city.html)
- [MOB RUSH](https://studyquests.pages.dev/mob-rush.html)
- [ZIG SNAKE](https://studyquesthub.web.app/zig-snake.html)
- [CATEGORY AGILITY](https://quizverses.pages.dev/category-agility.html)
- [CATEGORY MAKEUP](https://studyquesthub.web.app/category-makeup.html)
- [SWEET DESSERT HOLE](https://studyquests.github.io/sweet-dessert-hole.html)
- [QUIZ MASTER](https://quizverses.pages.dev/quiz-master.html)
- [STICKMAN ARCHER SHOOTING ARROWS AT REDS](https://quizverses.pages.dev/stickman-archer-shooting-arrows-at-reds.html)
- [ONLINE PORTAL](https://brainquests.netlify.app/)
- [CATEGORY TOP DOWN251](https://studyquests.github.io/category-top-down251.html)
- [PRIVACY](https://cryptotify.web.app/privacy.html)
- [SLIDE RABBIT](https://studyquests.github.io/slide-rabbit.html)
- [CATEGORY STICKMAN 2](https://studyquesthub.web.app/category-stickman-2.html)
- [CATEGORY PLATFORM260](https://studyplayings.web.app/category-platform260.html)
- [BLOCK BUILDER JAM](https://studyquests.github.io/block-builder-jam.html)
- [WILD RACE MASTER 3D](https://studyquests.pages.dev/wild-race-master-3d.html)
- [GOODS TRIPLE MATCH 3D](https://quizverses-9d2f2.web.app/goods-triple-match-3d.html)
- [TANKGANK COM](https://studyplayings.web.app/tankgank-com.html)
- [CATEGORY BUBBLE SHOOTER](https://studyplayings.web.app/category-bubble-shooter.html)
- [CATEGORY BOARDGAMES](https://studyplayings.web.app/category-boardgames.html)
- [PURRFECT SCOOPS](https://quizverses.pages.dev/purrfect-scoops.html)
- [LAMPHEAD](https://studyquests.github.io/lamphead.html)
- [FAMILY SQUID CHALLENGE](https://studyquesthub.web.app/family-squid-challenge.html)
- [CATEGORY SOCCER](https://studyquests.github.io/category-soccer.html)
- [FURRY KUNG FU](https://studyquesthub.web.app/furry-kung-fu.html)
- [SITEMAP](https://brainquests.github.io/sitemap.html)
- [ZUMBLE STORY](https://studyquests.github.io/zumble-story.html)
- [CATEGORY FREE RAGDOLL GAMES](https://studyplayings.web.app/category-free-ragdoll-games.html)
- [SPRING MAGIC ENCHANTED WARDROBE](https://studyquests.pages.dev/spring-magic-enchanted-wardrobe.html)
- [RACING GAME KING HP](https://quizverses.github.io/racing-game-king-hp.html)
- [BUS ESCAPE CLEAR JAM](https://studyplaying.github.io/bus-escape-clear-jam.html)
- [INDEX2](https://studyplayings.web.app/index2.html)
- [CAT EVOLUTION 2](https://quizverses.github.io/cat-evolution-2.html)
- [CATEGORY BIKE 2](https://studyplayings.web.app/category-bike-2.html)
- [MONSTER DUELIST](https://studyquesthub.web.app/monster-duelist.html)
- [CATEGORY MEDIEVAL15](https://studyquests.github.io/category-medieval15.html)
- [FAMILY TREE EMOJI](https://studyquests.github.io/family-tree-emoji.html)
- [PUSH TO GO](https://studyplaying.github.io/push-to-go.html)
- [ARCHERY RAGDOLL](https://learnquester.github.io/archery-ragdoll.html)
- [CATEGORY CASUAL971](https://quizverses-9d2f2.web.app/category-casual971.html)
- [CATEGORY UNBLOCKERS](https://learnquester.github.io/category-unblockers.html)
- [CATEGORY BATTLE523](https://studyquests.github.io/category-battle523.html)
- [WORD SCRAMBLE FAMILY TALES](https://studyquesthub.web.app/word-scramble-family-tales.html)
- [AIRPORT MASTER PLANE TYCOON](https://learnquester.github.io/airport-master-plane-tycoon.html)
- [FLOWER FAIRY ADVENTURE STORY](https://thelearnquester.web.app/flower-fairy-adventure-story.html)
- [SUPER STAR ANIMAL SALON](https://thelearnquester.web.app/super-star-animal-salon.html)
- [MERGE TIKTOK GRAVITY KNIFE](https://quizverses.github.io/merge-tiktok-gravity-knife.html)
- [FOOTBALL HEADS 2026](https://learnquesters.pages.dev/football-heads-2026.html)
- [CATEGORY SKILL254](https://studyplaying.github.io/category-skill254.html)
