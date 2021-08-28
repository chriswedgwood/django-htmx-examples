from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Contact
from .forms import ContactForm


def initial_state(request):
    context = {}
    contact = Contact.objects.first()
    context["contact"] = contact
    return render(request, "click_to_edit/initial_state.html", context)


@require_http_methods(["GET"])
def contact_edit(request, contact_id):
    context = {}
    contact = get_object_or_404(Contact, id=contact_id)

    form = ContactForm(instance=contact)
    context["form"] = form
    context["contact_id"] = contact_id
    return render(request, "click_to_edit/contact_edit.html", context)


@api_view(["GET", "PUT"])
def contact_detail(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "GET":
        return HttpResponseRedirect(reverse("click-to-edit-initial-state"))
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("click-to-edit-initial-state"))
    else:
        raise Http404
