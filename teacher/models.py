from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class subcategories(models.Model):
    categories = models.ForeignKey(categories, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    image = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    gains = models.TextField(null=True, blank=True)
    includes = models.CharField(max_length=200)
    scat_id = models.IntegerField(max_length=111)
    price = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    tags = models.CharField(max_length=200)
    user_id = models.IntegerField(max_length=111, default=0)

class VideoUploads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    section_id = models.IntegerField(max_length=111)
    url = models.CharField(max_length=200)

class Sections(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    course_id = models.IntegerField(max_length=111)
    type = models.CharField(max_length=200, default='1')

class todo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class questions(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1024)
    type = models.CharField(max_length=200)
    section_id = models.IntegerField(max_length=111)
    aw_1_type = models.CharField(max_length=200)
    aw_1_result = models.CharField(max_length=200)
    aw_1_data = models.TextField(null=True, blank=True)
    aw_2_type = models.CharField(max_length=200)
    aw_2_result = models.CharField(max_length=200)
    aw_2_data = models.TextField(null=True, blank=True)
    aw_3_type = models.CharField(max_length=200)
    aw_3_result = models.CharField(max_length=200)
    aw_3_data = models.TextField(null=True, blank=True)
    aw_4_type = models.CharField(max_length=200)
    aw_4_result = models.CharField(max_length=200)
    aw_4_data = models.TextField(null=True, blank=True)