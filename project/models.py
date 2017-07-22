from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = False)

class Prefecture(models.Model):
    name = models.CharField(max_length = 255)

class LargeGenre(models.Model):
    class Meta:
        unique_together = (('prefecture', 'name'),)

    prefecture = models.ForeignKey(Prefecture)
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = True)

class MiddleGenre(models.Model):
    class Meta:
        unique_together = (('prefecture', 'large_genre', 'name'),)

    name = models.CharField(max_length = 255)
    prefecture = models.ForeignKey(Prefecture)
    large_genre = models.ForeignKey(LargeGenre, related_name = 'middle_genres')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = True)

class Topic(models.Model):
    def get_image_path(filename):
        """カスタマイズした画像パスを取得する。
        :param self: インスタンス（models.Model)
        :param filename: 元ファイル名
        :return: カスタマイズしたファイル名を含む画像パス
        """
        prefix = 'images/'
        name = str(uuid.uuid4()).replace('-', '')
        extension = os.path.splitext(filename)[-1]
        return prefix + name + extension

    title = models.CharField(max_length = 255)
    description = models.TextField(max_length = 255)
    large_genre = models.ForeignKey(LargeGenre)
    middle_genre = models.ForeignKey(MiddleGenre, related_name="topics")
    prefecture = models.ForeignKey(Prefecture)
    tag_id = models.CharField(max_length = 255, default="")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = get_image_path, default="")

class Like(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
