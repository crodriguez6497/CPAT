.. _admin-portal:


Administration Portal
########################################


C-PAT offers integrations with `STIG Manager <https://github.com/NUWCDIVNPT/stig-manager>`_ and `Tenable.sc <https://www.tenable.com/products/security-center>`_.
While it is possible to run C-PAT independently, to fully realize the benefits of C-PAT it is **strongly** recommended that C-PAT be configured to run in conjunction with these tools.



User Management
########################################
.. note::
  C-PAT has been tested and configured to work when C-PAT and STIG Manager are housed within the same OIDC realm, therefor, the value set for ``CPAT_OIDC_PROVIDER`` will also be used for obtaining a token for STIG Manager.
  If you are using the provided `RMFTools Keycloak container <https://github.com/NSWC-Crane/C-PAT/tree/C-PAT-AUTH>`_, the default value for ``STIGMAN_OIDC_CLIENT_ID`` can be used.

.. list-table:: STIG Manager Environmenment Variables: 
 :widths: 20 25 55
 :header-rows: 1
 :class: tight-table

 * - Variable
   - Default
   - Description
 * - ``STIGMAN_OIDC_CLIENT_ID``
   - stig-manager
   - The OIDC clientId for STIG Manager.
 * - ``STIGMAN_API_URL``
   - http://localhost:54000/api
   - The URL to the STIG Manager API.
 * - ``STIGMAN_SCOPE_PREFIX``
   - **No default**
   - String used as a prefix for each STIG Manager scope when authenticating to the OIDC Provider. This will likely match your ``STIGMAN_CLIENT_SCOPE_PREFIX`` environment variable configured in STIG Manager (if applicable).
 * - ``STIGMAN_EXTRA_SCOPES``
   - **No default**
   - Scopes to request in addition to: ``stig-manager:stig`` ``stig-manager:stig:read`` ``stig-manager:collection`` ``stig-manager:user`` ``stig-manager:user:read`` ``stig-manager:op`` ``openid``



Collection Management
########################################

Collection management is the process of creating and managing collections of STIGs within C-PAT. Collections are used to group STIGs together for the purpose of running assessments against them. Collections can be created manually or automatically by importing collections from STIG Manager.



Integrations
########################################

STIG Manager
Tenable.sc



VRAM IAV Import
########################################

VRAM IAV Import



Nessus Plugin Mapping
########################################

Nessus Plugin Mapping



Set A&A Packages
########################################

Set A&A Packages



Set Assigned Teams
########################################

Set Assigned Teams