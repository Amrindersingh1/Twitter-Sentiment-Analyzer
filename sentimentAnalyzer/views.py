from django.shortcuts import render
from django.http import HttpResponse
from sentimentAnalyzer.util.sentimental import Analyzer

# Create your views here.

def index(request):
    return render(request, 'sentimentAnalyzer/index.html')


def analyzeData(request):
    if request.method == 'GET':

        req_tag = request.GET.get("searchTag")

        analyzer = Analyzer()
        analyzed_data = analyzer.analyzeData(req_tag)
        analyzed_data['tag'] = '#' + req_tag.upper()
        #print(analyzed_data)
        return render(request, 'sentimentAnalyzer/analysis.html', analyzed_data)