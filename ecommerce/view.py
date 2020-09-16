from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect



from .forms import ContactForm

def home_page(request):
	#print(request.session.get("first_name", "Unknown"))
	# request.session['first_name']
	context = {
		"title":"Hello World This is Home page",
		"content":"Hello,Chandan kumar using template you are doing django world! Home Page"
		
	}
	if request.user.is_authenticated():
		context["primium_content"] = "How waonder full of django series"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"Hello World This is About Us page",
		"content":"Hello,Chandan kumar using template you are doing django world! About Us Page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Hello World This is Contact Us page",
		"content":"Hello,Chandan kumar using template you are doing django world! Contact Us Page",
		"form":contact_form,
		"brand":"New Brand Name of the ecommerce Python django"
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	#if request.method == "POST":
		#print(request.POST)
		# print(request.POST.get('name'))
		# print(request.POST.get('email'))
		# print(request.POST.get('content'))
	return render(request, "contact/view.html", context)	

