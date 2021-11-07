from django.http import HttpResponse
# from django.shortcuts import render

def myview(request):
    num = request.session.get('num', 0) + 1
    request.session['num'] = num
    if num > 4 : del(request.session['num'])
    resp = HttpResponse('view count=' + str(num))
    resp.set_cookie('dj4e_cookie', '831704ea', max_age=1000)
    return resp