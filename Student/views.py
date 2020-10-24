from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,UpdateView,DeleteView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Student,Contact,Address
from .serializers import StudentGetSerializer,StudentMiniSerializer
from .forms import CreateStudentForm,CreateAddressForm,CreateContactForm,UpdateStudentForm,UpdateAddressForm,UpdateContactForm

# Create your views here.

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('homenew')
    return render(request,"pages/tableaddstudent.html")

def homepage_view(request):
    return render(request,"pages/homepage.html")

''' need to do more research still (not being used)'''
def add_studentform_view(request):
    return render(request,"components/addstudentform.html")

''' the django form function way (working fine) but found better way'''
def add_student_view(request): 
    studentform = StudentForm(request.POST or None)
    if studentform.is_valid():
        studobj = studentform.save(commit=False)
        studobj.save()
        form = StudentForm()

    addressform = AddressForm(request.POST or None)
    if addressform.is_valid():
        addobj = addressform.save(commit=False)
        addobj.save()
        addressform = AddressForm()

    contactform = ContactForm(request.POST or None)
    if contactform.is_valid():
        contobj = contactform.save(commit=False)
        contobj.save()
        contactform = ContactForm()
    
    data = {
        "studentform":studentform,
        "addressform":addressform,
        "contactform":contactform
        }
    return render(request,'components/studentform.html',context=data) # need to change this template as we updated

''' django Class form way '''
class StudentCreate(CreateView):
    model = Student
    form_class = CreateStudentForm
    template_name = 'forms/createStudentForm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StudentUpdate(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    template_name = 'forms/updateStudentForm.html'
    
    def get_success_url(self):
        pk = self.kwargs["pk"]
        student = Student.objects.get(id = pk)

        try:
            addressID = Address.objects.get(student = student).id
            return reverse("updateAddress", kwargs={"pk": addressID})

        except Address.DoesNotExist:
            print("There is no address for this student")
            return reverse('home')
            

class AddressCreate(CreateView):
    model = Address
    form_class = CreateAddressForm
    template_name = 'forms/createAddressForm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        if not self.request.user.is_authenticated:
            return None
        form = super().get_form(form_class=self.form_class)
        student = Student.objects.filter(user = self.request.user)
        form.fields['student'].queryset = student.filter(addresses = None)
        return form


class AddressUpdate(UpdateView):
    model = Address
    form_class = UpdateAddressForm
    template_name = 'forms/updateAddressForm.html'
    
    def get_success_url(self):
        addressId = self.kwargs["pk"]
        student = Address.objects.get(id = addressId).student

        try:
            contactID = Contact.objects.get(student = student).id
            return reverse("updateContact", kwargs={"pk": contactID})

        except: 
            print("There is no contact present for this student")
            return reverse('home')


class ContactCreate(CreateView):
    model = Contact
    form_class = CreateContactForm
    template_name = 'forms/createContactForm.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        if not self.request.user.is_authenticated:
            return None
        form = super().get_form(form_class=self.form_class)
        student = Student.objects.filter(user = self.request.user)
        form.fields['student'].queryset = student.filter(contacts = None)
        return form


class ContactUpdate(UpdateView):
    model = Contact
    form_class = UpdateContactForm
    template_name = 'forms/updateContactForm.html'
    success_url = reverse_lazy('home')


class StudentDelete(DeleteView):
    model = Student
    template_name = 'forms/deleteStudent.html'
    success_url = reverse_lazy('home')

    
'''used for testing purpose'''
def student_list_view(request):
    students = Student.objects.all()
    students_list = [{"name":student.full_name,"age":student.age} for student in students]
    data = {
        "response":students_list
    }
    return JsonResponse(data, status = status.HTTP_200_OK)
    
''' API List View '''
class GetStudentsMini(APIView):

    def get(self, request):
        qs = Student.objects.all()
        if self.request.user.is_authenticated:
            students = qs.filter(user = self.request.user)
            serializer = StudentMiniSerializer(students, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)


class GetStudentDetail(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        if not self.request.user.is_authenticated:
            return Response(status = status.HTTP_401_UNAUTHORIZED)    
        student = self.get_object(id)
        serializer = StudentGetSerializer(student)
        return Response(serializer.data, status = status.HTTP_200_OK)


def studentDetail(request, id):
    context = {'studentid':id}
    return render(request,'pages/studentdetail.html',context)

'''testing purpose'''
def get_address(request,id):
    student = Student.objects.get(id = id)
    address = student.addresses.first()
    contact = student.contacts.first()
    print('Housename is: ',address.housename)
    print('Society is: ',address.society)
    print('StreetNo is: ',address.streetno) 
    print('ContactNo is:',contact.phone)
    print('ContactNo is:',contact.email)
    return JsonResponse({}, status = status.HTTP_200_OK)
    
'''testing purpose'''
def get_addressid(request,pk):
    student = Student.objects.get(id = pk)
    address = Address.objects.get(student = student)
    addressid = address.id
    print(addressid)
    return JsonResponse({})

def addStudentCard(request):
    return render(request,'pages/studentcard.html')

