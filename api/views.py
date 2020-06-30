from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import customer
from .serializers import customerserializers
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http.response import JsonResponse
# Create your views here.

@api_view(["GET", "POST","DELETE"])
def show_list(request):
    if (request.method == "GET"):
        data = customer.objects.all()
        serializers = customerserializers(data, many=True)
        return Response(serializers.data)
    elif(request.method == "POST"):
        serializers =  customerserializers(data = request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == "DELETE"):
        count = customer.objects.all().delete()
        return JsonResponse({'message': '{} customer were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","DELETE"])
def customer_details(request, pk):
    try:
        cust = customer.objects.get(pk=pk)
        if request.method == 'GET':
            serializers = customerserializers([cust], many=True)
            return Response(serializers.data)
        elif request.method == 'DELETE':
            cust.delete()
            return JsonResponse({'message': 'Custmer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)











