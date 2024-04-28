from django.db import models
from django.contrib.auth.models import User

class FollowupBE(models.Model):
    date = models.DateField()
    tunnel_location = models.CharField(max_length=25, choices=[
        ('ADIT 1 L2-N1 (HSR)', 'ADIT 1 L2-N1 (HSR)'), 
        ('ADIT 1 L2-S1 (FRT)', 'ADIT 1 L2-S1 (FRT)'), 
        ('ADIT 1 L2-N2 (HSR)', 'ADIT 1 L2-N2 (HSR)'),
        ('ADIT 1 L2-S2 (FRT)', 'ADIT 1 L2-S2 (FRT)'),
        ('ADIT 2 L2-N3 (HSR)', 'ADIT 2 L2-N3 (HSR)'),
        ('ADIT 2 L2-S3 (HSR)', 'ADIT 2 L2-S3 (HSR)'),
        ('ADIT 2 L2-N4 (HSR)', 'ADIT 2 L2-N4 (HSR)'),
        ('ADIT 2 L2-S4 (HSR)', 'ADIT 2 L2-S4 (HSR)'),
        ('ADIT 3', 'ADIT 3'),
        ('ADIT 3 L3-N1 (HSR)', 'ADIT 3 L3-N1 (HSR)'),
        ('ADIT 3 L3-S1 (HSR)', 'ADIT 3 L3-S1 (HSR)'),
        ('ADIT 3 L3-N2 (HSR)', 'ADIT 3 L3-N2 (HSR)'),
        ('ADIT 3 L3-S2 (HSR)', 'ADIT 3 L3-S2 (HSR)'),
        ('ADIT 3N', 'ADIT 3N'),
        ('ADIT 3N L3-N3 (HSR)', 'ADIT 3N L3-N3 (HSR)'),
        ('ADIT 3N L3-S3 (HSR)', 'ADIT 3N L3-S3 (HSR)'),
        ('ADIT 3N L3-N4 (HSR)', 'ADIT 3N L3-N4 (HSR)'),
        ('ADIT 3N L3-S4 (HSR)', 'ADIT 3N L3-S4 (HSR)'),
        ])
    advance = models.IntegerField()
    blast_time = models.TimeField()
    holes_total_number = models.IntegerField()
    holes_length = models.DecimalField(max_digits=4, decimal_places=2)
    cut_holes_kg = models.DecimalField(max_digits=4, decimal_places=2)
    stop_holes_kg = models.DecimalField(max_digits=4, decimal_places=2)
    bottom_holes_kg = models.DecimalField(max_digits=4, decimal_places=2)
    perimeter_holes_kg = models.DecimalField(max_digits=4, decimal_places=2)
    contour_holes_kg = models.DecimalField(max_digits=4, decimal_places=2)
    incident_time_lost = models.TextField(default='No incident')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    total_quantity = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    username_field = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.tunnel_location

