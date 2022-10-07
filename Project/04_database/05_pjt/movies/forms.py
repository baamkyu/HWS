from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    genre_choice = [
        ('코미디','코미디'), ('공포','공포'), ('로맨스','로맨스')
    ]
    genre = forms.ChoiceField(
        choices = genre_choice,
        widget = forms.Select(
            attrs={
                'class': "form-select",
                'aria-label': "Default select example",
            }
        )
    )

    score = forms.FloatField(
        widget = forms.NumberInput(
            attrs={
                'class': "form-control",
                'type': 'number',
                'step': 0.5,
                'min': 0,
                'max': 5,
                'placeholder': 'Score',
            }
        )
    )

    release_date = forms.DateField(
        label = 'Release date',
        widget = forms.DateInput(
            attrs = {
                'class': "form-control",
                'type': 'date',
                'placeholder': "연도-월-일",
                'aria-label': "default input example",
            }
        )
    )


    title = forms.CharField(
        max_length=20,
        widget = forms.TextInput(
            attrs = {
                'class': "form-control",
                'type': "text",
                'placeholder': "제목을 입력하시오.",
            }
        )
    )

    audience = forms.IntegerField(
        widget = forms.TextInput(
            attrs = {
                'class': "form-control",
                'type': "number",
                'placeholder': "관객수를 입력하시오.",
            }
        )
    )


    poster_url = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class': "form-control",
                'id': "exampleFormControlTextarea1",
                'rows': "5",
            }
        )
    )

    description = forms.CharField(
    widget = forms.Textarea(
        attrs = {
            'class': "form-control",
            'id': "exampleFormControlTextarea1",
            'rows': "5",
        }
    )
)
#     <div class="mb-3">
#   <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
#   <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
# </div>


    class Meta:
        model = Movie
        fields = '__all__'

