from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from shows.models import Show
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def index(request):
    return redirect(reverse("my_shows"))

def shows(request):
    
    if 'form_data' in request.session:
        del request.session['form_data']
        
    shows = Show.objects.all()
    
    context = {
        'all_shows': shows
    }
    return render(request, "shows.html", context)

def new(request):  
    return render(request, "new.html")

def edit(request, show_id):
    this_show = Show.objects.get(id=show_id)
    
    context = {
            'this_show': this_show
    }
     
    if 'form_data' in request.session:
        return render(request, "edit.html", context)    
    else:
        form_data = {
            'show_title': this_show.title,
            'show_network': this_show.network,
            'show_date': this_show.release_date.strftime("%Y-%m-%d"),
            'show_description': this_show.description
        } 
        
        request.session['form_data'] = form_data

        return render(request, "edit.html", context)

def view(request, show_id):
    this_show = Show.objects.get(id=show_id)
    
    context = {
        'this_show': this_show,
    }
    return render(request, "view.html", context)

def create(request):
    #print (request.POST)
    
    # getting form variables
    show_title = request.POST['show_title']
    show_network = request.POST['show_network']
    show_date = request.POST['show_date']
    show_description = request.POST['show_description']
        
    # error dict is received
    errors = Show.objects.basic_validator(request.POST)
    
    # if there are errors
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        form_data = {
            'show_title': show_title,
            'show_network': show_network,
            'show_date': show_date,
            'show_description': show_description
        }
        
        request.session['form_data'] = form_data
            
        return redirect(reverse("my_new"))
    else:
        try:
            if show_description != '':          
                # create the show instance using the network object
                Show.objects.create(title=show_title, description=show_description, release_date=show_date, network=show_network)
            else:
                # calling create without description, so default is applied
                Show.objects.create(title=show_title, release_date=show_date, network=show_network)
                
            messages.success(request, "Show successfully created")
        
            return redirect(reverse("my_shows"))
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                messages.error(request, 'Title is already added to shows')
                
                form_data = {
                    'show_title': show_title,
                    'show_network': show_network,
                    'show_date': show_date,
                    'show_description': show_description
                }
                
                request.session['form_data'] = form_data

            return redirect(reverse("my_new"))

def update(request, show_id):
    
    #this_show = Show.objects.get(id=show_id)
    
    if request.POST:        
        # getting form variables
        show_title = request.POST['show_title']    
        show_network = request.POST['show_network']
        show_date = request.POST['show_date']
        show_description = request.POST['show_description']
    
        # receiving errors dict
        errors = Show.objects.basic_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            
            form_data = {
                'show_title': show_title,
                'show_network': show_network,
                'show_date': show_date,
                'show_description': show_description
            }
            
            request.session['form_data'] = form_data
                
            return redirect(reverse("my_edit", args=(show_id,)))
            #return redirect(f"/shows/{show_id}/edit/")
        else:
            try:
                # updating show
                show_to_update= Show.objects.get(id=show_id)
                show_to_update.title = show_title
                show_to_update.network = show_network
                show_to_update.release_date = show_date
                if show_description != '':
                    show_to_update.description = show_description

                show_to_update.save()
                
                messages.success(request, "Show successfully updated")

                # once updated, redirect to homepage (shows)
                return redirect(reverse("my_shows"))                
        
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    messages.error(request, 'Title is already added to shows')
                    
                    form_data = {
                        'show_title': show_title,
                        'show_network': show_network,
                        'show_date': show_date,
                        'show_description': show_description
                    }
                    
                    request.session['form_data'] = form_data

                return redirect(reverse("my_edit", args=(show_id,)))

def destroy(request, show_id):    
    print ('Id es ', show_id)
    # deleting show
    show_to_delete= Show.objects.get(id=show_id)
    show_to_delete.delete()
    
    messages.success(request, "Show has been deleted")
    
    # once updated, redirect to homepage (shows)
    return redirect(reverse("my_shows"))