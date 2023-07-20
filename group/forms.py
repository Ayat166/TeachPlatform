from django import forms
from .models import Group, Video

class GroupForm(forms.ModelForm):
    videos = forms.ModelMultipleChoiceField(
        queryset=Video.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Group
        fields = ['name', 'description', 'image', 'videos']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        filter_video = kwargs.pop('filter_video', None)
        super().__init__(*args, **kwargs)
        if filter_video:
            self.fields['videos'].queryset = Video.objects.filter(uploaded_by=filter_video)