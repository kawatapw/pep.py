# Rosu specific privilege constants
# If you fork please change these.
# Message to self: If you mess with these in the db, you suffer for hardcoding these.
# Hardcoding is the perfect, most maintainable way.
from __future__ import annotations

FULL_PERMS = 136104116219
FULL_PERMS_DONOR = 136104116223
DEV_SUPPORTER = 103621029391
DEVELOPER = 103621029387
GESTION_TEAM = 47513530619
SUPPORT_TEAM = 47244939515
MOD_BAT_DONOR = 816763391 # fuck u akeno
MOD_BAT = 816763387
MOD = 47244939515
BAT = 8594129163

ADMIN_PRIVS = (FULL_PERMS, DEVELOPER, GESTION_TEAM, SUPPORT_TEAM, MOD_BAT_DONOR, MOD_BAT, MOD, BAT)
