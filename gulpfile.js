var gulp = require('gulp'),
usemin = require('gulp-usemin'),
minifyCss = require('gulp-minify-css'),
minifyJs = require('gulp-uglify'),
concat = require('gulp-concat'),
rename = require('gulp-rename'),
ngAnnotate = require('gulp-ng-annotate');

var paths = {
            scripts: 'consultoria/static/angular/**/*.*',
            styles: 'consultoria/static/*.*',
            templates: 'consultoria/templates/**/*.html',
            index: 'consultoria/templates/index.html',
            bower_fonts: ['consultoria/static/fonts/**/*.{ttf,woff,woff2,eof,eot,svg}' ],
        };

gulp.task('usemin', function() {
    return gulp.src(paths.index)
        .pipe(usemin({
            js: [ngAnnotate(), minifyJs(), 'concat'],
            css: [minifyCss({keepSpecialComments: 0}), 'concat'],
            consultoriajs: [ngAnnotate(), minifyJs(), 'concat'],
            consultoriacss: [minifyCss({keepSpecialComments: 0}), 'concat'],
            outputRelativePath : '../../'
        }))
        .pipe(gulp.dest('./consultoria/templates/dist'));
});

gulp.task('build-assets', function() {
    return gulp.src(paths.bower_fonts)
        .pipe(rename({
            dirname: '/fonts'
        }))
        .pipe(gulp.dest('./consultoria/static/dist'));
});


gulp.task('default', ['usemin','build-assets']);
