from django import forms

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
