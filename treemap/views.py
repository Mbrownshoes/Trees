from django.shortcuts import render_to_response
from pygeocoder import Geocoder
from django.template import RequestContext
from django.forms.widgets import HiddenInput

from treemap.forms import UserForm, UserProfileForm

from models import Trees, Harbord

def map_page(request):
     lcount = Trees.objects.all().count()
     return render_to_response('treemap/map.html', {'tree_count' : lcount}) 

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'Post':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        #invalid form or forms.
        else:
            print user_form.errors, profile_form.errors

    #Not a HTTP POST, so we render our form using two ModelForm instances. These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        profile_form.fields['user'].widget = HiddenInput()
    #render the template depending on the context.
    return render_to_response('treemap/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)