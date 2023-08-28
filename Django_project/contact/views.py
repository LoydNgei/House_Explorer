from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from .forms import ContactForm  # Import the ContactForm
from .models import houses
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required  # Require the user be logged in to access the view
def contact_agent(request, house_id):
    # Get the house object
    house = houses.objects.get(pk=house_id)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact to the database
            contact = form.save(commit=False)
            contact.house = house  # Set the house object for the contact
            contact.user_id = request.user.id    # Set the user ID from the request

            contact.save()

            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
            return redirect(reverse('contact_agent', args=[house_id]))
    else:
        # If the request method is not POST, create an empty form instance
        form = ContactForm(initial={'user_id': request.user.id})

    return render(request, 'contact/contact_agent.html', {'house': house, 'form': form})
