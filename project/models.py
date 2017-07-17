from django.db import models

class User(models.Model):
    id = models.CharField(max_length = 255, primary_key = True)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = True)

class LargeCategory(models.Model):
    id = models.CharField(max_length = 255, primary_key = True)
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = True)

class MiddleCategory(models.Model):
    id = models.CharField(max_length = 255, primary_key = True)
    name = models.CharField(max_length = 255)
    large_genre_id = models.ForeignKey(LargeCategory, related_name = 'middle_categories')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = True)
