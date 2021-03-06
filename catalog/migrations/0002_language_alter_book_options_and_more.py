# Generated by Django 4.0.1 on 2022-01-14 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter book language', max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'author']},
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Born'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
