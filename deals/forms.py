from django import forms


class LocationForm(forms.Form):
    search_terms = forms.CharField(label='Find', max_length=50)
    location = forms.CharField(label='Near', max_length=100)

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields['search_terms'].widget.attrs['placeholder'] = 'Find'
        self.fields['location'].widget.attrs['placeholder'] = 'Near'
