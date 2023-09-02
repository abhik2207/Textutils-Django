# I have created this file - Abhik
from django.http import HttpResponse
from django.shortcuts import render

# PART - 1
# def index(request):
#     # params = {"name":"Abhik", "place":"Mars"} # A dictionary too can be used like this
#     # return render(request, 'index.html', params)
#     return render(request, 'index.html')
# def about(request):
#     text = '''
#     <h1>Made by Abhik Gupta</h1>
#     <button><a href="/">Back</a></button>
#     '''
#     return HttpResponse(text)  # Returns what is to be displayed on site
# def quote(request):
#     with open("textutils\\quote.txt", "r") as f: # Opening the file in read mode, we don't use r+ because file already exists, r+ is used when file doesn't exists then assigning it a variable named f
#         content = f.read() # Reading the contents of the file and storing it in a variable, we use read instead of readlines because readlines gives each line as a list element
#     text = f'<h1>{content}</h1><br><button><a href="/">Back</a></button>'
#     return HttpResponse(text)
# # Exercise 1 solution
# def mostUsedLinks(request):
#     text = '''
#     <a href="https://www.youtube.com/" target="blank">Youtube</a>
#     <a href="https://www.instagram.com/" target="blank">Instagram</a>
#     <a href="https://www.facebook.com/" target="blank">Facebook</a>
#     <br>
#     <button><a href="/">Back</a></button>
#     '''
#     return HttpResponse(text)
# def contact(request):
#     text = '''
#     <h1>Contact me at abhikgupta01@gmail.com</h1>
#     <button><a href="/">Back</a></button>
#     '''
#     return HttpResponse(text)
# def services(request):
#     text = '''
#     <h1>Contact me for programming services</h1>
#     <button><a href="/">Back</a></button>
#     '''
#     return HttpResponse(text)
# def gallery(request):
#     text = '''
#     <h1>This is an image gallery</h1>
#     <button><a href="/">Back</a></button>
#     '''
#     return HttpResponse(text)

# PART - 2
def index(request):
    # params = {"name":"Abhik", "place":"Mars"} # A dictionary too can be used like this
    # return render(request, 'index.html', params)
    return render(request, 'index.html')

def analyze(request):
    # Getting the text from textarea
    # formtext = request.GET.get("textarea", "default")
    formtext = request.POST.get("textarea", "default")

    # Checking checkbox values
    # removepunc = request.GET.get("removepunctuation", "off")
    # upcase = request.GET.get("uppercase", "off")
    # lowcase = request.GET.get("lowercase", "off")
    # capcase = request.GET.get("capitalize", "off")
    # newlineremove = request.GET.get("removenewline", "off")
    # extraspaceremove = request.GET.get("removeextraspace", "off")
    # countcharacters = request.GET.get("countchacaters", "off")
    removepunc = request.POST.get("removepunctuation", "off")
    upcase = request.POST.get("uppercase", "off")
    lowcase = request.POST.get("lowercase", "off")
    capcase = request.POST.get("capitalize", "off")
    newlineremove = request.POST.get("removenewline", "off")
    extraspaceremove = request.POST.get("removeextraspace", "off")
    countcharacters = request.POST.get("countchacaters", "off")

    # Fulfilling the purpose
    if removepunc == 'on':
        # Initializing analyzed text
        analyzed = ""
        punctuations = ''':;[]{}-_=+)'~`"(*&^%$#@!,.<>/?\|'''
        for char in formtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations!', 'analyzedText': analyzed}
        formtext = analyzed
    if upcase == 'on':
        # Initializing analyzed text
        analyzed = ""
        analyzed = formtext.upper()
        params = {'purpose': 'Transform to uppercase!', 'analyzedText': analyzed}
        formtext = analyzed
    if lowcase == 'on':
        # Initializing analyzed text
        analyzed = ""
        analyzed = formtext.lower()
        params = {'purpose': 'Transform to lowercase!', 'analyzedText': analyzed}
        formtext = analyzed
    if capcase == 'on':
        # Initializing analyzed text
        analyzed = ""
        analyzed = formtext.capitalize()
        params = {'purpose': 'Capitalize!', 'analyzedText': analyzed}
        formtext = analyzed
    if newlineremove == 'on':
        # Initializing analyzed text
        analyzed = ""
        for char in formtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                continue
        params = {'purpose': 'Remove new line!', 'analyzedText': analyzed}
        formtext = analyzed
    if extraspaceremove == 'on':
        # Initializing analyzed text
        analyzed = ""
        for index, char in enumerate(formtext):
            if formtext[index] == " " and formtext[index+1] == " ":
                continue
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra spaces!', 'analyzedText': analyzed}
        formtext = analyzed
    if countcharacters == 'on':
        # Initializing analyzed text
        analyzed = ""
        analyzed = f"Number of characters : {len(formtext)}"
        params = {'purpose': 'Count chacaters!', 'analyzedText': analyzed}

    if(removepunc=='off' and upcase=='off' and lowcase=='off' and capcase=='off' and newlineremove=='off' and extraspaceremove=='off' and countcharacters=='off'):
        return render(request, 'erroroccurred.html')

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')