import django_tables2 as tables 
from django_tables2 import RequestConfig
from .models import Activities

class ActivityTable(tables.Table):
    registrant = tables.ManyToManyColumn()
    
    

    class Meta:
        model = Activities
        sequence = ('start_date', 'end_date', 'reg_start')
<<<<<<< HEAD
        exclude = ['organization', 'id','registrant', 'description',"author","date_posted"]
=======
        exclude = ['organization', 'id','registrant', 'description', "author", "date_posted"]
>>>>>>> b2d828e74f16917ad3c220e390e6818cbed7c00a
      