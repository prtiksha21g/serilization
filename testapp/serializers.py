from rest_framework import serializers
from testapp.models import Student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
# class studentserializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     rollno = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
# #if we want to senf pos req compulsory we have tp call create() method insdie serializer class
#     def create(self,validated_data):#by passing this validated_data cretae method will crate dta
#         return Student.objects.create(**validated_data)
#     #**validated_data contain several key-value pairs with all pairs create validate data
#
#     def update(self,instance,validated_data):
#         instance.rollno=validated_data.get('rollno',instance.rollno)
#         instance.name = validated_data.get('name', instance.name)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#         #instance==>shows current create obj present in db
#         #validated_data==>shows patner appln  proviede data
#         #instance.rollno==>if patner appln provided data related to rollno consider taht value and assign that to
#         # rollno if not given rollno,then consider existing obj as it is
#
