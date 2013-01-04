from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy

MY_CHOICES = (
	('FOO', 'foo'),
	('BAR', 'bar'),
	('BAZ', 'baz'),
)

class Playground(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
	description = models.TextField(null=True, blank=True)
	my_choices = models.CharField(max_length=3, choices=MY_CHOICES)

	def __unicode__(self):
		return u"This is a %s" % (self.name,)

	def get_absolute_url(self):
		return reverse('playground_detail', kwargs={'pk': self.pk})

class Simple(models.Model):
	foo = models.CharField(max_length=10)

	def get_absolute_url(self):
		return reverse('simple_list')