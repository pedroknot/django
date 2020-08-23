from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        """ Roda toda vez antes de rodar os testes"""
        self.client = Client()
        self.url = reverse('index')
    
    def tearDown(self):
        """ Roda toda vez depois de rodar os testes"""
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')