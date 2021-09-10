from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser
from django.http import QueryDict

from .models import Customer
from .forms import Customer


def customer_status(request):
    context = {}
    customers = Customer.objects.all()
    context["customers"] = customers
    return render(request, "bulk_update/customer_status.html", context)


@require_http_methods(["PUT"])
def customer_activate(request):
    context = {}
    data = request.body.decode("utf-8")
    q = QueryDict(data, mutable=True)
    activated_ids = q.getlist("ids")
    Customer.objects.filter(pk__in=activated_ids).update(status=True)
    customers = Customer.objects.all()
    context["customers"] = customers
    return render(request, "bulk_update/customer_status_update.html", context)


@require_http_methods(["PUT"])
def customer_deactivate(request):
    context = {}
    data = request.body.decode("utf-8")
    q = QueryDict(data, mutable=True)
    activated_ids = q.getlist("ids")
    Customer.objects.filter(pk__in=activated_ids).update(status=False)
    customers = Customer.objects.all()
    context["customers"] = customers
    return render(request, "bulk_update/customer_status_update.html", context)
