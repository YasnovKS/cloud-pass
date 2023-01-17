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
    body.style.backgroundSize = "cover";
    body.style.backgroundPosition = "center";
}

const modal = document.querySelector('[data-modal]');
const error = document.querySelector('[data-error-modal]');

const how_button = document.querySelector('.how-button');
how_button.addEventListener('click', function(){
    modal.classList.remove('hidden');
}
)

const clear_button = document.querySelector('.hide-modal');
clear_button.addEventListener('click', function(){
    modal.classList.add('hidden')
}
)

const clear_error_button = document.querySelector('.hide-error');
if (clear_error_button) {
    clear_error_button.addEventListener('click', function(){
        error.classList.add('hidden')
    }
    )
}

getBackground();
