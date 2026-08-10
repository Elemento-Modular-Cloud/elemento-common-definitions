# AtomOS filesystem layout (POSIX / immutable-ready)

Role-named path constants live in [`paths.json`](paths.json) and are loaded by
[`paths.py`](paths.py).

## Layout summary

| Role | Location |
|------|----------|
| Image (read-only) | `/usr/libexec/elemento` |
| Config | `/etc/elemento` |
| Persistent state | `/var/lib/elemento` |
| Logs | `/var/log/elemento` |
| Scratch | `/var/tmp/elemento`, `/var/tmp/elemento_exported` |
| Runtime | `/run` (e.g. OpenRC under `/run/openrc`) |

Container-internal paths (`GUI_APP_DIR` `/opt/app`, `GUI_DAEMONS_DIR` `/opt/daemons`)
and developer-only `HOMEBREW_PREFIX` are unchanged.

## Host directories to create

Before services start, ensure these exist with appropriate ownership (via image
`tmpfiles.d` / packaging — not via application code):

- `/var/log/elemento`
- `/var/lib/elemento` (and children as needed: `exported`, `schedules`, `nucleus`, `docker-dhcp`, `docker-dhcpd`, `tailscale`, `permissions`, `clustering`)
- `/var/tmp/elemento`
- `/var/tmp/elemento_exported`
- `/etc/elemento` (certs, tunnel, maintenance flag as today)

## Legacy → new symlinks (operators)

Legacy AtomOS mixed install and state under `/opt/elemento`. After remapping,
**do not** replace the whole tree with a single `/opt/elemento` → `/usr/libexec/elemento`
link if mutable data still lives under the old prefix. Prefer **per-leaf** symlinks
so historical data remains reachable:

| Legacy | New |
|--------|-----|
| `/opt/elemento/kelvim` | `/usr/libexec/elemento/kelvim` |
| `/opt/elemento/venv` | `/usr/libexec/elemento/venv` |
| `/opt/elemento/elemento-monorepo-server` | `/usr/libexec/elemento/elemento-monorepo-server` |
| `/opt/elemento/hugepage_resizer.sh` | `/usr/libexec/elemento/hugepage_resizer.sh` |
| `/opt/elemento/docker-dhcp` | `/var/lib/elemento/docker-dhcp` |
| `/opt/elemento/docker-dhcpd` | `/var/lib/elemento/docker-dhcpd` |
| `/opt/elemento/tailscale` | `/var/lib/elemento/tailscale` |
| `/opt/elemento/.nucleus` | `/var/lib/elemento/nucleus` |
| `/var/elemento/exported` | `/var/lib/elemento/exported` |
| `/var/elemento/schedules` | `/var/lib/elemento/schedules` |
| `/etc/elemento/permissions` | `/var/lib/elemento/permissions` |
| `/etc/elemento/clustering` | `/var/lib/elemento/clustering` |
| `/tmp/elemento` | `/var/tmp/elemento` |
| `/tmp/elemento_exported` | `/var/tmp/elemento_exported` |
| CWD-relative `logs/` (optional) | `/var/log/elemento` |

Example (illustrative; run as root on the host, after moving or seeding data into the new locations):

```bash
ln -sfn /usr/libexec/elemento/kelvim /opt/elemento/kelvim
ln -sfn /var/lib/elemento/docker-dhcpd /opt/elemento/docker-dhcpd
ln -sfn /var/log/elemento /path/to/old/cwd/logs   # only if needed
```

Symlink creation is an **operator / image** responsibility; AtomOS application code
does not create these links.
