from django.db import models

# Create your models here.

class User(models.Model):
    type_user = (('S', 'Student'), ('T', 'Teacher'))
    username = models.CharField(max_length=15, null=False, primary_key=True)
    password = models.CharField(max_length=10, null=False)
    firstname = models.CharField(max_length=50, null=False)
    middlename = models.CharField(max_length=50, null= True)
    lastname = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=1, choices=type_user)


class Student(User):
    #username = models.CharField(max_length=15, null=False, primary_key=True)
    course = models.CharField(max_length=15, null=False)
    year = models.IntegerField(default=1, null= False)
    department = models.CharField(max_length=50, null= False)


class Teacher(User):
    age = models.IntegerField(default=1)


class Specialization(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)

    class Meta:
        unique_together = ('teacher', 'specialization')

class Room(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomName = models.CharField(max_length=50)

class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    evenTitle = models.CharField(max_length=150)
    dateOfEvent = models.DateField()
    maxParticipants = models.IntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student, related_name='attend', through='AttendEvent')

class AttendEvent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateRegistered = models.DateField()


