from django.shortcuts import render
from django.views.generic.base import View

from message import forms
from .models import UserMessage


# Create your views here.

class MessageView(View):
    def get(self, request):
        umsg_form = forms.UserMessageForm()
        context = dict(
            form=umsg_form
        )
        return render(request, 'msg_form.html', context=context)

    def post(self, request):
        umform = forms.UserMessageForm(data=request.POST)
        if not umform.is_valid():
            context = dict(
                form=umform
            )
            return render(request, "msg_form.html", context=context)
        form_data = umform.cleaned_data
        UserMessage.objects.create(**form_data)

        usermsg_queryset = UserMessage.objects.all()
        total = usermsg_queryset.count()
        data = usermsg_queryset
        context = dict(
            pagenum=1,
            total=total,
            prev=1,
            next=1,
            pagerange=range(1, 2),
            data=data,
            url=request.path,
            page=1,
        )
        return render(request, 'msg_list.html', context=context)
