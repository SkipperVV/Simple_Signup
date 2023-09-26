from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import  BasicSignupForm #, BaseRegisterForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import Group
import pprint

# class BaseRegisterView(CreateView):
#     model = User
#     form_class = BaseRegisterForm
#     success_url = '/'

class BasicSignupView(CreateView):
    model = User
    form_class = BasicSignupForm
    success_url = '/'

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_premium'] = self.request.user.groups.filter(group_name = 'premium').exists()
        context['groups'] = self.request.user.groups.get.all()
        return context 
    
@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='premium')
    if not request.user.groups.filter(name='premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')     