from django.shortcuts import render, redirect
from django import forms
from . import util
from mdutils.mdutils import MdUtils
from mdutils import Html
import markdown
from django.http import HttpResponse
from django.contrib import messages


class NewPage(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={'placeholder': 'Page Title'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(
        attrs={'placeholder': 'Enter new page content here in Markdown format'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new_page(request):
    form = NewPage(request.POST)
    if form.is_valid():
        f = open('entries/' + form.cleaned_data['title'] + '.md', 'x')
        f.write(form.cleaned_data['content'])
        f.close()
        messages.add_message(request, messages.INFO, 'file save success')
        return redirect('index')
    return render(request, './encyclopedia/newpage.html', {
        'form': form
    }
    )

    return render(request, './encyclopedia/newpage.html', {'form': form})

def view_entry(request,entry):
    return render(util.get_entr(entry))
