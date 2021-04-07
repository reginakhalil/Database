import django_tables2 as tables 
from django_tables2 import RequestConfig
from .models import Activities

class ActivityTable(tables.Table):
    registrant = tables.ManyToManyColumn()

    class Meta:
        model = Activities
        sequence = ('start_date', 'end_date', 'reg_start')
        exclude = ['organization', 'id','registrant', 'description']

class SimpleActivityTable(tables.Table):
    participant = tables.ManyToManyColumn(verbose_name="Child")
    start_date = tables.DateColumn(verbose_name="Next Date")

    class Meta:
        model = Activities

        sequence = ('participant', 'title','start_date')
        exclude = ['id','end_date','age_group_young','age_group_old','reg_start', 'reg_end', 'max_size','description','organization','date_posted','author']