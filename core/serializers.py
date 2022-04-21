from rest_framework import serializers
from core.models import Applicant
from hashlib import sha256


class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
