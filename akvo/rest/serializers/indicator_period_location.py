# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from akvo.rest.serializers.rsr_serializer import BaseRSRSerializer
from akvo.rsr.models import IndicatorPeriodActualLocation, IndicatorPeriodTargetLocation

from rest_framework import serializers


class IndicatorPeriodActualLocationSerializer(BaseRSRSerializer):

    period_unicode = serializers.ReadOnlyField(source='period.__unicode__')

    class Meta:
        model = IndicatorPeriodActualLocation


class IndicatorPeriodTargetLocationSerializer(BaseRSRSerializer):

    period_unicode = serializers.ReadOnlyField(source='period.__unicode__')

    class Meta:
        model = IndicatorPeriodTargetLocation
