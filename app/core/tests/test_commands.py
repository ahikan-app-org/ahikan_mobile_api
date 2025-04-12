"""
Test the custom management commands
"""

from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


class CommandTests(SimpleTestCase):

    @patch('django.core.management.base.BaseCommand.check')  # Patch de self.check
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available"""
        patched_check.return_value = True  # Simule une base de données disponible immédiatement
        call_command('wait_for_db')
        patched_check.assert_called_once()

    @patch('time.sleep')  # Empêcher le test de réellement attendre
    @patch('django.core.management.base.BaseCommand.check')  # Patch de self.check
    def test_wait_for_db(self, patched_check, patched_sleep):
        """Test waiting for db"""
        patched_check.side_effect = [OperationalError] * 4 + [True]  # Simule la BDD indisponible 4 fois puis disponible
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 5)  # Vérifie qu'on a bien réessayé 5 fois
