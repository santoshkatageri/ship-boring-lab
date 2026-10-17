# Verification

Foundation check: `python3 tools/check_repository.py`.

This checks required directories and common sensitive filenames. It does not prove absence of secrets. Review staged content before publishing; introduce a dedicated secret scanner before operational configuration is migrated.

Future gates: Terraform format/validation and reviewed plans; Ansible syntax and repeatability; manifest validation; Backstage unit/build checks; application smoke tests; auth denial; offline recovery; restore drill; rollback and node loss. None of these runtime checks has been performed in this repository yet.
