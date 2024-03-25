from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
def phone_validate(value):
    allowed_characters=set("01234567890-() ")
    for char in value:
        if char not in allowed_characters:
            raise ValidationError(
                ('Номер телефона содержит недопустимые символы'),
                params={'value':value}
            )
class Library(models.Model):
    image=models.ImageField(upload_to="library")
    name=models.CharField(max_length=100,verbose_name="Название библиотеки")
    address=models.CharField(max_length=255,verbose_name='Адрес')
    phone=models.CharField(max_length=20,validators=[phone_validate],verbose_name='Номер телефона')
    description=models.TextField()
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name='Библиотека'
        verbose_name_plural='Библиотеки'

    
class Author(models.Model):
    picture=models.ImageField(upload_to='author/',verbose_name='Фото профиля')
    FirstName=models.CharField(max_length=100,verbose_name="Имя")
    LastName=models.CharField(max_length=100,verbose_name="Фамилия")
    birthdate=models.DateField(verbose_name='Дата рождения')
    deathdate=models.DateField(verbose_name="Дата смерти",blank=True,null=True)
    aboutAuthor=models.TextField(verbose_name='О авторе')

    def __str__(self):
        return f"{self.FirstName } {self.LastName}"
    
    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'

class Book(models.Model):
    image=models.ImageField(upload_to='book/',verbose_name="Фотография книги")
    title=models.CharField(max_length=255,verbose_name="Название книги")
    description=models.TextField(verbose_name="Описание книги")
    year_of_issue=models.IntegerField(verbose_name="Год выпуска")
    libraries=models.ManyToManyField(Library)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Книги'
    

