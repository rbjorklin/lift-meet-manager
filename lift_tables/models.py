from django.db import models
                          
class Lifter(models.Model):
    def __str__(self):
        return " ".join([self.name, self.sur_name])

    name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=20)
    license_no = models.CharField(max_length=20, blank=True)
    birthday = models.DateField()

class Competition(models.Model):
    type = models.CharField(max_length=20)
    city = models.CharField(max_length=30, blank=True)
    date = models.DateField()

    def __str__(self):
        return "_".join([self.type, self.city, self.date.__str__()])

class Result(models.Model):
    def good_lift(left_judge, center_judge, right_judge):
        if left_judge and center_judge and right_judge:
            return True
        elif left_judge and center_judge and not right_judge:
            return True
        elif not left_judge and center_judge and right_judge:
            return True
        elif left_judge and not center_judge and right_judge:
            return True
        else:
            return False
    competition = models.ForeignKey(Competition)
    lifter = models.ForeignKey(Lifter)
    weight = models.FloatField(default=0)
    weight_unit = models.CharField(default='kg', max_length=3)
    height = models.FloatField(default=0)
    height_unit = models.CharField(default='cm', max_length=3)
    club = models.CharField(max_length=30, blank=True)
    squat_rack_height = models.IntegerField(default=0)
    bench_rack_height = models.IntegerField(default=0)
    bench_safety_height = models.IntegerField(default=0)
    squat1 = models.FloatField(default=0)
    squat1_left_judge = models.NullBooleanField(null=True)
    squat1_center_judge = models.NullBooleanField(null=True)
    squat1_right_judge = models.NullBooleanField(null=True)
    squat2 = models.FloatField(default=0)
    squat2_left_judge = models.NullBooleanField(null=True)
    squat2_center_judge = models.NullBooleanField(null=True)
    squat2_right_judge = models.NullBooleanField(null=True)
    squat3 = models.FloatField(default=0)
    squat3_left_judge = models.NullBooleanField(null=True)
    squat3_center_judge = models.NullBooleanField(null=True)
    squat3_right_judge = models.NullBooleanField(null=True)
    bench1 = models.FloatField(default=0)
    bench1_left_judge = models.NullBooleanField(null=True)
    bench1_center_judge = models.NullBooleanField(null=True)
    bench1_right_judge = models.NullBooleanField(null=True)
    bench2 = models.FloatField(default=0)
    bench2_left_judge = models.NullBooleanField(null=True)
    bench2_center_judge = models.NullBooleanField(null=True)
    bench2_right_judge = models.NullBooleanField(null=True)
    bench3 = models.FloatField(default=0)
    bench3_left_judge = models.NullBooleanField(null=True)
    bench3_center_judge = models.NullBooleanField(null=True)
    bench3_right_judge = models.NullBooleanField(null=True)
    deadlift1 = models.FloatField(default=0)
    deadlift1_left_judge = models.NullBooleanField(null=True)
    deadlift1_center_judge = models.NullBooleanField(null=True)
    deadlift1_right_judge = models.NullBooleanField(null=True)
    deadlift2 = models.FloatField(default=0)
    deadlift2_left_judge = models.NullBooleanField(null=True)
    deadlift2_center_judge = models.NullBooleanField(null=True)
    deadlift2_right_judge = models.NullBooleanField(null=True)
    deadlift3 = models.FloatField(default=0)
    deadlift3_left_judge = models.NullBooleanField(null=True)
    deadlift3_center_judge = models.NullBooleanField(null=True)
    deadlift3_right_judge = models.NullBooleanField(null=True)
    snatch1 = models.FloatField(default=0)
    snatch1_left_judge = models.NullBooleanField(null=True)
    snatch1_center_judge = models.NullBooleanField(null=True)
    snatch1_right_judge = models.NullBooleanField(null=True)
    snatch2 = models.FloatField(default=0)
    snatch2_left_judge = models.NullBooleanField(null=True)
    snatch2_center_judge = models.NullBooleanField(null=True)
    snatch2_right_judge = models.NullBooleanField(null=True)
    snatch3 = models.FloatField(default=0)
    snatch3_left_judge = models.NullBooleanField(null=True)
    snatch3_center_judge = models.NullBooleanField(null=True)
    snatch3_right_judge = models.NullBooleanField(null=True)
    clean1 = models.FloatField(default=0)
    clean1_left_judge = models.NullBooleanField(null=True)
    clean1_center_judge = models.NullBooleanField(null=True)
    clean1_right_judge = models.NullBooleanField(null=True)
    clean2 = models.FloatField(default=0)
    clean2_left_judge = models.NullBooleanField(null=True)
    clean2_center_judge = models.NullBooleanField(null=True)
    clean2_right_judge = models.NullBooleanField(null=True)
    clean3 = models.FloatField(default=0)
    clean3_left_judge = models.NullBooleanField(null=True)
    clean3_center_judge = models.NullBooleanField(null=True)
    clean3_right_judge = models.NullBooleanField(null=True)
