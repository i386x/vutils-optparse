#
# File:    ./tests/unit/test_version.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2022-11-20 00:37:41 +0100
# Project: vutils-optparse: Parsing command line options
#
# SPDX-License-Identifier: MIT
#
"""Test `vutils.optparse.version` module."""

from vutils.testing.testcase import TestCase

from vutils.optparse.version import __version__


class VersionTestCase(TestCase):
    """Test case for version."""

    __slots__ = ()

    def test_version(self):
        """Test if version is defined properly."""
        self.assertIsInstance(__version__, str)
