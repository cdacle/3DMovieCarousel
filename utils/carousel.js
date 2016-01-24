// Handlers for the carousel animation

var carousel;
var currPanel = 0;

//--------------------------------------
// Update the displayed movie info
//--------------------------------------
function updateMovieInfo() {
    movieValue = carousel.element.children[currPanel].getAttribute('movie')
    releaseValue = carousel.element.children[currPanel].getAttribute('release')
    ratingValue = carousel.element.children[currPanel].getAttribute('rating')
    directorValue = carousel.element.children[currPanel].getAttribute('director')
    starsValue = carousel.element.children[currPanel].getAttribute('stars')

    titleElement = document.getElementById('title');
    titleElement.innerHTML = "<div><p>" + movieValue + "</p><p></p></div>";
    releaseElement = document.getElementById('ReleaseDatefieldvalue');
    releaseElement.innerHTML = "<div><p>" + releaseValue + "</p><p></p></div>";
    ratingElement = document.getElementById('Ratingfieldvalue');
    ratingElement.innerHTML = "<div><p>" + ratingValue + "</p><p></p></div>";
    directorElement = document.getElementById('Directorfieldvalue');
    directorElement.innerHTML = "<div><p>" + directorValue + "</p><p></p></div>";
    starsElement = document.getElementById('Starsfieldvalue');
    starsElement.innerHTML = "<div><p>" + starsValue + "</p><p></p></div>";
}

//--------------------------------------
// Given the scroll direction, update the displayed movie info 
//--------------------------------------
function updateDisplayInfo(increment) {
    if (increment == -1) {
        // go previous
        currPanel = currPanel == 0 ? movieCount - 1 : currPanel - 1;
    } else if (increment == 1) {
        // go next
        currPanel = currPanel == movieCount - 1 ? 0 : currPanel + 1;
    }

    carousel.rotation += carousel.theta * increment * -1;
    carousel.transform();

    updateMovieInfo();

    $(function () {
        $('#title').fadeOut(0, function () {
            $('#title').fadeIn(500);
        });
        $('#movie').fadeOut(0, function () {
            $('#movie').fadeIn(500);
        });
    });
}

//--------------------------------------
// Handle left/right, page up/down
//--------------------------------------
var keyDownHandler = function (e) {
    increment = 0;
    // left arrow or page up
    if (e.keyCode == 37 || e.keyCode == 33) {
        increment = -1;
        // right arrow or page down
    } else if (e.keyCode == 39 || e.keyCode == 34) {
        increment = 1;
    }

    updateDisplayInfo(increment);
};

window.addEventListener('keydown', keyDownHandler, false)

//--------------------------------------
// Handle mouse scroll wheel
//--------------------------------------
var timeout;
var handleMouseWheelEvent = true;
window.addEventListener('mousewheel', function () {
    if (handleMouseWheelEvent) {
        // cross-browser wheel delta
        var e = window.event || e; // old IE support
        var increment = Math.max(-1, Math.min(1, (-e.wheelDelta || e.detail)));

        updateDisplayInfo(increment);

        handleMouseWheelEvent = false;
        clearTimeout(timeout);
        setTimeout(function () {
            handleMouseWheelEvent = true;
        }, 250);
    }
    if (evt.preventDefault)
        evt.preventDefault();
    else
        return false;
}, false);


//==================================================================================================================
// The following Carousel3D code is taken and adapted from http://desandro.github.io/3dtransforms/docs/carousel.html
//
// The MIT License (MIT)
// Copyright © 2016 David DeSandro
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
// (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, 
// merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished 
// to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
// OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
// LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
// IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
//--------------------------------------------------------------------------
// BEGIN sample Carousel3D code
//
var transformProp = Modernizr.prefixed('transform');

function Carousel3D(el) {
    this.element = el;
    this.rotation = 0;
    this.theta = 0;
}

Carousel3D.prototype.modify = function () {
    var panel, angle, i;

    this.panelSize = this.element['offsetWidth'];
    this.theta = 360 / movieCount;

    // do some trig to figure out how big the carousel
    // is in 3D space
    this.radius = Math.round((this.panelSize / 2) / Math.tan(Math.PI / movieCount));

    for (i = 0; i < movieCount; i++) {
        panel = this.element.children[i];
        angle = this.theta * i;
        panel.style.opacity = 1;
        panel.style[transformProp] = 'rotateY(' + angle + 'deg) translateZ(' + this.radius + 'px)';
    }

    // adjust rotation so panels are always flat
    this.rotation = Math.round(this.rotation / this.theta) * this.theta;

    this.transform();
};

Carousel3D.prototype.transform = function () {
    // push the carousel back in 3D space,
    // and rotate it
    this.element.style[transformProp] = 'translateZ(-' + this.radius + 'px) rotateY(' + this.rotation + 'deg)';
};

var init = function () {
    carousel = new Carousel3D(document.getElementById('carousel'));

    // populate on startup
    carousel.modify();

    updateMovieInfo();

    setTimeout(function () {
        document.body.addClassName('ready');
    }, 0);
};

window.addEventListener('DOMContentLoaded', init, false);
//
// END sample Carousel3D code
//--------------------------------------------------------------------------


