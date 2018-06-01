console.log("YOOOOOOOOOOOOOOO referneces.js");

var animation = function() {
    var fadeOutFrame = -1;
    var fadeOutElement = null;
    var fadeOutTime = null;
    var fadeOutId = -1;
    var fadeOutAnimationFrame = 0;
    
    function privateFadeOut(event) {
        if (fadeOutFrame == -1) {
            fadeOutFrame = 1.0;
            fadeOutElement = this;
            fadeOutId += 1;
            fadeOutAnimationFrame = 0;
        }
        var timeDelta = Date.now() - fadeOutTime;
        if (timeDelta > 5) {
            fadeOutTime = Date.now();
            fadeOutElement.style.opacity = fadeOutFrame;
            fadeOutFrame -= 0.05;
        }
        if (fadeOutFrame > 0.0) {
            window.requestAnimationFrame(privateFadeOut)
            console.log( "" + fadeOutId + " frame: " + fadeOutAnimationFrame++ + " opacitiy: " + fadeOutFrame);
        } else {
            fadeOutElement.style.opacity = 0.0;
            fadeOutFrame = -1;
            console.log( "" + fadeOutId + " frame: " + fadeOutAnimationFrame++ + " opacitiy: " + fadeOutFrame);
        }
    }
    
    var fadeInFrame = -1;
    var fadeInElement = null;
    var fadeInTime = null;
    var fadeInId = -1;
    var fadeInAnimationFrame = 0;

    function privateFadeIn(event) {
        if (fadeInFrame == -1) {
            fadeInFrame = 0.0;
            fadeInElement = this;
            fadeInId += 1;
            fadeInAnimationFrame = 0;
        }
        var timeDelta = Date.now() - fadeInTime;
        if (timeDelta > 5) {
            fadeInTime = Date.now();
            fadeInElement.style.opacity = fadeInFrame;
            fadeInFrame += 0.05;
        }
        if (fadeInFrame < 1.0) {
            window.requestAnimationFrame(privateFadeIn)
            console.log( "" + fadeInId + " frame: " + fadeInAnimationFrame++ + " opacitiy: " + fadeInFrame);
        } else {
            fadeInElement.style.opacity = 1.0;
            console.log( "" + fadeInId + " frame: " + fadeInAnimationFrame++ + " opacitiy: " + fadeInFrame);
            
            // cleaning the fields
            fadeInFrame = -1;
        }
    }

    return {
        // public funtions
        fadeOut: privateFadeOut,
        fadeIn: privateFadeIn
    }
}();

/*
var refImage = document.getElementById('ref_image_1');
refImage.onmouseover = animation.fadeOut;
refImage.onmouseout = animation.fadeIn;
console.log("references.js script initialized");
*/

// jquery approach

$( window ).on("load", function() {
    console.log("window loaded in jquery initializer");
    console.log("test");
    $("#ref_image_1").on("click", function() {
        var opac = this.style.opacity;
        if (opac == 0) {
            opac = 0;
            this.style.opacity = 1; 
        } else { 
            opac = 1;
            this.style.opacity = 0;
        }
        this.animate(
            {
                opacity: "0.0",
            },
            1000,
            function() {
                console.log("animation complete");
            }
        )
    });
    console.log("jquery image listener initialized");
});
