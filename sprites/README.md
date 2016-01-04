# Material icon sprites

Sprite images allow you to use images more efficiently.
Our recommended way to use sprites is to create a single SVG file with the subset of icons needed for the project compiled as symbols.
This will keep the file small and allow for the greatest flexibility in referencing each icon.
It will also allow you to include any other svgs in the project, like a logo, in a single reference file.

Note that symbol files must be `<use>`ed or opened in an editor in order to be viewed, while sprite sheets can be opened and previewed directly.

## Creating your own sprites

While PNG and SVG icon images can be combined manually in an editor, using a processor to combine them automatically and generate any needed companion files is definitely the most convenient.
Here are three good options for creating your own CSS and SVG sprites.

 * [Sprity](https://www.npmjs.com/package/sprity) (previously css-sprite) for PNG sprites with CSS sprite sheets.
 * [svg-sprite](https://www.npmjs.com/package/svg-sprite) for SVG sprites with CSS sprite sheets.
 * [svgstore](https://github.com/w0rm/gulp-svgstore) for SVG symbol sprites.

When creating a project, there are many similar and extended processors that can be for compilers such as gulp.

## Using the provided sprites

Material design icons come with CSS sprite sheets and SVG symbol sprites for each category of icon we include.
The icon sprites can be found in the `sprites` directory under `css-sprite` for png image sprites and `svg-sprite` for the various svg sprite techniques—including symbols.
Symbol sprites in the `svg-sprite` folder have an additional `-symbol` marker after their name.
If you are considering using svg sprites, you are encouraged to `<use>` the symbol sprites rather than traditional sprite sheets as they reduce the size of the files and the complexity and redundancy of using them.


## Using SVG symbol sprites

To add an icon using symbol sprites, you will need to add an svg element that `<use>`es the reference file with a link to the specific icon you want.
Since the icons are stored as `<symbol>`s, the viewbox is already set up and can be scaled relatively without needing to keep adjacent symbols in mind. You will only need set the size of the icon using CSS:

```CSS
.svg-24px {
  width: 24px;
  height: 24px;
}
```

Then reference the id for the icon you need:

```HTML
<svg class="svg-24px">
  <use xlink:href="MaterialIcons.svg#ic_face_24px"></use>
</svg>
```

The HTML can also be simplified further by targeting all svg tags, and then overriding the size for individual classes and IDs.
While you will need to be careful not to let this hamper your layout, this kind of sizing is generally a matter of course.
To make 24px the default for `<svg>` tags, add the tag properties in css:

```CSS
svg {
  width: 24px;
  height: 24px;
}
```

Then reference the icon:

```HTML
<svg><use xlink:href="MaterialIcons.svg#ic_face_24px"></use></svg>
```

### Stacking symbol sprite icons

Using symbol sprites, icons can also easily be stacked on top of each other by including them in a single svg `<use>` statement.
Each icon can then be referenced using ids and classes and likewise handled using javascript.
E.g. To add a blue checkmark on top of a checkbox outline than can then be hidden when needed, first add the fill property in CSS:

```CSS
.svg-24px {
  width: 24px;
  height: 24px;
}
.check {
  fill: blue;
}
```

Then add the check after the outline icon together with an id for the SVG tag (for targeting) and the check class for the checkmark:

```HTML
<svg class="svg-24px" id="checkbox-1">
  <use xlink:href="MaterialIcons.svg#ic_check_box_outline_blank"></use>
  <use class="check" xlink:href="MaterialIcons.svg#ic_check_box"></use>
</svg>

```

### External SVG symbols

The benefits to referencing an external svg come in the form of caching, as the same map file can be reused across the site and on subsequent visits.

Unfortunately, Internet Explorer, Edge, and older Android and iOS browsers cannot `<use>` external svg files.
Besides copying the svg file contents directly into each html file you need them in, there are two good ways to handle this:

 1. Use the [svg4everybody polyfill](https://github.com/jonathantneal/svg4everybody) (this is the preferred method)
 2. Use a simple AJAX call to include the symbol sprites in the document for all browsers, and then reference the svg directly wherever it is `<use>´d rather than the external file

### CSS Selectors, Transformation and the Shadow DOM

For some projects, parts of individual icons may be required to change or animate in some way relative to the icon, rather than as a whole. For example, an icon where the top part flies away or two parts are given separate colors. This is the power given to inline svg, as opposed to a simple image file.

Browser support for the `<use>` element, however, is still not good enough to properly allow the targeting of its shadow DOM. While not impossible, it can make selecting individual paths on a page very tricky.

In projects where individual paths need to be targeted, it is best to copy them inline or inject the paths into the html at build or load time, regardless of browser, to prevent issues that may arise due to the shadow DOM nature of the `<use>` element. There are two ways to handle this depending on the project:
 1. The recommended way to do this is automatically using a build script or with a tool like [gulp-inject](https://github.com/klei/gulp-inject) that can reference individual icons, as that will keep the html files small and prevent having to make an href request.
 2. If the project is designed to generate all pages dynamically using very few static elements, or none at all, the svg elements can instead be pulled in using javascript ajax calls. In this case, a purely concatenated xml file containing the individual icons required would work better and be easier to target than a symbol map.

## Using CSS sprite sheets

To use a CSS sprite sheet, reference the stylesheet for the icon category you wish to use, then include the icon definition in your markup.
E.g. using one of the play icons in `css-sprite-av`...

Reference the stylesheet:

```html
<link href="png/sprite-av-black.css" rel="stylesheet">
```

Create an element which will use the icon as a background, and include that icon as a class.
The example class here references the `icon` sprite sheet and specific `icon-ic_play_circle_outline_black_24dp` icon, which you can get from the above stylesheet.

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