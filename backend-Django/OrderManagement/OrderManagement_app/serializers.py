from rest_framework import serializers
from .models import Customer, Product, Order,OrderItem
from django.contrib.auth.models import User
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class OrderSerializer(serializers.ModelSerializer):

     id_order= serializers.IntegerField(source='id_order', read_only=True)
     customer = serializers.CharField(write_only=True, required=False)
     date = serializers.CharField(write_only=True)
     notes = serializers.CharField(write_only=True, required=False)
     last_updated = serializers.CharField(write_only=True, required=False)
     created_at = serializers.CharField(write_only=True, required=False)

     class Meta:
        model = Order
        fields = ('id_order', 'customer', 'date', 'notes', 'last_updated', 'created_at')

     def create(self, validated_data):
         print(validated_data)
         return Order.objects.create(**validated_data)

     def update(self, instance, validated_data):
        instance.id_orderd = validated_data.get('id_order', instance.id_order)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.date = validated_data.get('date', instance.date)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.last_updated = validated_data.get('last_updated', instance.last_updated)
        instance.created_at= validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'phone_number')
    def create(self, validated_data):
        print(validated_data)
        Customer_user = Customer.objects.create_user(**validated_data)
        return Customer_user

class ProductSerializer(serializers.ModelSerializer):
    name= serializers.CharField(max_length=200,required=True)
    price = serializers.CharField(write_only=True, required=False)
    type = serializers.CharField(write_only=True)
    class Meta:
        model = Product
        fields = ('__all__')
        # fields = ('name', 'price', 'price')

    def create(self, validated_data):
         print(validated_data)
         return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('id_order', instance.id_order)
        instance.price = validated_data.get('customer', instance.customer)
        instance.type = validated_data.get('date', instance.date)
        instance.save()
        return instance

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'quantity')
