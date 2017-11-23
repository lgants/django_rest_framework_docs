from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


# HyperlinkedModelSerializer differences from ModelSerializer: doesn't include id by default, includes a url field (via HyperlinkedIdentityField), Relationships use HyperlinkedRelatedField instead of PrimaryKeyRelatedField
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # source argument controls which attribute is used to populate a field
    # ReadOnlyField is untyped and always read-only; it's used for serialized representations, but will not be used for updating model instances when they are deserialized
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    # Highlight field is same type as url field, except it points to 'snippet-highlight' url pattern instead of 'snippet-detail' url pattern
    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


"""
# Replaced serializers.Serializer with serializers.ModelSerializer

class SnippetSerializer(serializers.Serializer):
    # Defines the fields that get serialized
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        # Create and return a new `Snippet` instance, given the validated data
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing `Snippet` instance, given the validated data
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
"""
