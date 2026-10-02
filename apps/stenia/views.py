from django.shortcuts import render


def files_browser(request):
    return render(request, "pages/files_browser.django")
