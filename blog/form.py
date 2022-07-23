import imp
from tkinter import Widget
from tkinter.ttk import Style
from django import forms
from django.forms import ModelForm
from .models import Blog, Comments

class BlogForm(ModelForm):
    class Meta:
        model= Blog
        fields= ['title', 'blog_image', 'categories','addcategory', 'tags','addtag', 'body']
        labels={
            'categories':'Category',
            'tags':'Tag',
            'addcategory': 'Add new category',
            'addtag':'addtag',
        }
       


class CommentForm(ModelForm):
    class Meta:
        model= Comments
        fields= [ 'name', 'body', 'reply_name', 'reply_body' ]

    def __init__(self, *args,**kwargs):
        super(CommentForm, self).__init__(*args,*kwargs)
        self.fields['name'].widget.attrs.update({"required":"","id":"name", "name":"name","placeholder":"Name"})
        self.fields['body'].widget.attrs.update({"required":"","style":"margin-bottom: 20px", "id":"body", "name": "body", "placeholder":"Comment"})
        self.fields['reply_name'].widget.attrs.update({"required":"","id":"reply_name", "name":"reply_body", "placeholder":"Name"})
        self.fields['reply_body'].widget.attrs.update({"required":"", "style":"margin-bottom: 20px", "id":"reply_body", "name": "reply_body", "placeholder":"Comment"})
        
    
