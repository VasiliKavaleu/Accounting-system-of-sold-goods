from django.shortcuts import render


from .services import get_latest_news


def get_main_page(request):
    return render(request, 'main.html',
                  {
                    'data_set1': get_latest_news()[0],
                    'data_set2': get_latest_news()[1],
                  })
