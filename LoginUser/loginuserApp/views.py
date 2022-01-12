from django.shortcuts import render
from . import forms


def userLoginView(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print("User", form.cleaned_data['userName'])
            print("Password", form.cleaned_data['password'])
    return render(request, 'LoginUser/LoginForm.html', {'form': form})
