from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.forms.models import model_to_dict
from .serializers import OperationSerializer
import ipdb

class OperationsView(APIView):
    def post(self, request: Request) -> Response:
        
        lista = request.data['data']
        
        lista_formatada = []
        
        operations = []
        
        shops = []
        
        for i in lista:
            object = {}
       
        
        
            object["Transaction_type"] = i[0:0+1]
            object["Data"]= f'{i[0+7:0+9]}/{i[0+5:0+7]}/{i[0+1:0+5]}'
            object["Value"] = f'R${int(i[0+9:0+19])},00'
            object["CPF"] = f'{i[0+19:0+22]}.{i[0+22:0+25]}.{i[0+25:0+28]}-{i[0+28:0+30]}'
            object["Card"] = f'{i[0+30:0+42]}'
            object["Time"] = f'{i[0+42:0+44]}:{i[0+44:0+46]}:{i[0+46:0+48]}'
            object["Owner"] = f'{i[0+48:0+62].rstrip()}'
            object["Shop_name"] = f'{i[0+62:0+80].rstrip()}'
            
            
            lista_formatada.append(object)

        for operation in lista_formatada:
            serializer = OperationSerializer(data=operation)
            serializer.is_valid()
            serializer.save()
            operations.append(serializer.data)
        

        for operation in operations:
            counter = 0
            for shop in shops:
                if operation["Shop_name"] in shop["Name"]:
                    if operation["Transaction_type"] == "Saída":
                        shop["Total"] = f'R${float(shop["Total"][2:-3]) - float(operation["Value"][2:-3])}'

                        shop["Transactions"] = [*shop["Transactions"], operation]
                    else:
                        shop["Total"] = f'R${float(shop["Total"][2:-3]) + float(operation["Value"][2:-3])}'
                
                        
                        shop["Transactions"] = [*shop["Transactions"], operation]
                        
                     
                    
                    counter = counter + 1
            
            if counter < 1:
                
                shop_info = {}
                shop_info["Name"] = operation["Shop_name"]
                shop_info["Owner"] = operation["Owner"]
                if operation["Transaction_type"] == "Saída":
                    shop_info["Total"] = f'R${0 - float(operation["Value"][2:-3])}'
                    shop_info["Transactions"] = []
                    shop_info["Transactions"].append(operation)
                    
                else:
                    shop_info["Total"] = f'R${0 + float(operation["Value"][2:-3])}'
                    shop_info["Transactions"] = []
                    shop_info["Transactions"].append(operation)
               
                
                
                shops.append(shop_info)

                
        
        return Response(shops, 200)