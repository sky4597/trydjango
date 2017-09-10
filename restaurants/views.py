from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

# Create your views here.
#function based view

# def home_old(request):
# 	html_var='f strings'
# 	html_ = f"""
# 	<!DOCTYPE HTML>
# 	<html lang=en>	
# 	<head>
# 	</head>
# 	<body>
# 	<h1>Hello World!</h1>
# 	<p>This is html coming through!</p>
# 	<p>This is {html_var} coming through!</p>

# 	"""
# 	return HttpResponse(html_)

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context= {
	"object_list":queryset
	}

	return render(request,template_name, context)

class RestaurantListView(ListView):


	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |  Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

class SearchRestaurantListView(ListView):
	template_name = 'restaurants/restaurants_list.html'

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |  Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.none()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(RestaurantDetailView, self).get_context_data(*args,**kwargs)
		print(context)
		return context

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation,id=rest_id) #pk = rest_id
	# 	return obj


	

def home(request):
	

	num	= None
	some_list = [
	random.randint(0,10000),
	random.randint(0,100),
	random.randint(50,100000)
	]

	condition_bool_item = True

	if condition_bool_item:
		num = random.randint(0,100000) 
	context = {
	"num":num,
	"some_list":some_list
	}
	return render(request,"home.html",context)			#response

def about(request):
	context = {
	}
	return render(request,"about.html",context)			#response

def contact(request):
	context = {
	}
	return render(request,"contact.html",context)			#response

class ContactView(View):
	def get(self, request, *args, **kwargs):
		# print(kwargs)
		context={}
		return render(request,"contact.html",context)

	def put(self, request, *args, **kwargs):
		# print(kwargs)
		context={}
		return render(request,"contact.html",context)

	def post(self, request, *args, **kwargs):
		# print(kwargs)
		context={}
		return render(request,"contact.html",context)

# class HomeView(TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args,**kwargs)
# 		num	= None
# 		some_list = [
# 		random.randint(0,10000),
# 		random.randint(0,100),
# 		random.randint(50,100000)
# 		]

# 		condition_bool_item = True

# 		if condition_bool_item:
# 			num = random.randint(0,100000) 
# 		context = {
# 		"num":num,
# 		"some_list":some_list
# 		}
# 		return context

		