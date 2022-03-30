# Generated by Django 4.0.3 on 2022-03-30 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('name', models.CharField(max_length=150, verbose_name='اسم عکس')),
                ('image_describe', models.TextField(blank=True, verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='images', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'عکسها',
            },
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='اسم')),
                ('video_describe', models.TextField(blank=True, verbose_name='توضیحات')),
                ('video', models.FileField(upload_to='videos', verbose_name='ویدیو')),
                ('story', models.TextField(blank=True, verbose_name='داستان')),
                ('published', models.BooleanField(default=False, verbose_name='منتشر شود؟')),
                ('video_thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_thumbnail', to='api.imagemodel', verbose_name='بنر')),
            ],
            options={
                'verbose_name': 'ویدیو',
                'verbose_name_plural': 'ویدیوها',
            },
        ),
        migrations.CreateModel(
            name='StoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='اسم')),
                ('story', models.TextField(verbose_name='متن')),
                ('published', models.BooleanField(default=False, verbose_name='منتشر شود؟')),
                ('story_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='story_image', to='api.imagemodel', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'متن',
                'verbose_name_plural': 'متنها',
            },
        ),
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='اسم آلبوم')),
                ('album_describe', models.TextField(blank=True, verbose_name='توضیحات')),
                ('published', models.BooleanField(default=False, verbose_name='منتشر شود؟')),
                ('album_image', models.ManyToManyField(related_name='album_image', to='api.imagemodel', verbose_name='عکسهای آلبوم')),
                ('album_thumbnail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_thumbnail', to='api.imagemodel', verbose_name='بنر آلبوم')),
            ],
            options={
                'verbose_name': 'آلبوم',
                'verbose_name_plural': 'آلبومها',
            },
        ),
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('age', models.IntegerField(default=0, verbose_name='سن')),
                ('birthday', models.CharField(max_length=4, verbose_name='روز تولد')),
                ('degree', models.CharField(max_length=250, verbose_name='مدرک تحصیلی')),
                ('trophy', models.TextField(verbose_name='افتخارات')),
                ('self_describe', models.TextField(verbose_name='توضیحات')),
                ('self_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='self_image', to='api.imagemodel', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]
