from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Student, Room


class StudentForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput)
    middlename = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    type = 'S'
    course = forms.CharField(widget=forms.TextInput)
    year = forms.CharField(widget=forms.NumberInput)
    department = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Student
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname', 'course', 'year', 'department']

    def __int__(self,*args,**kwargs):
        super(StudentForm, self).__init__(*args,*kwargs)
        self.instance.type = self.type
        self.fields['middlename'].required=False

    def clean_year(self):
        year = self.cleaned_data['year']
        if int(year) > 5 or int(year) < 1:
            raise ValidationError('Year must be broken 1 - 5')
        else:
            return year

class RoomForm(ModelForm):
    roomID = forms.IntegerField(widget=forms.NumberInput)
    roomName = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Room
        fields = ['roomID', 'roomName']