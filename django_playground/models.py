from django.db import models

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