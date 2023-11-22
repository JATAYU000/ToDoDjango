from django.shortcuts import render, redirect #for redirect to login page
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages #for alert message
from django.views.generic import ListView, DetailView,DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

def main(request):
	context = {
		'items': Task.objects.all()
	}
	return render(request,'todo/home.html',context)



class TaskListView(ListView):
	model = Task
	template_name = 'todo/home.html'
	context_object_name = 'items'
	# def get_context_data(self,**kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['items']=context['items'].filter(user=self.request.user)
	# 	return context


class TaskDetailView(DetailView):# will check app/model_task.html
	model = Task

class TaskCreateView(LoginRequiredMixin,CreateView):# will check app/model_task.html
	model = Task
	success_url='/'
	fields=['taskname','description','status']
	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):# will check app/model_task.html
	model = Task
	success_url='/'
	fields=['taskname','description','status']
	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)
	def test_func(self):
		task = self.get_object()
		if self.request.user == task.user:
			return True
		return False


class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):# will check app/model_task.html
	model = Task
	success_url='/'
	def test_func(self):
		task = self.get_object()
		if self.request.user == task.user:
			return True
		return False

def login(request):
	return render(request,'todo/login.html')

def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}! You can now Login.')
			return redirect('login-page')
	else:
		form = UserCreationForm()
	return render(request,'todo/register.html',{'form':form})