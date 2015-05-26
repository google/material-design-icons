# Material design icons

Material design icons are the official [icon set](http://www.google.com/design/spec/style/icons.html#icons-system-icons) from Google that are designed under the [material design guidelines](http://www.google.com/design/spec).

We have made these icons available for you to incorporate them into your
products under the [Creative Common Attribution 4.0 International License (CC-BY 4.0)](http://creativecommons.org/licenses/by/4.0/). Feel free to remix and re-share these icons and documentation in your
products.  We'd love attribution in your app's *about* screen, but it's not required. The only thing we ask is that you not re-sell
the icons themselves.

## What's included?

* SVG versions of all icons in both 24px and 48px flavours
* 1x, 2x icons targeted at the Web (PNG)
* 1x, 2x, 3x icons targeted at iOS (PNG)
* Hi-dpi versions of all icons (hdpi, mdpi, xhdpi, xxhdpi, xxxhdpi) for Android (PNG)
* SVG and CSS sprites of all icons

A live [preview](http://google.github.io/material-design-icons/)  of the icon set is available.

## Getting started

You have a few options for getting the icons.

### Download all the icons

Choose either:

  * Latest stable [zip archive (v1.0.1)](https://github.com/google/material-design-icons/releases/download/1.0.1/material-design-icons-1.0.1.zip)
  * Bleeding-edge [zip archive (master)](https://github.com/google/material-design-icons/archive/master.zip)

### Bower

Install the icons using the [Bower](http://bower.io) package manager.

```sh
$ bower install material-design-icons
```

### npm

You can also find all the icons on [npm](http://npmjs.org).

```sh
$ npm install material-design-icons
```

## Usage

Take a look at the included `index.html` file for a preview of all icons included in the set. You are free to use the icons in the way that makes most sense to your project.

## Structure

### Icons

In general, an icon category (e.g `action`) will include the following directories, containing multiple resolutions of our icons.

* 1x, 2x Web
* 1x, 2x, 3x iOS
* drawable hdpi, mdpi, xhdpi, xxhdpi, xxxhdpi
* SVG

Decide on the icon resolution required for your project and copy, then reference the icons you wish to use.

### Using sprite sheets

In `css-sprite` and `svg-sprite` are pre-generated sprite sheets. Instructions for using them are in the [sprites documentation](https://github.com/google/material-design-icons/tree/master/sprites).

## Polymer icons

If you wish to use the icon set with Polymer, we recommend consuming them via the [`<core-icons>`](https://github.com/Polymer/core-icons) element.


## License

All icons are released under an [Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license.
