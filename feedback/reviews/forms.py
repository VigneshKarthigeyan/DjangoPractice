from .models import ReviewModel
from django import forms

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = ReviewModel
        fields = "__all__"
        labels={
            "user_name":"User Name",
            "review_text":"Review Text",
            "rating":"Rating"
        }


# class ReviewForm(forms.Form):
#     user_name=forms.CharField(max_length=10,label="User Name",error_messages={
#         "required":"Kindly fill this field",
#         "max_length":"This field should not exceed 10 characters"
#     })