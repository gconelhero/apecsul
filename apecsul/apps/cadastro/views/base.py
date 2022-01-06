# -*- coding: utf-8 -*-

from apecsul.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from apecsul.apps.cadastro.forms import PessoaJuridicaForm, PessoaFisicaForm, EnderecoFormSet, PastorFormSet, FilhoFormSet, TelefoneFormSet, EmailFormSet, \
    SiteFormSet, BancoFormSet, DocumentoFormSet
from apecsul.apps.cadastro.models import PessoaFisica, PessoaJuridica, Endereco, Pastor, Filho, Telefone, Email, Site, Banco, Documento


class AdicionarPessoaView(CustomCreateView):

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, nome_razao_social=self.object.nome_razao_social)

    def get(self, request, form, *args, **kwargs):
        self.object = None

        veiculo_form = kwargs.pop('veiculo_form', None)

        pessoa_juridica_form = PessoaJuridicaForm(prefix='pessoa_jur_form')
        pessoa_fisica_form = PessoaFisicaForm(prefix='pessoa_fis_form')

        endereco_form = EnderecoFormSet(prefix='endereco_form')
        endereco_form.can_delete = False

        pastor_form = PastorFormSet(prefix='pastor_form')
        pastor_form.can_delete = False

        filho_form = FilhoFormSet(prefix='filho_form')
        filho_form.can_delete = False

        banco_form = BancoFormSet(prefix='banco_form')
        banco_form.can_delete = False

        documento_form = DocumentoFormSet(prefix='documento_form')
        documento_form.can_delete = False

        telefone_form = TelefoneFormSet(prefix='telefone_form')
        telefone_form.can_delete = False
        
        email_form = EmailFormSet(prefix='email_form')
        email_form.can_delete = False
        
        site_form = SiteFormSet(prefix='site_form')
        site_form.can_delete = False

        formsets = [telefone_form, email_form, site_form]

        return self.render_to_response(self.get_context_data(form=form,
                                                             pessoa_juridica_form=pessoa_juridica_form,
                                                             pessoa_fisica_form=pessoa_fisica_form,
                                                             endereco_form=endereco_form,
                                                             pastor_form=pastor_form,
                                                             filho_form=filho_form,
                                                             banco_form=banco_form,
                                                             formsets=formsets,
                                                             veiculo_form=veiculo_form))

    def post(self, request, form, *args, **kwargs):
        extra_forms = []
        veiculo_form = kwargs.pop('veiculo_form', None)

        endereco_form = EnderecoFormSet(request.POST, prefix='endereco_form')
        
        pastor_form = PastorFormSet(request.POST, prefix='pastor_form')
        filho_form = FilhoFormSet(request.POST, prefix='filho_form')
        
        banco_form = BancoFormSet(request.POST, prefix='banco_form')
        documento_form = DocumentoFormSet(request.POST, prefix='documento_form')

        telefone_form = TelefoneFormSet(request.POST, prefix='telefone_form')
        email_form = EmailFormSet(request.POST, prefix='email_form')
        site_form = SiteFormSet(request.POST, prefix='site_form')

        formsets = [telefone_form, email_form, site_form]

        if veiculo_form:
            extra_forms = [veiculo_form, ]

        if form.is_valid():

            self.object = form.save(commit=False)
            self.object.tipo_pessoa = 'PJ'
            if self.object.tipo_pessoa == 'PJ':
                pessoa_form = PessoaJuridicaForm(
                    request.POST, prefix='pessoa_jur_form')
            else:
                pessoa_form = PessoaFisicaForm(
                    request.POST, prefix='pessoa_fis_form')
            

            if (all(formset.is_valid() for formset in formsets) and
                pessoa_form.is_valid() and
                endereco_form.is_valid() and
                pastor_form.is_valid() and
                filho_form.is_valid() and
                banco_form.is_valid() and
                    all(extra_form.is_valid() for extra_form in extra_forms)):

                self.object.save()

                # Salvar informacoes endereco
                endereco_form.instance = self.object
                end = endereco_form.save()
                if len(end):
                    self.object.endereco_padrao = end[0]

                 # Salvar informacoes 
                pastor_form.instance = self.object
                pastor = pastor_form.save()
                #if len(faz):
                    #self.object. = faz[0]
                
                
                filho_form.instance = self.object
                filho = filho_form.save()

                # Salvar informacoes bancarias
                banco_form.instance = self.object
                ban = banco_form.save()
                if len(ban):
                    self.object.banco_padrao = ban[0]

                # salvar telefone
                telefone_form.instance = self.object
                tel = telefone_form.save()
                if len(tel):
                    self.object.telefone_padrao = tel[0]

                # salvar email
                email_form.instance = self.object
                ema = email_form.save()
                if len(ema):
                    self.object.email_padrao = ema[0]

                # salvar site
                site_form.instance = self.object
                sit = site_form.save()
                if len(sit):
                    self.object.site_padrao = sit[0]

                if veiculo_form:
                    veiculo_form.instance = self.object
                    veiculo_form.save()
                
                # salvar objeto criado e pessoa fisica/juridica
                self.object.save()
                pessoa_form.instance.pessoa_id = self.object
                pessoa_form.save()

                return self.form_valid(form)

        pessoa_juridica_form = PessoaJuridicaForm(
            request.POST, prefix='pessoa_jur_form')
        pessoa_fisica_form = PessoaFisicaForm(
            request.POST, prefix='pessoa_fis_form')

        return self.form_invalid(form=form,
                                 pessoa_juridica_form=pessoa_juridica_form,
                                 pessoa_fisica_form=pessoa_fisica_form,
                                 endereco_form=endereco_form,
                                 pastor_form=pastor_form,
                                 filho_form=filho_form,
                                 veiculo_form=veiculo_form)


class PessoasListView(CustomListView):

    def __init__(self, *args, **kwargs):
        super(PessoasListView, self).__init__(*args, **kwargs)


class EditarPessoaView(CustomUpdateView):

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, nome_razao_social=self.object.nome_razao_social)

    def get(self, request, form, *args, **kwargs):
        self.object.tipo_pessoa = 'PJ'
        if self.object.tipo_pessoa == 'PJ':
            pessoa_juridica_form = PessoaJuridicaForm(
                instance=self.object, prefix='pessoa_jur_form')
            pessoa_fisica_form = PessoaFisicaForm(prefix='pessoa_fis_form')
        else:
            pessoa_juridica_form = PessoaJuridicaForm(prefix='pessoa_jur_form')
            pessoa_fisica_form = PessoaFisicaForm(
                instance=self.object, prefix='pessoa_fis_form')

        endereco_form = EnderecoFormSet(
            instance=self.object, prefix='endereco_form')
        pastor_form = PastorFormSet(
            instance=self.object, prefix='pastor_form')
        filho_form = FilhoFormSet(
            instance=self.object, prefix='filho_form')
        banco_form = BancoFormSet(
            instance=self.object, prefix='banco_form')
        documento_form = DocumentoFormSet(
            instance=self.object, prefix='documento_form')

        telefone_form = TelefoneFormSet(
            instance=self.object, prefix='telefone_form')
        email_form = EmailFormSet(
            instance=self.object, prefix='email_form')
        site_form = SiteFormSet(
            instance=self.object, prefix='site_form')

        if Telefone.objects.filter(pessoa_tel=self.object.pk).count():
            telefone_form.extra = 0
        if Endereco.objects.filter(pessoa_end=self.object.pk).count():
            endereco_form.extra = 0
        if Pastor.objects.filter(pastor_id=self.object.pk).count():
            pastor_form.extra = 0
        if Filho.objects.filter(filho_id=self.object.pk).count():
            filho_form.extra = 0
        if Email.objects.filter(pessoa_email=self.object.pk).count():
            email_form.extra = 0
        if Site.objects.filter(pessoa_site=self.object.pk).count():
            site_form.extra = 0
        if Banco.objects.filter(pessoa_banco=self.object.pk).count():
            banco_form.extra = 0
        if Documento.objects.filter(pessoa_documento=self.object.pk).count():
            documento_form.extra = 0

        formsets = [telefone_form, email_form, site_form]


        return self.render_to_response(self.get_context_data(form=form,
                                                             pessoa_juridica_form=pessoa_juridica_form,
                                                             pessoa_fisica_form=pessoa_fisica_form,
                                                             endereco_form=endereco_form,
                                                             pastor_form=pastor_form,
                                                             filho_form=filho_form,
                                                             banco_form=banco_form,
                                                             formsets=formsets,
                                                             object=self.object))

    def post(self, request, form, *args, **kwargs):
        self.object = self.get_object()
        extra_forms = []
        veiculo_form = kwargs.pop('veiculo_form', None)

        endereco_form = EnderecoFormSet(
            request.POST, prefix='endereco_form', instance=self.object)
        pastor_form = PastorFormSet(
            request.POST, prefix='pastor_form', instance=self.object)
        filho_form = FilhoFormSet(
            request.POST, prefix='filho_form', instance=self.object)
        banco_form = BancoFormSet(
            request.POST, prefix='banco_form', instance=self.object)
        documento_form = DocumentoFormSet(
            request.POST, prefix='documento_form', instance=self.object)

        telefone_form = TelefoneFormSet(
            request.POST, prefix='telefone_form', instance=self.object)
        email_form = EmailFormSet(
            request.POST, prefix='email_form', instance=self.object)
        site_form = SiteFormSet(request.POST, prefix='site_form', instance=self.object)

        formsets = [telefone_form, email_form, site_form]
        

        if veiculo_form:
            extra_forms = [veiculo_form, ]

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.tipo_pessoa = 'PJ'
            if self.object.tipo_pessoa == 'PJ':
                pessoa_form = PessoaJuridicaForm(
                    request.POST, prefix='pessoa_jur_form')
            else:
                pessoa_form = PessoaFisicaForm(
                    request.POST, prefix='pessoa_fis_form')

            if (all(formset.is_valid() for formset in formsets) and
                pessoa_form.is_valid() and
                endereco_form.is_valid() and
                pastor_form.is_valid() and
                filho_form.is_valid() and
                banco_form.is_valid() and
                    all(extra_form.is_valid() for extra_form in extra_forms)):

                self.object = form.save(commit=False)
                self.object.save()
                self.object.tipo_pessoa = 'PJ'
                if self.object.tipo_pessoa == 'PJ':
                    # Remover pessoa fisica da DB se existir
                    PessoaFisica.objects.filter(
                        pessoa_id=self.object.pk).delete()
                else:
                    # Remover pessoa juridica da DB se existir
                    PessoaJuridica.objects.filter(
                        pessoa_id=self.object.pk).delete()

                # Salvar informacoes endereco
                endereco_form.instance = self.object
                end = endereco_form.save()
                if len(end):
                    if self.object.endereco_padrao:
                        self.object.endereco_padrao = self.object.endereco_padrao
                    else:
                        self.object.endereco_padrao = end[0]
                
                # Salvar informacoes 
                pastor_form.instance = self.object
                pastor = pastor_form.save()
                if len(pastor):
                    self.object.pastor_form = pastor[0]

                filho_form.instance = self.object
                filho = filho_form.save()

                # Salvar informacoes bancarias
                banco_form.instance = self.object
                ban = banco_form.save()
                if len(ban):
                    self.object.banco_padrao = ban[0]


                # Salvar telefone
                telefone_form.instance = self.object
                tel = telefone_form.save()
                if len(tel):
                    self.object.telefone_padrao = tel[0]

                # Salvar email
                email_form.instance = self.object
                ema = email_form.save()
                if len(ema):
                    self.object.email_padrao = ema[0]

                # Salvar site
                site_form.instance = self.object
                sit = site_form.save()
                if len(sit):
                    self.object.site_padrao = sit[0]

                if veiculo_form:
                    veiculo_form.instance = self.object
                    veiculo_form.save()

                return self.form_valid(form)

        logo_file = kwargs.pop('logo_file', None)
        self.object.tipo_pessoa = 'PJ'
        if self.object.tipo_pessoa == 'PJ':
            pessoa_juridica_form = PessoaJuridicaForm(
                request.POST, prefix='pessoa_jur_form', instance=self.object)
            pessoa_fisica_form = PessoaFisicaForm(
                request.POST, prefix='pessoa_fis_form')
        else:
            pessoa_juridica_form = PessoaJuridicaForm(
                request.POST, prefix='pessoa_jur_form')
            pessoa_fisica_form = PessoaFisicaForm(
                request.POST, prefix='pessoa_fis_form', instance=self.object)

        return self.form_invalid(form=form,
                                 pessoa_juridica_form=pessoa_juridica_form,
                                 pessoa_fisica_form=pessoa_fisica_form,
                                 endereco_form=endereco_form,
                                 pastor_form=pastor_form,
                                 filho_form=filho_form,
                                 banco_form=banco_form,
                                 formsets=formsets,
                                 veiculo_form=veiculo_form,
                                 logo_file=logo_file)
