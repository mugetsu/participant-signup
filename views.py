from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core import mail
from .forms import EntryForm
from .models import Participant
import os.path

def entry(request):

    current_url = request.get_host()

    if request.method == 'POST':
        
        form = EntryForm(request.POST)
        
        if form.is_valid():
			email = form.cleaned_data['email']
			last_name = form.cleaned_data['last_name']
			first_name = form.cleaned_data['first_name']
			name = first_name + ' ' + last_name
			password = Participant.objects.make_random_password(length=10, allowed_chars='123456789')
			
			if email == 'cprjk.buzz@gmail.com':
				return render(request, 'participant-signup/warning.html')

			else:
				participant = Participant.objects.create_user(email, email, password)
				participant.first_name = first_name
				participant.last_name = last_name
				participant.email = email
				participant.confirmed = False
				participant.save()
				send_entry(name, email, current_url)
				return HttpResponseRedirect('thanks')

    else:
        form = EntryForm()

    return render_to_response('participant-signup/form.html', { 'form': form }, context_instance=RequestContext(request))

def thanks(request):
	return render(request, 'participant-signup/thanks.html')

def send_entry(name, email, current_url):

	participant = Participant.objects.get(email=email)

	subjectAdmin = '%s registered.' % name
	messageAdmin = '%s (%s) just have registered!' % (name, email)
	subjectSender = '%s is now ready for confirmation.' % email
	messageSender = '%s, to completely register (%s) please click this <a href="%s%s">link</a> to confirm.' % (name, email, current_url, reverse('confirm_entry', kwargs={ 'key': participant.key }))

	admin = 'bandolier.test@gmail.com'

	connection = mail.get_connection()

	connection.open()

	notifySender = mail.EmailMessage(subjectSender, messageSender, admin, [email])
	notifyAdmin = mail.EmailMessage(subjectAdmin, messageAdmin, admin, [admin])

	connection.send_messages([notifySender, notifyAdmin])
	connection.close()

def confirm_entry(request, key):
	try:
		participant = Participant.objects.get(key=key)
	except Participant.DoesNotExist:
		template = 'participant-signup/404.html'
	else:
		participant.confirmed = True
		participant.save()
		template = 'participant-signup/confirm.html'

	return render(request, template)
