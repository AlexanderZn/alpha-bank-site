from django import forms


class FindPersonForm(forms.Form):

    CHOICES = [('True', 'male'),
               ('False', 'female'),
               ('Some', 'some')]

    male = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    age_from = forms.CharField(max_length=2)
    age_to = forms.CharField(max_length=2)
    sal_from = forms.CharField(max_length=7)
    sal_to = forms.CharField(max_length=7)
