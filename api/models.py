from django.db import models


class DateCreatedModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        abstract = True


class ImageModel(DateCreatedModel):
    name = models.CharField(max_length=150, verbose_name='اسم عکس')
    image_describe = models.TextField(blank=True, verbose_name='توضیحات')
    image = models.ImageField(upload_to='images', verbose_name='عکس')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکسها'
    
    def __str__(self):
        return self.name


class AlbumModel(DateCreatedModel):
    name = models.CharField(max_length=150, unique=True, verbose_name='اسم آلبوم')
    album_describe = models.TextField(blank=True, verbose_name='توضیحات')
    album_thumbnail = models.ForeignKey(ImageModel,related_name='album_thumbnail', null=True, on_delete=models.SET_NULL, verbose_name='بنر آلبوم')
    album_image = models.ManyToManyField(ImageModel, related_name='album_image', verbose_name='عکسهای آلبوم')
    published = models.BooleanField(default=False, verbose_name='منتشر شود؟')
    class Meta:
        verbose_name = 'آلبوم'
        verbose_name_plural = 'آلبومها'

    def __str__(self):
        return self.name


class StoryModel(DateCreatedModel):
    name = models.CharField(max_length=150, unique=True, verbose_name='اسم')
    story_image = models.ForeignKey(ImageModel, related_name='story_image', null=True, on_delete=models.SET_NULL, blank=True, verbose_name='عکس')
    story = models.TextField(verbose_name='متن')
    published = models.BooleanField(default=False, verbose_name='منتشر شود؟')

    class Meta:
        verbose_name = 'متن'
        verbose_name_plural = 'متنها'
    
    def __str__(self):
        return self.name


class AboutModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    self_image = models.ForeignKey(ImageModel, related_name='self_image', null=True, on_delete=models.SET_NULL, blank=True, verbose_name='عکس')
    age = models.IntegerField(default=0, verbose_name='سن')
    birthday = models.CharField(max_length=4, verbose_name='روز تولد')
    degree = models.CharField(max_length=250, verbose_name='مدرک تحصیلی')
    trophy = models.TextField(verbose_name='افتخارات')
    self_describe = models.TextField(verbose_name='توضیحات')
    
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
    
    def __str__(self):
        return self.first_name + self.last_name


class VideoModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='اسم')
    video_thumbnail = models.ForeignKey(ImageModel, blank=True, null=True, related_name='video_thumbnail', on_delete=models.SET_NULL, verbose_name='بنر')
    video_describe = models.TextField(blank=True, verbose_name='توضیحات')
    video = models.FileField(upload_to='videos', verbose_name='ویدیو')
    story = models.TextField(blank=True, verbose_name='داستان')
    published = models.BooleanField(default=False, verbose_name='منتشر شود؟')

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیوها'
    
    def __str__(self):
        return self.name