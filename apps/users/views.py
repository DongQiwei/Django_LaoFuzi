from django.shortcuts import render, redirect
from django.views.generic.base import View
from books.models import Tag, Art
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from datetime import datetime

from .forms import LoginForm, RegisterForm
from .models import UserProfile
from .tasks import send_register_email
from .models import EmailVerifyRecord


def create_pwd_md5(str_password):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str_password.encode(encoding="utf-8"))
    return h1.hexdigest()


# Create your views here.

def index(request):
    if request.method == 'GET':
        t_id = request.GET.get('t', '')
        if not t_id:
            t_id = 1
            arts = Art.objects.filter(t_id=t_id).all()
        elif t_id == '0':
            arts = Art.objects.all()
        else:
            t_id = int(t_id)
            arts = Art.objects.filter(t_id=t_id).all()
        tags = Tag.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(arts, 12, request=request)

        arts = p.page(page)
        sort = t_id
        return render(request, 'index_handler.html', {'tags': tags, 'data': arts, 'sort': sort})

    if request.method == 'POST':
        pass


class ActiveUserView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = 1
                user.save()
        else:
            return render(request, "active_fail.html")

        return render(request, "login.html")


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = create_pwd_md5(request.POST.get("password", ""))
            user = UserProfile.objects.filter(username=username, password=password).first()
            if user is not None:
                if user.is_active:
                    request.session["muser"] = user
                    return redirect('/')
                else:
                    return render(request, "login.html", {"msg": "用户未激活！"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.is_active = False
            user_profile.email = user_name
            user_profile.password = create_pwd_md5(pass_word)
            user_profile.save()
            print('start send mail time:', datetime.now())
            send_register_email.delay(user_name, "register")
            print('end send mail time:', datetime.now())
            return render(request, 'waitint.html')
        else:
            return render(request, "register.html", {"register_form": register_form})
