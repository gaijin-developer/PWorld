from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=100, )
#     last_name = forms.CharField(label='Last name', max_length=100)
#     email = forms.EmailField(label="Email")
#     review = forms.CharField(label='Enter Your Review', max_length=300,
#                              widget=forms.Textarea(attrs={'class': 'reviewbox'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = dict(first_name='Your First Name', last_name='Last Name', stars='Your Rating')
        error_messages = {
            'stars': dict(min_value='Yo whatsup', max_value='its 5')
        }
