#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mastodon import Mastodon
from config import *

def tootea(toot):
    mastodon = Mastodon(
        access_token = M_ACCESS_TOKEN,
        api_base_url = M_API_BASE_URL
    )
    mastodon.status_post(toot)

if __name__ == '__main__':
    tootea("Proba")