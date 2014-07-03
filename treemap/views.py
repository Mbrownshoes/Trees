from django.shortcuts import render_to_response
from pygeocoder import Geocoder
from treemap.forms import UserForm, UserProfileForm

from models import Trees, Harbord

def map_page(request):
     lcount = Trees.objects.all().count()
     return render_to_response('treemap/map.html', {'tree_count' : lcount}) 

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'Post':
        user_form - UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        #invalid form or forms.
        else:
            print user_form.errors, profile_form.errors

    #Not a HTTP POST, so we render our form using two ModelForm instances. These forms will be blank, ready for user input.
else:
    user_form = UserForm()
    profile_form = UserProfileForm()

#render the template depending on the context.
return render_to_response('treemap/registered.html',
    {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
    context)