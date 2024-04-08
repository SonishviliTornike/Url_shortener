from django.shortcuts import render, redirect
from django.http import Http404
from .forms import TakeUrl
from .models import Urls
from .utils import generate_short_code



def index(request):
    if request.method == 'POST':
        url_form = TakeUrl(request.POST)
        if  url_form.is_valid():
            original_url = url_form.cleaned_data['url_form']
            short_code = generate_short_code(length = 6)
            Urls.objects.create(original_url = original_url, short_url=short_code)
            return redirect('history')
        
    url_form = TakeUrl()

    return render(request, 'index.html', {'url_form': url_form})


def shorten_history(request):
    urls = Urls.objects.all()

    return render(request, 'shortening_history.html', {'urls':urls})


def redirect_short_code(request, short_code):
    try:
        url_mapping = Urls.objects.get(short_url = short_code)
        url_mapping.visit_count += 1
        url_mapping.save()
        return redirect(url_mapping.original_url)
    
    except Urls.DoesNotExist:
        raise Http404("Short URL Doesn't Exist!")
 

def urls_info(request, short_code):
    url = Urls.objects.get(short_url = short_code)

    return render(request, 'info.html', {'url':url})