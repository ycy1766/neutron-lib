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

from neutron_lib.api.definitions import tap_mirror
from neutron_lib.api.definitions import tap_mirror_lport
from neutron_lib.api.definitions import tap_mirror_rules
from neutron_lib.tests.unit.api.definitions import base


class TapMirrorRulesDefinitionTestCase(base.DefinitionBaseTestCase):
    extension_module = tap_mirror_rules
    # The sub-resource hangs off tap_mirrors, defined by the tap-mirror
    # extension.
    extension_resources = (tap_mirror.COLLECTION_NAME,)
    extension_subresources = (tap_mirror_rules.RULE_COLLECTION_NAME,)
    extension_attributes = ('priority', 'action', 'direction', 'ethertype',
                            'protocol',
                            'source_ip_prefix', 'destination_ip_prefix',
                            'source_port_range_min', 'source_port_range_max',
                            'destination_port_range_min',
                            'destination_port_range_max')

    def test_rules_subresource_parent_is_tap_mirror(self):
        parent = self.subresource_map[
            tap_mirror_rules.RULE_COLLECTION_NAME]['parent']
        self.assertEqual(tap_mirror.COLLECTION_NAME,
                         parent['collection_name'])
        self.assertEqual(tap_mirror.RESOURCE_NAME, parent['member_name'])

    def test_requires_lport_extension(self):
        self.assertIn(tap_mirror_lport.ALIAS,
                      tap_mirror_rules.REQUIRED_EXTENSIONS)

    def test_rule_priority_starts_at_one(self):
        priority = self.subresource_map[
            tap_mirror_rules.RULE_COLLECTION_NAME]['parameters']['priority']
        self.assertEqual((1, tap_mirror_rules.RULE_PRIORITY_MAX),
                         priority['validate']['type:range'])

    def test_rule_direction_is_optional(self):
        direction = self.subresource_map[
            tap_mirror_rules.RULE_COLLECTION_NAME]['parameters']['direction']
        self.assertIsNone(direction['default'])
        self.assertEqual(['IN', 'OUT', None],
                         direction['validate']['type:values'])
