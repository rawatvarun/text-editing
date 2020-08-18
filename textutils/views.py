import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    name1={'name':'harry', 'place':'mars'}
    return render(request,'index.html',name1)
    
#def removepunc(request):
def analyze(request):
    #get the text
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','default'))
    fullcaps=(request.POST.get('fullcaps','default'))
    newlineremover=(request.POST.get('newlineremover','default'))
    extraspaceremover=(request.POST.get('extraspaceremover','default'))
    
    print(removepunc)
    #print(djtext)
    #analyze=djtext
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyze="" 
    #check which is on 
    if removepunc=='on':
        
        for char in djtext:
            if char not in punctuations:
                analyze=analyze + char
    
    #analyze the text
        params={'purpose':'remove punctuation','analyzed_text':analyze}
        djtext=analyze
        #return render(request,'analyze.html',params)
    
    if(fullcaps=='on'):
        analyze=''
        for char in djtext:
            analyze=analyze +char.upper()
        params={'purpose':'CHANGE TO UPPER CASE','analyzed_text':analyze}
        djtext=analyze
        #return render(request,'analyze.html',params)
    if(newlineremover=='on'):
        analyze=''
        for char in djtext:
            if char !='\n' and char !='\r':
                analyze=analyze + char
        params={'purpose':'removed new line','analyzed_text':analyze}
        djtext=analyze
       #return render(request,'analyze.html',params)
    if(extraspaceremover=='on'):
        analyze=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyze=analyze + char
        params={'purpose':'removed new line','analyzed_text':analyze}
        djtext=analyze
        #return render(request,'analyze.html',params)
    
    
    if(removepunc !='on' and (fullcaps!='on') and (newlineremover=='on') and (extraspaceremover=='on') ):
        return HttpResponse("please select one of the operations")
    # if (Download text):
    #     f=open("file001.txt",'w')
    #     f.write(params)
    #     f.close()
    
    return render(request,'analyze.html',params)
    
    #return HttpResponse("remove punc")
def download1(request):
    return render(request,'analyze.html',params)
        

def ex(request):
    return HttpResponse('''
    <head><link href="https://fonts.googleapis.com/css?family=Abel" rel="stylesheet"></head>
    <style> .h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6 {
   margin-bottom: .5rem;
   font-family: 'abel', sans-serif;
   font-weight: 700;
   line-height: 1.2
   } body {
   font-size: 1rem;
   background-color: Cyan}</style>
 
    <div class="container">

    <h1>My Website</h1> <a href='/' "https://rohandas28.github.io/"> Click To Visit My Tiny Little Website!  back </a>
    <h1>Harry Bhai Ka Website </h1> <a href="https://www.codewithharry.com/"> Click To Visit The Best Website!</a>
    <h1>My Favourite Movie </h1> <a href= "https://www.google.com/search?q=interstellar&oq=interstellar&aqs=chrome..69i57j69i65.6672j0j1&sourceid=chrome&ie=UTF-8"> Click to See!</a>
    <h1>My Favourite Youtube creator </h1> <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww"> Click To Visit And Subscribe To Him!</a>
    <h1>Psst! Follow Me On Github! LoL!</h1> <a href="https://github.com/RohanDas28"> Click To Visit And Follow!</a>
    </div>''')


