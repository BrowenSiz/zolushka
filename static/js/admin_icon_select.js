// Используем безопасный способ дождаться загрузки django.jQuery
if (window.django && window.django.jQuery) {
    (function($) {
        $(document).ready(function() {
            // Функция, которая будет форматировать каждый пункт в списке
            function formatIcon(option) {
                if (!option.id) {
                    return option.text;
                }
                // Создаем HTML: иконка + текст
                var $option = $(
                    '<span><span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 8px;">' + option.id + '</span> ' + option.text + '</span>'
                );
                return $option;
            };

            // Находим наше поле по его ID
            var iconSelect = $('#id_icon_selector');

            // --- ОТЛАДКА: Проверяем, нашелся ли элемент ---
            console.log('Поиск элемента #id_icon_selector:', iconSelect);
            
            if (iconSelect.length) {
                // Применяем Select2 к нашему полю с кастомным форматированием
                iconSelect.select2({
                    templateResult: formatIcon,  // Форматирует пункты в выпадающем списке
                    templateSelection: formatIcon, // Форматирует выбранный пункт
                    width: 'resolve'
                });
                console.log('Select2 успешно применен!');
            } else {
                console.error('Элемент #id_icon_selector не найден на странице!');
            }
        });
    })(django.jQuery);
}