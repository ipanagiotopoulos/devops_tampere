from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import dateparse
from .models import Request
from .serializers import RequestSerializer
from .helper import get_client_ip
from datetime import datetime
import os
import signal

class RequestListApiView(APIView):

    # 1. List all request made by service 1
    def get(self, request, *args, **kwargs):

        requests_serv_1 = Request.objects.filter().all()
        serializer = RequestSerializer(requests_serv_1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create request models objects that have been sent by service 1
    def post(self, request, *args, **kwargs):
        data = {
            'ipv4_address': get_client_ip(request),
            'name': request.data.get("name"),
            'message': request.data.get("message"),
            'timestamp': datetime.now().isoformat(),
            'http_method': "POST",
        }

        if (data.get('message') != "STOP"):
            msg = data.get('message') +" "+ data.get("ipv4_address")+":"+os.getenv("CLIENT_PORT")    #request.META['SERVER_PORT']
        else:
            msg = data.get('message')
        if  msg is not None:
            with open('/application_django/logs/service2.log', 'a') as f:
             if f.tell() == 0:
                print('service2.log does not exist, initializing...')
                f.write(msg+'\n')
             else:
                print('service2.log exists, appending to file')
                f.write(msg+'\n')
        if msg == "STOP":
                   print("SIGINT signal received by server 1: "+data.get('ipv4_address')+":"+request.META.get('SERVER_PORT'))
                   os.kill(os.getpid(), signal.SIGINT)
        data.update(message=msg)
        serializer = RequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
