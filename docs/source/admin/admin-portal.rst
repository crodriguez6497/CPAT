.. _admin-portal:


Administration Portal
########################################

The Admin Portal is a centralized interface for managing C-PAT. It provides a way to manage users, collections, integrations, and fine-tune options that best align with individual organizational policies and operations.
The Admin Portal is accessible to users with the ``admin`` role assigned by the OIDC provider and subsequently provided to C-PAT via the users token. Users whose token contains the admin role will automatically be presented with an "Admin Portal" button in the side menu bar. 



User Management
########################################

The User Management section allows administrators to view, manage, and modify user accounts within C-PAT.

.. note::
	By default, when a user first logs into C-PAT, they are assigned a ``PENDING`` account status and will not be able to access the application until an administrator approves their account. This step is implemented to ensure that only authorized users have access to the application and administrators have the ability and oversight to dictate more precise permissions and access.
	To approve a user account, an administrator must navigate to the User Management section, select the user account from the dropdown at the bottom of the User Table, and change the Account Status to ``ACTIVE``. Once approved, the user will be able to access the application and navigate to any collections for which they have been assigned permissions.

Assuming a correct C-PAT and OIDC configuration, user data *should* be automatically populated from the OIDC provider. If the user data is not automatically populated, the user data can be manually entered by an administrator. Accurate and complete user data is important to the flow of the C-PAT application, particularly when it comes to exporting into the eMASS excel format. User first name, last name, email, phone number, and office/organization are all pre-populated into a C=PAT export when available.

.. list-table:: C-PAT Collection Privileges: 
  :widths: 20 60 20
  :header-rows: 1
  :class: tight-table

  * - Privilege
    - Allows
  * - Viewer
    - The Viewer role is most commonly attributed to readonly access. Users who have been granted the Viewer role for a collection can view the collection and its associated POAMs, Assets, Labels, etc. Users with the Viewer role however, cannot make any changes or add new items.
  * - Submitter
    - The Submitter role is the recommended role for users who should not be restricted to readonly access and who do not explicitly need POAM approval access for the collection. Users with Submitter access will have access to add and modify data for POAMs, Assets, Labels, etc.
  * - Approver 
    - The Approver role is the recommended role for users who need to approve POAMs for the collection. Users with the Approver role will have the same access as that of the Submitter role, in addition to access to issue final approval or rejection for CAT II and CAT III POAMs. In the case of CAT I POAMs, an Approver can (and should) review and mark the POAM as approved, but the final approval must be issued by a CAT I Approver.
  * - CAT I Approver  
    - The CAT I Approver role provides the highest level of access to a collection. Users with the CAT I Approver role will have the same access as that of the Approver role, in addition to the ability to issue final approval for CAT I POAMs. CAT I Approvers are the only users who can issue final approval for CAT I POAMs.

Collection Management
########################################

.. warning::
	Manual creation of collections is not recommended when data ingestion from STIG Manager or Tenable is desired. Collections should be created automatically imported via the STIG Manager or Tenable Import section within the Admin Portal to ensure the proper collection association.

Collection management provides C-PAT administrators with the ability to manually create new collections, alter existing collections, or export all of the POAMs contained within a collection into the eMASS excel format.


.. note::
	While the Collection Name is the only required field for a collection, it is strongly recommended that all Collection fields are filled out to ensure proper data flow within C-PAT.

Collection Field Mappings:
 * Collection Name: The name of the collection. For collections that are imported from STIG Manager or Tenable, the collection name should match the collection name from the respective system. The collection name will be displayed in navigation across C-PAT and be contained in the file name of POAM exports.
 * Collection Description: A brief description of the collection.
 * System Type: This field will map to Cell ``L2`` in the eMASS format excel export.
 * System Name: This field will map to Cell ``D5`` in the eMASS format excel export.
 * CC/S/A/FA: This field will map to Cell ``D4`` in the eMASS format excel export.
 * A&A Package: C-PAT provides the ability to associate an A&A package with a collection. When a collection has an A&A package set, this field will be automatically populated for any POAM created within the collection.



Integrations
########################################

STIG Manager
----------------------------------------


Tenable.sc
----------------------------------------



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