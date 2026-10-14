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

from neutron_lib.api.definitions import logging as log_api
from neutron_lib.api.definitions import logging_output_type
from neutron_lib.tests.unit.api.definitions import base


class LoggingOutputTypeDefinitionTestCase(base.DefinitionBaseTestCase):

    extension_module = logging_output_type
    extension_resources = (log_api.LOGS, log_api.LOG_TYPES)
    extension_attributes = (logging_output_type.OUTPUT_TYPE,
                            logging_output_type.OUTPUT_TYPES)

    def test_output_type_defaults_to_packet_log(self):
        attr = self.resource_map[log_api.LOGS][
            logging_output_type.OUTPUT_TYPE]
        self.assertEqual(logging_output_type.PACKET_LOG, attr['default'])
        self.assertTrue(attr['allow_post'])
        self.assertFalse(attr['allow_put'])
        self.assertTrue(attr['enforce_policy'])
        self.assertEqual(
            logging_output_type.LOG_OUTPUT_TYPES,
            attr['validate']['type:values'])

    def test_output_types_is_read_only(self):
        attr = self.resource_map[log_api.LOG_TYPES][
            logging_output_type.OUTPUT_TYPES]
        self.assertFalse(attr['allow_post'])
        self.assertFalse(attr['allow_put'])
        self.assertTrue(attr['is_visible'])
