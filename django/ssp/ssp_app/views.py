from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt

from .serializers import *
from .models import Sistem1, Sistem2, Sistem3

def webview(request):
    """A view of all bands."""
    view1 = Sistem1.objects.all().values()
    view2 = Sistem2.objects.all().values()
    view3 = Sistem3.objects.all().values()
    return render(request, 'webview.html', {'views1': view1, 'views2':view2, 'views3':view3})

# class SensorDetails(RetrieveUpdateDestroyAPIView):
#     serializer_class = SensorSerializer
#     queryset = Sensor.objects.all()
#     def retrieve(self, request, *args, **kwargs):
#         temp = Sensor.objects.get(name="temp")
#         frik = Sensor.objects.get(name="frik")
#         dl = Sensor.objects.get(name="dl")
#         sensor_value={"Sensor Temperatur": int(temp.value), "Sensor Friksi": int(frik.value),"Sensor Daya Listrik": int(dl.value)}
#         return Response(sensor_value)     

def on_message_konduktivitas(client, userdata, msg):
    konduktivitas = Sistem1.objects.get(name="konduktivitas")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem1Serializer(konduktivitas, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new konduktivitas data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')}) 
    
def on_message_tekanan(client, userdata, msg):
    tekanan = Sistem1.objects.get(name="tekanan")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem1Serializer(tekanan, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new tekanan data ', msg.payload.decode('utf-8'))   
    return Response({"value": msg.payload.decode('utf-8')})
    
def on_message_temperatur(client, userdata, msg):
    temperatur = Sistem1.objects.get(name="temperatur")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem1Serializer(temperatur, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new temperatur data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_ph(client, userdata, msg):
    ph = Sistem2.objects.get(name="ph")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem2Serializer(ph, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new ph data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_oksigen(client, userdata, msg):
    oksigen = Sistem2.objects.get(name="oksigen")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem2Serializer(oksigen, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new oksigen data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_aliran(client, userdata, msg):
    aliran = Sistem2.objects.get(name="aliran")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem2Serializer(aliran, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new aliran data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_gas(client, userdata, msg):
    gas = Sistem3.objects.get(name="gas")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem3Serializer(gas, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new gas data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_suara(client, userdata, msg):
    suara = Sistem3.objects.get(name="suara")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem3Serializer(suara, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new suara data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_kelembaban(client, userdata, msg):
    kelembaban = Sistem3.objects.get(name="kelembaban")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = Sistem3Serializer(kelembaban, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        print('recieved a new kelembaban data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

client = mqtt.Client("ssp_app")

client.message_callback_add('ssp/konduktivitas', on_message_konduktivitas)
client.message_callback_add('ssp/tekanan', on_message_tekanan)
client.message_callback_add('ssp/temperatur', on_message_temperatur)

client.message_callback_add('ssp/ph', on_message_ph)
client.message_callback_add('ssp/oksigen', on_message_oksigen)
client.message_callback_add('ssp/aliran', on_message_aliran)

client.message_callback_add('ssp/gas', on_message_gas)
client.message_callback_add('ssp/suara', on_message_suara)
client.message_callback_add('ssp/kelembaban', on_message_kelembaban)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('ssp/#')
