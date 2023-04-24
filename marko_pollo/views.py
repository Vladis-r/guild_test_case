import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from marko_pollo.utils import gen_marko_polo


@login_required
@csrf_exempt
def one_mp_view(request):
    """
    Ручка принимает число от 0 до 1000.
    Возвращает значение Марко, Поло, МаркоПоло или число.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        if "mp_one" in data:
            num = data["mp_one"]
            res = gen_marko_polo.generate_one(num)
        else:
            res = "Отправьте необходимые данные согласно образцу: '{mp_one: <number>}'"
        return JsonResponse({"result": res})


@login_required
@csrf_exempt
def list_mp_view(request):
    """
    Ручка принимает список чисел от 0 до 1000.
    Возвращает список значений (Марко, Поло, МаркоПоло или число).
    """
    if request.method == "POST":
        data = json.loads(request.body)
        if "mp_list" in data:
            list_of_mp = data["mp_list"]
            res = gen_marko_polo.generate_list(list_of_mp)
        else:
            res = "Отправьте необходимые данные согласно образцу: '{mp_list: [<number_1>, <number_2>, ...]}'"
        return JsonResponse({"result": res})


@login_required
@csrf_exempt
def range_mp_view(request):
    """
    Ручка принимает два числа start и end со значениями от 0 до 1000.
    Возвращает значение Марко, Поло, МаркоПоло или число.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        if "mp_start" and "mp_end" in data:
            start = data["mp_start"]
            end = data["mp_end"]
            res = gen_marko_polo.generate_range(start, end)
        else:
            res = "Отправьте необходимые данные согласно образцу:'{'mp_start': <number_start>, 'mp_end': <number_end>}'"
        return JsonResponse({"result": res})
