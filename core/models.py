from django.db import models

# Create your models here.
class Applicant(models.Model):

    # MANDATORY FIELDS
    firstName = models.CharField(blank=True, default="", max_length=100)
    lastName = models.CharField(blank=True, default="", max_length=100)
    email = models.CharField(blank=True, default="", max_length=100)
    gender = models.CharField(blank=True, default="", max_length=100)
    org = models.CharField(blank=True, default="", max_length=100)
    country = models.CharField(blank=True, default="", max_length=100)
    phone = models.CharField(blank=True, default="", max_length=100)
    contact = models.CharField(blank=True, default="", max_length=1000)
    currentEng = models.CharField(blank=True, default="", max_length=100)
    linkedIn = models.CharField(blank=True, default="", max_length=100)
    fbUrl = models.CharField(blank=True, default="", max_length=100)
    commitWeeklyTime = models.CharField(blank=True, default="", max_length=100)

    progRating = models.CharField(blank=True, default="", max_length=100)
    takenWorkshopsInPast = models.CharField(blank=True, default="", max_length=100)
    whatToLearn = models.CharField(blank=True, default="", max_length=5000)
    whySelectMe = models.TextField(blank=True, default="", max_length=5000)
    whyArDev = models.TextField(blank=True, default="", max_length=5000)
    devCircle = models.CharField(blank=True, default="", max_length=100)
    githubId = models.CharField(blank=True, default="", max_length=100)
    personalWebsite = models.CharField(blank=True, default="", max_length=100)
    experience = models.CharField(blank=True, default="", max_length=100)

    # For professionals
    # less1, 1plus, 2plus, 5plus
    years_of_exp_in_sparkar = models.CharField(
        blank=True, default="1plus", max_length=20
    )

    # less1, 1to3, 4to10, 10plus
    years_of_exp_in_3d = (
        models.CharField(blank=True, default="less1", max_length=100),
    )

    # "I can't code at all", "I have a basic understanding of coding principles", " I can code a little but need help", "I can get by on my own (I prototype and hack things together)", "I'm proficient (I write production code)"
    rate_coding_ability = models.CharField(
        blank=True,
        default="I have a basic understanding of coding principles",
        max_length=500,
    )

    # URL - demos created
    effects_created = models.CharField(blank=True, default="", max_length=200)

    # Yes, No
    done_commercial_project = models.BooleanField(default=False, blank=True)

    # URL - SPARK Portfolio
    sparkar_portfolio = models.CharField(blank=True, default="", max_length=200)

    # random(2-10)
    sparkar_effects_created = models.IntegerField(blank=True, default=0)

    # Yes, No
    devote_time_for_advanced = models.CharField(blank=True, default="", max_length=20)
    # Fields for Professional ends ---

    # For students
    # Yes, No
    laptop_w_min_requirements = models.CharField(blank=True, default="", max_length=20)

    # Yes, No
    having_idea_about_ar_vr = models.CharField(blank=True, default="", max_length=20)

    # Yes, No
    used_photoshop_or_blender = models.CharField(blank=True, default="", max_length=20)

    # Yes, No
    used_designing_tool = models.CharField(blank=True, default="", max_length=20)

    # [SINGLE] "2D-Skills", "3D-Skills", "Coding Skills", "Other digital creation skills (e.g., photography, music) OPEN TEXT", "None of these"
    experienced_in = models.CharField(
        blank=True, default="Coding Skills", max_length=70
    )

    # opt1-opt13 MULTI
    why_interested_in_ar = models.CharField(
        blank=True, default="", max_length=500
    )

    # opt1-8 MULTI
    target_filter_types = models.CharField(blank=True, default="", max_length=300)

    # opt1-5 MULTI
    other_ar_tools = models.CharField(blank=True, default="", max_length=100)
    # Fields for Student ends ---

    # Fields common to prof an student
    # [MULTI] 3D-Animator, 3D-Artist, AR Developer, 2D-Artist, 2D-Animator, Developer, Graphic Designer, Product Designer, Social Media Marketer
    most_suitable_job_description = models.CharField(
        blank=True, default="Graphic designer", max_length=150
    )

    # [MULTI] "2D-Skills", "3D-Skills", "Coding Skills", "Other digital creation skills (e.g., photography, music) OPEN TEXT", "None of these"
    experienced_in = models.CharField(
        blank=True, default="Coding Skills", max_length=150
    )

    # MONITOR
    is_shortlisted = models.BooleanField(default=False)
