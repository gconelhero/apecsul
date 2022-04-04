from apecsul.cadastro.models import PessoaJuridica, Endereco, Pastor, Telefone, Email, Site
from django.shortcuts import render, redirect
    

def igrejas_view(request):
    if request.user.is_authenticated:
        igrejas = PessoaJuridica.objects.all()
        igrejas_list = []
        for igreja in igrejas:
            endereco = Endereco.objects.all().filter(pk=igreja.pk)
            pastor = Pastor.objects.all().filter(pastor_id=igreja.pk)
            email = Email.objects.all().filter(pk=igreja.pk)
            telefone = Telefone.objects.all().filter(pk=igreja.pk)
            site = Site.objects.all().filter(pk=igreja.pk)
            igreja_obj = [igreja, endereco, pastor, email, telefone, site]
            igrejas_list.append(igreja_obj)
            
        context = {'fazenda': igrejas,
                   'igrejas': igrejas_list,
                   }
        
        return render(request, 'cadastro/igrejas_view.html', context)
    else:
        return redirect('accounts/login')

def igreja_view(request, pk):
    if request.user.is_authenticated:
        igreja = PessoaJuridica.objects.get(pk=pk)
        endereco = Endereco.objects.get(pk=igreja.pk)
        pastor = Pastor.objects.all().filter(pastor_id=igreja.pk)
        email = Email.objects.get(pk=igreja.pk)
        telefone = Telefone.objects.get(pk=igreja.pk)
        site = Site.objects.get(pk=igreja.pk)
        context = {'fazenda': igreja,
                   'endereco': endereco,
                   'pastor': pastor,
                   'email': email,
                   'telefone': telefone,
                   'site': site,
                   }

        return render(request, 'cadastro/igreja_view.html', context)
    else:
        return redirect('accounts/login')
