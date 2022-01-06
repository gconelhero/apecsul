# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

from apecsul.apps.cadastro.models import Pessoa, Pastor, Cliente, Endereco


import json

class InfoCliente(View):

    def post(self, request, *args, **kwargs):
        obj_list = []
        pessoa = Pessoa.objects.get(pk=request.POST['pessoaId'])
        cliente = Cliente.objects.get(pk=request.POST['pessoaId'])
        pastores = Pastor.objects.all().filter(pessoa_faz=request.POST['pessoaId'])
        enderecos = Endereco.objects.all().filter(pessoa_end=request.POST['pessoaId'])

        if pastores:
            obj_list += [pas for pas in pastores]
        if request.POST['pastorId'] and pastores:
            pastor = Pastor.objects.get(pk=request.POST['pastorId'])
        else:
            pastor = ''
        if pastor != '':
            obj_list.append(pastor)
        
        if enderecos:
            obj_list += [end for end in enderecos]
        if request.POST['enderecoId'] and enderecos:
            endereco = Endereco.objects.get(pk=request.POST['enderecoId'])
            pessoa.endereco_padrao = endereco
        
        obj_list.append(cliente)

        if pessoa.endereco_padrao:
            obj_list.append(pessoa.endereco_padrao)
        if pessoa.email_padrao:
            obj_list.append(pessoa.email_padrao)
        if pessoa.telefone_padrao:
            obj_list.append(pessoa.telefone_padrao)
        if pessoa.tipo_pessoa == 'PJ':
            obj_list.append(pessoa.pessoa_jur_info)
        elif pessoa.tipo_pessoa == 'PF':
            obj_list.append(pessoa.pessoa_fis_info)
        
        data = serializers.serialize('json', obj_list, fields=('indicador_ie', 'limite_de_credito', 'cnpj', 'inscricao_estadual', 'responsavel', 'cpf', 'rg', 'id_estrangeiro', 'logradouro', 'numero', 'bairro',
                                                            'municipio', 'cmun', 'uf', 'pais', 'complemento', 'cep', 'email', 'telefone','pastor', 'nome', 'nome_pastor','endereco', 'complemento', 'tipo_endereco'))
        
        return HttpResponse(data, content_type='application/json')


class SelectFormCliente(View):

    def get(self, request, *args, **kwargs):
        obj_list = []
        if request.is_ajax():
            term = request.GET.get('term')
            if term != None:

                clientes = [prod for prod in Cliente.objects.filter(nome_razao_social__icontains=term)]
            else:
                clientes = [prod for prod in Cliente.objects.all()]

            obj_list = [{'id': i.id, 'nome_razao_social': i.nome_razao_social} for i in clientes]

        else:
            return HttpResponse('Utilização incorreta.')
        
        return HttpResponse(json.dumps(obj_list), content_type='application/json')

