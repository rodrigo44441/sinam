# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render_to_response
from django.shortcuts import render, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q

# Create your views here.
from .models import Articulo
from django.views.generic.detail import DetailView
from django.views.generic import ListView, View
from .forms import ContactForm
#from .forms import AddCategory
#from django.core.mail import EmailMultiAlternatives

class ArticleList(ListView):
    model = Articulo
    queryset_list = Articulo.objects.all().order_by('-id')
    paginate_by = 4
    ordering = ['-id']


class ArticleDetail(DetailView):
    model = Articulo


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        '''
        for key, value in form.cleaned_data.iteritems():
            print key, value
        '''    
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Contacto SINAM'
        email_from = settings.EMAIL_HOST
        email_to = [email_from, 'rodrigo44441@gmail.com']
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto, 
            email_mensaje,
            email_from,
            email_to,
            fail_silently = True
            )
        return HttpResponseRedirect('/gracias/')
    context = {
        "form":form, 
    }
    return render(request, "tienda/contact.html", context)


class GraciasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tienda/gracias.html')


def getSearchResults(request):
    """
    Search for a post by title or abstract. To search http://example.com/search?q=title
    """
    # Get the query data
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    # Query the database
    results = Articulo.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query)).order_by('-id')

    # Add pagination
    pages = Paginator(results, 5)

    # Get specified page
    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display the search results
    return render_to_response('tienda/articulo_list.html',
                              {'page_obj': returned_page,
                               'object_list': returned_page.object_list,
                               'search': query})


'''def contacto_view(request):
    info_enviado = False
    email = ''
    titulo = ''
    texto = ''
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']

            # Configuracion del servidor 
            to_admin = 'rodrigo44441@gmail.com'
            html_content = "Informacion recibida <br><br><br> ** Mensaje ** <br><br>%s"%(texto)
            msg = EmailMultiAlternatives('Correo de Contacto',html_content,  'from@server.com', [to_admin])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

    else:
        formulario = ContactForm()
        ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
        return render_to_response('base.html', ctx, context_instance=RequestContext(request))

'''


'''
def contactView(request):
    titulo = "hola"
    if request.user.is_authenticated():
        titulo = "Bienvendio %s" %(request.user)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_data =  form.cleaned_data
        abc = form_data.get("nombre")
        obj = Categoria.objects.create(nombre=abc)
    context = {
        "titulo":titulo,
        "el_form":form,
    }
    return render(request, "tienda/contacto.html", context)
'''