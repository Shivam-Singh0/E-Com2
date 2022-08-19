from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm
from django.contrib  import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,
            
            last_name=last_name, email=email, password=password, username=username)
            user.phone_number = phone_number
            user.save()
            #user activation
            current_site = get_current_site(request)
            mail_subject = "Please activaate your account"
            message = render_to_string("account/account_verification_email.html",{
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),

            })
            to_email = email
            send_email  = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()


            return redirect("/account/login/?command=verification&email="+email)

    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form':form})


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate( email=email, password=password)

    
        if user is not None:
            auth.login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")


    return render(request, "account/login.html")

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out!')
    return redirect("login")


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        raise 
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated")
        return redirect("login")

    else:
        messages.danger(request, "Invalid Activation Link")
        return redirect("register")

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


def forgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact = email)
            current_site = get_current_site(request)
            mail_subject = "Rest Your Password"
            message = render_to_string("account/forgot_pass.html",{
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),

            })
            to_email = email
            send_email  = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'password reset link sent to your email')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist')
            return redirect('forgot')
    return render(request, 'account/forgot.html')
def reset(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, "Please reset your password")
        return redirect('resetpass')

    else:
        messages.error(request, "The link has been expired")
        return redirect("login")



def resetpass(request):
    if request.method == "POST":
        password = request.POST['password']
        confirm_pass = request.POST['confirm_pass']
        if password == confirm_pass:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful!')
            return redirect('login')
        else:
            messages.error(request, 'password does not match')
            return redirect('resetpass')
    return render(request, 'account/resetpass.html')