from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCategories
from categories.models import Categories
from datetime import datetime
from utils.helpers import capitalize_titles, humanreadable_dates

# Create your views here.
def subcategories_list(request):
	categories = Categories.objects.order_by('category_name', 'id')
	subcategories = SubCategories.objects.order_by('category', 'subcategory_name')
	return render(request, 'backend/pages/subcategories/subcategories_list.html', {'subcategories': subcategories, 'categories': categories})

def subcategories_list_by_subcat(request, slug):
	#categories_id = 
	categories = Categories.objects.all()	
	subcategories = SubCategories.objects.filter(category__slug__iexact=slug)
	return render(request, 'backend/pages/subcategories/subcat_list.html', {'subcategories': subcategories, 'categories': categories})

def subcategories_list_add(request):
	
	if request.method == 'POST':
		subcategory_name = request.POST.get('subcategory_name')
		subcategory_description = request.POST.get('subcategory_description')
		#category_name = request.POST.get('category_name')
		category_id = int(request.POST.get('category_name'))
		print(type(category_id))
		if subcategory_name == "" or subcategory_description == "":
			errors = "All fields are Required"
			return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
		if len(SubCategories.objects.filter(subcategory_name=subcategory_name)) != 0:
			errors = "This subcategory " + subcategory_name + " already exists in the subcategory List"
			return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
	category_name = Categories.objects.get(pk=category_id).category_name
	catObj = SubCategories(subcategory_name=capitalize_titles(subcategory_name), subcategory_description=subcategory_description, category_name=category_name, category_id=category_id)
	catObj.save()
	return redirect('subcategories_list')	

def subcategories_list_delete(request, pk):
	#categories = Categories.objects.all()
	try:
		obj_to_be_deleted = SubCategories.objects.get(pk=pk)
		obj_to_be_deleted.delete()
		return redirect('subcategories_list')	
	except:
		errors = "An error has occured while deleting a Category"
		return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
	return redirect('subcategories_list')	

def subcategories_list_edit(request, pk):
	#categories = Categories.objects.all()
	print(request.POST)
	obj_to_be_update = SubCategories.objects.get(pk=pk)
	obj_to_be_update.save()
	return render(request, 'backend/pages/categories/edit.html', {'obj_to_be_update': obj_to_be_update})

def subcategories_list_view(request):
	subcategories = SubCategories.objects.all()
	return render(request, 'backend/pages/subcategories/subcategories_list.html', {'subcategories': subcategories})