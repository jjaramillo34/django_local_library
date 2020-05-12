from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categories, CategoriesResource
from tablib import Dataset

# Create your views here.
def categories_list(request):
	categories = Categories.objects.all()
	for cat in categories:
		print (cat.id)
		print (cat.slug)
	return render(request, 'backend/pages/categories/categories_list.html', {'categories': categories})

def categories_list_add(request):
	#categories = Categories.objects.all()
	if request.method == 'POST':
		category_name = request.POST.get('category_name')
		category_description = request.POST.get('category_description')
		if category_name == "" or category_description == "":
			errors = "All fields are Required"
			return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
		if len(Categories.objects.filter(category_name=category_name)) != 0:
			errors = "This category " + category_name + " already exists in the category List"
			return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
	catObj = Categories(category_name=category_name, category_description=category_description)
	catObj.save()
	return redirect('categories_list')	

def categories_list_delete(request, pk):
	#categories = Categories.objects.all()
	try:
		obj_to_be_deleted = Categories.objects.get(pk=pk)
		obj_to_be_deleted.delete()
		return redirect('categories_list')	
	except:
		errors = "An error has occured while deleting a Category"
		return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
	return redirect('categories_list')	

def categories_list_edit(request):
	#categories = Categories.objects.all()
	print(request.POST)
	obj_to_be_update = Categories.objects.all()
	obj_to_be_update.save()
	return render(request, 'backend/pages/categories/edit.html', {'obj_to_be_update': obj_to_be_update})

#export_import files import files
def import_data(request):
	if request.method == 'POST' and request.FILES['importData']:
		print(request.POST)
		file_format = request.POST['file-format']
		employee_resource = CategoriesResource()
		dataset = Dataset()
		new_employees = request.FILES['importData']
		for data in dataset:
			print()
		if file_format == 'CSV':
			imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
			result = employee_resource.import_data(dataset, dry_run=True)
		elif file_format == 'JSON':
			imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
			result = employee_resource.import_data(dataset, dry_run=True)
		elif file_format == 'XLS':
			imported_data = dataset.load(new_employees,format='xls')
			result = employee_resource.import_data(dataset, dry_run=True)
		elif file_format == 'XLSX':
			imported_data = dataset.load(new_employees.read().decode('utf-8'),format='xlsx')
			result = employee_resource.import_data(dataset, dry_run=True)
		
		if not result.has_errors():
			employee_resource.import_data(dataset, dry_run=False)
		#return render(request, 'import.html')
	return redirect('categories_list')

#export_import files export files
def export_csv(request):
    person_resource = CategoriesResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="categories.csv"'
    return response

def export_excel(request):
    person_resource = CategoriesResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="categories.xls"'
    return response

def export_json(request):
    person_resource = CategoriesResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="categories.json"'
    return response

