from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings
from .models import Participant
from .forms import EntryForm

def entry(request):

	current_url = request.get_host()
	
	if request.method == 'POST':
		
		form = EntryForm(request.POST, request.FILES)
		
		if form.is_valid():

			email = form.cleaned_data['email']
			last_name = form.cleaned_data['last_name']
			first_name = form.cleaned_data['first_name']
			birthday = form.cleaned_data['birthday']
			contact = form.cleaned_data['contact']
			media = request.FILES['media']

			participant = Participant(
				last_name=last_name,
				first_name=first_name,
				email=email,
				contact=contact,
				birthday=birthday,
				media=media,
				confirmed=False,
			)

			participant.save()
			send_entry(email, current_url)
			return HttpResponseRedirect('thanks')

	else:
		form = EntryForm()

	return render_to_response('participant-signup/form.html', { 'form': form }, context_instance=RequestContext(request))

def thanks(request):
	return render(request, 'participant-signup/thanks.html')

def send_entry(pk, current_url):

	participant = Participant.objects.get(email=pk)

	email = pk
	admin_email = 'bandolier.test@gmail.com'
	full_name = participant.first_name + ' ' + participant.last_name

	subject, from_email, to = '%s is now ready for confirmation.' % email, admin_email, email
	html_content = 'Your entry details:<br/> <b>Name:</b> <i>%s</i><br/> <b>Birthday:</b> <i>%s</i><br/> <b>Email:</b> <i>%s</i><br/> <b>Contact:</b> <i>%s</i>, to complete your entry submission.<br/>Please click this <a href="http://%s%s">link</a> to confirm.' % (full_name, participant.birthday, email, participant.contact, current_url, reverse('confirm_entry', kwargs={ 'key': participant.key }))
	notifyParticipant = EmailMultiAlternatives(subject, html_content, from_email, [to])
	notifyParticipant.content_subtype = 'html'
	# notifyParticipant.attach_alternative(html_content, 'text/html') #media attach
	notifyParticipant.send()

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
