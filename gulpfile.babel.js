'use strict';

import _ from 'lodash';
import File from 'vinyl';
import gulp from 'gulp';
import merge from 'merge-stream';
import sprity from 'sprity';
import svgSprite from 'gulp-svg-sprite';
import through2 from 'through2';
import { humanize, titleize } from 'underscore.string';


/** Names of directories containing icons. */
const ICON_CATEGORIES = [
  'action',
  'alert',
  'av',
  'communication',
  'content',
  'editor',
  'file',
  'hardware',
  'image',
  'maps',
  'navigation',
  'notification',
  'places',
  'social',
  'toggle',
];


/** Standard PNG colors. */
const PNG_COLORS = [
  'black',
  'white',
];


/**
 * Generates PNG sprites and their corresponding CSS files for each category of
 * icon, and places them in `sprites/css-sprite`.
 *
 * TODO(shyndman): Add support for double density sprites.
 */
gulp.task('png-sprites', () =>
  _(getCategoryColorPairs())
    .map(([ category, color ]) =>
      sprity.src({
        src: `./${ category }/1x_web/*_${ color }_24dp.png`,
        style: `sprite-${ category }-${ color }.css`,
        name: `sprite-${ category }-${ color }`,
        engine: 'sprity-gm',
        orientation: 'left-right'
      }))
    .thru(merge)
    .value()
    .pipe(gulp.dest('./sprites/css-sprite/')));


/**
 * Generates CSS and Symbol-based SVG sprites for each category, and places
 * them in `sprites/svg-sprite`.
 */
gulp.task('svg-sprites', () =>
  _(ICON_CATEGORIES)
    .map((category) =>
      gulp.src(`./${ category }/svg/production/*_24px.svg`)
        .pipe(svgSprite(getSvgSpriteConfig(category))))
    .thru(merge)
    .value()
    .pipe(gulp.dest('./sprites/svg-sprite')));


/**
 * Generates a file to allow the consumption of the icon font by Iconjar
 * (http://geticonjar.com/).
 */
gulp.task('iconjar', () =>
  gulp.src('./iconfont/codepoints')
    .pipe(generateIjmap('MaterialIcons-Regular.ijmap'))
    .pipe(gulp.dest('./iconfont/')));


/** Runs all tasks. */
gulp.task('default', ['png-sprites', 'svg-sprites', 'iconjar']);


/**
 * Returns a stream that transforms between our icon font's codepoint file
 * and an Iconjar ijmap.
 */
function generateIjmap(ijmapPath) {
  return through2.obj((codepointsFile, encoding, callback) => {
    const ijmap = {
      icons: codepointsToIjmap(codepointsFile.contents.toString())
    };

    callback(null, new File({
      path: ijmapPath,
      contents: new Buffer(JSON.stringify(ijmap), 'utf8')
    }));

    function codepointsToIjmap(codepoints) {
      return _(codepoints)
        .split('\n')       // split into lines
        .reject(_.isEmpty) // remove empty lines
        .reduce((codepointMap, line) => {   // build up the codepoint map
          let [ name, codepoint ] = line.split(' ');
          codepointMap[codepoint] = { name: titleize(humanize(name)) };
          return codepointMap;
        }, {});
    }
  });
}


/**
 * Returns the SVG sprite configuration for the specified category.
 */
function getSvgSpriteConfig(category) {
  return {
    shape: {
      dimension: {
        maxWidth: 24,
        maxHeight: 24
      },
    },
    mode: {
      css : {
        bust: false,
        dest: './',
        sprite: `./svg-sprite-${ category }.svg`,
        example: {
          dest: `./svg-sprite-${ category }.html`
        },
        render: {
          css: {
            dest: `./svg-sprite-${ category }.css`
          }
        }
      },
      symbol : {
        bust: false,
        dest: './',
        sprite: `./svg-sprite-${ category }-symbol.svg`,
        example: {
          dest: `./svg-sprite-${ category }-symbol.html`
        }
      }
    }
  };
}


/**
 * Returns the catesian product of categories and colors.
 */
function getCategoryColorPairs() {
  return _(ICON_CATEGORIES)
    .map((category) =>
      _.zip(_.times(PNG_COLORS.length, () => category), PNG_COLORS))
    .flatten() // flattens 1 level
    .value();
}
