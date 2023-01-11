from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from . import util
from markdown2 import Markdown
import os

class NewPage(forms.Form):
    title = forms.CharField(label="Title",widget=forms.TextInput(
        attrs={'placeholder': 'Page Title'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(
        attrs={'placeholder': 'Enter new page content here in Markdown format'}))

class EditPage(forms.Form):
    content = forms.CharField(label="Content",required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Edit page\'s content here in Markdown format',
                'required':True,
                }))


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
        return redirect('index')
    return render(request, './encyclopedia/newpage.html', {
        'form': form
    }
    )

    return render(request, './encyclopedia/newpage.html', {'form': form})
def entry(request,title):
    markdowner = Markdown()
    content = util.get_entry(title)
    if content == None:
        return HttpResponse('Fuck you')
    else:
        content = markdowner.convert(util.get_entry(title))
        return render(request,'encyclopedia/entry.html',{
            'title':title,
            'content':content
        })

def edit(request,title):
   
    form = EditPage(request.POST)
    if form.is_valid():
        f = open('entries/' + form.cleaned_data['title'] + '.md', 'x')
        f.write(form.cleaned_data['content'])
        f.close()
        return redirect('index')
    return render(request, './encyclopedia/edit.html', {
        'title':title,
        'form': form
    }
    )
