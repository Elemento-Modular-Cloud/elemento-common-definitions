# #******************************************************************************#
# # Copyright(c) 2019-2026, Elemento srl, All rights reserved                    #
# #******************************************************************************#
#
# Frozen-layout tests for paths.json / paths.py.
# Source of truth: immutable-ready FHS AtomOS layout (absolute path strings below).
#

import json
import unittest
from os.path import dirname, join

import paths

# Frozen layout. Update together with paths.json when the on-disk contract changes.
FROZEN_LAYOUT = {
    "HOST_ETC": "/etc",
    "CONFIG_ROOT": "/etc/elemento",
    "CERTS_DIR": "/etc/elemento/certs",
    "MAINTENANCE_FLAG": "/etc/elemento/maintenance_mode",
    "TUNNEL_DIR": "/etc/elemento/tunnel",
    "HOST_HOME": "/home",
    "HOST_MNT": "/mnt",
    "VOLUME_MOUNT_GLOB_ONE": "/mnt/*",
    "VOLUME_MOUNT_GLOB_ANY": "/mnt/**",
    "BRICKS_MOUNT": "/mnt/bricks",
    "VAULT_MOUNT": "/mnt/elemento-vault",
    "REPOSITORY_MOUNT": "/mnt/repository",
    "HOST_OPT": "/opt",
    "GUI_APP_DIR": "/opt/app",
    "GUI_DAEMONS_DIR": "/opt/daemons",
    "HOMEBREW_PREFIX": "/opt/homebrew",
    "HOST_RUN": "/run",
    "OPENRC_RUN_DIR": "/run/openrc",
    "HOST_TMP": "/tmp",
    "HOST_USR": "/usr",
    "USR_BIN": "/usr/bin",
    "USR_LIBEXEC": "/usr/libexec",
    "INSTALL_ROOT": "/usr/libexec/elemento",
    "MONOREPO_ROOT": "/usr/libexec/elemento/elemento-monorepo-server",
    "HUGEPAGE_RESIZER": "/usr/libexec/elemento/hugepage_resizer.sh",
    "KELVIM_DIR": "/usr/libexec/elemento/kelvim",
    "EXPORTER_SCRIPTS_DIR": "/usr/libexec/elemento/scripts",
    "VENV_DIR": "/usr/libexec/elemento/venv",
    "USR_LOCAL": "/usr/local",
    "USR_SHARE": "/usr/share",
    "HOST_VAR": "/var",
    "HOST_VAR_LIB": "/var/lib",
    "STATE_ROOT": "/var/lib/elemento",
    "CLUSTERING_DIR": "/var/lib/elemento/clustering",
    "DHCP_DATA_DIR": "/var/lib/elemento/docker-dhcp",
    "DHCPD_DATA_DIR": "/var/lib/elemento/docker-dhcpd",
    "EXPORTED_LINKS_DIR": "/var/lib/elemento/exported",
    "NUCLEUS_DIR": "/var/lib/elemento/nucleus",
    "PERMISSIONS_DIR": "/var/lib/elemento/permissions",
    "SCHEDULES_DIR": "/var/lib/elemento/schedules",
    "TAILSCALE_DIR": "/var/lib/elemento/tailscale",
    "HOST_VAR_LOG": "/var/log",
    "APP_LOG_DIR": "/var/log/elemento",
    "SYSTEM_LOG_DIR": "/var/log/elemento",
    "HOST_VAR_RUN": "/var/run",
    "SCRATCH_DIR": "/var/tmp/elemento",
    "EXPORT_SCRATCH_DIR": "/var/tmp/elemento_exported",
}


class TestPathsFrozenLayout(unittest.TestCase):
    def test_module_attrs_match_frozen_layout(self):
        for key, expected in FROZEN_LAYOUT.items():
            with self.subTest(key=key):
                self.assertTrue(hasattr(paths, key), f"missing attribute {key}")
                self.assertEqual(getattr(paths, key), expected)

    def test_json_matches_frozen_layout(self):
        json_path = join(dirname(__file__), "paths.json")
        with open(json_path, encoding="utf-8") as fh:
            data = json.load(fh)
        self.assertEqual(data, FROZEN_LAYOUT)

    def test_helpers_match_frozen_layout(self):
        self.assertEqual(
            paths.certs_for_addr("1.2.3.4"),
            "/etc/elemento/certs/1.2.3.4.crt",
        )
        self.assertEqual(
            paths.tailscale_bridge_dir("br0"),
            "/var/lib/elemento/tailscale/br0",
        )
        self.assertEqual(
            paths.schedule_dir("daily"),
            "/var/lib/elemento/schedules/daily",
        )
        self.assertEqual(
            paths.scratch_pool_dir("pool"),
            "/var/tmp/elemento/pool",
        )
        self.assertEqual(paths.log_file("x.log"), "/var/log/elemento/x.log")
        self.assertEqual(
            paths.monorepo_server_dir("elemento-matcher-server"),
            "/usr/libexec/elemento/elemento-monorepo-server/elemento-matcher-server",
        )


if __name__ == "__main__":
    unittest.main()
