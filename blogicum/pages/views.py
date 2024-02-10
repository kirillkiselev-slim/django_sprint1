from django.shortcuts import render


def about(request):
    """Функция рендерит страницу 'О проекте'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Функция рендерит страницу 'Наши правила'."""
    template = 'pages/rules.html'
    return render(request, template)
