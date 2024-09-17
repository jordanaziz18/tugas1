from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Muhammad Jordan ',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)