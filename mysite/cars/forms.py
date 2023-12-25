from django import forms


class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100, )
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label='Enter Your Review', max_length=300,
                             widget=forms.Textarea(attrs={'class': 'reviewbox'}))
