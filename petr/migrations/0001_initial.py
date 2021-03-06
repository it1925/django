# Generated by Django 4.0.4 on 2022-04-13 20:10

from django.db import migrations, models
import django.db.models.deletion
import petr.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=100, unique=True, verbose_name='Art Name')),
                ('type', models.CharField(choices=[('painting', 'Painting'), ('sculpture', 'Sculpture'), ('digital', 'Digital'), ('audio-visual', 'Audio-Visual')], max_length=100, verbose_name='Type of art')),
                ('img', models.ImageField(blank=True, null=True, upload_to='gallery/img/%Y/%m/%d/', verbose_name='Image')),
                ('year', models.DateField(blank=True, help_text='datum', null=True, verbose_name='Date')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Genre')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='atachment title')),
                ('file', models.FileField(null=True, upload_to=petr.models.attachment_path, verbose_name='file')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petr.art')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='art',
            name='genres',
            field=models.ManyToManyField(help_text='Genre', to='petr.genre'),
        ),
    ]
