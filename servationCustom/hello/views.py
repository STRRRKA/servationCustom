from django.shortcuts import render
from .models import Person, TicketCinema, Session, Movie
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.serializers.json import DjangoJSONEncoder

def getSessions(tmp=None):
    if tmp is None:
        return Session.objects.all()
    elif type(tmp) is Movie:
        return Session.objects.get(movie = tmp)
    elif type(tmp) is int:
        return Session.objects.get(id=tmp)

def createhall(request):
    if request.method == "POST":
        print(request.POST.get("code"))
    return render(request, "createhall.html")

def index(request):

    return render(request, "index.html")

def hotel(request ):    
    people = Person.objects.all()
    return render(request, "hotel.html", {"people": people})

def avia(request):

    return render(request, "avia.html")

def session(request, id):
    # добавить в модель количество занятых
    session = getSessions(id)
    return render(request, 'session.html', {"session": session})

def cinema(request):
    sessions = getSessions()
    if request.method == "POST":
        name1 = Movie.objects.get(name=request.POST.get("name"))
        # check = Session.objects.get(movie = name1)
        check = getSessions(name1)
        return render(request, "cinema.html", {"sessions": sessions, "check": check})
    # name1 = Movie.objects.get(name = request.POST.get("name"))
    # print(name1)
    # if request.method == "GET":
    
    return render(request, "cinema.html", {"sessions": sessions})
    # elif request.method == "POST":
        
        # sessions = Session.objects.get(name)
        # return render(request, "cinema.html", {"sessions": sessions})
#     people = Person.objects.all()
#     peopledict = people.values()
#     dic2 = people[1].name
#     dictlist = []
#     dict1 = {}
#     data = list(people)
#     data2 = list(people)
#     m=1
#     print(data2)
#     for person in people:
#         listofid = ['id', person.id]
#         listofname = ['name', person.name]
#         listofage = ['age', person.age]
#         listoflist = []
#         listoflist.append(listofid)
#         listoflist.append(listofname)
#         listoflist.append(listofage)
#         dict2 = dict(listoflist)
#         print("dict2: ",dict2)
#         dict1.update(dict2)
#         print("dict1: ", dict1)
#         # dictlist.append(listoflist)
#         # dicktlistsep = []
#         # dicktlistsep.append("name")
#         # dicktlistsep.append(person.name)
#         # dicktlistsep.append("name")
#         # print(dicktlistsep)
#         # # dicktlistsep.append(person.name)
#         # # dicktlistsep.append("age")
#         # # dicktlistsep.append(person.age)
#         # dictlist.append(dicktlistsep)
#     print (dict1)
#     # dic = dict(dictlist)
#     classes = {
#     'Python': [
#         'Intro Python', 'Advanced Python', 'Data Science', 'Django'
#     ],
#     'Databases': [
#         'Intro PostgreSQL', 'Intro MySQL', 'Intro SQL Server', 'Intro Oracle'
#     ],
#     'Web': [
#         'HTML', 'CSS', 'JavaScript'
#     ],
#     'XML': [
#         'Intro XML'
#     ]
# }

    
#     # for person in people:
#     #     print(person.name)
#     if request.method == "POST":
#         check = request.POST.get('movie')
#         # if check =="aa":
#         title = request.POST.get('title') 
#         name = request.POST.get('name')
#         print(name)
#         # return HttpResponseRedirect("")
#         # data.append(title)
#         # m= m + 1
#             # data.append(list(people))
#             # return render(request, "cinema.html", {"people": data})
#             # return HttpResponseRedirect("/cinema", {'check': check})
        
#         # for person in peopledict:
#         #     return JsonResponse(person, safe=False, encoder=PersonEncoder)
#     # print(dic)
#     return render(request, "cinema.html", {"people": data})

