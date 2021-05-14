from django.http.response import HttpResponse
from main.models import Poll
from .forms import CreatePollForm
from django.shortcuts import redirect, render

def index(request):
    polls = Poll.objects.all().order_by('-id')
    return render(request, 'home.html', {'polls':polls})

def create(request):
    form = CreatePollForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("index")
    return render(request, 'create.html', {'form':form})

def vote(request, pk):
    ques = Poll.objects.get(id=pk)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            ques.option_one_count += 1
        elif selected_option == 'option2':
            ques.option_two_count += 1
        elif selected_option == 'option3':
            ques.option_three_count +=1
        else:
            return HttpResponse(400, 'Invalid Syntax')
        ques.save()
        return redirect("results", ques.id)
    return render(request, 'vote.html', {'ques':ques})

def results(request, pk):
    ques = Poll.objects.get(id=pk)
    return render(request, 'results.html', {'ques':ques})
