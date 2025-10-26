from django.db import models

from django.db import models

class PortfolioCategory(models.Model):
    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("URL (для фильтра)", unique=True)

    class Meta:
        verbose_name = "Категория портфолио"
        verbose_name_plural = "Категории портфолио"

    def __str__(self):
        return self.name

class PortfolioProject(models.Model):
    title = models.CharField("Заголовок проекта", max_length=200)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    short_description = models.TextField("Краткое описание (для модального окна)")
    preview_image = models.ImageField("Главное фото (для карточки)", upload_to='portfolio/previews/')
    image_before = models.ImageField("Фото 'ДО'", upload_to='portfolio/before_after/')
    
    # Статистика
    area = models.CharField("Площадь", max_length=50, blank=True)
    time_spent = models.CharField("Затрачено времени", max_length=50, blank=True)
    team_size = models.CharField("Размер команды", max_length=50, blank=True)
    
    date_completed = models.DateField("Дата выполнения", blank=True, null=True)
    is_visible = models.BooleanField("Отображать на сайте", default=True)
    order = models.PositiveIntegerField("Порядок сортировки", default=0)
    
    class Meta:
        verbose_name = "Проект в портфолио"
        verbose_name_plural = "Проекты в портфолио"
        ordering = ['-date_completed', 'order']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE, related_name="after_images", verbose_name="Проект")
    image = models.ImageField("Фотография 'ПОСЛЕ'", upload_to='portfolio/gallery/')
    caption = models.CharField("Подпись к фото (необязательно)", max_length=255, blank=True)

    class Meta:
        verbose_name = "Фото 'ПОСЛЕ' для галереи"
        verbose_name_plural = "Фото 'ПОСЛЕ' для галереи"

    def __str__(self):
        return f"Фото для проекта '{self.project.title}'"