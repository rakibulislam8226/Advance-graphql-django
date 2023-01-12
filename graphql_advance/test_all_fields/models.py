from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse
from ..events.my_new_app.models import Category, Ingredient


# Create your models here.
class TestAllFields(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category1")
    integradient = models.ManyToManyField(Ingredient, related_name="ingredient1")
    EVENT_STATUS_CHOICES = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
    )
    status_selection = MultiSelectField(choices=EVENT_STATUS_CHOICES, max_choices = 3, max_length=6)
    MAX_NUMBER_CHOICES = (
        ("1", "5"),
        ("2", "10"),
        ("3", "15"),
        ("4", "25"),
        ("5", "50"),
        ("6", "100"),
        ("7", "200"),
        ("8", "300"),
    )
    max_number_events = models.CharField(choices=MAX_NUMBER_CHOICES, default=4, max_length=100)
    is_active = models.BooleanField(default=True)
    internal_note = models.TextField()
    title = models.CharField(max_length=50)
    PUBLISH_STATUS =(
        (1, 'Draft'),
        (2, "Pending"),
        (3, "Success"),
    )
    publish_status = models.IntegerField(choices=PUBLISH_STATUS, default=2)

    class Meta:
        verbose_name = "TestAllField"
        verbose_name_plural = "TestAllFields"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("TestAllFields", kwargs={"pk": self.pk})
