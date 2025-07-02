from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField

from store.models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            FloatingField("isbn"),
            Submit("submit", "Create Book", css_class="btn-primary"),
        )