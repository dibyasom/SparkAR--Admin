from ast import parse
import random
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from core.models import Applicant

from core.serializers import ApplicantSerializer

URL = "https://sparkschool.reskilll.com/admin/api/internal/responses"

import requests


def multi_weighted_random(choices: list, samples: int, weights: list):
    random_samples = random.choices(choices, weights=weights, k=samples)
    return ",".join(random_samples)


def multi_random(choices: list, samples: int):
    random_samples = random.sample(choices, samples)
    return ",".join(random_samples)


def random_affirm():
    return multi_random(["Yes", "No"], 1)


# Create your views here.
def sync_with_remote_server(request):
    if request.method == "GET":
        # sending get request and saving the response as response object

        # Failed and Pass counts
        failed = 0
        passed = 0
        found = 0

        r = requests.get(url=URL)
        parsed_response = r.json()

        if len(parsed_response):
            for applicant in parsed_response:
                # Each applicant has the following attributes
                # 'takenWorkshopsInPast': 'NA',
                # '_id': '624d36b00537cbf2e7d85e9d',
                # 'firstName': 'Dibyasom',
                # 'lastName': 'Puhan',
                # 'email': 'dibyasom.dev@gmail.com',
                # 'githubId': '',
                # 'personalWebsite': '',
                # 'experience': 'NA',
                # '__v': 0,
                # 'contact': '',
                # 'devCircle': 'student',
                # 'fbUrl': '',
                # 'org': '',
                # 'progRating': 'Intermediate',
                # 'whatToLearn': '',
                # 'whyArDev': '',
                # 'whySelectMe': 'yjyj'

                # Remove unnecessary data
                applicant.pop("__v")
                applicant.pop("_id")

                # Determine current eng
                current_eng = None
                try:
                    current_eng = applicant["currentEng"]
                except:
                    current_eng = multi_weighted_random(
                        ["Student", "Working Professional"], 1, [75, 25]
                    )

                # Inject current_eng
                applicant["currentEng"] = current_eng

                if current_eng == "Student":
                    # Proffessional only
                    applicant["years_of_exp_in_sparkar"] = multi_weighted_random(
                        ["less1", "1plus", "2plus", "5plus"], 1, [20, 50, 20, 5]
                    )
                    applicant["years_of_exp_in_3d"] = multi_weighted_random(
                        ["less1", "1to3", "4to10", "10plus"], 1, [20, 70, 20, 5]
                    )
                    applicant["rate_coding_ability"] = multi_weighted_random(
                        [
                            "I can't code at all",
                            "I have a basic understanding of coding principles",
                            " I can code a little but need help",
                            "I can get by on my own (I prototype and hack things together)",
                            "I'm proficient (I write production code)",
                        ],
                        1,
                        [11, 22, 39, 47, 7],
                    )
                    applicant["effects_created"] = "NA"
                    applicant["done_commercial_project"] = random_affirm()
                    applicant["sparkar_portfolio"] = "NA"
                    applicant["sparkar_effects_created"] = random.randint(0, 9)
                    applicant["devote_time_for_advanced"] = random_affirm()
                else:
                    # Students only
                    applicant["laptop_w_min_requirements"] = random_affirm()
                    applicant["having_idea_about_ar_vr"] = random_affirm()
                    applicant["used_photoshop_or_blender"] = random_affirm()
                    applicant["used_designing_tool"] = random_affirm()

                # Common fields
                applicant["experienced_in"] = multi_random(
                    [
                        "3D-Animator",
                        "3D-Artist",
                        "AR Developer",
                        "2D-Artist",
                        "2D-Animator",
                        "Developer",
                        "Graphic Designer",
                        "Product Designer",
                        "Social Media Marketer",
                    ],
                    random.randint(1, 5),
                )
                applicant["why_interested_in_ar"] = multi_weighted_random(
                    [
                        "As part of my day-to-day job",
                        "To build things for my own use (personal projects)",
                        "To gain experience in order to maximize future opportunities",
                        "To make money",
                        "To promote or extend my company’s products or brand",
                        "I had a personal interest in it",
                        "To learn a new skill",
                        "To try something new",
                        "To promote or extend my personal brand",
                        "I believe it will have a positive impact on the world",
                        "To express my creativity",
                        "To stand out from the crowd",
                        "I am not sure",
                    ],
                    random.randint(1, 5),
                    [5, 15, 20, 10, 7, 25, 30, 30, 15, 20, 35, 35, 10],
                )
                applicant["target_filter_types"] = multi_random(
                    [
                        "Art",
                        "Educational",
                        "Games",
                        "Fashion",
                        "Interactive",
                        "Music",
                        "Games",
                        "Viral",
                    ],
                    random.randint(1, 5),
                )
                applicant["other_ar_tools"] = multi_weighted_random(
                    [
                        "ARore",
                        "ARKit",
                        "Lightship",
                        "Unity",
                        "Unreal",
                        "Vuforia",
                        "Wikitude",
                        "Lenstudio",
                    ],
                    random.randint(1, 3),
                    [15, 20, 10, 10, 10, 10, 10, 10],
                )
                applicant["most_suitable_job_description"] = multi_random(
                    [
                        "3D-Animator",
                        "3D-Artist",
                        "AR Developer",
                        "2D-Artist",
                        "2D-Animator",
                        "Developer",
                        "Graphic Designer",
                        "Product Designer",
                        "Social Media Marketer",
                    ],
                    random.randint(1, 4),
                )

                # Check doesn't exist already --
                applicant_exists = False
                all_applicants = Applicant.objects.all()
                try:
                    applicant_exists = Applicant.objects.get(email=applicant["email"])
                except:
                    applicant_exists = False

                if not applicant_exists:
                    applicant_srz = ApplicantSerializer(data=applicant)
                    try:
                        applicant_srz.is_valid(raise_exception=True)
                        applicant_srz.save()
                        passed += 1
                    except Exception as err:
                        failed += 1
                        print("ERROR", err)
                else:
                    found += 1
            return HttpResponse(
                    f"Done, Received- {len(parsed_response)} | Failed @{failed} | Passed @{passed} | Added @{found - len(all_applicants)} new entries."
                )

        else:
            return HttpResponse("Failed to update")
