export class Portfolio {
    constructor(container) {
        this.container = container;
        if (!this.container) return;

        this.initFilters();
        this.initModal();
    }

    // --- Хелпер для правильного склонения слова "клинер" ---
    getCleanersString(count) {
        const num = parseInt(count, 10);
        if (isNaN(num)) return count; // Если в админке ввели не число, а текст

        const lastDigit = num % 10;
        const lastTwoDigits = num % 100;

        if (lastTwoDigits >= 11 && lastTwoDigits <= 19) {
            return `${num} клинеров`;
        }
        if (lastDigit === 1) {
            return `${num} клинер`;
        }
        if (lastDigit >= 2 && lastDigit <= 4) {
            return `${num} клинера`;
        }
        return `${num} клинеров`;
    }

    initFilters() {
        const filterBtns = this.container.querySelectorAll('.filter-btn');
        const projectCards = this.container.querySelectorAll('.project-card');

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.dataset.filter;

                projectCards.forEach(card => {
                    card.hidden = filter !== 'all' && card.dataset.category !== filter;
                });
            });
        });
    }

    initModal() {
        this.modal = document.getElementById('project-modal');
        this.modalContent = document.getElementById('modal-body-content');
        if (!this.modal) return;

        // Открытие модального окна
        this.container.addEventListener('click', (e) => {
            const openBtn = e.target.closest('.open-project-modal');
            if (openBtn) {
                this.openModal(openBtn.dataset.projectId);
            }
        });

        // Закрытие модального окна
        this.modal.addEventListener('click', (e) => {
            if (e.target.matches('[data-close-modal]')) {
                this.closeModal();
            }
        });
    }

    async openModal(projectId) {
        this.modalContent.innerHTML = '<div class="loader"></div>';
        this.modal.hidden = false;
        document.body.style.overflow = 'hidden';

        try {
            const response = await fetch(`/portfolio/project/${projectId}/`);
            if (!response.ok) throw new Error('Project not found');
            const data = await response.json();

            // 1. Миниатюры для галереи
            const sliderThumbHtml = `
                <button class="thumb active" data-type="slider">
                    <span class="material-symbols-outlined">compare</span>
                    До/После
                </button>`;
            const imagesThumbHtml = data.after_images_urls.map((url, index) => `
                <button class="thumb" data-type="image" data-src="${url}">
                    <img src="${url}" alt="Фото ${index + 1}">
                </button>`).join('');

            // 2. Основной HTML модального окна
            this.modalContent.innerHTML = `
                <div class="modal-grid">
                    <div class="modal__visuals">
                        <div class="modal__viewer">
                            </div>
                        <div class="modal__thumbnails">
                            ${sliderThumbHtml}
                            ${imagesThumbHtml}
                        </div>
                    </div>
                    <div class="modal__info">
                        <h2 class="modal__title">${data.title}</h2>
                        <div class="modal-section">
                            <p>${data.short_description}</p>
                        </div>
                        <div class="modal__stats">
                            <div class="stat-item"><span class="material-symbols-outlined">crop_square</span><div><strong>Площадь:</strong> ${data.area} м²</div></div>
                            <div class="stat-item"><span class="material-symbols-outlined">schedule</span><div><strong>Время:</strong> ${data.time_spent}</div></div>
                            <div class="stat-item"><span class="material-symbols-outlined">groups</span><div><strong>Команда:</strong> ${this.getCleanersString(data.team_size)}</div></div>
                        </div>
                        <a href="#toggle-form" class="button button--accent button--full modal__cta">Рассчитать похожий проект</a>
                    </div>
                </div>
            `;
            
            // 3. Логика галереи
            this.viewer = this.modalContent.querySelector('.modal__viewer');
            this.thumbnails = this.modalContent.querySelectorAll('.thumb');
            
            this.showSlider(data.image_before_url, data.after_images_urls[0]); // Показываем слайдер по умолчанию

            this.thumbnails.forEach(thumb => {
                thumb.addEventListener('click', () => {
                    this.thumbnails.forEach(t => t.classList.remove('active'));
                    thumb.classList.add('active');

                    if (thumb.dataset.type === 'slider') {
                        this.showSlider(data.image_before_url, data.after_images_urls[0]);
                    } else {
                        this.showImage(thumb.dataset.src);
                    }
                });
            });

            // 4. Логика для кнопки "Рассчитать"
            const ctaButton = this.modalContent.querySelector('.modal__cta');
            if (ctaButton) {
                ctaButton.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.closeModal();
                    
                    setTimeout(() => {
                        const form = document.querySelector('#toggle-form');
                        if (form) {
                            form.scrollIntoView({ behavior: 'smooth' });
                        }
                    }, 300);
                });
            }

        } catch (error) {
            console.error("Failed to load project data:", error);
            this.modalContent.innerHTML = '<p>Не удалось загрузить данные проекта.</p>';
        }
    }

    showSlider(beforeSrc, afterSrc) {
        if (!beforeSrc || !afterSrc) {
            this.viewer.innerHTML = '<p>Нет изображений для сравнения.</p>';
            return;
        }
        this.viewer.innerHTML = `
            <img-comparison-slider>
                <img slot="first" src="${beforeSrc}" alt="До уборки">
                <img slot="second" src="${afterSrc}" alt="После уборки">
            </img-comparison-slider>`;
    }

    showImage(src) {
        this.viewer.innerHTML = `<img class="single-image-view" src="${src}" alt="Результат работы">`;
    }

    closeModal() {
        this.modal.hidden = true;
        this.modalContent.innerHTML = '';
        document.body.style.overflow = '';
    }
}