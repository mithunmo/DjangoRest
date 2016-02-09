from django.test import TestCase

# Create your tests here.
# Create your tests here.
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#from myproject.apps.core.models import Account
from models import Portal

class PortalTests(APITestCase):

    """
    def setUp(self):
        Portal.objects.create(brandID=4, status="Enabled")
        Portal.objects.create(brandID=5, status="Disabled")
    """
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('portal-list')
        data = {'brandID': 5, 'status' : 'Enabled'}
        response = self.client.post(url, data, format='json')

        #response = self.client.get(url)
        #print response
        #response = self.client.get('/v1/portal/1/')
        #print response
        #self.assertEqual(response.data["ud"], {'id': 1, 'brandID': 4})
        self.assertEqual(response.data["brandID"], 5)

        """
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')
        """