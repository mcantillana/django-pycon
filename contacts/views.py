from django.shortcuts import render
from contacts.forms import ContactForm
from django.contrib import messages

def add_contact(request):
    template_name = 'add_contact.html'
    data = {}

    if request.method == 'POST':

        data['form'] = ContactForm(request.POST)

        if data['form'].is_valid():
            
            data['form'].save()

            str_msg = 'Registro exitoso!'
            messages.add_message(
                request,
                messages.SUCCESS,
                str_msg
            )
        else:
            str_msg = 'Problemas con el registro! intente nuevamente'
            
            messages.add_message(
                request,
                messages.ERROR,
                str_msg
            )    

    else:
        data['form'] = ContactForm()

    return render(request, template_name, data)