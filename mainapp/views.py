from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0 
        request.session['activities'] = [] 

    context = {
        "gold":request.session['gold']

    }
    return render(request, 'index.html', context)

def process(request):
    # print(request.POST['location'])
    time = strftime("%Y-%m-%d-%H:%M-%p", gmtime())
    if request.POST['location'] == 'farm':
        amount_to_add = random.randint(10, 20)
        
        # activity = f"Earned {amount_to_add} from farm at {time}" 
        activity = f"<div class='gain'><p>Earned {amount_to_add} from farm at {time} </p></div>" 

    elif request.POST['location'] == 'house':
        amount_to_add = random.randint(5, 10)
        # activity = f"Earned {amount_to_add} from house at {time}" 
        activity = f"<div class='gain'><p>Earned {amount_to_add} from house at {time} </p></div>" 


    elif request.POST['location'] == 'cave':
        amount_to_add = random.randint(2, 5)
        # activity = f"Earned {amount_to_add} from cave at {time}"
        activity = f"<div class='gain'><p>Earned {amount_to_add} from cave at {time} </p></div>" 


    elif request.POST['location'] == 'casino':
        amount_to_add = random.randint(-50, 50)
        if amount_to_add < 0: 
            # activity = f"Lost {amount_to_add} from casino at {time}" 
            activity = f"<div class='lost'><p>Earned {amount_to_add} from casion at {time} </p></div>" 

        else:
            # activity = f"Earned {amount_to_add} from casino at {time}"
            activity = f"<div class='gain'><p>Earned {amount_to_add} from casion at {time} </p> </div>" 


    request.session['gold'] += amount_to_add
    request.session['activities'].append(activity)
    

    return redirect("/")

def reset(request):
    if "gold" in request.session:
        del request.session['gold']

    return redirect("/")

    

