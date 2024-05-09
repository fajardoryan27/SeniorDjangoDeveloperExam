from django.db import models

class  book(models.Model):
    #Field names, Data Types and Constraints
    id = models.AutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=150, null=False)
    author = models.CharField(max_length=50, null=False)
    publication_year =  models.CharField(max_length=255)
    isbn =  models.CharField(max_length=255,null=False)
    genre = models.CharField(max_length=50, null=False)
    availablity_status = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title
    
    class Meta:
        # Table Configurations
        db_table = "book"
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class  Author(models.Model):
    #Field names, Data Types and Constraints
    id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    biography =  models.CharField(max_length=255)
    nationality =  models.CharField(max_length=30)

    def __str__(self):
        
        return self.last_name
    
    class Meta:
        # Table Configurations
        db_table = "author"
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class  Genre(models.Model):
    #Field names, Data Types and Constraints
    id = models.AutoField(primary_key=True,unique=True)
    genre_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.genre_name
    
    class Meta:
        # Table Configurations
        db_table = "genre"
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
