export class PhoneMask {
    constructor(selector) {
        this.input = document.getElementById(selector);
        if (!this.input) return;

        this.init();
    }

    init() {
        this.input.addEventListener('input', (e) => this.handleInput(e));
        this.input.addEventListener('keydown', (e) => this.handleKeyDown(e));
    }

    handleInput(e) {
        const input = e.target;
        let value = input.value.replace(/\D/g, '');
        let formattedValue = '';

        if (!value) {
            input.value = '';
            return;
        }

        if (value.length > 0) {
            formattedValue = '+7 (';
            if (value.length > 1) {
                formattedValue += value.substring(1, 4);
            }
            if (value.length > 4) {
                formattedValue += ') ' + value.substring(4, 7);
            }
            if (value.length > 7) {
                formattedValue += '-' + value.substring(7, 9);
            }
            if (value.length > 9) {
                formattedValue += '-' + value.substring(9, 11);
            }
        }

        input.value = formattedValue;
    }
    
    handleKeyDown(e) {
        const input = e.target;
        if (e.key === 'Backspace' && (input.value.length <= 4 || input.value.indexOf('(') === -1)) {
            e.preventDefault();
            input.value = '';
        }
    }
}