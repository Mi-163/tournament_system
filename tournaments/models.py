from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    rules = models.TextField()

class Team(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    members = models.TextField()  # Comma-separated names

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    result = models.CharField(max_length=100, blank=True)
