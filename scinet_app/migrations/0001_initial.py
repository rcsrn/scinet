# Generated by Django 4.1.3 on 2022-12-16 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateField()),
                ('country', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'institution',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('journal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'journal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'topic',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('content', models.TextField(blank=True)),
                ('doi', models.CharField(max_length=255)),
                ('journal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scinet_app.journal')),
                ('topic', models.ManyToManyField(blank=True, to='scinet_app.topic')),
            ],
            options={
                'db_table': 'publication',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GeneralUser',
            fields=[
                ('general_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('institutions', models.ManyToManyField(blank=True, to='scinet_app.institution')),
                ('publications', models.ManyToManyField(blank=True, to='scinet_app.publication')),
            ],
            options={
                'db_table': 'generaluser',
                'managed': True,
            },
        ),
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
