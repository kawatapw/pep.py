"""Global objects and variables"""
from __future__ import annotations

import time
from typing import TYPE_CHECKING

from redis import Redis

from collection.channels import ChannelList
from collection.matches import MatchList
from collection.streams import StreamList
from collection.tokens import TokenList
from config import conf

if TYPE_CHECKING:
    from helpers.status_helper import StatusManager

# Consts.
DATADOG_PREFIX = "peppy"
BOT_NAME = "FokaBot"

__version__ = "3.1.0"

application = None
db = None
redis: Redis = None
config = conf
banchoConf = None
namespace = {}
streams = StreamList()
tokens = TokenList()
channels = ChannelList()
matches = MatchList()
verifiedCache = {}
cached_passwords: dict = {}
chatFilters = None
pool = None
busyThreads = 0

debug = False
restarting = False

startTime = int(time.time())
user_statuses: StatusManager = None
