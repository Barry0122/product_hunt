#這裡是account的view 
#專門處理相對應動作

from django.shortcuts import render , redirect
from django.contrib.auth.models import User #導入django內有的用戶註冊模板
# Create your views here.

def signup(request):
	if request.method == 'GET' :
		return render(request, 'signup.html') #如果呼叫signup_function會跳轉到sign.html裏頭
	elif request.method == 'POST' :
		user_account = request.POST['會員帳號']
		user_pwd = request.POST['會員密碼']
		user_check_pwd = request.POST['會員確認密碼']
		try:
			User.objects.get(username = user_account)
			return render(request, 'signup.html', {'帳號錯誤' : '該帳號已存在'})
		except User.DoesNotExist:
			if user_pwd == user_check_pwd:
				User.objects.create(username = user_account, password = user_pwd)
				return redirect('主頁面')
			else:
				return render(request, 'signup.html', {'密碼錯誤' : '輸入密碼不一致'})

"""
這邊要注意，必須判斷請求是get 還是post get的話代表是剛進來這個頁面 =>我要給他signup.html
但是如果是post的method 代表我點選了"立即註冊"
然後我們用	request.POST['XXXX'] 來存取使用者輸入的內容 這邊是用字典的方式來存放
再來，我們用 User.objects.get(username = user_account) User內建的語法，意思是get資料庫裏頭有沒有相同的username 也就是說有重複的名稱了 ps.這邊一個等號而已
	如果被我們用try抓到 那就return 一個render到signup.html   外加一個字典 =>  (key,value)是('帳號錯誤','該帳號已存在')
	如果沒被try抓到 => 代表沒有重複名稱 ， 使用者可以使用 ，但是此時會報錯 會報一個叫做User.DoesNotExist的錯誤
	因此才用try except去避免這項錯誤， 當這個錯誤被我們catch到的時候 代表可以使用
	我們就要判斷密碼是否相符，相符 => 我們就用User的api =>  User.objects.create(username = user_account, password = user_pwd)
	將帳號設置為user_account密碼設置為user_pwd 
	User.objects.create(username = 帳號, password = 密碼)
"""
