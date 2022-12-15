# Generated by Django 4.1.3 on 2022-12-15 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scinet_app', '0003_remove_publication_citations_delete_citation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citee', to='scinet_app.publication')),
                ('citer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citer', to='scinet_app.publication')),
            ],
            options={
                'unique_together': {('citer', 'citee')},
            },
        ),
    ]