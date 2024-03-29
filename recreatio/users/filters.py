import django_filters 
from django_filters import DateFilter, NumberFilter
from .models import Activities

class ActivityFilter(django_filters.FilterSet):
    child_age_young = NumberFilter(field_name='age_group_young', lookup_expr="lte", label="Activities this age and up")
    child_age_old = NumberFilter(field_name="age_group_old", lookup_expr="gte", label = "Activities for this age and below")
    
    class Meta:
        model = Activities
        fields = "__all__"
        exclude = ["age_group_young", "age_group_old","organization","registrant", "description", "author", "date_posted", "end_date", "title","max_size"]

class ActivityFilterGeneric(django_filters.FilterSet):
    child_age_young = NumberFilter(field_name='age_group_young', lookup_expr="lte", label="Activities this age and up")
    child_age_old = NumberFilter(field_name="age_group_old", lookup_expr="gte", label = "Activities for this age and below")
    
    class Meta:
        model = Activities
        fields = "__all__"
<<<<<<< HEAD
        exclude = ["age_group_young", "age_group_old","organization","registrant", "description", "max_size", "reg_start", "reg_end", "title", "author", "date_posted"]
=======
        exclude = ["age_group_young", "age_group_old","organization","registrant", "description", "max_size", "reg_start", "reg_end", "author", "title", "date_posted"]
>>>>>>> b2d828e74f16917ad3c220e390e6818cbed7c00a
        
