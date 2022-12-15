from django.db import models

class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'journal'
        
class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        managed = True
        db_table = 'topic'

class Publication(models.Model):
    publication_id = models.AutoField(primary_key=True)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    content = models.TextField(blank=True)
    doi = models.CharField(max_length=255)
    topic = models.ManyToManyField(Topic, blank=True)


    class Meta:
        managed = True
        db_table = 'publication'
        

class Citations(models.Model):
    citer = models.ForeignKey('Publication', on_delete=models.CASCADE, related_name='citer')
    citee = models.ForeignKey('Publication', on_delete=models.CASCADE, related_name='citee')
    
    class Meta:
        unique_together = ('citer', 'citee')



class Institution(models.Model):
    institution_id = models.AutoField(primary_key=True)
    creation_date = models.DateField()
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'institution'

class GeneralUser(models.Model):
    general_user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    publications = models.ManyToManyField(Publication, blank=True)
    institutions = models.ManyToManyField(Institution, blank=True)

    class Meta:
        managed = True
        db_table = 'generaluser'