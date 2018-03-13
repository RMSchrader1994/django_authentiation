from django.test import TestCase
from .views import *
from .models import Message
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class MessageViewTests(TestCase):
    def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, "messenger/inbox.html")

    def test_sent_template(self):
        response = self.client.get('/messenger/sent/')
        self.assertTemplateUsed(response, "messenger/sent_items.html")

    def test_view_message_does_not_exist(self):
        response = self.client.get('/messenger/message/1')
        self.assertEqual(response.status_code, 404)


    def test_view_message_that_exists(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')

        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()

        response = self.client.get('/messenger/message/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messenger/view_message.html")
        

    def test_get_compose_form(self):
        response = self.client.get('/messenger/message/compose/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messenger/compose_message.html")


    def test_post_message(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')
        self.client.login(username="sender", password="sender")
        
        message = {
            "subject": "Test Subject",
            "body": "Test Body",
            "recipient": recipient.id
        }

        response = self.client.post('/messenger/message/compose/', message)
        self.assertEqual(response.status_code, 302)
        
        
        
        
    def test_viewing_a_message_marks_it_as_read(self):
        sender = User.objects.create_user('sender', 'sender@example.com', 'sender')
        recipient = User.objects.create_user('recipient', 'recipient@example.com', 'recipient')

        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()

        self.assertEqual(message.read, False)
        
        response = self.client.get('/messenger/message/1')
        
        message = get_object_or_404(Message, pk=1)
        self.assertEqual(message.read, True)