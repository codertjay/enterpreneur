from django import forms


class ContactForm(forms.Form):
    full_name= forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self,*args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith('.edu'):
            raise forms.ValidationError('This form does not need your edu email abeg')
        return email
