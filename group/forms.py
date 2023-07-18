from django import forms
from .models import Group , Video

class GroupForm(forms.ModelForm):
    videos = forms.ModelMultipleChoiceField(queryset=Video.objects.all(), required=False)

    class Meta:
        model = Group
        fields = ['name', 'description', 'image', 'videos']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }