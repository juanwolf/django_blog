var staticPath = "./juanwolf_fr/static/";
var jsPath = staticPath + "js/";
var cssPath = staticPath + "stylesheets/";
var cssStylesheet = cssPath + 'stylesheet.css';
var scssMainFile = cssPath + 'stylesheet.scss';
var bowerConcatFile = jsPath + "bower.js",
    bowerCssFile = cssPath + "bower.css",
    indexFile = jsPath + "index.js",
    mainFile = jsPath + "main.js",
    minMainFile = jsPath + "main.min.js";


module.exports = function(grunt) {

    grunt.initConfig({
        bower_concat: {
            all: {
                dest: {
                    "js": "juanwolf_fr/static/js/bower-concat.js",
                    "css": "juanwolf_fr/static/stylesheets/bower.css",
                },

            }
        },
        concat: {
            dist: {
                src: [
                    "./juanwolf_fr/static/js/bower-concat.js",
                    "./juanwolf_fr/static/js/index.js"
                ],
                dest: "./juanwolf_fr/static/js/main.js"

            }
        },
        uglify: {
            build: {
                src: "./juanwolf_fr/static/js/main.js",
                dest: "./juanwolf_fr/static/js/main.min.js"
            }
        },
        sass: {
            dist: {                            // Target
                options: {                       // Target options
                    style: 'compressed'
                },
                files: {                         // Dictionary of files
                    // 'destination': 'source'
                    "./juanwolf_fr/static/stylesheets/stylesheet.css":"./juanwolf_fr/static/stylesheets/stylesheet.scss"
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-bower-concat');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.registerTask('default', ['bower_concat', 'concat', 'uglify', 'sass']);
}
