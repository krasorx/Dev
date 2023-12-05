from django.shortcuts import render

def home(request):
    #return render(request, 'home.html')
    return render(
            request=request,
            template_name='fact/home.html',
        )
