from django.contrib import messages, auth
from django.contrib.auth.models import User

from .admin import AdminSample
from .models import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.
def mainpage(request):
    return render(request, 'html/ripplesmainpage.html')


def aboutus(request):
    return render(request, 'html/ripplesaboutus.html')


def events(request):
    return render(request, 'html/rippleseventspage.html')


def te1(request):
    if request.method == "POST":
        try:  # use of try block because if user tries to register without logging in there would be error
            user = request.user
            z = 0
            for i in Te1.objects.all():
                if i.username == user.username:
                    z = 1
                    break
            if z == 0:
                en = Te1(username=user.username, email=user.email)
                en.save()
                messages.info(request, "You have successfully registered for the event.")

            else:
                messages.info(request, "You have already registered for this event.")


            return redirect('/te1/')

        except:
            return redirect('/signup/')
    else:
        return render(request, 'html/techevent1.html')


def te2(request):
    if request.method == "POST":
        try:  # use of try block because if user tries to register without logging in there would be error
            user = request.user
            z = 0
            for i in Te2.objects.all():
                if i.username == user.username:
                    z = 1
                    break
            if z == 0:
                en = Te2(username=user.username, email=user.email)
                en.save()
                messages.info(request, "You have successfully registered for the event.")

            else:
                messages.info(request, "You have already registered for this event.")
            return redirect('/te2/')

        except:
            return redirect('/signup/')
    else:
        return render(request, 'html/techevent2.html')


def te3(request):
    if request.method == "POST":
        try:  # use of try block because if user tries to register without logging in there would be error
            user = request.user
            z = 0
            for i in Te3.objects.all():
                if i.username == user.username:
                    z = 1
                    break
            if z == 0:
                en = Te3(username=user.username, email=user.email)
                en.save()
                messages.info(request, "You have successfully registered for the event.")

            else:
                messages.info(request, "You have already registered for this event.")
            return redirect('/te3/')

        except:
            return redirect('/signup/')
    else:
        return render(request, 'html/techevent3.html')


def nte1(request):
    if request.method == "POST":
        try:  # use of try block because if user tries to register without logging in there would be error
            user = request.user
            z = 0
            for i in Nte1.objects.all():
                if i.username == user.username:
                    z = 1
                    break
            if z == 0:
                en = Nte1(username=user.username, email=user.email)
                en.save()
                messages.info(request, "You have successfully registered for the event.")

            else:
                messages.info(request, "You have already registered for this event.")
            return redirect('/nte1/')

        except:
            return redirect('/signup/')
    else:
        return render(request, 'html/nontechevent1.html')


def nte2(request):
    if request.method == "POST":
        try:  # use of try block because if user tries to register without logging in there would be error
            user = request.user
            z = 0
            for i in Nte2.objects.all():
                if i.username == user.username:
                    z = 1
                    break
            if z == 0:
                en = Nte2(username=user.username, email=user.email)
                en.save()
                messages.info(request, "You have successfully registered for the event.")

            else:
                messages.info(request, "You have already registered for this event.")
            return redirect('/nte2/')

        except:
            return redirect('/signup/')
    else:
        return render(request, 'html/nontechevent2.html')


def nte3(request):
    if request.method == "POST":
        try:  # use of try block because if user tries to register without logging in there would be error
            user = request.user
            z = 0
            for i in Nte3.objects.all():
                if i.username == user.username:
                    z = 1
                    break
            if z == 0:
                en = Nte3(username=user.username, email=user.email)
                en.save()
                messages.info(request, "You have successfully registered for the event.")

            else:
                messages.info(request, "You have already registered for this event.")
            return redirect('/nte3/')

        except:
            return redirect('/signup/')
    else:
        return render(request, 'html/nontechevent3.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        mailid = request.POST['mailid']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 15:
            display_name = username[0:username.index(' ')]
        else:
            display_name = username
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'NAME ALREADY EXISTS')
                return redirect('/signup/')
            elif User.objects.filter(email=mailid).exists():
                messages.info(request, 'EMAIL ALREADY USED')
                return redirect('/signup/')
            else:  # all condition satisfied
                user = User.objects.create_user(username=username, email=mailid, password=pass1, last_name=display_name)
                user.save()

                return redirect('/signin/')  # after account created sign in
        else:
            messages.info(request, 'PASSWORD NOT MATCHED')
            return redirect('/signup/')
    else:
        return render(request, 'html/loginform.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:  # user has account
            auth.login(request, user)  # logging him with his credentials
            return redirect('/')  # redirecting to home
        else:
            messages.info(request, "BAD CREDENTIALS")
            return redirect('/signin/')
    else:
        return render(request, 'html/signinform.html')


def mylist(request):

    events = {'Te1': 'Paper Presentation', 'Te2' : 'Circuit Craze', 'Te3' : 'Dynamic Array',
              'Nte1': 'Paper Presentation', 'Nte2' : 'Circuit Craze', 'Nte3' : 'Dynamic Array'}
    if request.method == "POST":
        try:
            user = request.user
            z = 0
            if user is not None:
                name = user.username
                for i in Te1.objects.all():
                    if i.username == name:
                        messages.info(request, events['Te1'])
                        z = 1
                        break

                for i in Te2.objects.all():
                    if i.username == name:
                        messages.info(request, events['Te2'])
                        z = 1
                        break

                for i in Te3.objects.all():
                    if i.username == name:
                        messages.info(request, events['Te3'])
                        z = 1
                        break

                for i in Nte1.objects.all():
                    if i.username == name:
                        messages.info(request, events['Nte1'])
                        z = 1
                        break

                for i in Nte2.objects.all():
                    if i.username == name:
                        messages.info(request, events['Nte2'])
                        z = 1
                        break

                for i in Nte3.objects.all():
                    if i.username == name:
                        messages.info(request, events['Nte3'])
                        z = 1
                        break
            if z == 0:
                messages.info(request, 'You have not yet registered for any event')
            return redirect('/mylist/')

        except:
            return redirect('/mylist/')

    return render(request, 'html/eventregistrationlist.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
