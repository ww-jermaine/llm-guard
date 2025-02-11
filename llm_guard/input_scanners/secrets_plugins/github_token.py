"""
This plugin searches for GitHub tokens
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class GitHubTokenCustomDetector(RegexBasedDetector):
    """Scans for GitHub tokens."""

    secret_type = "GitHub Token"

    denylist = [
        # ref. https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/
        re.compile(r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36}"),
    ]
