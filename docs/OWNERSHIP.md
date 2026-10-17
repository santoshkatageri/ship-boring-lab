# Ownership and migration

Terraform owns cloud foundation resources. Ansible owns host configuration and bootstrap. Argo CD owns assigned Kubernetes objects after bootstrap. Backstage exposes workflows; it does not bypass their approvals. Kargo promotes versions. KEDA owns configured workload replica scaling; node scaling is separate.

Before migrating existing infrastructure, inventory resource addresses, state backends, provider versions, deployment paths and CI consumers. Establish a no-change plan against the existing backend, update path consumers, validate, then retire the old path in a separate reviewed change. Never copy state into Git or initialize a second owner for existing resources.

Keep application and infrastructure releases independent. Keep the portal recoverable without using the portal itself.
