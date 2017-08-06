# Material design icons
[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg?style=flat-square)](https://github.com/google/material-design-icons/blob/master/LICENSE)

Material design icons are the official [icon set](http://www.google.com/design/spec/style/icons.html#icons-system-icons) from Google that are designed under the [material design guidelines](http://www.google.com/design/spec).

### 3.0.1 Update

* Changed license in package.json.
* Added missing device symbol sprites.

### 3.0.0 Update

License change to Apache 2.0!

## Getting Started

Read the [developer guide](http://google.github.io/material-design-icons/) on how to use the material design icons in your project.

### Using a font collection

The `iconfont` folder contains pre-generated font files that can be included in a project. This is especially convenient for the web; however, it is generally better to link to the web font hosted on Google Fonts:

```html
<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
```

Read more in the [font portion](http://google.github.io/material-design-icons/#icon-font-for-the-web) of our full developer guide.

### Using symbols and sprites

The `css-sprite` and `svg-sprite` folders contain pre-generated sprite sheets, as well as svg symbols that can be `<use>`d more directly and with fewer constraints. Instructions for using them are in the [sprites documentation](https://github.com/google/material-design-icons/tree/master/sprites).

## Polymer icons

If you wish to use the icon set with Polymer, we recommend consuming them via the [`<iron-icons>`](https://github.com/polymerelements/iron-icons) element ([`<core-icons>`](https://github.com/Polymer/core-icons) in v0.5).
