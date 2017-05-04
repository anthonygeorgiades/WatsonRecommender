from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from django.views.generic.edit import FormView
from watson_app.forms import CommentForm


class CommentView(FormView):
    template_name = 'watson/comment.html'
    form_class = CommentForm
    success_url = '.'

    def form_valid(self, form):
        serialized_json = json.dumps(form.ask_watson() , sort_keys=True, indent=4)
        return HttpResponse(serialized_json, content_type="application/json")