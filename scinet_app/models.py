from django.db import models

class Belongs(models.Model):
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    general_user = models.ForeignKey('Generaluser', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'belongs'


class Generaluser(models.Model):
    general_user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    is_alive = models.BooleanField()
    is_author = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'generaluser'


class Institution(models.Model):
    institution_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'institution'


class Journal(models.Model):
    journal_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'journal'


class Publication(models.Model):
    publication_id = models.IntegerField(primary_key=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'publication'


class Writes(models.Model):
    general_user = models.ForeignKey(Generaluser, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'writes'
