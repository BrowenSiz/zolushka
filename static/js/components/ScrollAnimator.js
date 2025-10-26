export class ScrollAnimator {
    constructor() {
        this.elements = document.querySelectorAll('.animate-on-scroll');
        if (!this.elements.length) return;

        this.observer = new IntersectionObserver(this.handleIntersect.bind(this), {
            root: null,
            rootMargin: '0px',
            threshold: 0.2
        });

        this.elements.forEach(el => this.observer.observe(el));
    }

    handleIntersect(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }
}