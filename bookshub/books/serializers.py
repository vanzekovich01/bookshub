from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    tags = serializers.Field(source='get_tags_display')

    class Meta:
        model = Book
        fields = ('id', 'title', 'condition', 'price', 'author', 'description',
                  'publisher', 'category', 'isbn_10', 'isbn_13', 'quantity',
                  'author', 'edition', 'tags')

    def save_object(self, obj, **kwargs):
        obj.owner = self.context['request'].user
        super(BookSerializer, self).save_object(obj, **kwargs)