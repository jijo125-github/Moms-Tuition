from rest_framework import serializers
from .models import Student,Address,Contact

class AddressGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ['housename','society','streetno','pincode','district']

class ContactGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['phone','phone2','email']

class StudentMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','full_name','age','gender','joining_date']

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['firstname','middlename','lastname','age','gender','standard']
    
    def validate(self, data):
        if data['age'] < 0:
            raise serializers.ValidationError({
                'error':'Age should be greater than 0'
            })
        return data


class StudentGetSerializer(serializers.ModelSerializer):
    student_address = AddressGetSerializer(many = True)
    student_contact = ContactGetSerializer(many = True)

    class Meta:
        model = Student
        fields = ['id','full_name','age','gender','standard','joining_date','student_address','student_contact']
        read_only_fields = ['id','joining_date']
        

'''not being used yet as of now'''
class PostStudentSerializer(serializers.ModelSerializer):
    housename = serializers.SerializerMethodField(read_only=True)
    society = serializers.SerializerMethodField(read_only=True)
    streetno = serializers.SerializerMethodField(read_only=True)
    pincode = serializers.SerializerMethodField(read_only=True)
    district = serializers.SerializerMethodField(read_only=True)
    phone = serializers.SerializerMethodField(read_only=True)
    phone2 = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = [
           'firstname',
           'middlename',
           'lastname',
           'age',
           'gender',
           'standard',
           'housename',
           'society',
           'streetno',
           'pincode',
           'district',
           'phone',
           'phone2',
           'email'
            ]
        
    def get_housename(self,obj):
        return obj.addresses.first().housename

    def get_society(self,obj):
        return obj.addresses.first().society

    def get_streetno(self,obj):
        return obj.addresses.first().streetno
        
    def get_pincode(self,obj):
        return obj.addresses.first().pincode

    def get_district(self,obj):
        return obj.addresses.first().district

    def get_phone(self,obj):
        return obj.contacts.first().phone
    
    def get_phone2(self,obj):
        return obj.contacts.first().phone2

    def get_email(self,obj):
        return obj.contacts.first().email

