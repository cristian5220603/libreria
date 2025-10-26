from rest_framework import serializers
from .models import Book, Author, Category, Loan, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','slug']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id','title','subtitle','authors','categories','description','isbn','available_copies','average_rating']

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews.exists(): return None
        return round(sum([r.rating for r in reviews]) / reviews.count(), 2)

class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book', write_only=True)

    class Meta:
        model = Loan
        fields = ['id','user','book','book_id','status','requested_at','borrowed_at','due_date']
        read_only_fields = ['user','status','requested_at','borrowed_at','due_date']
