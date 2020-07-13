# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

# "larc_config" : class level 1
# the classes of level 1 are the first tables to be implemented in a app named Larcreation;
# Larcreation is the setup of Larc.
# Larconfig is a table of only one record, containing all the neccessary attributes to create
# the universes of Larc.
# A universe is a database contaning all the records for using Larc. (See the Book : Larc - aboiut the concepts.)
# TODO - use this link to implement language codes : http://j.poitou.free.fr/pro/html/typ/codes-iso.html
class c_config (models.Model):
    # Configuration table for absolute parameters, depending on nothing
    # Flag on tables not depending neither on years, neither on language
    # - c_config
    # Here is a tale for configuration that should not change over the years
    # Therte is one record and only one for configuration without time
    # There is a check that verify the Nr of s_Id that must be to 1
    # thes other record can not exist here.
    flag_config_ok = models.BooleanField(null=False,default=False) # l_config_table is ready to be used for generating the universe

    # The parameters
    nb_language = models.SmallIntegerField(default=1)
    language_sigle_1 = models.CharField(max_length=2,default="En")
    language_sigle_2 = models.CharField(max_length=2,default="Fr")
    language_label_1 = models.CharField(max_length=22,default="English")
    language_label_2 = models.CharField(max_length=22,default="Français")

    # Attributes for the school year
    acad_year = models.CharField(max_length=9,null=False,default="2018-2019")
    flag_acad_year_done = models.BooleanField(null=False,default=False)

    # Attributes for time
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #  PP classroom
    # ---------------
    pp1_enabled = models.BooleanField(null=False,default=False)
    pp1_nbClass = models.SmallIntegerField(default=0,null=False)
    pp1_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pp1_config_OK = models.BooleanField(null=False,default=False) # ppi classroom constraints are ready to be used for generating the universe

    pp2_enabled = models.BooleanField(null=False,default=False)
    pp2_nbClass = models.SmallIntegerField(default=0,null=False)
    pp2_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pp2_config_OK = models.BooleanField(null=False,default=False) # ppi classroom constraints are ready to be used for generating the universe

    pp3_enabled = models.BooleanField(null=False,default=False)
    pp3_nbClass = models.SmallIntegerField(default=0,null=False)
    pp3_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pp3_config_OK = models.BooleanField(null=False,default=False) # ppi classroom constraints are ready to be used for generating the universe

    pp4_enabled = models.BooleanField(null=False,default=False)
    pp4_nbClass = models.SmallIntegerField(default=0,null=False)
    pp4_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pp4_config_OK = models.BooleanField(null=False,default=False) # ppi classroom constraints are ready to be used for generating the universe

    #  PYP classroom
    # ---------------
    pyp1_enabled = models.BooleanField(null=False,default=False)
    pyp1_nbClass = models.SmallIntegerField(default=0,null=False)
    pyp1_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pyp1_config_OK = models.BooleanField(null=False,default=False) # pypi classroom constraints are ready to be used for generating the universe

    pyp2_enabled = models.BooleanField(null=False,default=False)
    pyp2_nbClass = models.SmallIntegerField(default=0,null=False)
    pyp2_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pyp2_config_OK = models.BooleanField(null=False,default=False) # pypi classroom constraints are ready to be used for generating the universe
    pyp3_enabled = models.BooleanField(null=False,default=False)
    pyp3_nbClass = models.SmallIntegerField(default=0,null=False)
    pyp3_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pyp3_config_OK = models.BooleanField(null=False,default=False) # pypi classroom constraints are ready to be used for generating the universe

    pyp4_enabled = models.NullBooleanField()
    pyp4_nbClass = models.SmallIntegerField(default=0,null=False)
    pyp4_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pyp4_config_OK = models.BooleanField(null=False,default=False) # pypi classroom constraints are ready to be used for generating the universe

    #  MYP classroom
    # ---------------
    myp1_enabled = models.BooleanField(null=False,default=False)
    myp1_nbClass = models.SmallIntegerField(default=0,null=False)
    myp1_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_myp1_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    myp2_enabled = models.BooleanField(null=False,default=False)
    myp2_nbClass = models.SmallIntegerField(default=0,null=False)
    myp2_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_myp2_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    myp3_enabled = models.BooleanField(null=False,default=False)
    myp3_nbClass = models.SmallIntegerField(default=0,null=False)
    myp3_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_myp3_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    myp4_enabled = models.BooleanField(null=False,default=False)
    myp4_nbClass = models.SmallIntegerField(default=0,null=False)
    myp4_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_myp4_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    myp5_enabled = models.BooleanField(null=False,default=False)
    myp5_nbClass = models.SmallIntegerField(default=0,null=False)
    myp5_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_myp5_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    #  PEI classroom
    # ---------------
    pei1_enabled = models.BooleanField(null=False,default=False)
    pei1_nbClass = models.SmallIntegerField(default=0,null=False)
    pei1_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pei1_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    pei2_enabled = models.BooleanField(null=False,default=False)
    pei2_nbClass = models.SmallIntegerField(default=0,null=False)
    pei2_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pei2_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    pei3_enabled = models.BooleanField(null=False,default=False)
    pei3_nbClass = models.SmallIntegerField(default=0,null=False)
    pei3_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pei3_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    pei4_enabled = models.BooleanField(null=False,default=False)
    pei4_nbClass = models.SmallIntegerField(default=0,null=False)
    pei4_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pei4_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    pei5_enabled = models.BooleanField(null=False,default=False)
    pei5_nbClass = models.SmallIntegerField(default=0,null=False)
    pei5_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_pei5_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    #  DPfr classroom
    # ---------------
    dpfr1_enabled = models.BooleanField(null=False,default=False)
    dpfr1_nbClass = models.SmallIntegerField(default=0,null=False)
    dpfr1_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_dpfr1_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    dpfr2_enabled = models.BooleanField(null=False,default=False)
    dpfr2_nbClass = models.SmallIntegerField(default=0,null=False)
    dpfr2_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_dpfr2_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    #  DPEn classroom
    # ---------------
    dpen1_enabled = models.BooleanField(null=False,default=False)
    dpen1_nbClass = models.SmallIntegerField(default=0,null=False)
    dpen1_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_dpen1_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe

    dpen2_enabled = models.BooleanField(null=False,default=False)
    dpen2_nbClass = models.SmallIntegerField(default=0,null=False)
    dpen2_maxEleves = models.SmallIntegerField(default=0,null=False)
    flag_dpen2_config_OK = models.BooleanField(null=False,default=False) # MYPi classroom constraints are ready to be used for generating the universe


    #  DPfr classroom
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True

    # To polulate the only one record of this table (c_config) you need be administrator (superuser)
    # in admin dashboard of Larc.

    """
0 - c_config
1 - language
1 - academicyear
1 - district


21 - c_config_year depend on :
        ** academicyear (level 1) THere is only one record in this table, for the only record of academicyear.
21 - natureparentutor depend on :
        ** language (level 1)
21 - concept depends on :
        ** language (level 1)
21 - globalcontext depends on
        ** language (level 1)
21 - campus depends on
        ** language (level 1)
21 - gender depends on
        ** language (level 1)
21 - program depends on
        ** language (level 1)


22 - term depends on
        ** language (level 1)
        ** academicyear (level 1)

31 - AECuser depends on
        * gender (level 2)

33 - subjectgroup depends on
        ** academicyear (level 1)
        ** program (level 2)
        * coordonator

32 - level depends on
        ** programs (level 2)
        ** (eventually) academicyear (level 1)

42 - levelsubject depends on
        ** level (level 3)
        ** subjectgroup

42 - classroom depends on
        ** level (level 3)
        * teachadm (level 2) (Opt)

41 - parentutor depends on
        *** data herited from AECUser
        * parentutornature

41 - student depends on
        *** data herited from AECUser
        ** mtm parentutor

41 - parentutor depends on
        *** data herited from AECUser
        * parentutornature

40 - teachadm
        *** data herited from AECUser

54 - classroom_termsubject depends on
        ** classroom
        ** sunbjectgroup
        ** teacher
        ** term

42 - learner depends on
        ** academic year - level 1
        ** student - level 3

52 - externalessay depends on
        ** levelsubject (level 4)
        ** teachadm 4

52 - learner_has_term depends on
        ** fk_learner
        ** fk_term

62 - learnerdp_has_termtdc
        ** fk_learnerdp
        ** fk_term

63 - learnerdp_has_termexternalessay
        ** fk_learnerdp
        ** fk_term
        ** fk_termexternalessay

63 - learner_has_termsubkect
        ** fk_learnerdp
        ** fk_term
        ** fk_termsubject

71 - learner_has_termsubkectDP
       inherited from learner_has_termsubject

71 - learner_has_termsubkectPEI
       inherited from learner_has_termsubject

    1- table_language_ok
    1- table_academicyear_ok
    3- table_externalessay_ok depnds on levelsubject
    21- table_natureparentutor_ok
    21- table_concept_ok
    21- table_globalcontext_ok
    21- table_campus_ok
    21- table_gender_ok
    22- table_program_ok
    22- table_term_ok = models.BooleanField(null=True,default=False)
    32- table_subjectgroup_ok = models.BooleanField(null=True,default=False)
    3- table_level_ok = models.BooleanField(null=True,default=False)
    4- table_levelsubject_ok = models.BooleanField(null=True,default=False)
    4- table_classroom_ok = models.BooleanField(null=True,default=False)
    4- table_criteria_of_subjectsgroup_ok = models.BooleanField(null=True,default=False)
    5- table_criteria_of_levelsubject_ok = models.BooleanField(null=True,default=False)
    table_parentutor_ok = models.BooleanField(null=True,default=False)
    table_AECUser_ok
    table_student_ok
    table_teachadm_ok
    table_classroom_termsubject_ok
    table_learner_ok = models.BooleanField(null=True,default=False)
    table_learner_has_term_ok = models.BooleanField(null=True,default=False)
    table_learner_has_termsubject_ok = models.BooleanField(null=True,default=False)
    table_learner_has_termsubjectDP_ok = models.BooleanField(null=True,default=False)
    table_learner_has_termsubjectPei_ok = models.BooleanField(null=True,default=False)
    table_learnerdp_has_tdc_ok = models.BooleanField(null=True,default=False)
    table_learnerdp_has_externalessay_ok = models.BooleanField(null=True,default=False)
    table_termsubject_has_agenda_ok = models.BooleanField(null=True,default=False)
    """
    # .


# "district" : class level 1
# the classes of level 1 have no foreignkeys and must be configured first
class district(models.Model):
    label = models.CharField(max_length=72)
    sigle = models.CharField(max_length=4,unique = True)     # sigle sur 4 caracteres
    arrondissement = models.CharField(null=True,max_length=3)             # sigle sur 2 caractères (Chiffres romains I,II, III, IV etc...)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard


    # according to the config table
    def selfcheck(self):
        return self.label



# "language" : class level 1
# the classes of level 1 have no foreignkeys and must be configured first
# See the function of univers creation, day 1 : creation_day_1
# Configuration attributs serving to populate this class : (vs clarc_config table)
#      - nb_languages (Max 2)
#      - language_sigle_1
#      - language_sigle_2
# TODO - use this link to implement language codes : http://j.poitou.free.fr/pro/html/typ/codes-iso.html
class language (models.Model):
    sigle = models.CharField(max_length=2)
    label = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True

    def __str__(self):
        return self.sigle

    # default population
    # This table can be modified with the admin dashboard

# "academicyear" : class level 1
# the classes of level 1 have no foreignkeys and must be configured first
# See the function of univers creation, day 1 : creation_jour_1
# Configuration attrinuts serving to populate this class :
#      - Year to be configured --> example 2018-2019
class academicyear (models.Model):
    TERM_NONE = 0
    TERM_ONE = 1
    TERM_TWO = 2
    TERM_THREE = 3
    TERM_FOUR = 4
    term_number_choices = (
        (TERM_NONE,0),
        (TERM_ONE,1),
        (TERM_TWO,2),
        (TERM_THREE,3),
        (TERM_FOUR,4),
    )
    s_id = models.SmallIntegerField(primary_key= True)
    label = models.CharField(max_length=9, unique = True)
    start_date = models.DateField()
    end_date = models.DateField()
    current_term_number = models.SmallIntegerField(
        choices = term_number_choices,
        default = TERM_NONE,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is to be completed with the admin dashboard

# "Nature_parentutor" : class level 1
# the classes of level 1 have no foreignkeys and must be configured first
# See the function of univers creation, day 1 : creation_jour_1
class natureparentutor(models.Model):
    s_id = models.SmallIntegerField(null=False)
                                        # Semantic ID, that depend not on the language
                                        # it is not a primary Key. It is just useful for translation mode.
                                        # Example :
                                        # if is_id = 1 for Mister (language = En)
                                        # --> is_id = 1 for Monsieur (language = Fr)
    label = models.CharField(max_length=10)
    fk_language = models.ForeignKey('language',on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
    def __str__(self):
        return self.label

    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "concept" : class level 1
# the classes of level 1 have no foreignkeys and must be configured first
# See the function of univers creation, day 1 : creation_day_1
# Configuration attributs serving to populate this class : (vs clarc_config table)
# There are :
#   -> Configuration given By IB models
#   -> Configuration given By the school
class concept (models.Model):
    s_id = models.SmallIntegerField(null=False)
                                        # Semantic ID, refering meaniong of a concept that depend not on the language
                                        # it is not a primary Key. It is just useful for translation mode.
                                        # Example :
                                        # if is_id = 1 for development concept (language = En)
                                        # --> is_id = 1 for développement for  (language = Fr)
    label = models.CharField(max_length=36,null=False)
    fk_language = models.ForeignKey('language', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table


# "globalcontext" : class level 1
# the classes of level 1 have no foreignkeys and must be configured first
# See the function of univers creation, day 1 : creation_day_1
# Configuration attributs serving to populate this class : (vs clarc_config table)
# There are :
#   -> Configuration given By IB models
class globalcontext (models.Model):
    s_id = models.SmallIntegerField(null=False)
                                        # Semantic ID, refering meaniong of a concept that depend not on the language
                                        # it is not a primary Key. It is just useful for translation mode.
                                        # Example :
                                        # if is_id = 1 for "equity & development" (language = En)
                                        # --> is_id = 1 for "Equité et développement" for  (language = Fr)
    label = models.CharField(max_length=55, null=False)
    description = models.TextField(default='Enter description')
    fk_language = models.ForeignKey('language', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "campus" : class level 2
# the classes of level 2 have no foreignkeys and must be configured first
# See the function of univers creation, day 2 : creation_day_2
class campus(models.Model):
    s_id = models.SmallIntegerField(null=False)
                                        # Semantic ID, refering meaniong of a concept that depend not on the language
                                        # it is not a primary Key. It is just useful for translation mode.
                                        # Example :
                                        # if is_id = 1 for "equity & development" (language = En)
                                        # --> is_id = 1 for "Equité et développement" for  (language = Fr)
    label = models.CharField(max_length=72)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=72)
    country = CountryField()
    tel_1 = models.CharField(max_length=12)
    tel_2 = models.CharField(null=True,max_length=12)
    email_1 = models.EmailField()
    email_2 = models.EmailField(null=True)
    fk_district = models.ForeignKey('district',on_delete=models.PROTECT)
    fk_language = models.ForeignKey('Language',on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "gender" : class level 2
# the classes of level 2 have foreignkeys from class level1 and must be configured at the second position
# See the function of univers creation, day 2 : creation_day_2
class gender (models.Model):
    s_id = models.SmallIntegerField(null=False)
                                        # Semantic ID, refering meaning of a gender that depend not on the language
                                        # it is not a primary Key. It is just useful for translation mode.
                                        # Example :
                                        # if is_id = 1 for "equity & development" (language = En)
                                        # --> is_id = 1 for "Equité et développement" for  (language = Fr)
    label = models.CharField (max_length=12)
    sigle = models.CharField (max_length=4)
    fk_language = models.ForeignKey('language',on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.sigle + " : " + self.sigle
    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "program" : class level 2
# the classes of level 2 have foreignkeys from class level 1 and must be configured at the second position
# See the function of univers creation, day 2 : creation_day_2
# s_Id : the programm ID is buit with these two values :
#       - the value of language 1 : English / 2 : Français etc..
#       - the value of the program PYP : 1 - MYP : 2 - DP : 3
# example of s_id : 23 : DP francophone
class program(models.Model):
    s_id= models.SmallIntegerField(null=False) # Id sémentique (voir language)
    sigle = models.CharField(max_length=4)
    label = models.CharField(max_length=55)
    fk_language = models.ForeignKey('language', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.sigle
    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "term" : class level 3
# the classes of level 3 have foreignkeys from class level 2 and must be configured at the second position
# See the function of univers creation, day 3 : creation_day_3
# Bulding S_id with theses following values
#       - code of the year
#       - code of the trimester on 2 digits : 01 - 02 - 03 - 04
# Example : 102 - 2e trimestre de la première année.
class term (models.Model):
    trim = models.SmallIntegerField (null=False)
    label = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    fk_language = models.ForeignKey('language',on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table
#
# "subjectgroup" : class level 3
# the classes of level 3 have foreignkeys from class level 2 and must be configured at the second position
# See the function of univers creation, day 3 : creation_day_3
# Depends on IBO configuration each year
class subjectgroup(models.Model):
    s_id= models.SmallIntegerField(null=False,default=1) # Id sémentique (voir language)
    label = models.CharField(max_length=44)
    description = models.TextField(blank=True)
    nr_group_in_pgm = models.SmallIntegerField(null=False,default=1)
    fk_program = models.ForeignKey('program',on_delete=models.PROTECT)
    fk_coordonator = models.ForeignKey('teachadm',on_delete=models.PROTECT)
    fk_language = models.ForeignKey('language',default=1,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table


# "level" : class level 3
# the classes of level 3 have foreignkeys from class level 2 and must be configured at the second position
# See the function of univers creation, day 3 : creation_day_3
# Depends on IBO configuration each year
# The s_Id : the level ID is build with these values :
#       1 the pgm ID
#       2 the level in the program biginning by the first level
# Ex : 112 is the 2nd level for english PYP program
# Nb : level_in_pgm is the level in the program biginning by the first level
class level(models.Model):
    s_id= models.SmallIntegerField(default=1,null=False) # Id sémentique (voir language)
    label = models.CharField(max_length=33,unique=True)
    description = models.TextField(blank=True)
    level_in_pgm = models.SmallIntegerField(null=False,blank=False)
    fk_program = models.ForeignKey('program',on_delete=models.PROTECT)
    fk_language = models.ForeignKey('language',default=1,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "levelsubject" : class level 4
# the classes of level 4 have foreignkeys from class level 3 and must be configured at the second position
# See the function of univers creation, day 4 : creation_day_4
# Depends on school configuration.
class levelsubject(models.Model):
    s_id= models.SmallIntegerField(default=1,null=False) # Id sémentique (voir language)
    label = models.CharField(max_length=55,null=False,blank=False)
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=False)
    fk_subjectgroup = models.ForeignKey('subjectgroup', on_delete=models.PROTECT)
    fk_level = models.ForeignKey('level',on_delete=models.PROTECT)
    fk_language = models.ForeignKey('language',default=1,on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table

# "classroom" : class level 4
# the classes of level 4 have foreignkeys from class level 3 and must be configured at the second position
# See the function of univers creation, day 4 : creation_day_4
# Depends on school configuration
# See in larc_configuration table :
#   - Program_enabled for P ?
#       - Nbr classroom level 1 for program P
#       - Nbr classroom level 2 for program P
#       - Nbr classroom level 3 for program P
#       - Nbr classroom level 4 for program P
#       - Nbr classroom level 5 for program P
#  The s_ID : the classroom ID is built with these values :
#       - the level ID
#       - The No of the classromm biginnig by 1
#  Example : 222 : la deuxième classe de PYP-2
class classroom(models.Model):
    label = models.CharField(max_length=33,unique=True)
    index_in_level = models.SmallIntegerField(default=1) # index à ajouter pour définir la classe
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=False)
    fk_level = models.ForeignKey('level',on_delete=models.PROTECT)
    fk_headteacher = models.ForeignKey('teachadm',on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    # Population
    # The table is populate with the admin dashboard
    # according to the config table


# -------------------------------------------------------------------------------------------------------
#
# personn/ parentutor / Student / techadmin : class level 3
# the classes of level 3 have foreignkeys from class level 2 and must be configured at the third position
# See the function of univers creation, day 3 : creation_day_3
#
# --------------------------------------------------------------------------------------------------------
class AECUser(AbstractUser):
    # last_name --> user
    # first_name --> user
    # email --> user
    # password --> user
    # Rappel : authentification se fait sur le username et le password.
    # group --> eleve/parent/coordonnateur/professeur/Staff
    # user persission --> concerning what he can do
    firstname_2 = models.CharField(max_length=72,blank=True,null=True)
    date_entree = models.DateField(null=True,blank=True)
    tel_maison = models.CharField(max_length = 20, default='+228 - ',null=True,blank=True)
    tel_smartphone_1 = models.CharField(max_length = 20, default='+228 - ',null=True,blank=True)
    tel_smartphone_2 = models.CharField(max_length = 20, default='+228 - ',null=True,blank=True)
    emailperso = models.EmailField(null=True,blank=True)
    passdelph =  models.CharField(max_length = 20, default='AEC-2020',null=True,blank=True)
    avatar  = models.ImageField(upload_to='larcauth_avatar/', blank=True)
    picture2 = models.BinaryField(blank=True,editable=True)
    type_parentutor = models.NullBooleanField()
    type_teacher = models.NullBooleanField()
    type_coordonator = models.NullBooleanField()
    type_supervisor = models.NullBooleanField()
    type_student = models.NullBooleanField()
    type_director = models.NullBooleanField()
    fk_gender = models.ForeignKey('gender', on_delete=models.PROTECT,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    """
    # Population
    # The table is populate with a script with default values
    # according to the config table
    """
class parentutor(AECUser):
    enabled = models.BooleanField(null=True,default=False)
    fk_parentutor_nature = models.ForeignKey ('natureparentutor',default=1,on_delete=models.PROTECT)

    def __str__(self):
        return self.fk_parentutor_nature
    """
    # Population
    # The table is populate with a script with default values
    # according to the config table
    """

class student(AECUser):
    # This Id is unique for each univers
    # There is one universe created per year. But the time has no impact
    # on this table.
    # SO This Id is composed by values when the student enter the school:
    # - The year in which the student is entered : 1, 2 or 3 etc... See the schoolyear table
    # - The code of the language of the programm Ex: (1 for English), (2 for French)
    # - The pgm of the student on 2 digit  (01 for PYP ,02 for MYP or 03 for DP),
    # - The level in the pgm, on 2 digit    - (01 or 02 or 03 or 04) for PYP
    #                                       - (01 or 02 or 03 or 04) for MYP
    #                                       - (01 or 02) for DP
    # - The classroom in the level on 2 digits ( vs classroom --> attribut no_inlevel =
    #              0                         - (01 or 02 or 03 etc...)
    # - The Number of the student in the classroom (filling order)S considering the max
    # Example : 010202030123 - Id of a student who arrived in year 1 in class of PEI3 (Fr)
    # and the 23rd enrolled in the fist class of PEI-3
    aec_id = models.CharField(max_length=12,unique=True)
    enabled = models.BooleanField (default=False)
    mtm_parentutor = models.ManyToManyField('parentutor',blank=True)
    s_classroom = models.ForeignKey('classroom',on_delete = models.PROTECT)
    created_s = models.DateTimeField(auto_now_add=True)
    updated_s = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.aec_id
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """


class teachadm (AECUser):
    is_teacher= models.BooleanField (default=False)
    is_adm = models.BooleanField (default=False)
    is_coordonator = models.BooleanField (default=False)
    is_secretary = models.BooleanField (default=False)
    enabled = models.BooleanField (default=False)

    def __str__(self):
        return "Professeur"
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

# -------------------------------------------------------------------------------------------------------
#
# End - Tables : personn/ parentutor / Student / techadmin : class level 3
#
# -------------------------------------------------------------------------------------------------------


# "classroom_termsubject" : class level 4
# the classes of level 4 have foreignkeys from class level 3 and must be configured at the second position
# See the function of univers creation, day 4 : creation_day_4
# Depends on school configuration
# See larc_configuration file :
#       max number of potential subjects per level of each program
class classroom_termsubject(models.Model):
    label = models.CharField(max_length=72,null=False,blank=False)
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=False)
    fk_classroom = models.ForeignKey('classroom',on_delete=models.PROTECT)
    fk_levelsubject = models.ForeignKey('levelsubject', on_delete=models.PROTECT)
    fk_teacher = models.ForeignKey('teachadm', default=0, on_delete=models.PROTECT)
    fk_term = models.ForeignKey('term', default=0, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True

    def __str__(self):
        return self.label
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """
    """
    """

class agenda(models.Model):
    date_all = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.s_id


class event_type(models.Model):
    # type d'évènements possibles pour les élèves
    # Sortie de classe
    # Absence cours
    # Absence 1/2 journée
    # Absence journée
    # Retard AM
    # Retard PM
    # Devoir/tâche non rendu
    # Profile + ou -  (ex. : bonne recherche, plagiat etc.. )
    label : models.CharField(max_length=30)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class student_has_events(models.Model):

    nb_sortie = models.SmallIntegerField(default=0)
    nb_absence = models.SmallIntegerField(default=0)
    nb_retard = models.SmallIntegerField(default=0)
    nb_profile_remarks = models.SmallIntegerField(default=0)
    nb_task_undone = models.SmallIntegerField(default=0)
    lbl_option1 = models.CharField(max_length= 22,default='')
    lbl_option2 = models.CharField(max_length = 22,default='')
    lbl_option3 = models.CharField(max_length = 22,default='')
    lbl_option4 = models.CharField(max_length = 22,default='')
    nb_option1 = models.SmallIntegerField(default=0)
    nb_option2 = models.SmallIntegerField(default=0)
    nb_option3 = models.SmallIntegerField(default=0)
    nb_option4 = models.SmallIntegerField(default=0)
    # Notification des évènement - texte délimité :
    # Heure - Event Type
    #    Teachadmm - Matière
    #    Compélement
    # notificationconcernant le temps ( sortie / absence et retard )
    notif_time = models.TextField(default='')
    notif_profile = models.TextField(default='')
    notif_task = models.TextField(default='')
    notif_ontion1 = models.TextField(default='')
    notif_option2 = models.TextField(default='')
    notif_option3 = models.TextField(default='')
    notif_option4 = models.TextField(default='')

    enabled = models.BooleanField(default=False)
    fk_jour = models.ForeignKey('agenda',on_delete = models.PROTECT)
    fk_student = models.ForeignKey('student',on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.fk_student
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table

"""

# 'learner_has_subjectgroup' class level 6
class learner_has_subjectgroup(models.Model):
    note_on_7 = models.SmallIntegerField(null=True)
    sum_on_7 = models.SmallIntegerField(null=True)
    average_on_7 = models.SmallIntegerField(null=True)
    description = models.CharField(max_length = 1500,default='')
    enabled = models.BooleanField(default=False)
    validated  = models.BooleanField(default=False)
    fk_subjectgroup = models.ForeignKey('subjectgroup', on_delete=models.PROTECT)
    fk_student = models.ForeignKey('student',default=0, on_delete = models.PROTECT)
    fk_term = models.ForeignKey('term' ,on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fk_student
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

# 'learner_has_term' class level 6
# the classes of level 5 have foreignkeys from class level 5 and must be configured at the second position
# See the function of univers creation, day 6 : creation_day_6
# This table is populate with defaut values for a whole year depending of the configuration file.
class learner_has_term(models.Model):
    # Pour le PEI
    term_mark_on_56 = models.SmallIntegerField(blank=True,null=True)
    # Pour le DP
    term_mark_on_45 = models.SmallIntegerField(blank=True,null=True)
    term_eetdc_bonus = models.SmallIntegerField(default=0,null=True)
    # Poue tous
    observation_global = models.TextField(blank=True,null=True)
    observation_profil = models.TextField(blank=True,null=True)
    term_average_global_on_20 = models.FloatField(blank=True,null=True)
    enabled = models.BooleanField(default=False)
    validated  = models.BooleanField(default=False)
    fk_student = models.ForeignKey('student',default=0, on_delete = models.PROTECT)
    fk_term = models.ForeignKey('term' ,on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fk_student
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

#
#
#
#
#
class classroom_termothersubject(models.Model):
    label = models.CharField(max_length=144,blank=True)
    description = models.TextField(blank=True)
    unit_multisubjects = models.BooleanField(default=False)
    # In case of pluridisciplinary unité
    nb_subjects = models.SmallIntegerField(blank=True,null=True)
    # références aux unité dans leur matières
    ref_unit_subject1 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnée trimest
    ref_unit_subject2 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest
    ref_unit_subject3 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest
    ref_unit_subject4 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest
    ref_unit_subject5 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest
    ref_unit_subject6 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest
    ref_unit_subject7 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest
    ref_unit_subject8 = models.SmallIntegerField(null=True)# référence à l'unité - associe à un trimestre donnéeu trimest

    fk_classroom = models.ForeignKey('classroom',on_delete=models.PROTECT)
    fk_term = models.ForeignKey('term' ,on_delete = models.PROTECT)
    fk_supervisor = models.ForeignKey('teachadm', on_delete=models.PROTECT) # externalessay is always link to a DP subject
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

#
class learner_has_termothersubject(models.Model):
    titre = models.CharField(max_length=144,blank=True)
    bareme = models.SmallIntegerField(blank=True,null=True)
    mark_on_bareme = models.FloatField(blank=True,null=True)
    mark_on_20 = models.FloatField(blank=True,null=True)
    mark_on_letter = models.CharField(max_length=1,blank=True,null=True)
    observation_global = models.TextField(blank=True,null=True)
    observation_target = models.CharField(max_length=144, blank=True)
    os_note_a = models.SmallIntegerField(null=True)
    os_note_b = models.SmallIntegerField(null=True)
    os_note_c = models.SmallIntegerField(null=True)
    os_note_d = models.SmallIntegerField(null=True)
    os_note_e = models.SmallIntegerField(null=True)
    os_note_f = models.SmallIntegerField(null=True)
    os_observation = models.CharField(null=True,max_length=1500)
    enabled = models.BooleanField(default=False)
    validated  = models.BooleanField(default=False)

    ref_teacher_used = models.BooleanField(default=False)
    # Professeur de référence dans le cas de matière comme le memoire / ou le projet personnel / ou CAS
    ref_teacher = models.SmallIntegerField(null=True)

    fk_student = models.ForeignKey('student',default=0, on_delete = models.PROTECT)
    fk_termothersubject = models.ForeignKey('classroom_termothersubject' ,on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fk_studentdp

"""
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

# 'learner_has_termsubject' class level 6
# the classes of level 6 have foreignkeys from class level 5 and must be configured at the second position
# See the function of univers creation, day 6 : creation_day_6
# This table is populate with defaut values for a whole year depending of the configuration file.
class learner_has_termsubject(models.Model):
    enabled = models.BooleanField(default=False)
    fk_student = models.ForeignKey('student',on_delete = models.PROTECT)
    fk_classroom_termsubject = models.ForeignKey('classroom_termsubject',on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

# 'learner_has_subjectDP' class level 7
# the classes of level 6 have foreignkeys from class level 5 and must be configured at the second position
# See the function of univers creation, day 6 : creation_day_6
# This table is populate with defaut values for a whole year depending of the configuration file.
class learnerDP_has_termsubjectDP(learner_has_termsubject):
    f01_observation = models.CharField(null=True,max_length=255)
    f02_observation = models.CharField(null=True,max_length=255)
    f03_observation = models.CharField(null=True,max_length=144)
    f04_observation = models.CharField(null=True,max_length=255)
    f05_observation = models.CharField(null=True,max_length=255)
    f06_observation = models.CharField(null=True,max_length=255)
    f07_observation = models.CharField(null=True,max_length=255)
    f08_observation = models.CharField(null=True,max_length=255)
    f09_observation = models.CharField(null=True,max_length=255)
    f10_observation = models.CharField(null=True,max_length=255)
    f11_observation = models.CharField(null=True,max_length=255)
    f12_observation = models.CharField(null=True,max_length=255)
    s01_observation = models.CharField(null=True,max_length=255)
    s02_observation = models.CharField(null=True,max_length=255)
    s03_observation = models.CharField(null=True,max_length=255)
    s04_observation = models.CharField(null=True,max_length=255)
    s05_observation = models.CharField(null=True,max_length=255)
    s06_observation = models.CharField(null=True,max_length=255)
    s07_observation = models.CharField(null=True,max_length=255)
    s08_observation = models.CharField(null=True,max_length=255)
    s09_observation = models.CharField(null=True,max_length=255)
    s10_observation = models.CharField(null=True,max_length=255)
    s11_observation = models.CharField(null=True,max_length=255)
    s12_observation = models.CharField(null=True,max_length=255)
    cp_observation = models.CharField(null=True,max_length=255)

    f01_note = models.FloatField(null=True)
    b01 = models.SmallIntegerField(null=True)
    f01_note_a = models.SmallIntegerField(null=True)
    f01_note_b = models.SmallIntegerField(null=True)
    f01_note_c = models.SmallIntegerField(null=True)
    f01_note_d = models.SmallIntegerField(null=True)
    f01_note_e = models.SmallIntegerField(null=True)
    f01_note_f = models.SmallIntegerField(null=True)

    f02_note = models.FloatField(null=True)
    b02 = models.SmallIntegerField(null=True)
    f02_note_a = models.SmallIntegerField(null=True)
    f02_note_b = models.SmallIntegerField(null=True)
    f02_note_c = models.SmallIntegerField(null=True)
    f02_note_d = models.SmallIntegerField(null=True)
    f02_note_e = models.SmallIntegerField(null=True)
    f02_note_f = models.SmallIntegerField(null=True)

    f03_note = models.FloatField(null=True)
    b03 = models.SmallIntegerField(null=True)
    f03_note_a = models.SmallIntegerField(null=True)
    f03_note_b = models.SmallIntegerField(null=True)
    f03_note_c = models.SmallIntegerField(null=True)
    f03_note_d = models.SmallIntegerField(null=True)
    f03_note_e = models.SmallIntegerField(null=True)
    f03_note_f = models.SmallIntegerField(null=True)

    f04_note = models.FloatField(null=True)
    b04 = models.SmallIntegerField(null=True)
    f04_note_a = models.SmallIntegerField(null=True)
    f04_note_b = models.SmallIntegerField(null=True)
    f04_note_c = models.SmallIntegerField(null=True)
    f04_note_d = models.SmallIntegerField(null=True)
    f04_note_e = models.SmallIntegerField(null=True)
    f04_note_f = models.SmallIntegerField(null=True)

    f05_note = models.FloatField(null=True)
    b05 = models.SmallIntegerField(null=True)
    f05_note_a = models.SmallIntegerField(null=True)
    f05_note_b = models.SmallIntegerField(null=True)
    f05_note_c = models.SmallIntegerField(null=True)
    f05_note_d = models.SmallIntegerField(null=True)
    f05_note_e = models.SmallIntegerField(null=True)
    f05_note_f = models.SmallIntegerField(null=True)

    f06_note = models.FloatField(null=True)
    b06 = models.SmallIntegerField(null=True)
    f06_note_a = models.SmallIntegerField(null=True)
    f06_note_b = models.SmallIntegerField(null=True)
    f06_note_c = models.SmallIntegerField(null=True)
    f06_note_d = models.SmallIntegerField(null=True)
    f06_note_e = models.SmallIntegerField(null=True)
    f06_note_f = models.SmallIntegerField(null=True)

    f07_note = models.FloatField(null=True)
    b07 = models.SmallIntegerField(null=True)
    f07_note_a = models.SmallIntegerField(null=True)
    f07_note_b = models.SmallIntegerField(null=True)
    f07_note_c = models.SmallIntegerField(null=True)
    f07_note_d = models.SmallIntegerField(null=True)
    f07_note_e = models.SmallIntegerField(null=True)
    f07_note_f = models.SmallIntegerField(null=True)

    f08_note = models.FloatField(null=True)
    b08 = models.SmallIntegerField(null=True)
    f08_note_a = models.SmallIntegerField(null=True)
    f08_note_b = models.SmallIntegerField(null=True)
    f08_note_c = models.SmallIntegerField(null=True)
    f08_note_d = models.SmallIntegerField(null=True)
    f08_note_e = models.SmallIntegerField(null=True)
    f08_note_f = models.SmallIntegerField(null=True)

    f09_note = models.FloatField(null=True)
    b09 = models.SmallIntegerField(null=True)
    f09_note_a = models.SmallIntegerField(null=True)
    f09_note_b = models.SmallIntegerField(null=True)
    f09_note_c = models.SmallIntegerField(null=True)
    f09_note_d = models.SmallIntegerField(null=True)
    f09_note_e = models.SmallIntegerField(null=True)
    f09_note_f = models.SmallIntegerField(null=True)

    f10_note = models.FloatField(null=True)
    b10 = models.SmallIntegerField(null=True)
    f10_note_a = models.SmallIntegerField(null=True)
    f10_note_b = models.SmallIntegerField(null=True)
    f10_note_c = models.SmallIntegerField(null=True)
    f10_note_d = models.SmallIntegerField(null=True)
    f10_note_e = models.SmallIntegerField(null=True)
    f10_note_f = models.SmallIntegerField(null=True)

    f11_note = models.FloatField(null=True)
    b11 = models.SmallIntegerField(null=True)
    f11_note_a = models.SmallIntegerField(null=True)
    f11_note_b = models.SmallIntegerField(null=True)
    f11_note_c = models.SmallIntegerField(null=True)
    f11_note_d = models.SmallIntegerField(null=True)
    f11_note_e = models.SmallIntegerField(null=True)
    f11_note_f = models.SmallIntegerField(null=True)

    f12_note = models.FloatField(null=True)
    b12 = models.SmallIntegerField(null=True)
    f12_note_a = models.SmallIntegerField(null=True)
    f12_note_b = models.SmallIntegerField(null=True)
    f12_note_c = models.SmallIntegerField(null=True)
    f12_note_d = models.SmallIntegerField(null=True)
    f12_note_e = models.SmallIntegerField(null=True)
    f12_note_f = models.SmallIntegerField(null=True)
    s01_note = models.FloatField(null=True)
    s01_note_a = models.SmallIntegerField(null=True)
    s01_note_b = models.SmallIntegerField(null=True)
    s01_note_c = models.SmallIntegerField(null=True)
    s01_note_d = models.SmallIntegerField(null=True)
    s01_note_e = models.SmallIntegerField(null=True)
    s01_note_f = models.SmallIntegerField(null=True)
    s02_note = models.FloatField(null=True)
    s02_note_a = models.SmallIntegerField(null=True)
    s02_note_b = models.SmallIntegerField(null=True)
    s02_note_c = models.SmallIntegerField(null=True)
    s02_note_d = models.SmallIntegerField(null=True)
    s02_note_e = models.SmallIntegerField(null=True)
    s02_note_f = models.SmallIntegerField(null=True)
    s03_note = models.FloatField(null=True)
    s03_note_a = models.SmallIntegerField(null=True)
    s03_note_b = models.SmallIntegerField(null=True)
    s03_note_c = models.SmallIntegerField(null=True)
    s03_note_d = models.SmallIntegerField(null=True)
    s03_note_e = models.SmallIntegerField(null=True)
    s03_note_f = models.SmallIntegerField(null=True)
    s04_note = models.FloatField(null=True)
    s04_note_a = models.SmallIntegerField(null=True)
    s04_note_b = models.SmallIntegerField(null=True)
    s04_note_c = models.SmallIntegerField(null=True)
    s04_note_d = models.SmallIntegerField(null=True)
    s04_note_e = models.SmallIntegerField(null=True)
    s04_note_f = models.SmallIntegerField(null=True)
    s05_note = models.FloatField(null=True)
    s05_note_a = models.SmallIntegerField(null=True)
    s05_note_b = models.SmallIntegerField(null=True)
    s05_note_c = models.SmallIntegerField(null=True)
    s05_note_d = models.SmallIntegerField(null=True)
    s05_note_e = models.SmallIntegerField(null=True)
    s05_note_f = models.SmallIntegerField(null=True)
    s06_note = models.FloatField(null=True)
    s06_note_a = models.SmallIntegerField(null=True)
    s06_note_b = models.SmallIntegerField(null=True)
    s06_note_c = models.SmallIntegerField(null=True)
    s06_note_d = models.SmallIntegerField(null=True)
    s06_note_e = models.SmallIntegerField(null=True)
    s06_note_f = models.SmallIntegerField(null=True)
    s07_note = models.FloatField(null=True)
    s07_note_a = models.SmallIntegerField(null=True)
    s07_note_b = models.SmallIntegerField(null=True)
    s07_note_c = models.SmallIntegerField(null=True)
    s07_note_d = models.SmallIntegerField(null=True)
    s07_note_e = models.SmallIntegerField(null=True)
    s07_note_f = models.SmallIntegerField(null=True)
    s08_note = models.FloatField(null=True)
    s08_note_a = models.SmallIntegerField(null=True)
    s08_note_b = models.SmallIntegerField(null=True)
    s08_note_c = models.SmallIntegerField(null=True)
    s08_note_d = models.SmallIntegerField(null=True)
    s08_note_e = models.SmallIntegerField(null=True)
    s08_note_f = models.SmallIntegerField(null=True)
    s09_note = models.FloatField(null=True)
    s09_note_a = models.SmallIntegerField(null=True)
    s09_note_b = models.SmallIntegerField(null=True)
    s09_note_c = models.SmallIntegerField(null=True)
    s09_note_d = models.SmallIntegerField(null=True)
    s09_note_e = models.SmallIntegerField(null=True)
    s09_note_f = models.SmallIntegerField(null=True)
    s10_note = models.FloatField(null=True)
    s10_note_a = models.SmallIntegerField(null=True)
    s10_note_b = models.SmallIntegerField(null=True)
    s10_note_c = models.SmallIntegerField(null=True)
    s10_note_d = models.SmallIntegerField(null=True)
    s10_note_e = models.SmallIntegerField(null=True)
    s10_note_f = models.SmallIntegerField(null=True)
    s11_note = models.FloatField(null=True)
    s11_note_a = models.SmallIntegerField(null=True)
    s11_note_b = models.SmallIntegerField(null=True)
    s11_note_c = models.SmallIntegerField(null=True)
    s11_note_d = models.SmallIntegerField(null=True)
    s11_note_e = models.SmallIntegerField(null=True)
    s11_note_f = models.SmallIntegerField(null=True)
    s12_note = models.FloatField(null=True)
    s12_note_a = models.SmallIntegerField(null=True)
    s12_note_b = models.SmallIntegerField(null=True)
    s12_note_c = models.SmallIntegerField(null=True)
    s12_note_d = models.SmallIntegerField(null=True)
    s12_note_e = models.SmallIntegerField(null=True)
    s12_note_f = models.SmallIntegerField(null=True)

    cp_note = models.FloatField(null=True)
    cp_note_a = models.SmallIntegerField(null=True)
    cp_note_b = models.SmallIntegerField(null=True)
    cp_note_c = models.SmallIntegerField(null=True)
    cp_note_d = models.SmallIntegerField(null=True)
    cp_note_e = models.SmallIntegerField(null=True)
    cp_note_f = models.SmallIntegerField(null=True)


    jgt_a = models.SmallIntegerField(null=True)
    jgt_b = models.SmallIntegerField(null=True)
    jgt_c = models.SmallIntegerField(null=True)
    jgt_d = models.SmallIntegerField(null=True)
    jgt_e = models.SmallIntegerField(null=True)
    jgt_f = models.SmallIntegerField(null=True)

    ei_note = models.FloatField(null=True)
    ei_observation = models.CharField(null=True,max_length=1500)
    ei_objectif = models.CharField(null=True,max_length=250)

    # 75% de la compo + 25 % de l'EI
    cpei = models.FloatField(null=True)
    # Controles continus
    cc_on_20 = models.FloatField(null=True)
    # Moyenne sur 20
    moy_on_20 = models.FloatField(null=True)
    # Note sur 7
    moy_on_7 = models.FloatField(null=True)
    # Note du Bac Blanc par rapport critere
    bacblanc_v = models.FloatField(null=True)
     # Note du Bac Blanc
    bacblanc = models.SmallIntegerField(null=True)
    # Observations
    term_observation = models.TextField(null=True)



    def __str__(self):
        return self.label
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

# 'learner_has_subjectPEI' class level 7
# the classes of level 6 have foreignkeys from class level 5 and must be configured at the second position
# See the function of univers creation, day 6 : creation_day_6
# This table is populate with defaut values for a whole year depending of the configuration file.
class learnerPei_has_termsubjectPEI(learner_has_termsubject):

    f01_observation = models.CharField(null=True,max_length=255)
    f02_observation = models.CharField(null=True,max_length=255)
    f03_observation = models.CharField(null=True,max_length=255)
    f04_observation = models.CharField(null=True,max_length=255)
    f05_observation = models.CharField(null=True,max_length=255)
    f06_observation = models.CharField(null=True,max_length=255)
    f07_observation = models.CharField(null=True,max_length=255)
    f08_observation = models.CharField(null=True,max_length=255)
    f09_observation = models.CharField(null=True,max_length=255)
    f10_observation = models.CharField(null=True,max_length=255)
    f11_observation = models.CharField(null=True,max_length=255)
    f12_observation = models.CharField(null=True,max_length=255)
    s01_observation = models.CharField(null=True,max_length=255)
    s02_observation = models.CharField(null=True,max_length=255)
    s03_observation = models.CharField(null=True,max_length=255)
    s04_observation = models.CharField(null=True,max_length=255)
    s05_observation = models.CharField(null=True,max_length=255)
    s06_observation = models.CharField(null=True,max_length=255)
    s07_observation = models.CharField(null=True,max_length=255)
    s08_observation = models.CharField(null=True,max_length=255)
    s09_observation = models.CharField(null=True,max_length=255)
    s10_observation = models.CharField(null=True,max_length=255)
    s11_observation = models.CharField(null=True,max_length=255)
    s12_observation = models.CharField(null=True,max_length=255)
    f01_note_a = models.SmallIntegerField(null=True)
    f01_note_b = models.SmallIntegerField(null=True)
    f01_note_c = models.SmallIntegerField(null=True)
    f01_note_d = models.SmallIntegerField(null=True)
    f01_note_e = models.SmallIntegerField(null=True)
    f01_note_f = models.SmallIntegerField(null=True)
    f02_note_a = models.SmallIntegerField(null=True)
    f02_note_b = models.SmallIntegerField(null=True)
    f02_note_c = models.SmallIntegerField(null=True)
    f02_note_d = models.SmallIntegerField(null=True)
    f02_note_e = models.SmallIntegerField(null=True)
    f02_note_f = models.SmallIntegerField(null=True)
    f03_note_a = models.SmallIntegerField(null=True)
    f03_note_b = models.SmallIntegerField(null=True)
    f03_note_c = models.SmallIntegerField(null=True)
    f03_note_d = models.SmallIntegerField(null=True)
    f03_note_e = models.SmallIntegerField(null=True)
    f03_note_f = models.SmallIntegerField(null=True)
    f04_note_a = models.SmallIntegerField(null=True)
    f04_note_b = models.SmallIntegerField(null=True)
    f04_note_c = models.SmallIntegerField(null=True)
    f04_note_d = models.SmallIntegerField(null=True)
    f04_note_e = models.SmallIntegerField(null=True)
    f04_note_f = models.SmallIntegerField(null=True)
    f05_note_a = models.SmallIntegerField(null=True)
    f05_note_b = models.SmallIntegerField(null=True)
    f05_note_c = models.SmallIntegerField(null=True)
    f05_note_d = models.SmallIntegerField(null=True)
    f05_note_e = models.SmallIntegerField(null=True)
    f05_note_f = models.SmallIntegerField(null=True)
    f06_note_a = models.SmallIntegerField(null=True)
    f06_note_b = models.SmallIntegerField(null=True)
    f06_note_c = models.SmallIntegerField(null=True)
    f06_note_d = models.SmallIntegerField(null=True)
    f06_note_e = models.SmallIntegerField(null=True)
    f06_note_f = models.SmallIntegerField(null=True)
    f07_note_a = models.SmallIntegerField(null=True)
    f07_note_b = models.SmallIntegerField(null=True)
    f07_note_c = models.SmallIntegerField(null=True)
    f07_note_d = models.SmallIntegerField(null=True)
    f07_note_e = models.SmallIntegerField(null=True)
    f07_note_f = models.SmallIntegerField(null=True)
    f08_note_a = models.SmallIntegerField(null=True)
    f08_note_b = models.SmallIntegerField(null=True)
    f08_note_c = models.SmallIntegerField(null=True)
    f08_note_d = models.SmallIntegerField(null=True)
    f08_note_e = models.SmallIntegerField(null=True)
    f08_note_f = models.SmallIntegerField(null=True)
    f09_note_a = models.SmallIntegerField(null=True)
    f09_note_b = models.SmallIntegerField(null=True)
    f09_note_c = models.SmallIntegerField(null=True)
    f09_note_d = models.SmallIntegerField(null=True)
    f09_note_e = models.SmallIntegerField(null=True)
    f09_note_f = models.SmallIntegerField(null=True)
    f10_note_a = models.SmallIntegerField(null=True)
    f10_note_b = models.SmallIntegerField(null=True)
    f10_note_c = models.SmallIntegerField(null=True)
    f10_note_d = models.SmallIntegerField(null=True)
    f10_note_e = models.SmallIntegerField(null=True)
    f10_note_f = models.SmallIntegerField(null=True)
    f11_note_a = models.SmallIntegerField(null=True)
    f11_note_b = models.SmallIntegerField(null=True)
    f11_note_c = models.SmallIntegerField(null=True)
    f11_note_d = models.SmallIntegerField(null=True)
    f11_note_e = models.SmallIntegerField(null=True)
    f11_note_f = models.SmallIntegerField(null=True)
    f12_note_a = models.SmallIntegerField(null=True)
    f12_note_b = models.SmallIntegerField(null=True)
    f12_note_c = models.SmallIntegerField(null=True)
    f12_note_d = models.SmallIntegerField(null=True)
    f12_note_e = models.SmallIntegerField(null=True)
    f12_note_f = models.SmallIntegerField(null=True)
    s01_note_a = models.SmallIntegerField(null=True)
    s01_note_b = models.SmallIntegerField(null=True)
    s01_note_c = models.SmallIntegerField(null=True)
    s01_note_d = models.SmallIntegerField(null=True)
    s01_note_e = models.SmallIntegerField(null=True)
    s01_note_f = models.SmallIntegerField(null=True)
    s02_note_a = models.SmallIntegerField(null=True)
    s02_note_b = models.SmallIntegerField(null=True)
    s02_note_c = models.SmallIntegerField(null=True)
    s02_note_d = models.SmallIntegerField(null=True)
    s02_note_e = models.SmallIntegerField(null=True)
    s02_note_f = models.SmallIntegerField(null=True)
    s03_note_a = models.SmallIntegerField(null=True)
    s03_note_b = models.SmallIntegerField(null=True)
    s03_note_c = models.SmallIntegerField(null=True)
    s03_note_d = models.SmallIntegerField(null=True)
    s03_note_e = models.SmallIntegerField(null=True)
    s03_note_f = models.SmallIntegerField(null=True)
    s04_note_a = models.SmallIntegerField(null=True)
    s04_note_b = models.SmallIntegerField(null=True)
    s04_note_c = models.SmallIntegerField(null=True)
    s04_note_d = models.SmallIntegerField(null=True)
    s04_note_e = models.SmallIntegerField(null=True)
    s04_note_f = models.SmallIntegerField(null=True)
    s05_note_a = models.SmallIntegerField(null=True)
    s05_note_b = models.SmallIntegerField(null=True)
    s05_note_c = models.SmallIntegerField(null=True)
    s05_note_d = models.SmallIntegerField(null=True)
    s05_note_e = models.SmallIntegerField(null=True)
    s05_note_f = models.SmallIntegerField(null=True)
    s06_note_a = models.SmallIntegerField(null=True)
    s06_note_b = models.SmallIntegerField(null=True)
    s06_note_c = models.SmallIntegerField(null=True)
    s06_note_d = models.SmallIntegerField(null=True)
    s06_note_e = models.SmallIntegerField(null=True)
    s06_note_f = models.SmallIntegerField(null=True)
    s07_note_a = models.SmallIntegerField(null=True)
    s07_note_b = models.SmallIntegerField(null=True)
    s07_note_c = models.SmallIntegerField(null=True)
    s07_note_d = models.SmallIntegerField(null=True)
    s07_note_e = models.SmallIntegerField(null=True)
    s07_note_f = models.SmallIntegerField(null=True)
    s08_note_a = models.SmallIntegerField(null=True)
    s08_note_b = models.SmallIntegerField(null=True)
    s08_note_c = models.SmallIntegerField(null=True)
    s08_note_d = models.SmallIntegerField(null=True)
    s08_note_e = models.SmallIntegerField(null=True)
    s08_note_f = models.SmallIntegerField(null=True)
    s09_note_a = models.SmallIntegerField(null=True)
    s09_note_b = models.SmallIntegerField(null=True)
    s09_note_c = models.SmallIntegerField(null=True)
    s09_note_d = models.SmallIntegerField(null=True)
    s09_note_e = models.SmallIntegerField(null=True)
    S09_note_f = models.SmallIntegerField(null=True)
    s10_note_a = models.SmallIntegerField(null=True)
    s10_note_b = models.SmallIntegerField(null=True)
    s10_note_c = models.SmallIntegerField(null=True)
    s10_note_d = models.SmallIntegerField(null=True)
    s10_note_e = models.SmallIntegerField(null=True)
    s10_note_f = models.SmallIntegerField(null=True)
    s11_note_a = models.SmallIntegerField(null=True)
    s11_note_b = models.SmallIntegerField(null=True)
    s11_note_c = models.SmallIntegerField(null=True)
    s11_note_d = models.SmallIntegerField(null=True)
    s11_note_e = models.SmallIntegerField(null=True)
    s11_note_f = models.SmallIntegerField(null=True)
    s12_note_a = models.SmallIntegerField(null=True)
    s12_note_b = models.SmallIntegerField(null=True)
    s12_note_c = models.SmallIntegerField(null=True)
    s12_note_d = models.SmallIntegerField(null=True)
    s12_note_e = models.SmallIntegerField(null=True)
    s12_note_f = models.SmallIntegerField(null=True)
    s12_note_g = models.SmallIntegerField(null=True)

    cp_note_a = models.SmallIntegerField(null=True)
    cp_note_b = models.SmallIntegerField(null=True)
    cp_note_c = models.SmallIntegerField(null=True)
    cp_note_d = models.SmallIntegerField(null=True)
    cp_note_e = models.SmallIntegerField(null=True)
    cp_note_f = models.SmallIntegerField(null=True)

    cp_observation = models.CharField(null=True,max_length=72)

    jgt_a = models.SmallIntegerField(null=True)
    jgt_b = models.SmallIntegerField(null=True)
    jgt_c = models.SmallIntegerField(null=True)
    jgt_d = models.SmallIntegerField(null=True)
    jgt_e = models.SmallIntegerField(null=True)
    jgt_f = models.SmallIntegerField(null=True)

    note_on_7 = models.SmallIntegerField(null=True)
    term_observation = models.TextField(null=True)

    def __str__(self):
        return self.label
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

# criteria_of_subjectsgroup
class criteria_of_subjectsgroup (models.Model):
    criteria_letter = models.CharField(max_length=1)
    criteria_label = models.CharField(max_length=72)
    criteria_description = models.TextField()
    enabled = models.BooleanField(default=True)
    aspects1nr = models.SmallIntegerField(default=0)
    aspect_11 = models.CharField(max_length=222, null=True)
    aspect_12 = models.CharField(max_length=222, null=True)
    aspect_13 = models.CharField(max_length=222, null=True)
    aspect_14 = models.CharField(max_length=222, null=True)
    aspect_15 = models.CharField(max_length=222, null=True)
    aspect_16 = models.CharField(max_length=222, null=True)
    aspect_17 = models.CharField(max_length=222, null=True)
    fk_subjectgroup = models.ForeignKey('subjectgroup',on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.label
    def populate_init(self):
        return self.label

# criteria_of_levelsubject
# Only for DP
# The criteria can be different for subjects in the same
# subjectgroup
class criteria_of_levelsubject (models.Model):
    criteria_letter = models.CharField(max_length=1)
    criteria_label = models.CharField(max_length=72)
    criteria_description = models.TextField()
    enabled = models.BooleanField(default=True)
    aspects1nr = models.SmallIntegerField(default=0)
    aspect_11 = models.CharField(max_length=222, null=True)
    aspect_12 = models.CharField(max_length=222, null=True)
    aspect_13 = models.CharField(max_length=222, null=True)
    aspect_14 = models.CharField(max_length=222, null=True)
    aspect_15 = models.CharField(max_length=222, null=True)
    aspect_16 = models.CharField(max_length=222, null=True)
    aspect_17 = models.CharField(max_length=222, null=True)
    fk_levelsubject = models.ForeignKey('levelsubject',on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.criteria_letter

# subject_has_calendar
# For all the subjects - 3 évènement possible dans chaque journée
class subject_has_calendar(models.Model):
    #targetDate = models.DateTimeField(null=True)
    time_1 = models.TimeField(null=True)
    nature_1 = models.CharField(max_length=72,default="",null=True)
    todo_1 = models.TextField(default="",null=True)
    time_2 = models.TimeField(null=True)
    nature_2 = models.CharField(max_length=72,default="",null=True)
    todo_2 = models.TextField(default="",null=True)
    time_3 = models.TimeField(null=True)
    nature_3 = models.CharField(max_length=72,default="",null=True)
    todo_3 = models.TextField(default="",null=True)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    fk_jour = models.ForeignKey('agenda',on_delete = models.PROTECT,null=True)
    fk_classroom_termsubject = models.ForeignKey('classroom_termsubject',on_delete = models.PROTECT)

    def __str__(self):
        return self.nature_1
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

class evaluation(models.Model):
    label = models.CharField(max_length=3, null=False, blank=False)
    nature = models.CharField(max_length=72, null=True, blank=True)
    baremeNoteDP = models.SmallIntegerField(default=20);
    type_evaluation = models.CharField(default='-',max_length=1, null=False, blank=False)
    index_eval = models.SmallIntegerField(default=0)
    crit_A = models.NullBooleanField()
    aspect_A1 = models.NullBooleanField()
    aspect_A2 = models.NullBooleanField()
    aspect_A3 = models.NullBooleanField()
    aspect_A4 = models.NullBooleanField()
    aspect_A5 = models.NullBooleanField()
    aspect_A6 = models.NullBooleanField()
    aspect_A7 = models.NullBooleanField()
    crit_B = models.NullBooleanField()
    aspect_B1 = models.NullBooleanField()
    aspect_B2 = models.NullBooleanField()
    aspect_B3 = models.NullBooleanField()
    aspect_B4 = models.NullBooleanField()
    aspect_B5 = models.NullBooleanField()
    aspect_B6 = models.NullBooleanField()
    aspect_B7 = models.NullBooleanField()
    crit_C = models.NullBooleanField()
    aspect_C1 = models.NullBooleanField()
    aspect_C2 = models.NullBooleanField()
    aspect_C3 = models.NullBooleanField()
    aspect_C4 = models.NullBooleanField()
    aspect_C5 = models.NullBooleanField()
    aspect_C6 = models.NullBooleanField()
    aspect_C7 = models.NullBooleanField()
    crit_D = models.NullBooleanField()
    aspect_D1 = models.NullBooleanField()
    aspect_D2 = models.NullBooleanField()
    aspect_D3 = models.NullBooleanField()
    aspect_D4 = models.NullBooleanField()
    aspect_D5 = models.NullBooleanField()
    aspect_D6 = models.NullBooleanField()
    aspect_D7 = models.NullBooleanField()
    crit_E = models.NullBooleanField()
    aspect_E1 = models.NullBooleanField()
    aspect_E2 = models.NullBooleanField()
    aspect_E3 = models.NullBooleanField()
    aspect_E4 = models.NullBooleanField()
    aspect_E5 = models.NullBooleanField()
    aspect_E6 = models.NullBooleanField()
    aspect_E7 = models.NullBooleanField()
    crit_F = models.NullBooleanField()
    aspect_f1 = models.NullBooleanField()
    aspect_f2 = models.NullBooleanField()
    aspect_f3 = models.NullBooleanField()
    aspect_f4 = models.NullBooleanField()
    aspect_f5 = models.NullBooleanField()
    aspect_f6 = models.NullBooleanField()
    aspect_f7 = models.NullBooleanField()
    fk_classroom_termsubject = models.ForeignKey('classroom_termsubject',on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.label
    """
    # Population
    # The table is populate with a script with default value
    # according to the config table
    """

    class Unit(models.Model):
        label = models.CharField(max_length=10, null=False, blank=False, default= 'Unit')
        title = models.CharField(max_length=144, null=False, blank=False)
        soi = models.CharField(max_length=250, blank=True)
        loi = models.CharField(max_length=250, blank=True)
        date_start =models.DateField(null=True)
        date_end =models.DateField(null=True)
        duration = models.CharField(max_length=55, null=True, blank=True)
        content = models.CharField(max_length=255, null=True, blank=True)
        finaltask = models.CharField(max_length=255, null=True, blank=True)

        details = models.TextField(default="",blank=True)
        crit_A = models.BooleanField(default=False)
        aspect_A1 = models.BooleanField(default=False)
        aspect_A2 = models.BooleanField(default=False)
        aspect_A3 = models.BooleanField(default=False)
        aspect_A4 = models.BooleanField(default=False)
        aspect_A5 = models.BooleanField(default=False)
        aspect_A6 = models.BooleanField(default=False)
        aspect_A7 = models.BooleanField(default=False)
        crit_B = models.BooleanField(default=False)
        aspect_B1 = models.BooleanField(default=False)
        aspect_B2 = models.BooleanField(default=False)
        aspect_B3 = models.BooleanField(default=False)
        aspect_B4 = models.BooleanField(default=False)
        aspect_B5 = models.BooleanField(default=False)
        aspect_B6 = models.BooleanField(default=False)
        aspect_B7 = models.BooleanField(default=False)
        crit_C = models.BooleanField(default=False)
        aspect_C1 = models.BooleanField(default=False)
        aspect_C2 = models.BooleanField(default=False)
        aspect_C3 = models.BooleanField(default=False)
        aspect_C4 = models.BooleanField(default=False)
        aspect_C5 = models.BooleanField(default=False)
        aspect_C6 = models.BooleanField(default=False)
        aspect_C7 = models.BooleanField(default=False)
        crit_D = models.BooleanField(default=False)
        aspect_D1 = models.BooleanField(default=False)
        aspect_D2 = models.BooleanField(default=False)
        aspect_D3 = models.BooleanField(default=False)
        aspect_D4 = models.BooleanField(default=False)
        aspect_D5 = models.BooleanField(default=False)
        aspect_D6 = models.BooleanField(default=False)
        aspect_D7 = models.BooleanField(default=False)
        crit_E = models.BooleanField(default=False)
        aspect_E1 = models.BooleanField(default=False)
        aspect_E2 = models.BooleanField(default=False)
        aspect_E3 = models.BooleanField(default=False)
        aspect_E4 = models.BooleanField(default=False)
        aspect_E5 = models.BooleanField(default=False)
        aspect_E6 = models.BooleanField(default=False)
        aspect_E7 = models.BooleanField(default=False)
        crit_F = models.BooleanField(default=False)
        aspect_f1 = models.BooleanField(default=False)
        aspect_F2 = models.BooleanField(default=False)
        aspect_F3 = models.BooleanField(default=False)
        aspect_F4 = models.BooleanField(default=False)
        aspect_F5 = models.BooleanField(default=False)
        aspect_F6 = models.BooleanField(default=False)
        aspect_F7 = models.BooleanField(default=False)
        fk_keyconcept = models.ForeignKey('levelsubject', on_delete=models.PROTECT, null=True)
        fk_relconcept1 =  models.SmallIntegerField(null=True)
        fk_relconcept2 =  models.SmallIntegerField(null=True)
        fk_relconcept3 =  models.SmallIntegerField(null=True)
        fk_relconcept4 =  models.SmallIntegerField(null=True)
        fk_globalcontext = models.ForeignKey('globalcontext', on_delete=models.PROTECT,null=True)
        id_order_in_yearsubject = models.SmallIntegerField(default=0) # En général, No dans la matière (1 et 2 pour le premier trimestre/ 2 et 3 pour le deuxième trimestre etc..)
        fk_classroom_termsubject = models.ForeignKey('classroom_termsubject', on_delete=models.PROTECT)

"""
    # Population
    # The table is populate with a script with default value
    # according to the config table


1- table_language_ok = models.BooleanField(default=False)
1- table_academicyear_ok = models.BooleanField(default=False)
22- table_natureparentutor_ok = models.BooleanField(default=False)
21- table_concept_ok = models.BooleanField(default=False)
21- table_globalcontext_ok = models.BooleanField(default=False)
21- table_campus_ok  = models.BooleanField(default=False)
21- table_gender_ok = models.BooleanField(default=False)
22- table_program_ok = models.BooleanField(default=False)
22- table_term_ok = models.BooleanField(null=True,default=False)
32- table_subjectgroup_ok = models.BooleanField(null=True,default=False)
3- table_level_ok = models.BooleanField(null=True,default=False)
4- table_levelsubject_ok = models.BooleanField(null=True,default=False)
4- table_classroom_ok = models.BooleanField(null=True,default=False)
1- table_externalessay_ok = models.BooleanField(null=True,default=False)
4- table_criteria_of_subjectsgroup_ok = models.BooleanField(null=True,default=False)
5- table_criteria_of_levelsubject_ok = models.BooleanField(null=True,default=False)
table_parentutor_ok = models.BooleanField(null=True,default=False)
table_AECUser_ok = models.BooleanField(default=False)
table_student_ok = models.BooleanField(null=True,default=False)
table_teachadm_ok = models.BooleanField(null=True,default=False)
table_classroom_termsubject_ok = models.BooleanField(null=True,default=False)
table_learner_ok = models.BooleanField(null=True,default=False)
table_learner_has_term_ok = models.BooleanField(null=True,default=False)
table_learner_has_termsubject_ok = models.BooleanField(null=True,default=False)
table_learner_has_termsubjectDP_ok = models.BooleanField(null=True,default=False)
table_learner_has_termsubjectPei_ok = models.BooleanField(null=True,default=False)
table_learnerdp_has_tdc_ok = models.BooleanField(null=True,default=False)
table_learnerdp_has_externalessay_ok = models.BooleanField(null=True,default=False)
table_termsubject_has_agenda_ok = models.BooleanField(null=True,default=False)
"""
# TODO Corriger la tables levelsubject et regénérer la table classroom_termsubject
# TODO Corriger la matiere francais dans le levelsubject !
# TODO Annoter les index des membres de l'administration et des professeurs :
#       - les index des teachAdms sont posés entre 1000 et 5000 dasn la base dedonnées
#       - les indexs des students sont imposés par leur classe la première année. La deuxième année, elle
#         est imposée par le No de la classromm qui l'intègre.
