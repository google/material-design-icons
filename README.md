# Material Design Icons

Material Design Icons are the official open-source icons featured in the Google [Material Design](http://www.google.com/design/spec) specification. 

## What's included?

* SVG versions of all icons in both 24px and 48px flavours
* SVG and CSS sprites of all icons
* 1x, 2x icons targeted at the Web (PNG)
* 1x, 2x, 3x icons targeted at iOS (PNG)
* Hi-dpi versions of all icons (hdpi, mdpi, xhdpi, xxhdpi, xxxhdpi) (PNG)


## Getting Started

You have a few options for getting the icon set.

### Download the Zip

Grab the latest [zip archive](https://github.com/google/material-design-icons/archive/master.zip) of all icons. 

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

## Structure

### Icons

In general, an icon category (e.g `action`) will include the following directories, containing multiple resolutions of our icons.

* 1x, 2x Web
* 1x, 2x, 3x iOS
* drawable hdpi, mdpi, xhdpi, xxhdpi, xxxhdpi
* svg

Decide on the icon resolution required for your project and copy, then reference the icons you wish to use.


### Spritesheets

Material Design icons come with SVG and CSS sprites for each category of icon we include. These can be found in the `sprites` directory, under the `svg-sprite` and `css-sprite` sub-directories.

#### Using CSS Sprites

To use a CSS spritesheet, reference the stylesheet for the icon category you wish to use, then include the icon definition in your markup. 

E.g: to use one of the play icons in `css-sprite-av`, we would do the following:

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



## Usage

Take a look at the included `index.html` file for a preview of all icons included in the set. You are free to use the icons in the way that makes most sense to your project.

## Licence

All icons are released under an [Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) license. 
