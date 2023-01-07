const images = [
    "url('/static/backgrounds/loon-image-original(1).jpg')",
    "url('/static/backgrounds/loon-image-original(2).jpg')",
    "url('/static/backgrounds/loon-image-original(3).jpg')",
    "url('/static/backgrounds/loon-image-original(4).jpg')",
    "url('/static/backgrounds/loon-image-original(5).jpg')",
    "url('/static/backgrounds/loon-image-original(6).jpg')",
]

function getBackground() {
    const body = document.getElementById('body');
    let index = Math.floor(Math.random() * 6);

    body.style.backgroundImage = images[index];
}

getBackground();
