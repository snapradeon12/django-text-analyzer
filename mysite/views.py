from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')

    # Remove punctuation
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_{|}~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed += char
        text=analyzed
        params = {
            'purpose': 'Removed Punctuation',
            'analyzed_text': analyzed
        }

        # return render(request, 'analyze.html', params)
    
    # Convert to uppercase
    if fullcaps == "on":
        analyzed = ""
        for char in text:
            analyzed += char.upper()

        params = {
            'purpose': 'Capitalized Letters',
            'analyzed_text': analyzed
        }
        text=analyzed
        # return render(request, 'analyze.html', params)

    # Remove newline characters
    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n":
                analyzed += char

        params = {
            'purpose': 'Remove New Line Characters',
            'analyzed_text': analyzed
        }
        text=analyzed
        # return render(request, 'analyze.html', params)

    # Error if no option is selected
    return render(request, 'analyze.html', params)
    
