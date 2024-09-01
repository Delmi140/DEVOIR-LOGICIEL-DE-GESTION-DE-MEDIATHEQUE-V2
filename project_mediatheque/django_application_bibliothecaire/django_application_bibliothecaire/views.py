from django.shortcuts import render
from django_application_bibliothecaire.forms import Creationmembre,Updatemembre,Creationlivre,Updatelivre,Creationcd, Updatecd,Creationdvd,Updatedvd,Creationjdp,Updatejdp
from django_application_bibliothecaire.models import Membre,Livre,Cd,Dvd,JeuxDePlateau

def listeMembre(request):
    membres = Membre.objects.all()
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jdps = JeuxDePlateau.objects.all()

    return render(request, 'application/application_bibliothecaire.html',
                  { 'livres': livres, 'membres': membres , 'cds': cds , 'dvds': dvds , 'jdps': jdps ,  } )






def ajoutmembre(request):
    if request.method == 'POST':
        creationmembre = Creationmembre(request.POST)
        if creationmembre.is_valid():
            membre = Membre()
            membre.nom = creationmembre.cleaned_data['nom']
            membre.prenom = creationmembre.cleaned_data['prenom']
            membre.Emprunt = creationmembre.cleaned_data['Emprunt']
            membre.save()
            membres =  Membre.objects.all()
            return render(request, 'application/application_bibliothecaire.html',
                          {'membres': membres})
    else:
        creationmembre = Creationmembre()
        return render(request,
                      'application/ajoutmembre.html',
                      {'creationMembre': creationmembre}
                      )

def updatemembre(request, id):
    if request.method == 'POST':
        membre = Membre.objects.get(pk=id)
        update_membre = Updatemembre(request.POST)
        if update_membre.is_valid():
            membre.nom = update_membre.cleaned_data['nom']
            membre.prenom = update_membre.cleaned_data['prenom']
            membre.Emprunt = update_membre.cleaned_data['Emprunt']
            membre.save()
        membres = Membre.objects.all()
        return render(request, 'application/application_bibliothecaire.html',
                      {'membres': membres})
    else:
        updatemembre = Updatemembre()
        return render(request,
                      'application/updatemembre.html',
                      {'updateMembre': updatemembre}
                      )

def deletemembre(request, id):
    membre = Membre.objects.get(pk=id)
    membre.delete()
    membres = Membre.objects.all()
    return render(request, 'application/application_bibliothecaire.html',
                  {'membres': membres})


def ajoutlivre(request):
    if request.method == 'POST':
        creationlivre = Creationlivre(request.POST)
        if creationlivre.is_valid():
            livre = Livre()
            livre.name = creationlivre.cleaned_data['name']
            livre.auteur = creationlivre.cleaned_data['auteur']
            livre.emprunteur = creationlivre.cleaned_data['emprunteur']
            livre.dateEmprunt = creationlivre.cleaned_data['dateEmprunt']
            livre.disponible = creationlivre.cleaned_data['disponible']


            livre.save()
            livres = Livre.objects.all()
            return render(request, 'application/application_bibliothecaire.html',
                          {'livres': livres})
    else:
        creationlivre = Creationlivre()
        return render(request,
                      'application/ajoutlivre.html',
                      {'creationLivre': creationlivre}
                      )



def updatelivre(request, id):
    if request.method == 'POST':
        livre = Livre.objects.get(pk=id)
        update_livre = Updatelivre(request.POST)
        if update_livre.is_valid():
            livre.name = update_livre.cleaned_data['name']
            livre.auteur = update_livre.cleaned_data['auteur']
            livre.disponible = update_livre.cleaned_data['disponible']
            livre.emprunteur = update_livre.cleaned_data['emprunteur']
            livre.dateEmprunt = update_livre.cleaned_data['dateEmprunt']
            livre.save()
        livres = Livre.objects.all()
        return render(request, 'application/application_bibliothecaire.html',
                      {'livres': livres})
    else:
        updatelivre = Updatelivre()
        return render(request,
                      'application/updatelivre.html',
                      {'updateLivre': updatelivre}
                      )


def deletelivre(request, id):
    livre = Livre.objects.get(pk=id)
    livre.delete()
    livres = Livre.objects.all()
    return render(request, 'application/application_bibliothecaire.html',
                  {'livres': livres})


def ajoutcd(request):
    if request.method == 'POST':
        creationcd = Creationcd(request.POST)
        if creationcd.is_valid():
            cd = Cd()
            cd.name = creationcd.cleaned_data['name']
            cd.auteur = creationcd.cleaned_data['auteur']
            cd.disponible = creationcd.cleaned_data['disponible']
            cd.emprunteur = creationcd.cleaned_data['emprunteur']
            cd.dateEmprunt = creationcd.cleaned_data['dateEmprunt']
            cd.save()
            cds =  Cd.objects.all()
            return render(request, 'application/application_bibliothecaire.html',
                          {'cds': cds})
    else:
        creationcd = Creationcd()
        return render(request,
                      'application/ajoutcd.html',
                      {'creationCd': creationcd}
                      )


def updatecd(request, id):
    if request.method == 'POST':
        cd = Cd.objects.get(pk=id)
        update_cd = Updatecd(request.POST)
        if update_cd.is_valid():
            cd.name = update_cd.cleaned_data['name']
            cd.auteur = update_cd.cleaned_data['auteur']
            cd.disponible = update_cd.cleaned_data['disponible']
            cd.emprunteur = update_cd.cleaned_data['emprunteur']
            cd.dateEmprunt = update_cd.cleaned_data['dateEmprunt']
            cd.save()
        cds = Cd.objects.all()
        return render(request, 'application/application_bibliothecaire.html',
                      {'cds': cds})

    else:
        updatecd = Updatecd()
        return render(request,
                      'application/updatecd.html',
                      {'updateCd': updatecd}
                      )

def deletecd(request, id):
    cd = Cd.objects.get(pk=id)
    cd.delete()
    cds = Cd.objects.all()
    return render(request, 'application/application_bibliothecaire.html',
                  {'cds': cds})


def ajoutdvd(request):
    if request.method == 'POST':
        creationdvd = Creationdvd(request.POST)
        if creationdvd.is_valid():
            dvd = Dvd()
            dvd.name = creationdvd.cleaned_data['name']
            dvd.auteur = creationdvd.cleaned_data['auteur']
            dvd.disponible = creationdvd.cleaned_data['disponible']
            dvd.emprunteur = creationdvd.cleaned_data['emprunteur']
            dvd.dateEmprunt = creationdvd.cleaned_data['dateEmprunt']
            dvd.save()
            dvds =  Dvd.objects.all()
            return render(request, 'application/application_bibliothecaire.html',
                          {'dvds': dvds})
    else:
        creationdvd = Creationdvd()
        return render(request,
                      'application/ajoutdvd.html',
                      {'creationDvd': creationdvd}
                      )


def updatedvd(request, id):
    if request.method == 'POST':
        dvd = Dvd.objects.get(pk=id)
        update_dvd = Updatedvd(request.POST)
        if update_dvd.is_valid():
            dvd.name = update_dvd.cleaned_data['name']
            dvd.auteur = update_dvd.cleaned_data['auteur']
            dvd.disponible = update_dvd.cleaned_data['disponible']
            dvd.emprunteur = update_dvd.cleaned_data['emprunteur']
            dvd.dateEmprunt = update_dvd.cleaned_data['dateEmprunt']
            dvd.save()
        dvds = Dvd.objects.all()
        return render(request, 'application/application_bibliothecaire.html',
                      {'dvds': dvds})

    else:
        updatedvd = Updatedvd()
        return render(request,
                      'application/updatedvd.html',
                      {'updateDvd': updatedvd}
                      )


def deletedvd(request, id):
    dvd = Dvd.objects.get(pk=id)
    dvd.delete()
    dvds = Dvd.objects.all()
    return render(request, 'application/application_bibliothecaire.html',
                  {'dvds':  dvds})


def ajoutjdp(request):
    if request.method == 'POST':
        creationjdp = Creationjdp(request.POST)
        if creationjdp.is_valid():
            jdp = JeuxDePlateau()
            jdp.name = creationjdp.cleaned_data['name']
            jdp.createur = creationjdp.cleaned_data['createur']

            jdp.save()
            jdps =  JeuxDePlateau.objects.all()
            return render(request, 'application/application_bibliothecaire.html',
                          {'jdps': jdps})
    else:
        creationjdp = Creationjdp()
        return render(request,
                      'application/ajoutjdp.html',
                      {'creationJdp':creationjdp}
                      )



def updatejdp(request, id):
    if request.method == 'POST':
        jdp = JeuxDePlateau.objects.get(pk=id)
        update_jdp = Updatejdp(request.POST)
        if update_jdp.is_valid():
            jdp.name = update_jdp.cleaned_data['name']
            jdp.createur = update_jdp.cleaned_data['createur']
            jdp.save()
        jdps = JeuxDePlateau.objects.all()
        return render(request, 'application/application_bibliothecaire.html',
                      {'jdps': jdps})
    else:
        updatejdp = Updatejdp()
        return render(request,
                      'application/updatejdp.html',
                      {'updateJdp': updatejdp}
                      )


def deletejdp(request, id):
    jdp = JeuxDePlateau.objects.get(pk=id)
    jdp.delete()
    jdps = JeuxDePlateau.objects.all()
    return render(request, 'application/application_bibliothecaire.html',
                  {'jdps':  jdps})


