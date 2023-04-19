

from django import forms

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=100)
    mobile=forms.IntegerField()
    email=forms.EmailField()


class CourseForm(forms.Form):
    cid=forms.IntegerField()
    sid=forms.IntegerField()
    cname=forms.CharField(max_length=100)
    Ctrianer=forms.CharField(max_length=100)