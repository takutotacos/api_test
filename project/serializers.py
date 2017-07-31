from rest_framework import serializers
from project.models import User, LargeGenre, MiddleGenre, Topic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'created_at', 'updated_at', 'is_deleted')

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'User' instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance

class LargeGenreSerializer(serializers.ModelSerializer):
    sub_content_count = serializers.SerializerMethodField()

    class Meta:
        model = LargeGenre
        fields = ('id', 'name', 'created_at', 'updated_at', 'is_deleted', 'sub_content_count')

    def get_sub_content_count(self, obj):
        return obj.middle_genres.all().count()

class MiddleGenreSerializer(serializers.ModelSerializer):
    topic_number = serializers.SerializerMethodField()
    def get_sub_content_count(self, obj):
        return obj.topics.all().count()

    class Meta:
        model = MiddleGenre
        fields = ('id', 'name', 'large_genre_id', 'created_at', 'updated_at', 'is_deleted', 'sub_content_count')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'description', 'large_genre_id', 'middle_genre_id', 'tag_id', 'image')
