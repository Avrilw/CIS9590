# Generated by Django 2.2.5 on 2019-12-07 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=268)),
                ('release_date', models.DateField()),
                ('box_office', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('genre', models.TextField()),
                ('casts', models.TextField()),
                ('rate', models.FloatField()),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=16)),
                ('occuptation', models.CharField(max_length=254)),
                ('register_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienjoy_app.Movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienjoy_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=268)),
                ('re_content', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienjoy_app.Movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienjoy_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('com_content', models.CharField(max_length=512)),
                ('com_date', models.DateTimeField(auto_now_add=True)),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienjoy_app.Review')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movienjoy_app.User')),
            ],
        ),
    ]
