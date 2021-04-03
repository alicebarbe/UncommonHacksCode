(function() {

    //let memes = [    ]

    const showMemes = (data) => {
        data.forEach(item => {
            let div = document.querySelector('.memeDiv');
            let img = document.createElement('video')
            img.className = 'meme'
            img.src = item
            div.appendChild(img)
        });
    };

    let currentPage = 1;

    window.addEventListener('scroll', () => {
        const {
            scrollTop,
            scrollHeight,
            clientHeight
        } = document.documentElement;

        if (scrollTop + clientHeight >= scrollHeight - 5) {
            currentPage++;
            showMemes(memes.slice(currentPage * 10, (currentPage + 1) * 10));
        }
    }, {
        passive: true
    });

    // initialize
    showMemes(memes.slice(0, 10));

})();