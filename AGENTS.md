# Engineering instructions

Read these instructions and relevant nested instructions before editing.
Preserve unrelated changes. Never print secrets, state or customer data.
AWS and DNS mutations must use reviewed Terraform plans; host/container setup uses versioned Ansible.
Do not apply infrastructure or migrate state merely because configuration exists.
GitOps and Ansible must not both own the same Kubernetes resource after bootstrap.
Keep environments, credentials and states isolated. Production requires explicit workflow approval and scoped roles.
Public contributions must never receive deployment credentials. Do not use pull_request_target to execute contribution code.
Pin dependencies and actions when introducing them; validate supported versions before installation.
Record checks actually executed; distinguish planned from implemented capabilities.
