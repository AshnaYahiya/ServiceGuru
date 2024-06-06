from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import authentication,permissions

from api.serializers import CustomerSerializer,WorkSerializer

from api.models import Customer

from rest_framework.decorators import action



class CustomerViewSetView(ModelViewSet):

    serializer_class=CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):
        
        serializer.save(technician=self.request.user)

 # ========= CUSTOM METHOD =======================

 
    @action(methods=['post'],detail=True)          # action decorater is used to know which method
    def add_work(self,request,*args,**kwargs):     #oru customerine edukumpol pullide work adeel varanam athin venditt  ee class nte ollil thanne kodukunnu ======
                                                            
        id=kwargs.get('pk')

        # customer_instance=self.get_object()

        customer_instance=Customer.objects.get(id=id)

        serializer=WorkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(customer=customer_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)




    




