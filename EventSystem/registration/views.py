from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import StudentForm, RoomForm


# Create your views here.

class HomeView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


class RegisterStudent(View):
    template = 'createStudent.html'

    def get(self, request):
        form = StudentForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})


class RegisterRoom(View):
    template = 'createRoom.html'

    def get(self, request):
        form = RoomForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:index'))
        return render(request, self.template, {'form': form})



