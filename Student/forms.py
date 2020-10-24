from django import  forms
from .models import Student,Address,Contact

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', 'joining_date', 'leaving_date')

        widgets = {
            'firstname' : forms.TextInput(attrs = {
                'class' : 'form-control',
                }),

            'middlename' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : '(optional)'
                }),

            'lastname' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : '(optional)'
                }),

            'age' : forms.NumberInput(attrs = {
                'class' : 'form-control',
                }),

            'gender' : forms.Select(attrs = {
                'class' : 'form-control',
                }),

            'standard' : forms.NumberInput(attrs = {
                'class' : 'form-control',
                }),
        }

        
class CreateAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('student','housename','society','streetno','pincode','district')

        widgets = {
            'student' : forms.Select(attrs = {'class' : 'form-control'}),
            'housename' : forms.TextInput(attrs = {
                'class' : 'form-control',
                }),
            'society' : forms.TextInput(attrs = {
                'class' : 'form-control',
                }),
            'streetno' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'pincode' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'district' : forms.TextInput(attrs = {'class' : 'form-control'})
        }


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user']

        widgets = {
            'student' : forms.Select(attrs = {'class' : 'form-control'}),
            'phone' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'phone2' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs = {'class' : 'form-control'})
        }

        labels = {
            'phone':'Mobile No',
            'phone2':'Mobile No2'
            }


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user', 'joining_date', 'leaving_date')

        widgets = {
            'firstname' : forms.TextInput(attrs = {
                'class' : 'form-control',
                }),

            'middlename' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : '(optional)'
                }),

            'lastname' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : '(optional)'
                }),

            'age' : forms.NumberInput(attrs = {
                'class' : 'form-control',
                }),

            'gender' : forms.Select(attrs = {
                'class' : 'form-control',
                }),

            'standard' : forms.NumberInput(attrs = {
                'class' : 'form-control',
                }),
        }


class UpdateAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('housename','society','streetno','pincode','district')

        widgets = {
            'housename' : forms.TextInput(attrs = {
                'class' : 'form-control',
                }),
            'society' : forms.TextInput(attrs = {
                'class' : 'form-control',
                }),
            'streetno' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'pincode' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'district' : forms.TextInput(attrs = {'class' : 'form-control'})
        }
        

class UpdateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone','phone2','email')

        widgets = {
            'phone' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'phone2' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs = {'class' : 'form-control'})
        }

        labels = {
            'phone':'Mobile No',
            'phone2':'Mobile No2'
            }
