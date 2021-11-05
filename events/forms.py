from django import forms
from events.models import Event, EventGallery


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    images = forms.ImageField(label='Images', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = EventGallery
        fields = ('event', 'images')

    # def save(self, *args, **kwargs):
    #     files = (self.cleaned_data['images'])
    #     import pdb
    #     pdb.set_trace()
    #     for file in files:
    #         super(GalleryForm, self).save(*args, **kwargs)

    # def save(self, request, commit=True):
    #     model = super(GalleryForm, self).save(commit=False)
    #     # files = (self.cleaned_data['images'])
    #     files = request.FILES.getlist('images')
