from django.shortcuts import render, redirect
from .models import *
from datetime import *

# Create your views here.
def add(request):
    return render(request,'add_show/add_show.html')

def display_show(request,show_id):
    context = {
        'show' : Show.objects.get(id=show_id),
    }

    return render(request,'add_show/display_show.html', context)

def all_shows(request):
    create_table_for_home(request)
    return render(request,'add_show/all_shows.html')


def edit_show(request,show_id):
    request.session['processing'] = 'edit'
    request.session['show_id'] = show_id
    current_show = Show.objects.get(id=show_id)

    date = current_show.release_date

    context = {
        'show': current_show,
        'show_release_date': str(date),
    }

    return render(request,'add_show/edit_show.html', context)

def edit_process(request):
    if request.method=="POST":
        current_show = Show.objects.get(id=request.session['show_id'])

        current_show.title = request.POST['title']
        current_show.network = request.POST['network']
        current_show.release_date = request.POST['release_date']
        current_show.description = request.POST['description']
        current_show.save()
    return redirect('/shows')

def add_process(request):
    if request.method=="POST":
        date = request.POST['release_date']
        date = datetime.strptime(date, '%Y-%m-%d')
        new_entry = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        new_entry.save()

    return redirect('/shows')

def delete_show(request,show_id):
    current_show = Show.objects.get(id=show_id)

    current_show.delete()

    return redirect('/shows')

def home(request):
    return redirect('/shows')

def create_table_for_home(request):
    request.session['for_print'] = []
    shows = Show.objects.all()

    for x in range(0,len(shows),1):
        show_url = f"<a href='/shows/{shows[x].id}' class='btn btn-sm btn-info'>Show</a>"
        edit_url = f"<a href='/shows/{shows[x].id}/edit' class='btn btn-sm btn-info'>Edit</a>"
        delete_url = f"<a href='/shows/{shows[x].id}/delete' class='btn btn-sm btn-info'>Delete</a>"
        request.session['for_print'].append(f"<tr><th scope='col'>{shows[x].id}</th><th scope='col'>{shows[x].title}</th><th scope='col'>{shows[x].network}</th><th scope='col'>{shows[x].release_date}</th><th scope='col'>{show_url}</th><th scope='col'>{edit_url}</th><th scope='col'>{delete_url}</th></tr>")

    return redirect('/shows')