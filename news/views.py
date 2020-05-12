from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import News
from main.models import Main
from categories.models import Categories
from subcategories.models import SubCategories
from utils.helpers import str2bool, humanbytes
import datetime
import arrow

IMAGE_FILE_TYPE = ['png', 'jpg', 'jpge']

utc = arrow.now()
localTime = utc.to('US/Eastern')


# Create your views here.
def news_detail(request, slug):
	site = Main.objects.get(pk=2)
	news = News.objects.filter(slug__iexact=slug).order_by('article_date_created')
	for nn in news:
		print(nn.id)
	return render(request, 'front/news_details.html', {'news': news, 'site': site })

def profile(request):
	news = News.objects.all()
	return render(request, 'backend/pages/list/profile.html', {'news': news})

def add_news_profile(request):
	article_picture_name = 'default.png'
	article_picture_url = '/media/default/default.png'
	article_percentage = 50
	article_status = 'warning'		
	article_date = utc.to('US/Eastern').format('MM/DD/YYYY | HH:mm:ss A')
	article_live = False
	#form fields
	article_name = request.POST.get('article_name')
	article_short = request.POST.get('article_short')
	article_author = request.POST.get('article_author')
	article_body = request.POST.get('article_body')
	print(article_date)
	if request.method == 'POST':
		if article_name == "" or article_short == "" or article_author == "" or article_body == "" :			
			errors = "All fields are required"
			return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
		else:
			send_form = News(
				article_name=article_name, 
				article_short=article_short, 
				article_author=article_author, 
				article_date=article_date, 
				article_body=article_body, 
				article_percentage=article_percentage, 
				article_status=article_status, 
				article_live=article_live,
				article_picture_name=article_picture_name,
				article_picture_url=article_picture_url
			)
			send_form.save()
			return redirect('profile')
	return redirect('profile')

def news_list(request):
	news = News.objects.all()
	return render(request, 'backend/pages/list/list.html', {'news': news})

def test_update(request):
	#print(request.POST)
	if request.method == 'POST':
		article_name_id = request.POST.get('article_name_id', '')
		checked = request.POST.get('check', '')
		print (type(checked))
		print(str2bool(checked))

		todo = News.objects.get(id=article_name_id)
		todo.article_live = str2bool(checked)
		todo.save()
		return redirect('news_list')
	return redirect('news_list')

def add_news(request):

	categories = Categories.objects.all()
	subcategories = SubCategories.objects.all()

	try:
		if request.method == 'POST' and request.FILES['article_picture']:
			#print ('Form data has been sent suffesfully... ')

			category_id = request.POST.get('article_category')
			subcategory_id = request.POST.get('article_subcategory')

			article_name = request.POST.get('article_name')
			article_short = request.POST.get('article_short')
			article_author = request.POST.get('article_author')
			article_date = utc.to('US/Eastern').format('MM/DD/YYYY | HH:mm:ss A')
			#article_picture = request.POST.get('article_picture')
			#article_category = request.POST.get('article_category')
			article_body = request.POST.get('article_body')

			if article_name == "" or article_short == "" or article_body == "":
				errors = "All fields are required"
				return render(request, 'backend/pages/errors/errors.html', {'errors': errors})
			else:
				try:
					article_percentage = 100
					article_status = 'success'
					image_file = request.FILES.get('article_picture')
					fs = FileSystemStorage()
					filename = fs.save(image_file.name, image_file)
					image_url = fs.url(filename)
					if str(image_file.content_type).startswith("image"):
						print(image_file.size)						
						if image_file.size < 5000000:
							success = "News post has been created succesfully"
							imageUpload = "Image uploaded succesfully " + image_file.name
							category_name = Categories.objects.get(pk=category_id).category_name

							subcategory_name = SubCategories.objects.get(pk=subcategory_id).subcategory_name
							
							send_form = News(
								article_name=article_name, 
								article_short=article_short, 
								article_body=article_body, 
								article_category=category_name,
								article_subcategory=subcategory_name, 
								article_date=article_date, 
								article_picture_name=filename, 
								article_picture_url=image_url, 
								article_author=article_author, 
								article_percentage=article_percentage, 
								article_status=article_status,
								article_live=True,
								article_image_size=image_file.size,
							)
							send_form.save()
							return render(request, 'backend/pages/list/success.html', {'success': success, 'imageUpload': imageUpload})
						else:
							print('Image size greater than 5MB')
							errorsImage = "You file is not supported excedd the limit of 5MB. File size: " + str(humanbytes(image_file.size))
							return render(request, 'backend/pages/list/errorsImage.html', {'errorsImage': errorsImage})	
					else:
						fs = FileSystemStorage()
						fs.delete(filename)
						errorsImage = "You file is not supported only image files. " + image_file.content_type.split('/')[-1].upper() + "  invalid."
						return render(request, 'backend/pages/errors/errorsImage.html', {'errorsImage': errorsImage})
				except:
					errorsImage = "Please select an Image" + image_file.size
					return render(request, 'backend/pages/errors/errorsImage.html', {'errorsImage': errorsImage})
		return render(request, 'backend/pages/list/add.html', {'categories': categories, 'subcategories': subcategories})
	except:
		errorsImage = "Please select an Image"
		return render(request, 'backend/pages/errors/errorsImage.html', {'errorsImage': errorsImage})

def news_delete(request, pk):
	try:
		to_be_deleted = News.objects.get(pk=pk)
		print(to_be_deleted.article_picture_name)
		if to_be_deleted.article_picture_name == 'default.png':
			to_be_deleted.delete()
			return redirect('news_list')
		else:
			fs = FileSystemStorage()
			fs.delete(to_be_deleted.article_picture_name)
			to_be_deleted.delete()
			return redirect('news_list')
	except:
		errors = "Error deleting"
		return render(request, 'backend/pages/errors/errorsImage.html', {'errors': errors})
	return redirect('news_list')

def edit_news(request, pk):
	news = News.objects.filter(pk=pk)
	categories = Categories.objects.all()
	subcategories = SubCategories.objects.order_by('category_name', 'subcategory_name')
	return render(request, 'backend/pages/list/edit.html', {'news': news, 'categories': categories, 'subcategories': subcategories})

def tables(request):
	#news = News.objects.all()
	return render(request, 'backend/pages/tables/data.html')
