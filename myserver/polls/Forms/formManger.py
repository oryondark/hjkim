from django import forms

class inputForm(forms.Form):
    u_name = forms.CharField(label="Name", max_length=50)
    u_birth = forms.IntegerField(label="birthday", )
    u_hobby = forms.CharField(label="hobby", max_length=100)



