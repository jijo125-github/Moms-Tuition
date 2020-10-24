from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

User = settings.AUTH_USER_MODEL

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'students')
    firstname = models.CharField(max_length = 20)
    middlename = models.CharField(max_length = 20, blank = True, default = '')
    lastname = models.CharField(max_length = 20, blank = True, default = '')
    age = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    standard = models.PositiveIntegerField(validators = [MaxValueValidator(12)])
    joining_date = models.DateField(auto_now_add = True)
    leaving_date = models.DateField(blank = True, null=True)

    @property
    def student_address(self):
        return self.addresses.all()

    @property
    def student_contact(self):
        return self.contacts.all()

    @property
    def full_name(self):
        name = self.firstname
        if self.middlename is not None:
            name += ' ' + self.middlename
        if self.lastname is not None:
            name += ' ' + self.lastname 
        return name
    
    def get_absolute_url(self):
        return reverse('addAddress')

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "Student Info"
        ordering = ['-id']
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete = models.CASCADE, related_name = 'addresses')
    housename = models.CharField(max_length = 50, blank = True, default = '')
    society = models.CharField(max_length = 100)
    streetno = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(15)])
    pincode = models.PositiveIntegerField(validators = [MinValueValidator(100000), MaxValueValidator(999999)])
    district = models.CharField(max_length = 50, blank = True, default = 'Rajkot')

    class Meta:
        verbose_name_plural = "Student_Address_Details"
    
    def get_absolute_url(self):
        return reverse('addContact')

    def __str__(self):
        taddress = str(self.student) + ' address'
        return taddress  
        

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete = models.CASCADE, related_name = 'contacts')
    phone = models.PositiveIntegerField(validators = [MinValueValidator(8000000000), MaxValueValidator(9999999999)]) 
    phone2 = models.PositiveIntegerField(validators = [MinValueValidator(8000000000), MaxValueValidator(9999999999)])
    email = models.EmailField(blank = True, default = '') 

    class Meta:
        verbose_name_plural = "Student_Contact_Details"
    
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        tcontact = str(self.student) + ' Contact Details'
        return tcontact

    
      


    
