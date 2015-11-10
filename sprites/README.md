# Material icon sprites

Sprite images allow you to use images more efficiently.
Our recommended way to use sprites is to create an SVG spritemap file with the subset of icons needed for the project.
This will also allow you to include any other svgs in the project, like a logo, in a single reference file.

These sprites may not be completely up-to-date; they will be updated periodically.
Note that spritemap files must be `<use>`ed or opened in an editor in order to be viewed.

## Creating your own sprites

Our recommended way to use sprites is to create them with the subset of icons needed for the project.
Here are three good options for creating your own CSS and SVG sprites.

 * [Sprity](https://www.npmjs.com/package/sprity) (previously css-sprite) for PNG sprites with CSS spritesheets.
 * [svg-sprite](https://www.npmjs.com/package/svg-sprite) for SVG sprites with CSS spritesheets.
 * [svgstore](https://github.com/w0rm/gulp-svgstore) for SVG spritemaps

When creating a project, there are many similar and extended processors that can be for compilers such as gulp.

## Using provided sprite sheets

Material design icons come with CSS spritesheets and SVG spritemaps for each category of icon we include.
CSS spritesheets can be found in the `sprites` directory under `png` and `svg`, and SVG spritemaps can be found under `spritemap`.
`MaterialIcons.svg` is a complete spritemap file that includes the full set of current icons for reference.
If you are considering using svg sprites, you are encouraged to `<use>` the spritemaps rather than traditional spritesheets, as they reduce the size of the files and the complexity and redundancy of using them.

### Using CSS spritesheets

To use a CSS spritesheet, reference the stylesheet for the icon category you wish to use, then include the icon definition in your markup.
E.g. using one of the play icons in `css-sprite-av`...

Reference the stylesheet:

```html
	<link href="png/sprite-av-black.css" rel="stylesheet">
```

Create an element which will use the icon as a background:

```html
	<div></div>
```

Add a class referencing the `icon` sprite sheet and specific icon `icon-ic_play_circle_outline_black_24dp`, which you can get from the above stylesheet.

```html
	<div class="icon icon-ic_play_circle_outline_black_24dp"></div>
```

That's it! Well, for PNG sprites anyway.

If you are using svg sprites by referencing `svg/sprite-av-black.css` in this example instead, you will also need to set a dimension for the icon.
This can either be done inline or via a generic size class or a specific class such as this one:

```html
	<style>
		.svg-ic_play_circle_outline_black_24dp-dims { width: 24px; height: 24px; }
	</style>
```

Then, make sure you set the dimension for the specific icon, `svg-ic_play_circle_outline_black_24dp`, which you can get from the svg stylesheet.

```html
	<div class="svg-ic_play_circle_outline_black_24dp svg-ic_play_circle_outline_black_24dp-dims"></div>
```

Don't forget to publish the corresponding CSS and SVG/PNG files when deploying your project.

### Using SVG spritemaps

To add an icon using a spritemap, you will need to add an svg element that `<use>`es the reference file with a link to the specific icon you want.
With this method, you will only need set the size of the icon using CSS.
For example:

```CSS
.svg-ic_24px {
	width: 24px;
	height: 24px;
}
```

Then reference the icon you need.
Since the icons are stored as `<symbol>`s, the viewbox is already set up and can be scaled relatively without needing to keep adjacent symbols in mind.

```HTML
<svg class="svg-ic_24px">
	<use xlink:href="MaterialIcons.svg#ic_face"></use>
</svg>
```

### External SVG symbols

The benefits to referencing an external svg come in the form of caching, as the same map file can be reused across the site and on subsequent visits.

Unfortunately, Internet Explorer, Edge, and older Android and iOS browsers cannot `<use>` external svg files.
Besides copying the svg file contents directly into each html file you need them in, there are two good ways to handle this:

[1] Use the [svg4everybody polyfill](https://github.com/jonathantneal/svg4everybody)
[2] Use a simple AJAX call to include the symbol map in the document for all browsers.

### CSS Selectors, Transformation and the Shadow DOM

For some projects, parts of individual icons may be required to change or animate in some way relative to the icon, rather than as a whole. For example, an icon where the top part flies away or two parts are given separate colors. This is the power given to inline svg, as opposed to a simple image file.

Browser support for the `<use>` element, however, is still not good enough to properly allow the targeting of its shadow DOM. While not impossible, it can make selecting individual paths on a page very tricky.

In projects where individual paths need to be targeted, it is best to copy them inline or inject the paths into the html at build or load time, regardless of browser, to prevent issues that may arise due to the shadow DOM nature of the `<use>` element. There are two ways to handle this depending on the project:
[1] The recommended way to do this is automatically using a build script or with a tool like [gulp-inject](https://github.com/klei/gulp-inject) that can reference individual icons, as that will keep the html files small and prevent having to make an href request.
[2] If the project is designed to generate all pages dynamically using very few static elements, or none at all, the svg elements can instead be pulled in using javascript ajax calls. In this case, a purely concatenated xml file containing the individual icons required would work better and be easier to target than a symbol map.