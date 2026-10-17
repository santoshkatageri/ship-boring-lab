# Ship Boring Lab

Status: repository foundation only. No clusters, Backstage application, or cloud resources are provisioned by this commit.

A generic self-hosted platform engineering lab using dummy services and example data.

## Structure

- `infra/terraform/`: infrastructure definitions, separated by environment.
- `infra/ansible/`: host configuration and cluster bootstrap.
- `gitops/`: desired Kubernetes configuration reconciled by Argo CD.
- `backstage/`: future portal source, templates and catalog.
- `docs/`: architecture, implementation gates and verification records.

## Selected design

Ubuntu 24.04 LTS and K3s; Backstage for the portal; GitHub Actions for CI; Argo CD for reconciliation; Kargo for promotion; KEDA for pod scaling. Node autoscaling is a separate later component.

Local development precedes preprod and production. Management hosts shared tooling independently of scheduled preprod shutdown. Versions, resource sizing and production availability remain to be validated.

## Repository checks

Run `python3 tools/check_repository.py`. This is a lightweight hygiene check, not a comprehensive secret scan or deployment validation.

## Scope

No credentials, customer data, Terraform state, plans or kubeconfigs belong here. Infrastructure mutations use Terraform and host setup uses versioned Ansible. Existing resources must be adopted deliberately; do not recreate or move state as part of repository setup.

## License

No open-source license has been selected yet. Public visibility does not grant a general reuse license.
