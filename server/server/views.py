from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'POST'])
def users_list(request,format =None):

    #get all the drinks
    #serialize them
    #return json

    if request.method == 'GET':
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method == 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    

        

    


# here we're returning nothing other than object we can remove safe =False
# there are three ways of using API 
# admin page
# html page
# postman app
