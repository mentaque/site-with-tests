# Generated by Django 4.2.1 on 2023-05-13 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_answer_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answers', models.IntegerField()),
                ('all_answers', models.IntegerField()),
                ('testsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.testsession')),
            ],
        ),
    ]
