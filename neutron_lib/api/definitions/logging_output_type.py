# Copyright 2026 KT Cloud
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

from neutron_lib.api.definitions import logging
from neutron_lib.types import (
    ActionMap,
    ResourceAttributeMap,
    SubResourceAttributeMap,
)

# The alias of the extension.
ALIAS = 'logging-output-type'

# Whether or not this extension is simply signaling behavior to the user
# or it actively modifies the attribute map.
IS_SHIM_EXTENSION = False

# Whether the extension is marking the adoption of standardattr model for
# legacy resources, or introducing new standardattr attributes. False or
# None if the standardattr model is adopted since the introduction of
# resource extension.
# If this is True, the alias for the extension should be prefixed with
# 'standard-attr-'.
IS_STANDARD_ATTR_EXTENSION = False

# The name of the extension.
NAME = 'Logging output type'

# The description of the extension.
DESCRIPTION = ('Adds the output_type attribute to the log resource and the '
               'output_types attribute to the loggable resources, so that a '
               'log can request flow samples instead of packet log lines.')

# A timestamp of when the extension was introduced.
UPDATED_TIMESTAMP = "2026-10-14T10:00:00-00:00"

OUTPUT_TYPE = 'output_type'
OUTPUT_TYPES = 'output_types'

# The log output types. "packet_log" is the behavior of the logging
# backends before this extension: one log line per matched packet.
# "flow_sample" requests samples of the matched traffic exported by the
# backend, for example OVN ACL sampling exported with IPFIX.
PACKET_LOG = 'packet_log'
FLOW_SAMPLE = 'flow_sample'
LOG_OUTPUT_TYPES = [PACKET_LOG, FLOW_SAMPLE]

# The resource attribute map for the extension.
RESOURCE_ATTRIBUTE_MAP: ResourceAttributeMap = {
    logging.LOGS: {
        OUTPUT_TYPE: {
            'allow_post': True,
            'allow_put': False,
            'validate': {'type:values': LOG_OUTPUT_TYPES},
            'is_filter': True,
            'is_sort_key': False,
            'default': PACKET_LOG,
            'enforce_policy': True,
            'is_visible': True,
        },
    },
    logging.LOG_TYPES: {
        OUTPUT_TYPES: {
            'allow_post': False,
            'allow_put': False,
            'is_filter': False,
            'is_visible': True,
        },
    },
}

# The subresource attribute map for the extension.
SUB_RESOURCE_ATTRIBUTE_MAP: SubResourceAttributeMap = {}

# The action map.
ACTION_MAP: ActionMap = {}

# The action status.
ACTION_STATUS = {}

# The list of required extensions.
REQUIRED_EXTENSIONS = [logging.ALIAS]

# The list of optional extensions.
OPTIONAL_EXTENSIONS = []
