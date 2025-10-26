export class Tabs {
    constructor(container) {
        this.container = container;
        if (!this.container) return;

        this.tabButtons = this.container.querySelectorAll('.tabs-nav__btn');
        this.tabPanes = this.container.querySelectorAll('.tabs-content__pane');
        this.init();
    }

    init() {
        this.tabButtons.forEach(button => {
            button.addEventListener('click', () => this.activateTab(button));
        });
    }

    activateTab(clickedButton) {
        const tabId = clickedButton.dataset.tab;

        this.tabButtons.forEach(btn => btn.classList.remove('active'));
        clickedButton.classList.add('active');

        this.tabPanes.forEach(pane => {
            if (pane.id === `tab-${tabId}`) {
                pane.classList.add('active');
            } else {
                pane.classList.remove('active');
            }
        });
    }
}