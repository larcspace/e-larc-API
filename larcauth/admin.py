from django.contrib import admin

# Register your models here.
# Register your models here.
# from .forms import AECUserCreationForm, AECUserChangeForm
from .models import AECUser,c_config,language,academicyear
from .models import natureparentutor,concept,globalcontext,campus
from .models import gender,program,term,level,levelsubject,classroom
from .models import criteria_of_subjectsgroup,criteria_of_levelsubject
from .models import academicyear, student, subject_has_calendar

# Administration of table level 1
admin.site.register(c_config)
admin.site.register(language)
admin.site.register(academicyear)

# Administration of table level 2
admin.site.register(campus)
admin.site.register(gender)


# Administration of table level 3
admin.site.register(program)
admin.site.register(term)
admin.site.register(concept)
admin.site.register(natureparentutor)

# Administration of table level 3
admin.site.register(globalcontext)
admin.site.register(level)
admin.site.register(levelsubject)
admin.site.register(classroom)
admin.site.register(criteria_of_subjectsgroup)
admin.site.register(criteria_of_levelsubject)

# Administration des users
#admin.site.register(AECUser, AECUserAdmin)
