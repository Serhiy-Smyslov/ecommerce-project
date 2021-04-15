from .models import Category


def menu_links(request):
    """Return links on every category."""
    links = Category.objects.all()
    return dict(links=links)