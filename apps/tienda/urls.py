from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    ArticleList,
    ArticleDetail,
    getSearchResults,
    contact,
    GraciasView,
)

urlpatterns = [
    url(r'^gracias/$', GraciasView.as_view(), name='gracias'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^$', ArticleList.as_view(), name='list'),
    #url(r'^(?P<slug>[\w-]+)/$', ArticleDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[/\w-]+)/$', ArticleDetail.as_view(), name='detail'),
    # URL search
    url(r'^buscar', getSearchResults, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)