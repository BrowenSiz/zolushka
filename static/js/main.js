import { Navigation } from './components/Navigation.js';
import { FormHandler } from './components/FormHandler.js';
import { Portfolio } from './components/Portfolio.js';
import { Tabs } from './components/Tabs.js';

document.addEventListener('DOMContentLoaded', () => {
    new Navigation();
    new FormHandler('toggle-form');

    const portfolioContainer = document.getElementById('portfolio-page');
    if (portfolioContainer) {
        new Portfolio(portfolioContainer);
    }

    const tabsContainer = document.querySelector('.checklist-tabs');
    if (tabsContainer) {
        new Tabs(tabsContainer);
    }

    const form = document.getElementById('toggle-form');
    if (form) {
        const toggles = form.querySelectorAll('input[name="object_type_toggle"]');
        const privateFields = document.getElementById('private-fields');
        const commercialFields = document.getElementById('commercial-fields');

        toggles.forEach(toggle => {
            toggle.addEventListener('change', (event) => {
                const isPrivate = event.target.value === 'private';
                privateFields.hidden = !isPrivate;
                commercialFields.hidden = isPrivate;
            });
        });
    }
});