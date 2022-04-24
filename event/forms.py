from django import forms

from catalog.models import Follower


def courses_for_student_as_choices(student):
    return [(f.course.id, f.course.name) for f in Follower.objects.filter(student=student)]


class EventForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course = forms.ChoiceField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['course'] = forms.ChoiceField(
            widget=forms.Select(attrs={'class': 'form-control'}),
            choices=courses_for_student_as_choices(self.request.user)
        )
