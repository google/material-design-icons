## Material Icons / Material Symbols

These are two different official icon sets from Google. Material Icons is the classic set, while Material Symbols was introduced in April 2022, built on variable font technology.

The icons can be browsed in a more user-friendly way at https://fonts.google.com/icons (use the popdown menu near top left to choose between the two sets, Material Symbols is the default).

The icons are designed under the [material design guidelines](https://material.io/guidelines/).

### Material Icons

The icons can be browsed in a more user-friendly way at https://fonts.google.com/icons?icon.set=Material+Icons

These classic icons are available in five distinct styles:
- Outlined
- Filled
- Rounded
- Sharp
- Two tone

Additionally, there are several fonts available, each corresponding to one of the sets above:
- Material Icons (the filled style)
- Material Icons Outlined
- Material Icons Round
- Material Icons Sharp
- Material Icons Two Tone

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

### Material Symbols

These newer icons can be browsed in a more user-friendly way at https://fonts.google.com/icons. (Use the popdown menu near top left to choose between the two sets, Material Symbols is the default).

These icons were built/designed as variable fonts first (based on the 24 px designs from Material Icons). There are three separate Material Symbols variable fonts:
- Outlined
- Rounded
- Sharp
- (although there is no separate Filled font, the Fill axis allows access to filled styles on all three fonts.)

Each of the fonts has these design axes, which can be varied in CSS, or in many more modern design apps:
- Optical Size (opsz) from 20 to 48 px. The default is 24.
- Weight from 100 (Thin) to 700 (Bold). Regular is 400.
- Grade from -50 to 200. The default is 0 (zero).
- Fill from 0 to 100. The default is 0 (zero).

The following directories in this repo contain specifically Material Symbols (not Material Icons) content:
- symbols
- variablefont

What is currently _not_ available in Material Symbols?
- sizes other than 24 are not designed with perfect pixel-grid alignment
- the only pre-made fonts are the variable fonts
- there are no two-tone icons

### 4.0.0 Update

Restructured repository, updated assets.

### 3.0.1 Update

* Changed license in package.json.
* Added missing device symbol sprites.

### 3.0.0 Update

License change to Apache 2.0!

## Getting Started

Read the [developer guide](https://google.github.io/material-design-icons/) on how to use the material design icons in your project.

### Using a font

The `font` folder contains pre-generated font files that can be included in a project. This is especially convenient for the web; however, it is generally better to link to the web font hosted on Google Fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Material+Icons"
      rel="stylesheet">
```

Read more in the [font portion](https://google.github.io/material-design-icons/#icon-font-for-the-web) of our full developer guide.


## License

We have made these icons available for you to incorporate into your products under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt). Feel free to remix and re-share these icons and documentation in your products.
We'd love attribution in your app's *about* screen, but it's not required.
