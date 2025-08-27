from django.db import models

class Library(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'

class Author(models.Model):
    name = models.CharField(max_length=155)
    birth_year = models.CharField(max_length=155)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Авторы'
    

class Book(models.Model):
    title = models.CharField(max_length=155)
    desscription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    published_year = models.PositiveIntegerField(blank=True, null=True, verbose_name='Год Публикаций')
    genre = models.CharField(
        max_length=155,
        verbose_name='Жанр',
        blank=True, null=True
    )
    pages = models.CharField(
        max_length=155,
        verbose_name='Кол-во Страниц',
        blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновленр')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']