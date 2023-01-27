from django import forms

class PostForm(forms.Form):	
    pname = forms.CharField(max_length=4,initial='')
    pprice = forms.IntegerField(initial='',required=False)
    pimages = forms.CharField(max_length=50,initial='',required=False)
    pdescription = forms.CharField(max_length=100,initial='',required=False)
    paccount = forms.CharField(max_length=15,initial='',required=False)
    pfirstname = forms.CharField(max_length=10,initial='',required=False)
    plastname = forms.CharField(max_length=10,initial='',required=False)
    pmail = forms.CharField(max_length=25,initial='',required=False)
    pcode = forms.CharField(max_length=20,initial='',required=False)