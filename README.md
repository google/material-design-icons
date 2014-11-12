# Material Design Icons

Material Design Icons are the official open-source [icons](http://www.google.com/design/spec/resources/sticker-sheets.html#sticker-sheets-components) featured in the Google [Material Design](http://www.google.com/design/spec) specification.

## What's included?

* SVG versions of all icons in both 24px and 48px flavours
* SVG and CSS sprites of all icons
* 1x, 2x icons targeted at the Web (PNG)
* 1x, 2x, 3x icons targeted at iOS (PNG)
* Hi-dpi versions of all icons (hdpi, mdpi, xhdpi, xxhdpi, xxxhdpi) (PNG)

A live [preview](http://google.github.io/material-design-icons/)  of the icon set is available.

## Getting Started

You have a few options for getting the icons.

### Download the Zip

Grab the latest stable [zip archive](https://github.com/google/material-design-icons/releases/download/1.0.1/material-design-icons-1.0.1.zip) (~57MB) of all icons or the bleeding-edge version from [master](https://github.com/google/material-design-icons/archive/master.zip).

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
* svg

Decide on the icon resolution required for your project and copy, then reference the icons you wish to use.


### Spritesheets

Material Design icons come with SVG and CSS sprites for each category of icon we include. These can be found in the `sprites` directory, under `svg-sprite` and `css-sprite`.

#### Using CSS Sprites

To use a CSS spritesheet, reference the stylesheet for the icon category you wish to use, then include the icon definition in your markup. E.g to use one of the play icons in `css-sprite-av`:

Reference the stylesheet:

```html
	<link href="css-sprite/sprite-av-black.css" rel="stylesheet">
```

Create an element which will use the icon as a background:

```html
	<div></div>
```

Add a class referencing the `icon` spritesheet and specific icon `icon-ic_play_circle_outline_black_24dp`, which you can get from the above stylesheet.

```html
	<div class="icon icon-ic_play_circle_outline_black_24dp"></div>
```

That's it!

Don't forget to publish the corresponding CSS and SVG/PNG files when deploying your project.

#### Using SVG Sprites

Similarly, to use an SVG spritesheet, reference the stylesheet for the icon category, then include the icon definition in your markup.

E.g: to use one of the play icons in `svg-sprite-av`, reference the stylesheet:

```html
	<link href="svg-sprite/svg-sprite-av.css" rel="stylesheet">
```

Create an element which will use the icon as a background:

```html
	<div></div>
```

Next, make sure to set a dimension for the icon. This can either be done inline or via a class. We'll use a class for this example:

```html
	<style>
		.svg-ic_play_circle_outline_24px-dims { width: 24px; height: 24px; }
	</style>
```

Finally, set the dimension and specific icon `svg-ic_play_circle_outline_24px`, which you can get from the above stylesheet.

```html
	<div class="svg-ic_play_circle_outline_24px svg-ic_play_circle_outline_24px-dims"></div>
```


## Licence

All icons are released under an [Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license.
