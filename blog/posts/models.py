from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='media/')
	body = models.TextField()

	def __str__(self):
		return self.title

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

	def summary(self):
		if len(self.body) > 100:
			return self.body[:100]+' ...'
		else:
			return self.body