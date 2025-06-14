from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        orders = Order.objects.all().order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = Product.objects.get(id=request.data['product'])
                quantity = int(request.data['quantity'])
                if product.stock < quantity:
                    return Response({'error': 'Not enough stock'}, status=400)

                order = Order(product=product, quantity=quantity)
                order.save()

                return Response(OrderSerializer(order).data, status=201)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=404)
        return Response(serializer.errors, status=400)
