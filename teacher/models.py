from django.db import models

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

# class Course(models.Model):
    # id = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=127)
    # sub_title = models.CharField(max_length=127)
    # category = models.CharField(max_length=127, choices=COURSE_CATEGORY_TYPES, default='General Education')
    # description = models.TextField(null=True)
    # start_date = models.DateField(null=True)
    # finish_date = models.DateField(null=True)
    # is_official = models.BooleanField(default=False)
    # status = models.PositiveSmallIntegerField(default=settings.COURSE_UNAVAILABLE_STATUS)
    # image = models.ImageField(upload_to='uploads', null=True, blank=True)
    # students = models.ManyToManyField(Student)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    # def delete(self, *args, **kwargs):
    #     if self.image:
    #         if os.path.isfile(self.image.path):
    #             os.remove(self.image.path)
    #     super(Course, self).delete(*args, **kwargs) # Call the "real" delete() method

    # def __str__(self):
    #     return self.title

    # class Meta:
    #     db_table = 'at_courses'