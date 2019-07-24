import hashlib
from django.core.paginator import Paginator
from django.shortcuts import render
from ShopApp.models import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


# def login_index(fun):
# 	def inner(request, *args, **kwargs):
# 		cookies_user = request.COOKIES.get('username')
# 		session_user = request.session.get('username')
# 		print('cookie_user:', cookies_user)
# 		print('session_user:', session_user)
# 		if cookies_user and session_user and cookies_user == session_user:
# 			user = Seller.objects.filter(username=cookies_user).first()
# 			if user:
# 				return fun(request,*args, **kwargs)
# 		return HttpResponseRedirect('/shop/login')
# 	return inner
#
#
# @login_index
# def index(request):
# 	return render(request, 'shopapp/index.html')



# def set_password(password):
# 	md5 = hashlib.md5()
# 	md5.update(password.encode())
# 	result = md5.hexdigest()
# 	return result
# 设置密码
def set_password(password):
	md5 = hashlib.md5()
	md5.update(password.encode())
	result = md5.hexdigest()
	return result


def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			seller = Seller()
			seller.nickname = username
			seller.username = username
			seller.password = set_password(password)
			seller.save()
			# return HttpResponseRedirect('/shop/login/')
	return render(request, 'shopapp/register.html')


# def login(request):
#	""""
# 	编写登录功能
# 	成功-----> 首页
# 	失败-----> 登录页面
# 	"""
# 	response = render(request, 'shopapp/login.html')
# 	response.set_cookie('login_from', 'login_page')
# 	if request.method == 'POST':     # 当请求方式为post
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		if username and password:    # 当账号密码不为空
# 			user = Seller.objects.filter(username=username).first()   # 实例化seller 用户
# 			if user:    # 当user存在
# 				web_password = set_password(password)
# 				cookies = request.COOKIES.get('login_from')
# 				if user.password == web_password and cookies == 'login_page':
# 						response = HttpResponseRedirect('/shop/index/')
# 						response.set_cookie('username', username)
# 						request.session['username'] = username
# 						return response
# 	return response

# def login(request):
# 	response = render(request, 'shopapp/login.html')
# 	response.set_cookie('login_from', 'login_page')
# 	if request.method == 'POST':      # 获取方式为post
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		if username and password:   # 当 账号密码框输入框不为空，账号密码存在时
# 			user = Seller.objects.filter(username=username).first()     # 实例化Seller
# 			if user:  # 当实例化seller 存在时
# 				web_password = set_password(password)     # 前端密码和密码相等
# 				cookies = request.COOKIES.get('login_from')  # 当前设置的login_from的cookie 值
# 				# 当前端密码和数据库密码相同，cookies= 设置的login_page 的值
# 				if user.password == web_password and cookies == 'login_page':
# 					# 所有都成功 重定向到 首页index
# 					response = HttpResponseRedirect('/shop/index/')
# 					# 重新设置cookie值 和session 值
# 					response.set_cookie('username', username)
# 					request.session['username'] = username
# 					return response
# 	return response   # 当不成功 获取方式不为post 就返回 response


# def login(request):
	# 原登录的方式
# 	# print(request.method)
# 	response = render(request, 'shopapp/login.html')
# 	response.set_cookie('local_from', 'local_page')
# 	username = request.POST.get('username')
# 	password = request.POST.get('password')
# 	# print(username, password)
# 	if request.method == "POST":
# 		if username and password:
# 			user = Seller.objects.filter(username=username).first()
# 			if user:
# 				web_password = set_password(password)
# 				# print(web_password)
# 				cookies = request.COOKIES.get('local_from')
# 				# print(cookies)
# 				if web_password == user.password and cookies == 'local_page':
# 					response = HttpResponseRedirect('/shop/index/')
# 					response.set_cookie('username', username)
# 					response.set_cookie('user_id', user.id)
# 					request.session['username'] = username
# 					return response
# 	# return render(request, 'shopapp/login.html')
# 	return response


# def login(request):
# 	response = render(request, 'shopapp/login.html')
# 	response.set_cookie('local_from', 'local_page')
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		if username and password:
# 			user = Seller.objects.filter(username=username).first()
# 			if user:
# 				web_password = set_password(password)
# 				cookies = request.COOKIES.get('local_from')
# 				if user.password == web_password and cookies == 'local_page':
# 					response = HttpResponseRedirect('/shop/index/')
# 					response.set_cookie('username', username)
# 					response.set_cookie('user_id', user.id)
# 					request.session['username'] = username
# 					store = Store.objects.filter(user_id=user.id).first()
# 					if store:
# 						response.set_cookie('has_store', store.id)
# 					else:
# 						response.set_cookie('has_store', '')
# 					return response
# 	return response


def login(request):
	response = render(request, 'shopapp/login.html')
	response.set_cookie('local_from', 'local_page')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			user = Seller.objects.filter(username=username).first()
			if user:
				web_password = set_password(password)
				cookies = request.COOKIES.get('local_from')
				if user.password == web_password and cookies == 'local_page':
					response = HttpResponseRedirect('/shop/index')
					response.set_cookie('username', username)
					response.set_cookie('user_id', user.id)
					request.session['username'] = username
					store = Store.objects.filter(user_id=user.id).first()
					if store:
						response.set_cookie('has_store', store.id)
					else:
						response.set_cookie('has_store', '')
					return response
	return response



# def login_index(fun):
# 	# 原
# 	def inner(request, *args, **kwargs):
# 		cookie_username = request.COOKIES.get('username')
# 		session_username = request.session.get('username')
# 		if cookie_username and session_username and cookie_username == session_username:
# 			user = Seller.objects.filter(username=cookie_username).first()
# 			if user:
# 				return fun(request, *args, **kwargs)
# 		return HttpResponseRedirect('/shop/login/')
# 	return inner


def login_index(fun):
	def inner(request, *args, **kwargs):
		cookie_username = request.COOKIES.get('username')
		session_username = request.session.get('username')
		if cookie_username and session_username and cookie_username == session_username:
			return fun(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/shop/login/')
	return inner


# def login_index(fun):
# 	def inner(request, *args, **kwargs):
# 		cookies_name = request.COOKIES.get('username')
# 		session_username = request.session.get('username')
# 		if cookies_name and session_username and cookies_name == session_username:
# 			return fun(request, *args, **kwargs)
# 		else:
# 			return HttpResponseRedirect('/shop/login/')
# 	return inner


@ login_index
def index(request):
	return render(request, 'shopapp/index.html')
# def index(request):
# 	user_id = request.COOKIES.get('user_id')
# 	if user_id:
# 		user_id = int(user_id)
# 	else:
# 		user_id = 0
# 	store = Store.objects.filter(user_id=user_id).first()
# 	if store:
# 		is_store = 1
# 	else:
# 		is_store = 0
# 	return render(request, 'shopapp/index.html', {'is_store': is_store})


def forget(request):
	return render(request, 'shopapp/forgot-password.html')


@ login_index
def register_store(request):
	type_list = StoreType.objects.all()
	if request.method == 'POST':   # 以 post方式传递过来的数据
		past = request.POST
		store_name = past.get('store_name')
		store_address = past.get('store_address')
		store_descripton = past.get('store_descripton')
		store_phone = past.get('store_phone')
		store_money = past.get('store_money')

		user_id = int(request.COOKIES.get('user_id'))
		type_lists = past.getlist('type')
		# print('type_lists:', type_lists)
		store_logo = request.FILES.get('store_logo')

		store = Store()    # 店铺
		store.store_name = store_name
		store.store_address = store_address
		store.store_phone = store_phone
		store.store_money = store_money
		store.store_descripton = store_descripton
		store.user_id = user_id
		store.store_logo = store_logo
		store.save()

		for i in type_lists:
			store_type = StoreType.objects.get(id=i)
			store.type.add(store_type)
		store.save()
		response = HttpResponseRedirect('/shop/index')
		response.set_cookie('has_store', store.id)
		return response
	return render(request, 'shopapp/register_store.html', locals())

@ login_index
def add_goods(request):
	if request.method == 'POST':
		goods_name = request.POST.get('goods_name')
		goods_price = request.POST.get('goods_price')
		goods_number = request.POST.get('goods_number')
		goods_description = request.POST.get('goods_description')
		goods_date = request.POST.get('goods_date')
		goods_safeDate = request.POST.get('goods_safeDate')
		goods_store = request.COOKIES.get('has_store')
		goods_image = request.FILES.get('goods_image')
		goods = Goods()
		goods.good_name = goods_name
		goods.goods_price = goods_price
		goods.goods_number = goods_number
		goods.goods_description = goods_description
		goods.goods_date = goods_date
		goods.goods_safeDate = goods_safeDate
		goods.goods_image = goods_image
		goods.save()
		goods.store_id.add(
			Store.objects.get(id=int(goods_store))
		)
		goods.save()
		return HttpResponseRedirect('/shop/goods_list')
	return render(request, 'shopapp/add_goods.html')


# def goods_list(request):
# 	keywords = request.GET.get('keywords', '')
# 	page_num = request.GET.get('page.num', 1)
# 	if keywords:
# 		goods_list = Goods.objects.filter(good_name__contains=keywords)
# 	else:
# 		goods_list = Goods.objects.all()
# 	paginator = Paginator(goods_list, 2)
# 	page = paginator.page(int(page_num))
# 	print('page', page)
# 	page_range = paginator.page_range
# 	print('page_range', page_range)
# 	return render(request, 'shopapp/goods_list.html', {'page': page, 'page_range': page_range})

# 模糊查询
# def goods_list(request):
# 	keywords = request.GET.get('keywords', '')
# 	if keywords:
# 		goods_list = Goods.objects.filter(good_name__contains=keywords)
# 	else:
# 		goods_list = Goods.objects.all()
# 	return render(request, 'shopapp/goods_list.html', locals())

# def goods_list(request):
# 	keywords = request.GET.get('keywords', '')
# 	page_num = request.GET.get('page.num', 1)
# 	if keywords:
# 		goods_list = Goods.objects.filter(good_name__contains=keywords)
# 	else:
# 		goods_list = Goods.objects.all()
# 	paginator = Paginator(goods_list, 2)
# 	page = paginator.page(int(page_num))
# 	print('page', page)
# 	page_range = paginator.page_range
# 	print('page_range', page_range)
# 	return render(request, 'shopapp/goods_list.html', {'page': page, 'page_range': page_range})

# def goods_lists(request):
# 	keywords = request.GET.get('keywords', '')
# 	page_num = request.GET.get('page.num', 1)
# 	if keywords:
# 		goods_lists = Goods.objects.filter(good_name__contains=keywords)
# 	else:
# 		goods_lists = Goods.objects.all()
# 		paginator = Paginator(goods_lists, 2)
# 		page = paginator.page(int(page_num))
# 		page_range = paginator.page_range
# 	return render(request, 'shopapp/goods_list.html', locals())

# def goods_lists(request):
# 	# 原good_lists
# 	keywords = request.GET.get('keywords', '')
# 	page_num = request.GET.get('page_num', 1)
# 	if keywords:
# 		goods_lists = Goods.objects.filter(good_name__contains=keywords)
# 	else:
# 		goods_lists = Goods.objects.all()
# 	paginator = Paginator(goods_lists, 3)
# 	page = paginator.page(int(page_num))
# 	page_range = paginator.page_range
#
# 	return render(request, 'shopapp/goods_list.html', locals())


@ login_index
def goods_lists(request):
	keywords = request.GET.get('keywords', '')
	page_num = request.GET.get('page_num', 1)
	store_id = request.COOKIES.get('has_store')
	store = Store.objects.get(id=int(store_id))
	if keywords:
		goods_lists = store.goods_set.filter(good_name__contains=keywords)
	else:
		goods_lists = store.goods_set.all()
	paginator = Paginator(goods_lists, 3)
	page = paginator.page(int(page_num))
	page_range = paginator.page_range

	return render(request, 'shopapp/goods_list.html', locals())


@ login_index
def all_goods(request, goods_id):
	goods = Goods.objects.filter(id=goods_id).first()
	return render(request, 'shopapp/all_goods.html', locals())


@ login_index
def update_goods(request, goods_id):
	goods_data = Goods.objects.filter(id=goods_id).first()
	if request.method == 'POST':
		goods_name = request.POST.get('goods_name')
		goods_price = request.POST.get('goods_price')
		goods_number = request.POST.get('goods_number')
		goods_description = request.POST.get('goods_description')
		goods_date = request.POST.get('goods_date')
		goods_safeDate = request.POST.get('goods_safeDate')
		goods_image = request.POST.get('goods_image')

		goods = Goods.objects.get(id=int(goods_id))
		goods.good_name = goods_name
		goods.goods_price = goods_price
		goods.goods_number = goods_number
		goods.goods_description = goods_description
		goods.goods_date = goods_date
		goods.goods_safeDate = goods_safeDate

		if goods_image:
			goods.goods_image = goods_image
		goods.save()
		return HttpResponseRedirect("/shop/all_goods/%s/" % goods_id)

	return render(request, 'shopapp/update_goods.html', locals())