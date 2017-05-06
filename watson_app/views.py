from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django import forms
from django.conf import settings
from watson_app.models import Tone
import operator

# Watson dependencies
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3



# Watson authentication
#here is a comment
tone_analyzer = ToneAnalyzerV3(
    username='afad9d73-df3e-41c8-976c-9c505fa2dd12',
    password='SPBJxlMsVrl0',
    version='2016-02-11')


# Create your views here.
from django.views.generic.edit import FormView
from watson_app.forms import CommentForm


def submit(request):
    selected_choice = request.POST['userinput']
    # tone_analyzer.tone(selected_choice)
    # current_tone = Tone()
    # current_tone  # potentially use to save tones

    # arrays to save varies types of tones from watson
    emotions = dict()
    writing = dict()
    personality = dict()
    data = json.loads(json.dumps(tone_analyzer.tone(selected_choice), indent=2).decode("utf-8"))

    # parse Json object and fill arrays
    for cat in data['document_tone']['tone_categories']:
        # print('Category:', cat['category_name'])
        for tone in cat['tones']:
            if cat['category_name'] == 'Emotion Tone':
                emotions.update({tone['tone_name']: tone['score']})
            if cat['category_name'] == 'Writing Tone':
                writing.update({tone['tone_name']: tone['score']})
            if cat['category_name'] == 'Social Tone':
                personality.update({tone['tone_name']: tone['score']})
                # print('emmanuel thinks this is \n')
                # print(emotions[tone['tone_name']])
            # print('-', tone['tone_name'])
    # print(json.dumps(tone_analyzer.tone(selected_choice), indent=2))

    # get sorted representation of the dict and take the highest element
    sorted_emotions = sorted(emotions.items(), key=operator.itemgetter(1), reverse=True)
    my_reply = next(iter(sorted_emotions))
    # context = {
    #     'emotion': my_reply[0],
    #     'valence': my_reply[0],
    # }

    # return redirect('watson/emotion.html', my_reply[0])
    return HttpResponse(my_reply[0])



class CommentView(FormView):
    template_name = 'watson/comment.html'
    form_class = CommentForm
    success_url = '.'

    def form_valid(self, form):
        serialized_json = json.dumps(form.ask_watson(), sort_keys=True, indent=4)
        return HttpResponse(serialized_json, content_type="application/json")
