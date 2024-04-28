from django import forms
from .models import FollowupBE

class FollowupBEForm(forms.ModelForm):
    class Meta:
        model = FollowupBE
        fields = "__all__"
        

    



    