import django_tables2 as tables 
from django_tables2 import RequestConfig
from .models import Activities

class ActivityTable(tables.Table):
    registrant = tables.ManyToManyColumn()
    
    

    class Meta:
        model = Activities
        sequence = ('start_date', 'end_date', 'reg_start')
        exclude = ['organization', 'id','registrant', 'description',"author","date_posted"]
      