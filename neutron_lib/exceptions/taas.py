# Copyright 2011 VMware, Inc
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from neutron_lib._i18n import _
from neutron_lib import exceptions as qexception


class TapServiceNotFound(qexception.NotFound):
    message = _("Tap Service  %(tap_id)s does not exist")


class TapFlowNotFound(qexception.NotFound):
    message = _("Tap Flow  %(flow_id)s does not exist")


class InvalidDestinationPort(qexception.NotFound):
    message = _("Destination Port %(port)s does not exist")


class InvalidSourcePort(qexception.NotFound):
    message = _("Source Port  %(port)s does not exist")


# TODO(haleyb): remove in H+2
class PortDoesNotBelongToTenant(qexception.NotAuthorized):
    message = _("The specified port does not belong to the tenant")


class PortDoesNotBelongToProject(qexception.NotAuthorized):
    message = _("The specified port does not belong to the project")


# TODO(haleyb): remove in H+2
class TapServiceNotBelongToTenant(qexception.NotAuthorized):
    message = _("Specified Tap Service does not belong to the tenant")


class TapServiceNotBelongToProject(qexception.NotAuthorized):
    message = _("Specified Tap Service does not belong to the project")


class TapServiceLimitReached(qexception.OverQuota):
    message = _("Reached the maximum quota for Tap Services")


class TapMirrorNotFound(qexception.NotFound):
    message = _("Tap Mirror %(mirror_id)s does not exist")


class TapMirrorTunnelConflict(qexception.Conflict):
    message = _("Tap Mirror with tunnel_id %(tunnel_id)s already exists")


class TapMirrorRemotePortRequired(qexception.InvalidInput):
    message = _("Tap Mirror of type %(mirror_type)s requires remote_port_id")


class TapMirrorRemoteIpRequired(qexception.InvalidInput):
    message = _("Tap Mirror of type %(mirror_type)s requires remote_ip")


class TapMirrorRemotePortNotAllowed(qexception.InvalidInput):
    message = _("Tap Mirror of type %(mirror_type)s does not accept "
                "remote_port_id")


class TapMirrorSameSourceAndRemotePort(qexception.InvalidInput):
    message = _("Tap Mirror source port and remote port must differ")


class TapMirrorRemotePortNotBound(qexception.InvalidInput):
    message = _("Tap Mirror remote port %(port_id)s is not bound to a host")


class TapMirrorTunnelIdRequired(qexception.InvalidInput):
    message = _("Tap Mirror of type %(mirror_type)s requires a tunnel ID for "
                "direction %(direction)s")


class TapMirrorLportPortInUse(qexception.Conflict):
    message = _("Port %(port_id)s already has an lport Tap Mirror for "
                "direction %(direction)s")


class TapMirrorRuleNotFound(qexception.NotFound):
    message = _("Tap Mirror rule %(rule_id)s does not exist")


class TapMirrorRulesNotSupported(qexception.InvalidInput):
    message = _("Tap Mirror %(mirror_id)s of type %(mirror_type)s does not "
                "support rules")


class TapMirrorRuleConflict(qexception.Conflict):
    message = _("Tap Mirror %(mirror_id)s already has a rule with priority "
                "%(priority)s and the same match")


class TapMirrorRuleInvalidPortRange(qexception.InvalidInput):
    message = _("Invalid port range in Tap Mirror rule: %(reason)s")


class TapMirrorRuleDirectionNotMirrored(qexception.InvalidInput):
    message = _("Tap Mirror %(mirror_id)s does not mirror direction "
                "%(direction)s")
