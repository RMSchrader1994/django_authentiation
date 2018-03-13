
from django.test import TestCase
from .views import *
from django.core.urlresolvers import resolve
 
class MessengerTests(TestCase):
    def test_inbox_page_resolves(self):
        page = resolve('/messenger/inbox/')
        self.assertEqual(page.func, inbox)
        
    def test_sent_page_resolves(self):
        page = resolve('/messenger/sent/')
        self.assertEqual(page.func, sent)
        
    def test_compose_page_resolves(self):
        page = resolve('/messenger/message/compose/')
        self.assertEqual(page.func, compose_message)
    
    def test_message_page_resolves(self):
        page = resolve('/messenger/message/1/')
        self.assertEqual(page.func, view_message)

    def test_message_requires_id(self):
        response = self.client.get('/messenger/message/')
        self.assertEqual(response.status_code, 404)