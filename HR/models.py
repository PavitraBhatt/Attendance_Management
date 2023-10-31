from django.db import models
from Department.models import Department
import io

from PIL import Image 
# Create your models here.

class HR(models.Model):
#     def name(instance,filename):
#         return '/'.join('images',str(instance.HRID),filename)

    HRID = models.CharField(max_length=100,primary_key=True)
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile = models.IntegerField()
    DOB = models.DateField()
    HouseNumber = models.CharField(max_length=100)
    ApartmentNumber = models.CharField(max_length=100)
    Landmark = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State =  models.CharField(max_length=100)
    PIN = models.IntegerField()
    BloodGroup = models.CharField(max_length=100)
    NickName = models.CharField(max_length=100)
    EmergencyNumber = models.IntegerField()
    MatrialStatus = models.CharField(max_length=100)
    DepartmentID = models.ForeignKey(Department, on_delete = models.CASCADE,null=True)
    TimeZone = models.CharField(max_length=100)
    JoiningDate = models.DateField()
    AboutMe = models.CharField(max_length=100)
    Photo = models.ImageField()
    LegalDocument = models.ImageField() 
    # def save_image_to_field(self, image_data):
    #     img = Image.open(image_data)
    #     buffered = io.BytesIO()
    #     img.save(buffered, format="JPEG")  # You can specify the image format you're using
    #     self.photo = buffered.getvalue()    

    def __str__(self):
        return self.HRID