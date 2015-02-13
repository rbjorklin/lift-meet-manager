from django.db import models
                          
class Lifter(models.Model):
    def __str__(self):
        return " ".join([self.name, self.sur_name, self.date.__str__()])

    #def date(self):
    #    return self.competition.date.__str__()

    #def lifter_name(self):
    #    return " ".join([self.lifter.name, self.lifter.sur_name])

    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    birthday = models.DateField()
    date = models.DateField()
    weight = models.FloatField(default=0)
    weight_unit = models.CharField(default='kg', max_length=3)
    height = models.FloatField(default=0)
    height_unit = models.CharField(default='cm', max_length=3)
    club = models.CharField(max_length=30, blank=True)
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

class Competition(models.Model):
    participants = models.ManyToManyField(Lifter, blank=True)
    type = models.CharField(max_length=20)
    city = models.CharField(default='N/A', max_length=30)

    def __str__(self):
        return "_".join([self.type, self.city])
