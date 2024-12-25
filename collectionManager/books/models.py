# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookTags(models.Model):
    goodreads_book_id = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'book_tags'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


class Ratings(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ratings'


class Tags(models.Model):
    tag_id = models.IntegerField(blank=True, null=True)
    tag_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'tags'


class ToRead(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'to_read'

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    goodreads_book_id = models.IntegerField(blank=True, null=True)
    best_book_id = models.IntegerField(blank=True, null=True)
    work_id = models.IntegerField(blank=True, null=True)
    books_count = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    isbn13 = models.CharField(max_length=20, blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    original_publication_year = models.FloatField(blank=True, null=True)
    original_title = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    language_code = models.CharField(max_length=10, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    work_ratings_count = models.IntegerField(blank=True, null=True)
    work_text_reviews_count = models.IntegerField(blank=True, null=True)
    ratings_1 = models.IntegerField(blank=True, null=True)
    ratings_2 = models.IntegerField(blank=True, null=True)
    ratings_3 = models.IntegerField(blank=True, null=True)
    ratings_4 = models.IntegerField(blank=True, null=True)
    ratings_5 = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    small_image_url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'books'
