# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from akvo.rsr.models import RecipientCountry

from .rsr_serializer import BaseRSRSerializer

from rest_framework import serializers


class RecipientCountryRawSerializer(BaseRSRSerializer):

    class Meta:
        model = RecipientCountry


class RecipientCountrySerializer(RecipientCountryRawSerializer):

    country_label = serializers.ReadOnlyField(source='iati_country_unicode')
