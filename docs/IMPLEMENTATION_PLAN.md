# Implementation plan

## 0. Foundation — implemented

Repository layout, ownership rules and lightweight hygiene validation. No deployment performed.

## 1. Local lab — pending

Inspect available OrbStack resources without deleting existing clusters. Validate Ubuntu/K3s compatibility and pin versions. Use Ansible for repeatable setup. Acceptance: node readiness, DNS/network checks, dummy workload recovery and local data restore.

## 2. CI and GitOps — pending

Build immutable images, validate manifests, deploy locally with Argo CD, configure Kargo promotion. Acceptance: successful release and failed-release recovery evidence. Database migrations need a separate recovery strategy.

## 3. Preprod — pending

Review Terraform plan and cost before apply. Separate state, identity and dummy data. Validate backup restoration, worker replacement and scheduled stop/start. Add KEDA before node autoscaling; Spot is optional after baseline validation.

## 4. Portal — pending

Generate a pinned Backstage application, configure authentication, catalog, TechDocs and deployment visibility. Add workflow entry points only after workflows exist. Keep production approval outside the portal as well. Back up the portal database.

## 5. Production — pending

Verify account, database choice, budget, recovery targets and access controls. Complete independent security and operational review. Promote verified image digests; do not copy preprod data. No production readiness claim until evidence is recorded.

## Decisions outstanding

Management account access; Mac resources; exact tool versions; region and budget; database hosting; downtime/data-loss targets; production topology; public demo license.
