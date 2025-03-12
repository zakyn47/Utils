const canvas = document.getElementById("Canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const weeds = [];
const weedImg = new Image();
weedImg.src = "https://clipart.info/images/ccovers/1503426372marijuana-leaf-png-real.png";

class FallingWeed {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * -canvas.height;
        this.speed = Math.random() * 3 + 1;
        this.size = Math.random() * 50 + 30;
    }

    update() {
        this.y += this.speed;
        if (this.y > canvas.height) {
            this.y = Math.random() * -canvas.height;
            this.x = Math.random() * canvas.width;
        }
    }

    draw() {
        ctx.drawImage(weedImg, this.x, this.y, this.size, this.size);
    }
}

function init() {
    for (let i = 0; i < 20; i++) {
        weeds.push(new FallingWeed());
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    weeds.forEach(cup => {
        cup.update();
        cup.draw();
    });
    requestAnimationFrame(animate);
}

window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

weedImg.onload = () => {
    init();
    animate();
};
