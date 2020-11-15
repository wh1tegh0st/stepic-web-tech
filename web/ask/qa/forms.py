from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Answer, Question


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = user

    def clean(self):
        pass

    def save(self):
        self.cleaned_data['author'] = self._user
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=None)  # follow the task description

    def __init__(self, user, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = user
        self._question = question
        self.fields['question'].queryset = Question.objects.filter(id=self._question.id)  # see above

    def clean(self):
        pass

    def save(self):
        self.cleaned_data['author'] = self._user
        return Answer.objects.create(**self.cleaned_data)


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data["username"],
                                        email=self.cleaned_data["email"],
                                        password=self.cleaned_data["password"])
        return user


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self._authenticaled_user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self._authenticaled_user = authenticate(username=username, password=password)
            if self._authenticaled_user is None:
                raise forms.ValidationError(
                    "Incorrect login or password",
                    code='incorrect_credentials'
                )
        return self.cleaned_data

    def get_user(self):
        return self._authenticaled_user
