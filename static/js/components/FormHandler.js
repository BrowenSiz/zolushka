export class FormHandler {
    constructor(formId) {
        this.form = document.getElementById(formId);
        if (!this.form) return;

        this.submitBtn = this.form.querySelector('button[type="submit"]');
        this.init();
    }

    init() {
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleSubmit();
        });
    }

    async handleSubmit() {
        this.submitBtn.disabled = true;
        this.submitBtn.textContent = 'Отправка...';

        const formData = new FormData(this.form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch(this.form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': data.csrfmiddlewaretoken,
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();

            if (result.success) {
                this.form.reset(); // Очищаем форму
                alert(result.message); // Показываем сообщение об успехе
            } else {
                throw new Error(result.message || 'Произошла ошибка.');
            }

        } catch (error) {
            console.error('Submit error:', error);
            alert('Не удалось отправить заявку. Пожалуйста, попробуйте еще раз.');
        } finally {
            this.submitBtn.disabled = false;
            this.submitBtn.textContent = 'Узнать стоимость';
        }
    }
}