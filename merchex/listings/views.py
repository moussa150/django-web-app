
from django.shortcuts import redirect, render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Annonce
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.models import BandForm

def band_list(request):
    bands=Band.objects.all()
    return render(request,'listings/band_list.html',{'bands':bands})

def band_detail(request,id):
    band=Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',{'band':band})


def createBand(request):
    if request.method=='POST':

        form=BandForm(request.POST)
        if form.is_valid():
            band=form.save()

            return redirect('band-detail',band.id)
    else:
        form=BandForm()

    return render(request,'listings/band-create.html',{'form':form})





def updateBand(request,id):
    band=Band.objects.get(id=id)
    if(request.method == 'POST'):
        form=BandForm(request.POST,instance=band)
    # form=BandForm(instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail',band.id)
    else:
         form=BandForm(instance=band)

    return render(request,'listings/band-update.html',{'form':form})





def deleteBand(request,id):
    band=Band.objects.get(id=id)

    if request.method == 'POST':
            # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    return render(request,'listings/band-delete.html',{'band':band})




def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons Merch</p>')




def listing(request):
    ancs=Annonce.objects.all()
    return render(request,'listings/listings.html',{'ancs':ancs})



def contact(request):
    if request.method == 'POST':
        form=ContactUsForm(request.POST)

        if form.is_valid():
              send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )

        redirect('email-sent')

    else:
        form=ContactUsForm()
        
    return render(request,'listings/contact.html',{'form':form})

def email(request):
    return HttpResponse('<h1>Welcome</h1>')
