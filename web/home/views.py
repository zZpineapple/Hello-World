from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def text(request):
	# 获取去请求路径
	p = request.path
	# 获取请求方式
	m = request.method
	# 获取GET请求的数据
	g = request.GET
	g_a = request.GET.get('a')
	g_c = request.GET.get('c', '老子是默认值')
	g_list = request.GET.getlist('a')

	context = {'p':p, 'm':m, 'g':g ,'g_a':g_a, 'g_c':g_c, 'g_list':g_list}



	# return render(request,'text.html',context)
	return JsonResponse(context)

