from django.db import models


# Create your models here.
# Table for contact page .
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=70)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name + "--" + self.email


# Table for Personlist
class Allperson(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=130, default="this-s")
    image = models.ImageField(upload_to="myapp/images", default="upload-image")
    content = models.TextField()

    def __str__(self):
        return "Member " + self.name


# Table for Person Particular
class Member(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    )
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dsize = models.DecimalField(max_digits=4, decimal_places=2)
    speciality = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    content = models.TextField()

    def __str__(self):
        return "Detail of " + self.name + "-- " + "of speciality " + self.speciality
