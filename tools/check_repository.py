"""Small repository hygiene gate; not a full secret scanner."""
from pathlib import Path
import subprocess
root = Path(__file__).resolve().parents[1]
required = ["infra/terraform", "infra/ansible", "gitops", "backstage", "docs"]
errors = [f"Missing {p}" for p in required if not (root / p).is_dir()]
tracked = subprocess.check_output(["git", "ls-files"], cwd=root, text=True).splitlines()
for name in tracked:
    p = Path(name)
    if p.name.endswith(".example"):
        continue
    if any(s in p.name for s in (".tfstate", ".tfplan", "kubeconfig")) or p.suffix in (".pem", ".key", ".tfvars") or p.name == ".env" or p.name.startswith(".env."):
        errors.append(f"Sensitive filename tracked: {name}")
if errors:
    raise SystemExit("\n".join(errors))
print("Repository foundation checks passed; runtime validation remains pending.")
