"""
Tests for the Django Admin modifications
"""

from django.test import testcases
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTest(testcases.TestCase):
    """Test  for Django Admin."""

