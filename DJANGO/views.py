# exercise 2
from django.http import HttpResponse
from django.shortcuts import render


def home(requests):
    return render(requests, 'index.html')


def calculation(requests):
    return render(requests, 'calc.html')


def taker(requests):
    a = requests.POST.get('text', 'default')
    b = a
    punctick = requests.POST.get('remPunc', 'off')
    linetick = requests.POST.get('remLine', 'off')
    makeupper = requests.POST.get('makeUpper', 'off')
    esr = requests.POST.get('extraSpaceRemover', 'off')
    charCounter = requests.POST.get('charCount', 'off')

    # for punctuations
    if punctick == 'on':
        puncmarks = '!!?@#!!*&@!'
        val = ''
        for i in a:
            if i not in puncmarks:
                val = val + i
        a = val
    # for new line removal
    if linetick == 'on':
        val = ''
        for i in a:
            if i != "\n" and i != "\r":
                val = val + i
        a = val
    # for making uppercase
    if makeupper == 'on':
        val = a.upper()
        a = val
    if esr == 'on':
        val = ''
        for i, j in enumerate(b):
            if not(b[i] == ' ' and b[i+1] == ' '):
                val = val + j
        a = val

    if esr == 'on':
        val = ''
        for i, j in enumerate(a):
            if not (a[i] == ' ' and a[i+1] == ' '):
                val = val + j
        a = val

    # character Count
    if charCounter == 'on':
        val = 0
        for i in a:
            val += 1
        a += 'total Characters are - ' + str(val)
    dict = {'result': val}
    return render(requests, 'result.html', dict)
