from django import forms

class HouseSearchForm(forms.Form):
    Search_house = forms.CharField(required=False, label='Search by name or location')
    min_price = forms.DecimalField(required=False, label='Min Price')
    max_price = forms.DecimalField(required=False, label='Max Price')