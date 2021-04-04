(function() {

    let memes = [
        'https://i.imgur.com/T9HDYuf.jpg',
        'https://i.imgur.com/ZhvdR05.mp4',
        'https://i.imgur.com/MAWOlPC.mp4',
        'https://i.imgur.com/hdE2QNz.mp4',
        'https://i.redd.it/fdo5i4ny72e21.jpg',
        'https://i.imgur.com/m25Inv3.mp4',
        'https://i.imgur.com/w01mVZp.mp4',
        'https://i.imgur.com/xlWP4l6.mp4',
        'https://i.redd.it/jhnc9lol2by11.jpg',
        'https://i.imgur.com/mn3Wg7z.mp4',
        'https://i.redd.it/76sx51l80ln41.jpg',
        'https://i.imgur.com/ASggPx3.mp4',
        'https://i.redd.it/ebovt49g96551.jpg',
        'http://i.imgur.com/6SCid9Q.mp4',
        'https://i.imgur.com/JjGoVf6.mp4',
        'https://i.redd.it/x1w2v2r6g5m21.jpg',
        'https://i.imgur.com/9Cnme3V.mp4', ,
        'https://i.redd.it/u9hh56gf03kz.jpg',
        'https://i.imgur.com/nptaXEF.jpg',
        'https://i.redd.it/ptcwhz1b51951.jpg',
        'https://i.imgur.com/rUfI2MM.mp4',
        'https://i.imgur.com/ODPMAKx.mp4',
        'https://i.imgur.com/Dj6OKRS.mp4',
        'https://i.imgur.com/sliIvan.mp4',
        'https://i.imgur.com/lk5XLZp.mp4',
        'https://i.imgur.com/547pv2x.mp4',
        'https://i.imgur.com/Tiow98D.mp4',
        'https://i.imgur.com/0BX99KV.mp4',
        'https://i.redd.it/cyiz9lvarth21.jpg',
        'https://i.imgur.com/bU5iPFx.mp4',
        'https://i.imgur.com/DGwNFws.mp4',
        'https://i.redd.it/3g9z1gt7boc61.jpg',
        'https://i.redd.it/yvqnmt2aqny31.jpg',
        'https://imgur.com/D9BEoTl.mp4',
        'https://i.redd.it/ii5k59s5wck31.jpg',
        'https://i.imgur.com/Z7s9ax0.mp4',
        'https://i.redd.it/9rscvfim57b41.jpg',
        'https://i.redd.it/xx6bpswffs961.png',
        'https://i.redd.it/ea2sco6s4ig11.jpg',
        'https://i.redd.it/1loexknprp051.jpg',
        'https://i.imgur.com/HIVlonE.mp4',
        'https://i.imgur.com/Ljqg2vr.mp4',
        'https://i.imgur.com/x25LV6Y.mp4',
        'https://i.redd.it/miqh03iny5t31.jpg',
        'https://i.imgur.com/VPu0F2K.mp4',
        'https://i.redd.it/y4tjt57jdkh51.jpg',
        'https://i.imgur.com/OMXiylf.mp4',
        'https://i.redd.it/87bbww9nqlk21.jpg',
        'https://i.imgur.com/82aqPtq.mp4',
        'https://i.imgur.com/GQXiz9j.mp4',
        'https://i.redd.it/x1w2v2r6g5m21.jpg',
        'https://i.imgur.com/5THWTxi.mp4',
        'https://i.imgur.com/S95E30u.mp4',
        'https://i.imgur.com/95hiaPZ.mp4',
        'https://i.imgur.com/FxmvnVn.mp4',
        'https://i.redd.it/qwlxc4cut7d21.jpg',
        'https://i.imgur.com/TBmIXOo.mp4',
        'https://i.imgur.com/9KiElZa.mp4',
        'https://i.imgur.com/5TnG6eX.jpg',
        'https://i.imgur.com/sk5Ddfe.mp4',
        'https://i.redd.it/xkjikeh7evf11.jpg',
        'https://i.redd.it/hf0wt1qbfu521.jpg',
        'https://i.imgur.com/ROtLLl9.mp4',
        'https://i.redd.it/xsu70fsk2r461.mp4',
        'https://i.imgur.com/KKricjY.mp4',
        'https://i.imgur.com/Qos7hy0.mp4',
        'https://i.imgur.com/8glL1vh.mp4',
        'https://i.imgur.com/RASbQn9.mp4'
    ]

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