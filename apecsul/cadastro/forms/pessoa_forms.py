# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from apecsul.cadastro.models import PessoaJuridica, PessoaFisica


class PessoaJuridicaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            instance = kwargs.pop('instance')
            instance = PessoaJuridica.objects.get(pk=instance.pk)
            super(PessoaJuridicaForm, self).__init__(
                instance=instance, *args, **kwargs)
        else:
            super(PessoaJuridicaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PessoaJuridica
        fields = ('cnpj', 'data_cadastro',
                  'data_fundacao')

        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'data_cadastro': forms.DateInput(attrs={'class': 'form-control'}),
            'data_fundacao': forms.DateInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'cnpj': _('CNPJ'),
            'data_fundacao': _('Data de Fundação'),
            'data_cadastro': _('Data de Cadastro'),
        }


class PessoaFisicaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            instance = kwargs.pop('instance')
            instance = PessoaFisica.objects.get(pk=instance.pk)
            super(PessoaFisicaForm, self).__init__(
                instance=instance, *args, **kwargs)
        else:
            super(PessoaFisicaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PessoaFisica
        fields = ('cpf', 'rg', 'nascimento', )

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        }
        labels = {
            'cpf': _('CPF'),
            'rg': _('RG'),
            'nascimento': _('Nascimento'),
        }
