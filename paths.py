# #******************************************************************************#
# # Copyright(c) 2019-2026, Elemento srl, All rights reserved                    #
# # Author: Elemento srl                                                         #
# # Contributors are mentioned in the code where appropriate.                    #
# # Permission to use and modify this software and its documentation strictly    #
# # for personal purposes is hereby granted without fee,                         #
# # provided that the above copyright notice appears in all copies               #
# # and that both the copyright notice and this permission notice appear in the  #
# # supporting documentation.                                                    #
# # Modifications to this work are allowed for personal use.                     #
# # Such modifications have to be licensed under a                               #
# # Creative Commons BY-NC-ND 4.0 International License available at             #
# # http://creativecommons.org/licenses/by-nc-nd/4.0/ and have to be made        #
# # available to the Elemento user community                                     #
# # through the original distribution channels.                                  #
# # The authors make no claims about the suitability                             #
# # of this software for any purpose.                                            #
# # It is provided "as is" without express or implied warranty.                  #
# #******************************************************************************#
#
# #------------------------------------------------------------------------------#
# #elemento-monorepo-server                                                      #
# #Authors:                                                                      #
# #- Gabriele Gaetano Fronze' (gfronze at elemento.cloud)                        #
# #------------------------------------------------------------------------------#
#
# Central filesystem path prefixes for AtomOS.
# Names describe role/purpose; values live in paths.json
# (immutable-ready FHS layout: image under /usr/libexec/elemento,
# state/logs/scratch under /var, config under /etc/elemento).
#

from os.path import join, dirname, basename
from json import load

data = open(join(dirname(__file__), basename(__file__).replace('.py', '.json').replace('.jsonc', '.json')))
data_json = load(data)
globals().update(data_json)
del data_json
del data


def tailscale_bridge_dir(bridge_name: str) -> str:
    """Per-bridge Tailscale state/compose directory."""
    return join(TAILSCALE_DIR, bridge_name)


def certs_for_addr(addr: str) -> str:
    """Client certificate path for a peer address."""
    return join(CERTS_DIR, f"{addr}.crt")


def schedule_dir(frequency: str) -> str:
    """Backup schedule scripts directory for a frequency."""
    return join(SCHEDULES_DIR, frequency)


def scratch_pool_dir(pool_name: str) -> str:
    """Per-pool scratch mount directory."""
    return join(SCRATCH_DIR, pool_name)


def log_file(name: str) -> str:
    """Absolute application log file path under APP_LOG_DIR (/var/log/elemento)."""
    return join(APP_LOG_DIR, name)


def monorepo_server_dir(server_name: str) -> str:
    """Packaged server directory under the monorepo install root."""
    return join(MONOREPO_ROOT, server_name)
