from .models import Category

def menu_links(request):
    links = Category.objects.all()
    dict = {'links':links}
    return dict