from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from testapp.models import Student
from testapp.serializers import studentserializer
from django.http import HttpResponse
import io
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class Student_view(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=Student.objects.get(id=id)
            serializer=studentserializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Student.objects.all()
        serializer=studentserializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        serializer=studentserializer(data=data)
        if serializer.is_valid():#if not call this method assertion error get aries
            serializer.save()#it internally call create() method and save dta
            msg={'msg':'Resoursce created'}
            json_data=JSONRenderer().render(msg)#convert py dta to json to send it for patner application
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body # for geting data from patner appln i.e it is in json data
        stream=io.BytesIO(json_data) #convted into bytes
        pdata=JSONParser().parse(stream)#ptner appln dta convert into py dta
        id=pdata.get('id')#to get id which instance has to update ==>instance is already exixtin obj
        stu=Student.objects.get(id=id) #to pass id and we got id obj
        serilizer=studentserializer(stu,data=pdata,partial=True)#creating stu serializer obj with this provided pdata
        if serilizer.is_valid(): #If serializer is valid
            serilizer.save() #when we call this method then it ges to serialezer.py and call update method ad form that activity
            msg={'msg':'Resoursce updated successfully'} #if it ia valid it diaplay this msg
            json_data=JSONRenderer().render(msg)#if valid convert it into jsn dta
            return  HttpResponse(json_data,content_type='application/json')#sending response
        json_data=JSONRenderer().render(serilizer.errors) #when it is not valid data then send error to patner appln
        return HttpResponse(json_data,content_type='application/json',status=400)

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()#delete the data of respected id
        msg={'msg':"Resorce deleted succesfully"}#gives the msg
        json_data=JSONRenderer().render(msg)#convert it into json
        return HttpResponse(json_data,content_type='application/json')
