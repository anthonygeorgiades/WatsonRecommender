from django import forms
from django.http import HttpResponse
from django.conf import settings

# Watson dependencies
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

#Getting APIKEY variable from settings
# APIKEY = {
#   "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
#   "username": "24f37052-507d-4e52-a2e6-dd2b99b4666f",
#   "password": "vAFkxEExVyfl"
# }
#
#   "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
#   "username": "24f37052-507d-4e52-a2e6-dd2b99b4666f",
#   "password": "vAFkxEExVyfl"


# APIKEY = getattr(settings, "APIKEY", "SECRET")

# Watson authentication
tone_analyzer = ToneAnalyzerV3(
    username='afad9d73-df3e-41c8-976c-9c505fa2dd12',
    password='SPBJxlMsVrl0',
    version='2016-02-11')




# print(json.dumps(tone_analyzer.tone(text='userinput'), indent=2))

# print(json.dumps(tone_analyzer.tone(text='I am very happy'), indent=2))

# utterances = [{'text': 'I am very happy', 'user': 'glenn'}]
# print(json.dumps(tone_analyzer.tone(utterances), indent=2))


class CommentForm(forms.Form):
    comment = forms.CharField(
        label="Comment", widget=forms.Textarea(attrs={'rows': 10}), required=True)

    def ask_watson(self):
        text = self.cleaned_data['comment']
        combined_operations = ['doc-sentiment']
        return tone_analyzer.combined(text=text, extract=combined_operations)