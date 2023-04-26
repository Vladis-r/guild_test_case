from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from marko_pollo.utils import gen_marko_polo


def main_view(request):
    """
    Главная страница
    """
    if request.method == "GET":
        return render(request, "main.html")
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
@csrf_exempt
def one_mp_view(request):
    """
    Ручка принимает число от 0 до 1000.
    Возвращает значение Марко, Поло, МаркоПоло или число.
    """

    if request.method == "POST":
        num = request.POST.get('mp_one', None)
        if num.isnumeric():
            res = gen_marko_polo.generate_one(int(num))
        else:
            res = "Это должно быть числом от 0 до 1000"
        return render(request, "result.html", {"result": res})

    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
@csrf_exempt
def list_mp_view(request):
    """
    Ручка принимает список чисел от 0 до 1000.
    Возвращает список значений (Марко, Поло, МаркоПоло или число).
    """

    if request.method == "POST":
        nums = request.POST.get('mp_list', None)
        nums = nums.split()
        res = gen_marko_polo.generate_list(list(nums))
        return render(request, "result.html", {"result": res})
    else:
        return HttpResponse('<h1>Page not found</h1>')


@login_required
@csrf_exempt
def range_mp_view(request):
    """
    Ручка принимает два числа start и end со значениями от 0 до 1000.
    Возвращает значение Марко, Поло, МаркоПоло или число.
    """

    if request.method == "POST":
        start = request.POST.get('mp_start', None)
        end = request.POST.get('mp_end', None)
        if start.isnumeric() and end.isnumeric():
            res = gen_marko_polo.generate_range(int(start), int(end))
        else:
            res = "Это должно быть число от 0 до 1000"
        return render(request, "result.html", {"result": res})
    else:
        return HttpResponse('<h1>Page not found</h1>')


def websocket_view(request):
    """
    Ручка для теста websocket. URL отключен.
    Необходимо правильно прописать java скрипт в websocket.html.
    До тех пор, для теста websocket, можно пользоваться marko_pollo/websocket_client.py
    """
    return render(request, "websocket.html")
