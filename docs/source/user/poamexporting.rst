.. _poamexporting:
POAM Exporting
----------------

+----------+----------------------+--------------------------------+
| Column   | Source Field         | Notes                         |
+==========+======================+================================+
| C        | description         | Raw description                |
+----------+----------------------+--------------------------------+
| D        | controlAPs          | Default: "CM-6.5"             |
+----------+----------------------+--------------------------------+
| E        | officeOrg           | Organization                   |
+----------+----------------------+--------------------------------+
| F        | vulnerabilityId     | Identifier                     |
+----------+----------------------+--------------------------------+
| G        | requiredResources   | Resource requirements          |
+----------+----------------------+--------------------------------+
| H        | scheduledCompletionDate| Format: MM/dd/yyyy         |
+----------+----------------------+--------------------------------+
| I-K      | milestones          | Formatted milestone data       |
+----------+----------------------+--------------------------------+
| L        | vulnerabilitySource | Special formatting rules       |
+----------+----------------------+--------------------------------+
| M        | status              | "Completed" or "Ongoing"       |
+----------+----------------------+--------------------------------+
| N        | cci                 | Prefixed with "CCI-"           |
+----------+----------------------+--------------------------------+
| O, S     | rawSeverity         | Mapped severity value          |
+----------+----------------------+--------------------------------+
| P        | devicesAffected     | Affected system list           |
+----------+----------------------+--------------------------------+
| Q        | mitigations         | Mitigation steps              |
+----------+----------------------+--------------------------------+
| R        | predisposingConditions| Conditions list             |
+----------+----------------------+--------------------------------+
| V        | likelihood          | Risk likelihood               |
+----------+----------------------+--------------------------------+
| Y        | residualRisk        | Remaining risk assessment     |
+----------+----------------------+--------------------------------+
| AA       | adjSeverity         | Mapped adjusted severity      |
+----------+----------------------+--------------------------------+

Default Values
^^^^^^^^^^^^^^

.. code-block:: text

   Column T: "High"
   Column W: "High"
   Column U: "ADVERSARIAL - HIGH: Per table D-2 Taxonomy of Threat Sources..."
   Column Z: "After reviewing documentation, and interviewing system stakeholders..."

CCI Default
^^^^^^^^^^^
If no CCI is provided:
   - controlAPs: "CM-6.5"
   - cci: "CCI-000366"
   - Note: "Control mapping is unavailable..."

Severity Mapping
^^^^^^^^^^^^^^^^

+----------------------+-----------------+
| Input Severity       | Mapped Value    |
+======================+=================+
| CAT III - Info      | Very Low        |
+----------------------+-----------------+
| CAT III - Low       | Low             |
+----------------------+-----------------+
| CAT II - Medium     | Moderate        |
+----------------------+-----------------+
| CAT I - High        | High            |
+----------------------+-----------------+
| CAT I - Critical    | Very High       |
+----------------------+-----------------+

Milestone Formatting
^^^^^^^^^^^^^^^^^^^^

Milestones are formatted into two sections:

1. Comments (Column J):
   .. code-block:: text

      Milestone {number}:
      {comments}
      Milestone Status: {status}
      Milestone Date: MM/dd/yyyy

2. Changes (Column K):
   .. code-block:: text

      Milestone {number} Changes:
      {changeComments}
      Milestone Status: {status}
      Milestone Date Change: MM/dd/yyyy

.. note::
   Column I contains "1" if comments exist, empty otherwise

Export Process Notes
^^^^^^^^^^^^^^^^^^^^^

Filtering

- POAMs with status "Draft" are excluded from export
- Empty/undefined fields use configured default values
- Dates are consistently formatted as MM/dd/yyyy

Special Handling

- Vulnerability Source formatting:
  - STIG: Uses vulnerability title
  - Task Order: Prefixed with "Task Order #:"
  - Others: Raw source value
- Status mapping:
  - "Closed" → "Completed"
  - Others → "Ongoing"
- Impact descriptions are appended to CCI field when present