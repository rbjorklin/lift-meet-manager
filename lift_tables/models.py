from django.db import models


class Competition(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=13)
    city = models.CharField(default='N/A', max_length=30)
    country_code = models.CharField(default='N/A', max_length=30)

    def __str__(self):
        return "_".join([self.type, self.country_code, self.city,\
                          self.date.__str__().split()[0]])

class PowerLifter(models.Model):
    competition = models.ForeignKey(Competition)
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    birthday = models.DateField()
    weight = models.FloatField(default=0)
    weight_unit = models.CharField(max_length=3)
    height = models.FloatField(default=0)
    height_unit = models.CharField(max_length=3)
    club = models.CharField(max_length=30)
    squat_rack_height = models.IntegerField(default=0)
    bench_rack_height = models.IntegerField(default=0)
    bench_safety_height = models.IntegerField(default=0)
    squat1 = models.FloatField(default=0)
    squat2 = models.FloatField(default=0)
    squat3 = models.FloatField(default=0)
    bench1 = models.FloatField(default=0)
    bench2 = models.FloatField(default=0)
    bench3 = models.FloatField(default=0)
    deadlift1 = models.FloatField(default=0)
    deadlift2 = models.FloatField(default=0)
    deadlift3 = models.FloatField(default=0)

    def __str__(self):
        return " ".join([self.name, self.sur_name])

class WeightLifter(models.Model):
    competition = models.ForeignKey(Competition)
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    birthday = models.DateField()
    weight = models.FloatField(default=0)
    weight_unit = models.CharField(max_length=3)
    height = models.FloatField(default=0)
    height_unit = models.CharField(max_length=3)
    club = models.CharField(max_length=30)
    snatch1 = models.FloatField(default=0)
    snatch2 = models.FloatField(default=0)
    snatch3 = models.FloatField(default=0)
    clean1 = models.FloatField(default=0)
    clean2 = models.FloatField(default=0)
    clean3 = models.FloatField(default=0)

    def __str__(self):
        return " ".join([self.name, self.sur_name])
