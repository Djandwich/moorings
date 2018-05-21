from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import View, TemplateView
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from datetime import datetime, timedelta

from disturbance.helpers import is_officer, is_departmentUser
from disturbance.forms import *
from disturbance.components.proposals.models import Referral, Proposal, HelpPage
from disturbance.components.compliances.models import Compliance
from disturbance.components.proposals.mixins import ReferralOwnerMixin


class InternalView(UserPassesTestMixin, TemplateView):
    template_name = 'disturbance/dash/index.html'

    def test_func(self):
        return is_officer(self.request.user)

    def get_context_data(self, **kwargs):
        context = super(InternalView, self).get_context_data(**kwargs)
        context['dev'] = settings.DEV_STATIC
        context['dev_url'] = settings.DEV_STATIC_URL
        return context

class ExternalView(LoginRequiredMixin, TemplateView):
    template_name = 'disturbance/dash/index.html'

    def get_context_data(self, **kwargs):
        context = super(ExternalView, self).get_context_data(**kwargs)
        context['dev'] = settings.DEV_STATIC
        context['dev_url'] = settings.DEV_STATIC_URL
        return context

class ReferralView(ReferralOwnerMixin, DetailView):
    model = Referral
    template_name = 'disturbance/dash/index.html'

class ExternalProposalView(DetailView):
    model = Proposal
    template_name = 'disturbance/dash/index.html'

class ExternalComplianceView(DetailView):
    model = Compliance
    template_name = 'disturbance/dash/index.html'

class DisturbanceRoutingView(TemplateView):
    template_name = 'disturbance/index.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            if is_officer(self.request.user) or is_departmentUser(self.request.user):
                return redirect('internal')
            return redirect('external')
        kwargs['form'] = LoginForm
        return super(DisturbanceRoutingView, self).get(*args, **kwargs)

@login_required(login_url='ds_home')
def first_time(request):
    context = {}
    if request.method == 'POST':
        form = FirstTimeForm(request.POST)
        redirect_url = form.data['redirect_url']
        if not redirect_url:
            redirect_url = '/'
        if form.is_valid():
            # set user attributes
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.dob = form.cleaned_data['dob']
            request.user.save()
            return redirect(redirect_url)
        context['form'] = form
        context['redirect_url'] = redirect_url
        return render(request, 'disturbance/user_profile.html', context)
    # GET default
    if 'next' in request.GET:
        context['redirect_url'] = request.GET['next']
    else:
        context['redirect_url'] = '/'
    context['dev'] = settings.DEV_STATIC
    context['dev_url'] = settings.DEV_STATIC_URL
    #return render(request, 'disturbance/user_profile.html', context)
    return render(request, 'disturbance/dash/index.html', context)



class DisturbanceHelpView(LoginRequiredMixin, TemplateView):
    template_name = 'disturbance/help.html'

    def get_queryset(self):
        return HelpPage.objects.filter(application_type__name='Disturbance').order_by('-version')

    def get_context_data(self, **kwargs):
        context = super(DisturbanceHelpView, self).get_context_data(**kwargs)
        context['help'] = self.get_queryset().first()
        return context


class ApiaryHelpView(LoginRequiredMixin, DetailView):
    template_name = 'disturbance/help.html'

    def get_queryset(self):
        return HelpPage.objects.filter(application_type__name='Apiary').order_by('-version')

    def get_context_data(self, **kwargs):
        context = super(ApiaryHelpView, self).get_context_data(**kwargs)
        context['help'] = self.get_queryset().first()
        return context


class MyCustomView(LoginRequiredMixin, TemplateView):
    #template_name = 'admin/myapp/views/my_custom_template.html'
    template_name = 'disturbance/mgt_cmds_changelist.html'

    def get(self, request):
        data = {'test': 'test',
        #'opts': MyCustomView._meta,

        'change': True,
        'is_popup': False,
        'save_as': False,
        'has_delete_permission': False,
        'has_add_permission': False,
        'has_change_permission': False}

        return render(request, self.template_name, data)

    def get_context_data(self, **kwargs):
        context = super(MyCustomView, self).get_context_data(**kwargs)
        #import ipdb; ipdb.set_trace()
        #context['help'] = HelpPage.objects.all().first()
        return context

    def post(self, request):
      # Do something
      pass


