from django.db import models
from django.urls import reverse
from datetime import date

OILS = (
    ('R', 'Regular'),
    ('B', 'Blend'),
    ('S', 'Synthetic')
)

class Scooter(models.Model):
  model = models.CharField(max_length=100)
  make = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'scooter_id': self.id})

  def serviced_for_today(self):
    return self.service_set.filter(date=date.today()).count() >= len(OILS)

class Service(models.Model):
  date = models.DateField('service date')
  oil = models.CharField(
    max_length=1,
    choices=OILS,
    default=OILS[0][0]
  )
  scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_oil_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']