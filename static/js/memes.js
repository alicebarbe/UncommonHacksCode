(function() {

    const showMemes = (data) => {
        data.forEach(item => {
            let div = document.querySelector('.memeDiv');

            if (item.slice(-1) == "4") { //if video
                let vid = document.createElement('VIDEO')
                vid.className = 'meme'
                vid.src = item
                vid.autoplay = true
                vid.loop = true
                vid.defaultMuted = true
                vid.muted = true
                vid.height = "500"
                //removes if doesn't load properly
                vid.addEventListener("error", function(e) {
                    div.removeChild(vid);
                });
                div.appendChild(vid)
            } else { //if png or jpg
                let img = document.createElement('img')
                img.className = 'meme'
                img.src = item
                div.appendChild(img)
            }

        });

    };

    let currentPage = 1;

    window.addEventListener('scroll', () => {
        const {
            scrollTop,
            scrollHeight,
            clientHeight
        } = document.documentElement;

        if (scrollTop + clientHeight >= scrollHeight - 500) {
            currentPage++;
            showMemes(memes.slice(currentPage * 10, (currentPage + 1) * 10));
        }
    }, {
        passive: true
    });

    // initialize
    showMemes(memes.slice(0, 10));

})();