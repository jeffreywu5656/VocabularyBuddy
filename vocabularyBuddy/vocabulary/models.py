from django.db import models
#from users.models import User

###########################################################
# 2 modes:
# 1. browse the word
# 2. test my memory
###########################################################

class Word(models.Model):
    word = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=100, blank=True)
    meaning = models.TextField(blank=True)
    example = models.TextField(blank=True)
    proficiency = models.FloatField(default=0.0)
    #added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    #last_review_date = models.DateTimeField(null=True, blank=True)
    #category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.word