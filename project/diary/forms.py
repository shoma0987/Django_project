from django import forms
from .models import Day

# このforms.ModelFormがかなり強力なので、自分で調べると良い
class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = "__all__" #("title", "text", "date")

