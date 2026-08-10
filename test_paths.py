# #******************************************************************************#
# # Copyright(c) 2019-2026, Elemento srl, All rights reserved                    #
# #******************************************************************************#
#
# Frozen-layout tests for paths.json / paths.py.
# Source of truth: current on-disk AtomOS layout (absolute path strings below).
#

import json
import unittest
from os.path import dirname, join

import paths

# Frozen current on-disk layout. Update together with paths.json on POSIX remap.
FROZEN_LAYOUT = {
    "HOST_ETC": "/etc",
    "HOST_HOME": "/home",
    "HOST_MNT": "/mnt",
    "HOST_OPT": "/opt",
    "HOST_RUN": "/run",
    "HOST_TMP": "/tmp",
    "HOST_USR": "/usr",
    "HOST_VAR": "/var",
    "APP_LOG_DIR": "logs",
    "CONFIG_ROOT": "/etc/elemento",
    "CERTS_DIR": "/etc/elemento/certs",
    "CLUSTERING_DIR": "/etc/elemento/clustering",
    "MAINTENANCE_FLAG": "/etc/elemento/maintenance_mode",
    "PERMISSIONS_DIR": "/etc/elemento/permissions",
    "TUNNEL_DIR": "/etc/elemento/tunnel",
    "EXPORTER_SCRIPTS_DIR": "/home/scripts",
    "VOLUME_MOUNT_GLOB_ONE": "/mnt/*",
    "VOLUME_MOUNT_GLOB_ANY": "/mnt/**",
    "BRICKS_MOUNT": "/mnt/bricks",
    "VAULT_MOUNT": "/mnt/elemento-vault",
    "REPOSITORY_MOUNT": "/mnt/repository",
    "GUI_APP_DIR": "/opt/app",
    "GUI_DAEMONS_DIR": "/opt/daemons",
    "INSTALL_ROOT": "/opt/elemento",
    "NUCLEUS_DIR": "/opt/elemento/.nucleus",
    "DHCP_DATA_DIR": "/opt/elemento/docker-dhcp",
    "DHCPD_DATA_DIR": "/opt/elemento/docker-dhcpd",
    "MONOREPO_ROOT": "/opt/elemento/elemento-monorepo-server",
    "HUGEPAGE_RESIZER": "/opt/elemento/hugepage_resizer.sh",
    "KELVIM_DIR": "/opt/elemento/kelvim",
    "TAILSCALE_DIR": "/opt/elemento/tailscale",
    "VENV_DIR": "/opt/elemento/venv",
    "HOMEBREW_PREFIX": "/opt/homebrew",
    "OPENRC_RUN_DIR": "/run/openrc",
    "SCRATCH_DIR": "/tmp/elemento",
    "EXPORT_SCRATCH_DIR": "/tmp/elemento_exported",
    "USR_BIN": "/usr/bin",
    "USR_LIBEXEC": "/usr/libexec",
    "USR_LOCAL": "/usr/local",
    "USR_SHARE": "/usr/share",
    "STATE_ROOT": "/var/elemento",
    "EXPORTED_LINKS_DIR": "/var/elemento/exported",
    "SCHEDULES_DIR": "/var/elemento/schedules",
    "HOST_VAR_LIB": "/var/lib",
    "HOST_VAR_LOG": "/var/log",
    "SYSTEM_LOG_DIR": "/var/log/elemento",
    "HOST_VAR_RUN": "/var/run",
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
            "/opt/elemento/tailscale/br0",
        )
        self.assertEqual(
            paths.schedule_dir("daily"),
            "/var/elemento/schedules/daily",
        )
        self.assertEqual(
            paths.scratch_pool_dir("pool"),
            "/tmp/elemento/pool",
        )
        self.assertEqual(paths.log_file("x.log"), "logs/x.log")
        self.assertEqual(
            paths.monorepo_server_dir("elemento-matcher-server"),
            "/opt/elemento/elemento-monorepo-server/elemento-matcher-server",
        )


if __name__ == "__main__":
    unittest.main()
