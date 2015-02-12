from django.db import models

class PowerLifter(models.Model):
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    birthday = models.DateField()
    weight = models.FloatField()
    weight_unit = models.CharField(max_length=3)
    height = models.FloatField()
    height_unit = models.CharField(max_length=3)
    club = models.CharField(max_lenghth=30)
    squat_rack_height = models.IntegerField()
    bench_rack_height = models.IntegerField()
    bench_safety_height = models.IntegerField()
    squat1 = models.FloatField()
    squat2 = models.FloatField()
    squat3 = models.FloatField()
    bench1 = models.FloatField()
    bench2 = models.FloatField()
    bench3 = models.FloatField()
    deadlift1 = models.FloatField()
    deadlift2 = models.FloatField()
    deadlift3 = models.FloatField()

    def __str__(self):
        return " ".join(self.name, self.sur_name)

class Weight_lifter(models.Model):
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    birthday = models.DateField()
    weight = models.FloatField()
    weight_unit = models.CharField(max_length=3)
    height = models.FloatField()
    height_unit = models.CharField(max_length=3)
    club = models.CharField(max_lenghth=30)
    snatch1 = models.FloatField()
    snatch2 = models.FloatField()
    snatch3 = models.FloatField()
    clean1 = models.FloatField()
    clean2 = models.FloatField()
    clean3 = models.FloatField()

    def __str__(self):
        return " ".join(self.name, self.sur_name)

class Competition(models.Model):
    competition_date = models.DateField()
    lifters = models.CommaSeparatedIntegerField(max_length=50)
    competition_type = models.CharField(max_length=6)

    def __str__(self):
        return self.competition_type
