(function() {

    document.addEventListener('DOMContentLoaded', function() {
        var splide = new Splide('#image-slider', {
            video: {
                autoplay: true,
                loop: true,
                hideControls: true,
                mute: true,
                disableOverlayUI: true,
            },
            autoplay: true,
            interval: 15000,
            pauseOnHover: false,
            pauseOnFocus: false,
            resetProgress: false,
            'height': '85vh',
            'width': '90vw',
            'direction': 'ttb',
            'pagination': false,
        }).mount(window.splide.Extensions);

        let curpage = 1
        let refresh = false

        splide.on('move', function() {

            if (splide.index % 10 == 5) {
                refresh = false
            }

            if (splide.index % 10 == 8 && refresh == false) {
                showMemes(memes.slice(curpage * 10, (curpage + 1) * 10));
                splide.refresh(window.splide.Extensions);
                splide.mount(window.splide.Extensions)
                refresh = true
                splide.go(curpage * 9)
                curpage++;
            }
        })

        vids = document.querySelectorAll('video__slide')
        vids.forEach(item => {
            vids.style.background = "none"
        })

        var button = document.querySelector('.splide__play-pause');

        if (button) {
            var pausedClass = 'is-paused';

            // Remove the paused class and change the label to "Pause".
            splide.on('autoplay:play', function() {
                button.classList.remove(pausedClass);
                button.textContent = '\u23F8';
                button.style.padding = "15px 15px"
                button.setAttribute('aria-label', 'Pause Autoplay');
            });

            // Add the paused class and change the label to "Play".
            splide.on('autoplay:pause', function() {
                button.classList.add(pausedClass);
                button.textContent = '\u25B6';
                button.style.padding = "10px 15px"
                button.setAttribute('aria-label', 'Start Autoplay');
            });

            // Toggle play/pause when the button is clicked.
            splide.on('click', function() {
                var flag = 99;
                var Autoplay = splide.Components.Autoplay;

                if (button.classList.contains(pausedClass)) {
                    Autoplay.play(flag);
                } else {
                    Autoplay.pause(flag);
                }
            }, button);
        }
    });

    const showMemes = (data) => {
        data.forEach(item => {
            let ulist = document.querySelector('.splide__list');

            if (item.slice(-1) == "4") { //if video
                let li = document.createElement('LI')
                li.className = "splide__slide"
                li.setAttribute('data-splide-html-video', item);

                //removes if doesn't load properly
                li.addEventListener("error", function(e) {
                    ulist.removeChild(li);
                });
                ulist.appendChild(li)
            } else { //if png or jpg
                let li = document.createElement('LI')
                li.className = "splide__slide"
                let img = document.createElement('img')
                img.className = 'meme'
                img.src = item
                li.appendChild(img)
                ulist.appendChild(li)
            }

        });

    };

    // initialize
    showMemes(memes.slice(0, 10));

})();