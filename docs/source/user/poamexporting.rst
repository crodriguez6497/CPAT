POAM Exporting
=============

.. contents:: Table of Contents
   :local:
   :depth: 2

Field Mappings
-------------

The following table shows the mapping between Excel columns and POAM data fields:

.. list-table:: POAM Field Mappings
   :header-rows: 1
   :widths: 10 20 70

   * - Column
     - Source Field
     - Notes
   * - C
     - description
     - Raw description
   * - D
     - controlAPs
     - Default: "CM-6.5"
   * - E
     - officeOrg
     - Organization
   * - F
     - vulnerabilityId
     - Identifier
   * - G
     - requiredResources
     - Resource requirements
   * - H
     - scheduledCompletionDate
     - Format: MM/dd/yyyy
   * - I-K
     - milestones
     - Formatted milestone data
   * - L
     - vulnerabilitySource
     - Special formatting rules
   * - M
     - status
     - "Completed" or "Ongoing"
   * - N
     - cci
     - Prefixed with "CCI-"
   * - O, S
     - rawSeverity
     - Mapped severity value
   * - P
     - devicesAffected
     - Affected system list
   * - Q
     - mitigations
     - Mitigation steps
   * - R
     - predisposingConditions
     - Conditions list
   * - V
     - likelihood
     - Risk likelihood
   * - Y
     - residualRisk
     - Remaining risk assessment
   * - AA
     - adjSeverity
     - Mapped adjusted severity

Default Values
-------------

Standard Defaults
~~~~~~~~~~~~~~~

The following default values are applied to empty fields:

.. code-block:: none

   Column T: "High"
   Column W: "High"
   Column U: "ADVERSARIAL - HIGH: Per table D-2 Taxonomy of Threat Sources..."
   Column Z: "After reviewing documentation, and interviewing system stakeholders..."

CCI Default Values
~~~~~~~~~~~~~~~~

When no CCI is provided, the following defaults are applied:

* **controlAPs**: "CM-6.5"
* **cci**: "CCI-000366"
* **Note**: "Control mapping is unavailable..."

Severity Mapping
--------------

The following table shows how severity values are mapped:

.. list-table:: Severity Value Mappings
   :header-rows: 1
   :widths: 50 50

   * - Input Severity
     - Mapped Value
   * - CAT III - Info
     - Very Low
   * - CAT III - Low
     - Low
   * - CAT II - Medium
     - Moderate
   * - CAT I - High
     - High
   * - CAT I - Critical
     - Very High

Milestone Formatting
------------------

Milestones are formatted in two distinct sections:

Comments (Column J)
~~~~~~~~~~~~~~~~~

.. code-block:: none

   Milestone {number}:
   {comments}
   Milestone Status: {status}
   Milestone Date: MM/dd/yyyy

Changes (Column K)
~~~~~~~~~~~~~~~~

.. code-block:: none

   Milestone {number} Changes:
   {changeComments}
   Milestone Status: {status}
   Milestone Date Change: MM/dd/yyyy

.. note::

   Column I contains "1" if comments exist, empty otherwise

Export Process Details
--------------------

Filtering Rules
~~~~~~~~~~~~~

* POAMs with status "Draft" are excluded from export
* Empty/undefined fields use configured default values
* Dates are consistently formatted as MM/dd/yyyy

Special Field Handling
~~~~~~~~~~~~~~~~~~~~

Vulnerability Source
^^^^^^^^^^^^^^^^^^

* **STIG**: Uses vulnerability title
* **Task Order**: Prefixed with "Task Order #:"
* **Others**: Raw source value

Status Mapping
^^^^^^^^^^^^

* **Closed**: Mapped to "Completed"
* **Others**: Mapped to "Ongoing"

Impact Description
^^^^^^^^^^^^^^^

* Appended to CCI field when present

.. seealso::

   * :ref:`poam-creation`
   * :ref:`poam-management`
   * :ref:`export-templates`

.. warning::

   Ensure all required fields are populated before export to avoid unexpected default values in the exported document.