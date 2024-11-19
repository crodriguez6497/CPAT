.. _tenable:
Tenable
------------

The Tenable component is a comprehensive compilation of tools that provides a large majority of functionality contained in Tenable.sc in addition to numerous expanded capabilities. The tenable component is comprised of the Main Vulnerabilities, IAV Vulnerabilities, and Solutions components.

Main Vulnerabilities Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Main Vulnerabilities Component will display a table originating from Tenable's Vulnerabilities Summary (API tool ``sumid``) with filters to exclude "Informational" severity and include only items where the vulnerability was observed within the last 30 days by default.
When the Vulnerability Summary view is selected, the component will display columns for the following fields: ``POAM`` ``Plugin ID`` ``Name`` ``Family`` ``Severity`` ``VPR`` ``IAV`` ``Navy Comply Date`` ``Total`` ``Host Total``

To access the filter menu, a [colored] filter button is available to the top left of the table. At the top of the filter panel, a dropdown has been provided with several pre-made filters.
| Filter Preset | Applied Filters |
|--------------|----------------|
| Vulnerability Published 30+ Days | - Vulnerability Published: 30+ days |
| Exploitable Findings 7+ Days | - Exploit Available: true<br>- Vulnerability Published: 7+ days |
| Exploitable Findings 30+ Days | - Exploit Available: true<br>- Vulnerability Published: 30+ days |
| Critical/High 7+ Days | - Severity: Critical (4), High (3)<br>- Vulnerability Last Observed: 0-30 days<br>- Vulnerability Published: 7+ days |
| Critical/High 14+ Days | - Severity: Critical (4), High (3)<br>- Vulnerability Last Observed: 0-30 days<br>- Vulnerability Published: 14+ days |
| Critical/High 30+ Days | - Severity: Critical (4), High (3)<br>- Vulnerability Last Observed: 0-30 days<br>- Vulnerability Published: 30+ days |
| Medium 180+ Days | - Severity: Medium (2)<br>- Vulnerability Last Observed: 0-30 days<br>- Vulnerability Published: 180+ days |
| Low 365+ Days | - Severity: Low (1)<br>- Vulnerability Last Observed: 0-30 days<br>- Vulnerability Published: 365+ days |
| Cisco Findings 30+ Days | - Plugin Family: 33<br>- Vulnerability Last Observed: 0-30 days<br>- Severity: All (1-4) |
| Database Findings 30+ Days | - Plugin Family: 31<br>- Vulnerability Last Observed: 0-30 days<br>- Severity: All (1-4) |
| F5 Findings 30+ Days | - Plugin Family: 57<br>- Vulnerability Last Observed: 0-30 days<br>- Severity: All (1-4) |
| Linux/Ubuntu Findings 30+ Days | - Plugin Family: 1, 14<br>- Vulnerability Last Observed: 0-30 days<br>- Severity: All (1-4) |
Additional filters are available for the following items: ``ACR`` ``AES`` ``AES Severity`` ``Accept Risk`` ``Address`` ``Agent ID`` ``Application CPE`` ``Assets`` ``Audit File`` ``CCE ID`` ``Cross References`` ``CVE ID`` ``CVSS v2 Score`` ``CVSS v2 Vector`` ``CVSS v3 Score`` ``CVSS v3 Vector`` ``Data Format`` ``DNS Name`` ``Exploit Available`` ``Exploit Frameworks`` ``Host ID`` ``IAVM ID`` ``MS Bulletin ID`` ``Mitigated`` ``NetBIOS Name`` ``Patch Published`` ``Plugin Family`` ``Plugin ID`` ``Plugin Modified`` ``Plugin Name`` ``Plugin Published`` ``Plugin Type`` ``Port`` ``Protocol`` ``Recast Risk`` ``STIG Severity`` ``Scan Policy Plugins`` ``Severity`` ``Users`` ``Vulnerability Discovered`` ``Vulnerability Last Observed`` ``Vulnerability Priority Rating`` ``Vulnerability Published`` ``Vulnerability Text`` ``Vulnerability Type``

Additionally, local filters are available for the following items when the Vulnerability Summary view is selected: ``POAM`` ``IAV`` ``Navy Comply Date``

.. note::
   Because of the potential for large amounts of data to be returned, Tenable server side pagination and server side filtering are used to limit the amount of data returned to the client when Vulnerability List view is selected in the main vulnerabilities component. Local filtering for POAM, IAV, and Navy Comply Date are only available when the Vulnerability Summary view is selected. All external filters are available in both views.


The main vulnerabilites component has been configured 

IAV Vulnerabilities Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
