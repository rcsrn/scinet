# Generated by Django 4.1.3 on 2022-12-02 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scinet_app', '0002_quotes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='belongs',
            old_name='general_user',
            new_name='general_user_id',
        ),
        migrations.RenameField(
            model_name='belongs',
            old_name='institution',
            new_name='institution_id',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='journal',
            new_name='journal_id',
        ),
        migrations.RenameField(
            model_name='writes',
            old_name='general_user',
            new_name='general_user_id',
        ),
        migrations.RenameField(
            model_name='writes',
            old_name='publication',
            new_name='publication_id',
        ),
    ]