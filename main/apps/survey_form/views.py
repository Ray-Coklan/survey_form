from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited   
def index(request):
    return render(request,"survey_form/index.html")



def process(request):
    request.session['name'] = request.POST['name']
    request.session['comment'] = request.POST['comment']
    request.session["counter"] += 1
    return redirect('/result')

def result(request):
        context = {
        'name': request.session['name'],
        'comment': request.session['comment'],
        'counter': request.session['counter']
}
        return render(request,'survey_form/results.html', context)