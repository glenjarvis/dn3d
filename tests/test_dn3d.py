#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dn3d` package."""

import unittest
from click.testing import CliRunner

from dn3d import dn3d
from dn3d import cli


class TestDn3d(unittest.TestCase):
    """Tests for `dn3d` package."""

    def setUp(self):
        """Set up test components, if needed"""

    def tearDown(self):
        """Tear down test components, if needed"""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'dn3d.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
