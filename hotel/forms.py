from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    choice = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Rather Not Say'),
    )
    gender = forms.ChoiceField(choices=choice)
    email = forms.EmailField(required=False)
    phone = forms.RegexField(required=False, regex='^[6-9]\d{9}$')

    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)

        if not (cleaned_data.get('email') or cleaned_data.get('phone')):
            raise forms.ValidationError('Please Enter either email or phone!', code='invalid')


    def clean_email(self):
       data = self.cleaned_data['email']
       if '@' not in data:
           raise forms.ValidationError('invalid domain', code='invalid')
