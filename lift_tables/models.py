from django.db import models

class Competition(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=13)
    city = models.CharField(default='N/A', max_length=30)
    country_code = models.CharField(default='N/A', max_length=30)

    def __str__(self):
        return "_".join([self.type, self.country_code, self.city])
                          

class Lifter(models.Model):
    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    birthday = models.DateField()

    def __str__(self):
        return " ".join([self.name, self.sur_name])

class LifterMeta(models.Model):
    def date(self):
        return self.competition.date.__str__()

    def lifter_name(self):
        return " ".join([self.lifter.name, self.lifter.sur_name])

    competition = models.ForeignKey(Competition)
    lifter =  models.ForeignKey(Lifter)
    weight = models.FloatField(default=0)
    weight_unit = models.CharField(max_length=3)
    height = models.FloatField(default=0)
    height_unit = models.CharField(max_length=3)
    club = models.CharField(max_length=30)
    squat_rack_height = models.IntegerField(default=0)
    bench_rack_height = models.IntegerField(default=0)
    bench_safety_height = models.IntegerField(default=0)
    lift1_attempt1 = models.FloatField(default=0)
    lift1_attempt1_left_judge = models.NullBooleanField(null=True)
    lift1_attempt1_center_judge = models.NullBooleanField(null=True)
    lift1_attempt1_right_judge = models.NullBooleanField(null=True)
    lift1_attempt2 = models.FloatField(default=0)
    lift1_attempt2_left_judge = models.NullBooleanField(null=True)
    lift1_attempt2_center_judge = models.NullBooleanField(null=True)
    lift1_attempt2_right_judge = models.NullBooleanField(null=True)
    lift1_attempt3 = models.FloatField(default=0)
    lift1_attempt3_left_judge = models.NullBooleanField(null=True)
    lift1_attempt3_center_judge = models.NullBooleanField(null=True)
    lift1_attempt3_right_judge = models.NullBooleanField(null=True)
    lift2_attempt1 = models.FloatField(default=0)
    lift2_attempt1_left_judge = models.NullBooleanField(null=True)
    lift2_attempt1_center_judge = models.NullBooleanField(null=True)
    lift2_attempt1_right_judge = models.NullBooleanField(null=True)
    lift2_attempt2 = models.FloatField(default=0)
    lift2_attempt2_left_judge = models.NullBooleanField(null=True)
    lift2_attempt2_center_judge = models.NullBooleanField(null=True)
    lift2_attempt2_right_judge = models.NullBooleanField(null=True)
    lift2_attempt3 = models.FloatField(default=0)
    lift2_attempt3_left_judge = models.NullBooleanField(null=True)
    lift2_attempt3_center_judge = models.NullBooleanField(null=True)
    lift2_attempt3_right_judge = models.NullBooleanField(null=True)
    lift3_attempt1 = models.FloatField(default=0)
    lift3_attempt1_left_judge = models.NullBooleanField(null=True)
    lift3_attempt1_center_judge = models.NullBooleanField(null=True)
    lift3_attempt1_right_judge = models.NullBooleanField(null=True)
    lift3_attempt2 = models.FloatField(default=0)
    lift3_attempt2_left_judge = models.NullBooleanField(null=True)
    lift3_attempt2_center_judge = models.NullBooleanField(null=True)
    lift3_attempt2_right_judge = models.NullBooleanField(null=True)
    lift3_attempt3 = models.FloatField(default=0)
    lift3_attempt3_left_judge = models.NullBooleanField(null=True)
    lift3_attempt3_center_judge = models.NullBooleanField(null=True)
    lift3_attempt3_right_judge = models.NullBooleanField(null=True)

    def __str__(self):
        return " ".join([self.lifter.__str__(), self.competition.__str__()])
