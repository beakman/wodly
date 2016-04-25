# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet

from .models import User, Wod, Exercise
from .forms import WodForm, ExerciseForm, ExerciseFormSet


class WodDetailView(LoginRequiredMixin, DetailView):
    model = Wod


class WodUpdateView(LoginRequiredMixin, UpdateView):

    model = Wod
    form_class = WodForm

    def get_context_data(self, **kwargs):
        context = super(WodUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ExerciseFormSet(self.request.POST)
        else:
            context['formset'] = ExerciseFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            # assuming your model has ``get_absolute_url`` defined.
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class WodCreateView(LoginRequiredMixin, CreateView):

    model = Wod
    form_class = ExerciseFormSet

    def get_context_data(self, **kwargs):
        context = super(WodCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ExerciseFormSet(self.request.POST)
        else:
            context['formset'] = ExerciseFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid():
		    wod = form.save(commit=False)
		    wod.user = self.request.user
		    wod.save()
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            # assuming your model has ``get_absolute_url`` defined.
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class WodListView(LoginRequiredMixin, ListView):
    model = Wod

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['username'])
        if user.username == self.request.user.username:
            return Wod.objects.filter(user=self.request.user)
        else:
            return Wod.objects.filter(user=user, is_public=True)

    def get_context_data(self, **kwargs):
        context = super(WodListView, self).get_context_data(**kwargs)
        context['current_user'] = self.request.user
        context['query_user'] = User.objects.get(
            username=self.kwargs['username'])
        return context
