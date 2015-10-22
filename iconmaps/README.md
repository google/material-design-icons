# Material Icon Symbol Map

Our recommended way to use symbol sheets is to create them with the subset of icons needed for the project. A good option for creating your own symbol map is to use [gulp-svgstore](https://github.com/w0rm/gulp-svgstore) with individual development icons. This will also allow you to include any other svgs in the project, like a logo, in a single reference file.

## Using provided symbol maps

Material design icons come with an SVG symbol map for each icon category we include. These can be found in the `iconmaps` directory. The full set of current icons is in `MaterialIcons.svg`.

To add an icon, place the following in your document wherever it is needed:

```HTML
<svg class="svg-ic_24px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink>
	<use xlink:href="svg/MaterialIcons.svg#ic_face_24px"></use>
</svg>
```

with the following css to constrain the size:

```CSS
.svg-ic_24px {
	width: 24px;
	height: 24px;
}
```

### External SVG

The benefits to referencing an external svg come in the form of caching, as the same map file can be reused across the site and on subsequent visits.

Unfortunately, Internet Explorer cannot `<use>` external svg files. There are two ways to handle this:
[1] Use the [svg4everybody polyfill](https://github.com/jonathantneal/svg4everybody)
[2] Use a simple AJAX call to include the symbol map in the document for all browsers.

### CSS Selectors, Transformation and the Shadow DOM

For some projects, parts of individual icons may be required to change or animate in some way relative to the icon, rather than as a whole. For example, an icon where the top part flies away or two parts are given separate colors. This is the power given to inline svg, as opposed to a simple image file.

Browser support for the `<use>` element, however, is still not good enough to properly allow the targeting of its shadow DOM. While not impossible, this can make selecting individual paths on a page very tricky.

In projects where individual paths need to be targeted, it is best to inject the paths into the html at build or load time, regardless of browser, to prevent issues that may arise due to the shadow DOM nature of the `<use>` element. There are two ways to handle this depending on the project:
[1] The recommended way to do this is automatically using a build script or with a tool like [gulp-inject](https://github.com/klei/gulp-inject) that can reference individual icons, as that will keep the html files small and prevent having to make an href request.
[2] If the project is designed to generate all pages dynamically using very few static elements, or none at all, the svg elements can instead be pulled in using javascript ajax calls. In this case, a purely concatenated xml file containing the individual icons required would work better and be easier to target than a symbol map.