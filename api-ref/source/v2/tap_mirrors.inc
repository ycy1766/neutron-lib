.. -*- rst -*-

===========
Tap Mirrors
===========

Tap Mirrors provide a way to mirror traffic from a Neutron port to an external
IP in a GRE or ERSPAN v1 tunnel, or, with the ``tap-mirror-lport`` extension,
to another Neutron port inside the overlay (``lport`` mirror type, ML2/OVN
only).

List Tap Mirrors
=================

.. rest_method:: GET /v2.0/taas/tap_mirrors

List tap mirrors that belong to a given project.

The list might be empty.

.. include:: filtering-list.inc

Normal response codes: 200

Error response codes: 401

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project_id-query
   - project-domain: project-domain_taas

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: tap_mirror_id
   - name: tap_mirror_name
   - description: description
   - tenant_id: project_id
   - port_id: tap_mirror_port_id
   - mirror_type: mirror_type
   - remote_ip: remote_ip_tap_mirror
   - remote_port_id: remote_port_id_tap_mirror
   - directions: directions_tap_mirror

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror-list-response.json
   :language: javascript

Create Tap Mirror
=================

.. rest_method:: POST /v2.0/taas/tap_mirrors

Creates a Tap Mirror.

Error response codes: 401, 403, 404, 409

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project_id-query
   - project-domain: project-domain_taas
   - tenant_id: project_id
   - name: tap_mirror_name
   - port_id: tap_mirror_port_id
   - mirror_type: mirror_type
   - remote_ip: remote_ip_tap_mirror
   - remote_port_id: remote_port_id_tap_mirror
   - directions: directions_tap_mirror
   - description: description

Request Example
---------------

.. literalinclude:: samples/taas/tap_mirror-create-request.json
   :language: javascript

Request Example (``lport`` mirror)
----------------------------------

.. literalinclude:: samples/taas/tap_mirror-create-lport-request.json
   :language: javascript

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: tap_mirror_id
   - name: tap_mirror_name
   - description: description
   - tenant_id: project_id
   - port_id: tap_mirror_port_id
   - mirror_type: mirror_type
   - remote_ip: remote_ip_tap_mirror
   - remote_port_id: remote_port_id_tap_mirror
   - directions: directions_tap_mirror

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror-create-response.json
   :language: javascript

Response Example (``lport`` mirror)
-----------------------------------

.. literalinclude:: samples/taas/tap_mirror-create-lport-response.json
   :language: javascript

Update Tap Mirror
=================

.. rest_method:: PUT /v2.0/taas/tap_mirrors/{tap_mirror_id}

Updates Tap Mirror.

Normal response codes: 200

Error response codes: 400, 401, 404, 412

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tap_mirror_id: tap_mirror_id-query
   - description: description
   - name: tap_mirror_name

Request Example
---------------

.. literalinclude:: samples/taas/tap_mirror-update-request.json
   :language: javascript

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: tap_mirror_id
   - name: tap_mirror_name
   - description: description
   - tenant_id: project_id
   - port_id: tap_mirror_port_id
   - mirror_type: mirror_type
   - remote_ip: remote_ip_tap_mirror
   - remote_port_id: remote_port_id_tap_mirror
   - directions: directions_tap_mirror

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror-update-response.json
   :language: javascript

Delete Tap Mirror
=================

.. rest_method:: DELETE /v2.0/taas/tap_mirrors/{tap_mirror_id}

Deleted a Tap Mirror.

Normal response codes: 204

Error response codes: 400, 401, 404, 412

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tap_mirror_id: tap_mirror_id-query

Response Parameters
-------------------

There is no body content for the response of a successful DELETE request.

Show Tap Mirror
===============

.. rest_method:: GET /v2.0/taas/tap_mirrors/{tap_mirror_id}

Shows details for a tap mirror.

.. include:: filtering-show.inc

Normal response codes: 200

Error response codes: 401, 404

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project_id-query
   - project-domain: project-domain_taas
   - tap_mirror_id: tap_mirror_id-query

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: tap_mirror_id
   - name: tap_mirror_name
   - description: description
   - tenant_id: project_id
   - port_id: tap_mirror_port_id
   - mirror_type: mirror_type
   - remote_ip: remote_ip_tap_mirror
   - remote_port_id: remote_port_id_tap_mirror
   - directions: directions_tap_mirror

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror-show-response.json
   :language: javascript

Tap Mirror Rules
================

The ``tap-mirror-rules`` extension adds a ``rules`` sub-resource to tap
mirrors of type ``lport``. A rule selects the traffic that the mirror copies
with the vocabulary of security group rules (``ethertype``, ``protocol``, IP
prefixes and port ranges), a ``priority`` (1-32767, higher is evaluated
first) and an ``action``, ``mirror`` or ``skip``. A mirror without rules, or
traffic that matches no rule, is mirrored. Rules are immutable and are
deleted with their tap mirror. Rules are rejected on ``gre`` and
``erspanv1`` mirrors.

List Tap Mirror Rules
=====================

.. rest_method:: GET /v2.0/taas/tap_mirrors/{tap_mirror_id}/rules

Lists the rules of a tap mirror.

.. include:: filtering-list.inc

Normal response codes: 200

Error response codes: 401, 404

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tap_mirror_id: tap_mirror_id-query

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - rules: tap_mirror_rules
   - id: tap_mirror_rule_id
   - tenant_id: project_id
   - priority: tap_mirror_rule_priority
   - action: tap_mirror_rule_action
   - direction: tap_mirror_rule_direction
   - ethertype: tap_mirror_rule_ethertype
   - protocol: tap_mirror_rule_protocol
   - source_ip_prefix: tap_mirror_rule_source_ip_prefix
   - destination_ip_prefix: tap_mirror_rule_destination_ip_prefix
   - source_port_range_min: tap_mirror_rule_source_port_range_min
   - source_port_range_max: tap_mirror_rule_source_port_range_max
   - destination_port_range_min: tap_mirror_rule_destination_port_range_min
   - destination_port_range_max: tap_mirror_rule_destination_port_range_max

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror_rules-list-response.json
   :language: javascript

Create Tap Mirror Rule
======================

.. rest_method:: POST /v2.0/taas/tap_mirrors/{tap_mirror_id}/rules

Creates a rule on an ``lport`` tap mirror.

Normal response codes: 201

Error response codes: 400, 401, 403, 404, 409

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tap_mirror_id: tap_mirror_id-query
   - rule: tap_mirror_rule
   - priority: tap_mirror_rule_priority
   - action: tap_mirror_rule_action-request
   - direction: tap_mirror_rule_direction-request
   - ethertype: tap_mirror_rule_ethertype-request
   - protocol: tap_mirror_rule_protocol-request
   - source_ip_prefix: tap_mirror_rule_source_ip_prefix-request
   - destination_ip_prefix: tap_mirror_rule_destination_ip_prefix-request
   - source_port_range_min: tap_mirror_rule_source_port_range_min-request
   - source_port_range_max: tap_mirror_rule_source_port_range_max-request
   - destination_port_range_min: tap_mirror_rule_destination_port_range_min-request
   - destination_port_range_max: tap_mirror_rule_destination_port_range_max-request

Request Example
---------------

.. literalinclude:: samples/taas/tap_mirror_rule-create-request.json
   :language: javascript

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - rule: tap_mirror_rule
   - id: tap_mirror_rule_id
   - tenant_id: project_id
   - priority: tap_mirror_rule_priority
   - action: tap_mirror_rule_action
   - direction: tap_mirror_rule_direction
   - ethertype: tap_mirror_rule_ethertype
   - protocol: tap_mirror_rule_protocol
   - source_ip_prefix: tap_mirror_rule_source_ip_prefix
   - destination_ip_prefix: tap_mirror_rule_destination_ip_prefix
   - source_port_range_min: tap_mirror_rule_source_port_range_min
   - source_port_range_max: tap_mirror_rule_source_port_range_max
   - destination_port_range_min: tap_mirror_rule_destination_port_range_min
   - destination_port_range_max: tap_mirror_rule_destination_port_range_max

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror_rule-create-response.json
   :language: javascript

Show Tap Mirror Rule
====================

.. rest_method:: GET /v2.0/taas/tap_mirrors/{tap_mirror_id}/rules/{rule_id}

Shows details for a tap mirror rule.

.. include:: filtering-show.inc

Normal response codes: 200

Error response codes: 401, 404

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - rule_id: tap_mirror_rule_id-path
   - tap_mirror_id: tap_mirror_id-query

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - rule: tap_mirror_rule
   - id: tap_mirror_rule_id
   - tenant_id: project_id
   - priority: tap_mirror_rule_priority
   - action: tap_mirror_rule_action
   - direction: tap_mirror_rule_direction
   - ethertype: tap_mirror_rule_ethertype
   - protocol: tap_mirror_rule_protocol
   - source_ip_prefix: tap_mirror_rule_source_ip_prefix
   - destination_ip_prefix: tap_mirror_rule_destination_ip_prefix
   - source_port_range_min: tap_mirror_rule_source_port_range_min
   - source_port_range_max: tap_mirror_rule_source_port_range_max
   - destination_port_range_min: tap_mirror_rule_destination_port_range_min
   - destination_port_range_max: tap_mirror_rule_destination_port_range_max

Response Example
----------------

.. literalinclude:: samples/taas/tap_mirror_rule-show-response.json
   :language: javascript

Delete Tap Mirror Rule
======================

.. rest_method:: DELETE /v2.0/taas/tap_mirrors/{tap_mirror_id}/rules/{rule_id}

Deletes a tap mirror rule.

Normal response codes: 204

Error response codes: 401, 404

Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - rule_id: tap_mirror_rule_id-path
   - tap_mirror_id: tap_mirror_id-query

Response Parameters
-------------------

There is no body content for the response of a successful DELETE request.
