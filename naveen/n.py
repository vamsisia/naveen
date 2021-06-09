from django.http import HttpResponse
from django.shortcuts import render

def ab(p):
    return render(p,"countwords.html");
def about(p):
    return render(p,"about.html")
def bc(p):
    mess=p.GET['message'];
    a=mess.split();
    print(a)
    le=len(a)
    wordscount={}
    for word in a:
        if word in wordscount:
            wordscount[word]+=1;
        else:
            wordscount[word]=1;


    return render(p,"count.html",{'msg':mess, 'length':le, 'abc':wordscount});

def nav(request):
    d={'vamsi':100,'naveen':200 }
    return render(request,"url.html", {'avatar':d.values()});
