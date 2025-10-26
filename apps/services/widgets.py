from django import forms
from django.utils.safestring import mark_safe

class IconSelectWidget(forms.Select):
    
    # Мы переопределяем метод, который отвечает за отрисовку одного <option>
    def render_option(self, selected_choices, option_value, option_label):
        # Если значение опции существует (это не пустой пункт '-------')
        if option_value:
            # Создаем HTML с иконкой и текстом
            # mark_safe() говорит Django, что этот HTML безопасен и его не нужно экранировать
            option_label = mark_safe(f'<span class="material-symbols-outlined" style="vertical-align: middle; margin-right: 8px;">{option_value}</span> {option_label}')
        
        # Вызываем оригинальный метод с нашим новым, красивым текстом
        return super().render_option(selected_choices, option_value, option_label)