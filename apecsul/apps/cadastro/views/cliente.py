# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from apecsul.apps.cadastro.forms import ClienteForm, cliente
from apecsul.apps.cadastro.models import Cliente

from .base import AdicionarPessoaView, PessoasListView, EditarPessoaView


class AdicionarClienteView(AdicionarPessoaView):
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy('cadastro:listaclientesview')
    success_message = "Igreja <b>%(nome_razao_social)s </b>adicionado com sucesso."
    permission_codename = 'add_cliente'

    def get_context_data(self, **kwargs):
        context = super(AdicionarClienteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR IGREJA'
        context['return_url'] = reverse_lazy('cadastro:listaclientesview')
        context['tipo_pessoa'] = 'cliente'
        return context

    def get(self, request, *args, **kwargs):
        form = ClienteForm(prefix='cliente_form')
        return super(AdicionarClienteView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        req_post = request.POST.copy()

        request.POST = req_post
        form = ClienteForm(request.POST, request.FILES,
                           prefix='cliente_form', request=request)
        return super(AdicionarClienteView, self).post(request, form, *args, **kwargs)


class ClientesListView(PessoasListView):
    template_name = 'cadastro/pessoa_list.html'
    model = Cliente
    context_object_name = 'all_clientes'
    success_url = reverse_lazy('cadastro:listaclientesview')
    permission_codename = 'view_cliente'

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'IGREJAS CADASTRADAS'
        context['add_url'] = reverse_lazy('cadastro:addclienteview')
        context['tipo_pessoa'] = 'cliente'
        return context


class EditarClienteView(EditarPessoaView):
    form_class = ClienteForm
    model = Cliente
    template_name = "cadastro/pessoa_edit.html"
    success_url = reverse_lazy('cadastro:listaclientesview')
    success_message = "Igreja <b>%(nome_razao_social)s </b>editado com sucesso."
    permission_codename = 'change_cliente'

    def get_context_data(self, **kwargs):
        context = super(EditarClienteView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listaclientesview')
        context['tipo_pessoa'] = 'cliente'
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form_class.prefix = "cliente_form"
        form = self.get_form(form_class)

        return super(EditarClienteView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        req_post = request.POST.copy()
        request.POST = req_post
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES,
                          prefix='cliente_form', instance=self.object, request=request)
        
        return super(EditarClienteView, self).post(request, form, *args, **kwargs)