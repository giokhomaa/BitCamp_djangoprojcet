from django.shortcuts import render
from django import forms

from django.http import HttpResponseRedirect
from django.urls import reverse

#შევქმენით ფორმი რომელსაც ცვლადის სახით ვამატებთ html-ფაილში
#form შეგვეძლო გაგვეწერა html-შიც, მაგრამ აქედან გაწერით ბევრად მოსახერხებელია, ავტომატურად აკეთებს რაღაც მოქმედებებს
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

#tasks = ["foo", "bar", "baz"]

def index(request):
    #იქმნება ზევით შექმინ tasks ლისტის მაგივრად
    #სესიის მეშვეობით ყველა ახალ user-ს უკეთებს ახალ საცავს, ლისტს, იმ შემთხვევაში თუ იგი უკვე არ არსებობს
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        #session-ში ჩვამატეთ ლისტი
        "tasks" : request.session["tasks"]
    })

def add(request):

    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            #index-ში მყოფ tasks-ს ამატებს ხელით შეყვანილ task-ებს
            #tasks.append(task)

            #იგივე პრინციპით ვამატებთ Input-ში შეყვანილ ინფორმაციას
            request.session["tasks"] += [task]

            #ავტომატურად გადავყავართ ფრჩხილებში ჩაწერილ url-ზე
            return HttpResponseRedirect(reverse('tasks:index'))

    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })

