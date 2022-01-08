# -*- coding: utf-8 -*-

from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from apecsul.cadastro.models import Pessoa, Endereco, Pastor, Filho, Telefone, Email, Site


class EnderecoForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ('logradouro', 'numero', 'bairro',
                  'complemento', 'uf', 'cep', 'municipio')

        labels = {
            'logradouro': _("Logradouro"),
            'numero': _("Número"),
            'bairro': _("Bairro"),
            'complemento': _("Complemento"),
            'municipio': _("Município (sem acentuação)"),
            'cep': _("CEP (Apenas dígitos)"),
            'uf': _("UF"),
        }
        widgets = {
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class PastorForm(forms.ModelForm):

    class Meta:
        model = Pastor
        fields = ('funcao','nome','cpf','rg','logradouro', 'numero', 'bairro',
                  'complemento', 'uf', 'cep', 'municipio')

        labels = {
            'funcao': _("Função"),
            'nome': _("Nome"),
            'cpf': _("CPF"),
            'rg': _("RG"),
            'logradouro': _("Logradouro"),
            'numero': _("Número"),
            'bairro': _("Bairro"),
            'complemento': _("Complemento"),
            'municipio': _("Município (sem acentuação)"),
            'cep': _("CEP (Apenas dígitos)"),
            'uf': _("UF"),
        }

        widgets = {
            'ministerio': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
        }


class FilhoForm(forms.ModelForm):

    class Meta:
        model = Filho
        fields = ('sexo','idade')

        labels = {
            'sexo': _("Sexo"),
            'idade': _("Idade"),
        }
        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TelefoneForm(forms.ModelForm):

    class Meta:
        model = Telefone
        fields = ('telefone',)
        labels = {
            'telefone': _('Telefone'),
        }
        widgets = {
            'tipo_telefone': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email',)
        labels = {
            'email': _('Email')
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('site',)
        labels = {
            'site': _('Site'),
        }
        widgets = {
            'site': forms.TextInput(attrs={'class': 'form-control'}),
        }


EnderecoFormSet = inlineformset_factory(
    Pessoa, Endereco, form=EnderecoForm, extra=1, can_delete=True)
PastorFormSet = inlineformset_factory(
    Pessoa, Pastor, form=PastorForm, extra=1, can_delete=True)
FilhoFormSet = inlineformset_factory(
    Pessoa, Filho, form=FilhoForm, extra=1, can_delete=True)
TelefoneFormSet = inlineformset_factory(
    Pessoa, Telefone, form=TelefoneForm, extra=1, can_delete=True)
EmailFormSet = inlineformset_factory(
    Pessoa, Email, form=EmailForm, extra=1, can_delete=True)
SiteFormSet = inlineformset_factory(
    Pessoa, Site, form=SiteForm, extra=1, can_delete=True)
