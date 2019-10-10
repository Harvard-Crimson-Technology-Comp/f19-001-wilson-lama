from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django.http import HttpResponseNotFound

"""
You will create many 4 key views here: register, buy, sell, and list

register - allows a user to register and obtain an API token
buy - allows a user to buy some stocks by submitting a symbol and an amount
sell - allows a user to sell some stocks by submitting a symbol and an amount
list - allows a user to see their current portfolio, does not take arguments
"""

def remove_me(request):
    return HttpResponseNotFound('API: TODO')

@require_http_methods(["POST"])
def register(request):
    fields = ["first_name", "last_name"]
    for field in fields:
        if field not in fields:
            return JsonResponse({'error': 'missing field'})
    return JsonResponse({})

@require_http_methods(["POST"])
@csrf_exempt
def buy(request):
    fields = ['api_token', 'symbol', 'quantity']

    for field in fields:
        if field not in fields:
            return Json({'error': f'field - {field} - not found'})
    
    user = UserModel.objects.filter(api_token=request.POST.get('api_token '))

    try:
        symbol, meta = ts.get_quote_endpoint(symbol=request.POST.get('symbol').upper())
    except ValueError:
        return JsonResponse

    