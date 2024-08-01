from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=30, widget= forms.TextInput(attrs={'placeholder':'Entrez votre pseudo', 'class': "form-control"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Entrez votre mot de passe', 'class': "form-control"}))

class MessagerieForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()