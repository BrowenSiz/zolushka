export class Navigation {
    constructor() {
        this.header = document.querySelector('.header');
        this.burger = document.querySelector('.burger-btn');
        this.menu = document.querySelector('.nav-menu');
        this.init();
    }

    init() {
        if (!this.header || !this.burger || !this.menu) return;

        window.addEventListener('scroll', () => this.handleScroll());

        this.burger.addEventListener('click', () => this.toggleMenu());
    }

    handleScroll() {
        if (window.scrollY > 50) {
            this.header.classList.add('scrolled');
        } else {
            this.header.classList.remove('scrolled');
        }
    }

    toggleMenu() {
        this.burger.classList.toggle('open');
        this.menu.classList.toggle('open');
        document.body.classList.toggle('no-scroll');
    }
}