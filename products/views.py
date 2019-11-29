from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #登入權限監視
from .models import Animal
from django.utils import timezone #django抓時間的東西
# Create your views here.


def product_list(request):
	return render(request, 'product_list.html') 

@login_required    #只有登入才可以啟動這頁面，輸入網址也來不了
def publish(request):
	if request.method == 'GET':
		return render(request, 'publish.html') 
	elif request.method == 'POST':
		animal_id = request.POST['編號']
		animal_variety = request.POST['品種']
		animal_sex = request.POST['性別']
		animal_old = request.POST['歲數']
		animal_size = request.POST['大小']
		animal_color = request.POST['毛色']
		animal_from = request.POST['來源地']
		animal_health = request.POST['健康情況']
		animal_remark = request.POST['備註']
		#animal_image = request.FILES['圖片']

			#以下寫入資料庫
		DBanimal = Animal() #需要import
		DBanimal.animal_id = animal_id
		DBanimal.animal_variety = animal_variety
		DBanimal.animal_sex = animal_sex
		DBanimal.animal_old = animal_old
		DBanimal.animal_size = animal_size
		DBanimal.animal_color = animal_color
		DBanimal.animal_from = animal_from
		DBanimal.animal_health = animal_health	
		DBanimal.animal_remark = animal_remark
		#DBanimal.animal_image = animal_image

		DBanimal.pub_data = timezone.datetime.now()
		DBanimal.animal_owner = request.user

		DBanimal.save()
		return redirect('主頁面')
		#except Exception as err:
		#	return render(request, 'publish.html', {'錯誤':'請上傳圖片'})

		
