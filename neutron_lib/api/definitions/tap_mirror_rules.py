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

from neutron_lib.api import converters
from neutron_lib.api.definitions import taas
from neutron_lib.api.definitions import tap_mirror
from neutron_lib.api.definitions import tap_mirror_lport
from neutron_lib import constants
from neutron_lib.db import constants as db_const
from neutron_lib.types import (
    ActionMap,
    ResourceAttributeMap,
    SubResourceAttributeMap,
    SubResourceParent,
)

ALIAS = 'tap-mirror-rules'
IS_SHIM_EXTENSION = False
IS_STANDARD_ATTR_EXTENSION = False
NAME = "Tap as a Service mirror filtering rules"
DESCRIPTION = ("Neutron Tap as a Service extension to select the traffic "
               "mirrored by an lport tap mirror with priority ordered "
               "rules.")
UPDATED_TIMESTAMP = "2026-09-23T10:00:00-00:00"

# Filtering rules sub-resource: /taas/tap_mirrors/{id}/rules
RULE_RESOURCE_NAME = 'rule'
RULE_COLLECTION_NAME = 'rules'
RULE_PARENT: SubResourceParent = {
    'collection_name': tap_mirror.COLLECTION_NAME,
    'member_name': tap_mirror.RESOURCE_NAME,
}

RULE_ACTION_MIRROR = 'mirror'
RULE_ACTION_SKIP = 'skip'
RULE_ACTIONS = [RULE_ACTION_MIRROR, RULE_ACTION_SKIP]

# OVN Mirror_Rule priority range. The backend keeps priority 0 for the
# implicit "mirror everything" flow of the mirror, so user rules start at 1.
RULE_PRIORITY_MIN = 1
RULE_PRIORITY_MAX = 32767

# A rule applies to both mirrored directions unless ``direction`` selects
# one of them.
RULE_DIRECTIONS = [taas.DIRECTION_IN, taas.DIRECTION_OUT]

RULE_ETHERTYPES = [constants.IPv4, constants.IPv6]
RULE_PROTOCOLS = [
    constants.PROTO_NAME_TCP,
    constants.PROTO_NAME_UDP,
    constants.PROTO_NAME_SCTP,
    constants.PROTO_NAME_ICMP,
    constants.PROTO_NAME_IPV6_ICMP,
]

RESOURCE_ATTRIBUTE_MAP: ResourceAttributeMap = {}

SUB_RESOURCE_ATTRIBUTE_MAP: SubResourceAttributeMap = {
    RULE_COLLECTION_NAME: {
        'parent': RULE_PARENT,
        'parameters': {
            'id': {
                'allow_post': False,
                'allow_put': False,
                'validate': {'type:uuid': None},
                'is_visible': True,
                'is_filter': True,
                'is_sort_key': True,
                'primary_key': True
            },
            'project_id': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:string': db_const.PROJECT_ID_FIELD_SIZE},
                'required_by_policy': True,
                'is_visible': True,
                'is_filter': True
            },
            'priority': {
                'allow_post': True,
                'allow_put': False,
                'convert_to': converters.convert_to_int,
                'validate': {
                    'type:range': (RULE_PRIORITY_MIN, RULE_PRIORITY_MAX)},
                'is_visible': True,
                'is_filter': True,
                'is_sort_key': True
            },
            'action': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:values': RULE_ACTIONS},
                'default': RULE_ACTION_MIRROR,
                'is_visible': True,
                'is_filter': True
            },
            'direction': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:values': RULE_DIRECTIONS + [None]},
                'default': None,
                'is_visible': True,
                'is_filter': True
            },
            'ethertype': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:values': RULE_ETHERTYPES},
                'default': constants.IPv4,
                'is_visible': True,
                'is_filter': True
            },
            'protocol': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:values': RULE_PROTOCOLS + [None]},
                'default': None,
                'is_visible': True,
                'is_filter': True
            },
            'source_ip_prefix': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:subnet_or_none': None},
                'default': None,
                'is_visible': True,
                'is_filter': True
            },
            'destination_ip_prefix': {
                'allow_post': True,
                'allow_put': False,
                'validate': {'type:subnet_or_none': None},
                'default': None,
                'is_visible': True,
                'is_filter': True
            },
            'source_port_range_min': {
                'allow_post': True,
                'allow_put': False,
                'convert_to': converters.convert_to_int_if_not_none,
                'validate': {'type:range_or_none': (1, 65535)},
                'default': None,
                'is_visible': True
            },
            'source_port_range_max': {
                'allow_post': True,
                'allow_put': False,
                'convert_to': converters.convert_to_int_if_not_none,
                'validate': {'type:range_or_none': (1, 65535)},
                'default': None,
                'is_visible': True
            },
            'destination_port_range_min': {
                'allow_post': True,
                'allow_put': False,
                'convert_to': converters.convert_to_int_if_not_none,
                'validate': {'type:range_or_none': (1, 65535)},
                'default': None,
                'is_visible': True
            },
            'destination_port_range_max': {
                'allow_post': True,
                'allow_put': False,
                'convert_to': converters.convert_to_int_if_not_none,
                'validate': {'type:range_or_none': (1, 65535)},
                'default': None,
                'is_visible': True
            },
        }
    }
}

ACTION_MAP: ActionMap = {}
ACTION_STATUS = {}
REQUIRED_EXTENSIONS = [tap_mirror.ALIAS, tap_mirror_lport.ALIAS]
OPTIONAL_EXTENSIONS = []
