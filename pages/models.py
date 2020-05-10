from django.db import models

class TemplateClass(models.Model):
    title = models.CharField('название', max_length=150)
    description = models.TextField('описание', blank=True)
    slug = models.SlugField('чпу', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Page(TemplateClass):
    menu = models.ManyToManyField('Menu', verbose_name='меню', blank=True)
    categories = models.ManyToManyField('Category', verbose_name='категория')
    image = models.ImageField('изображение', upload_to='page_images/', height_field=None, width_field=None, max_length=100, blank=True)
    show_on_home = models.BooleanField('на главную', default=False, help_text='Показать на гланой странице')
    draft = models.BooleanField('черновик', default=False)
    

    class Meta:
	    verbose_name = "Страница"
	    verbose_name_plural = "Страницы"

class Category(TemplateClass):
    
    class Meta:
	    verbose_name = "Категория"
	    verbose_name_plural = "Категории"

class Menu(TemplateClass):
    slug = None
    
    class Meta:
	    verbose_name = "Меню"
	    verbose_name_plural = "Меню"