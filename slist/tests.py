from django.test import TestCase
from slist.models import UserList, Shoppinglist
import uuid
# Create your tests here.
from django.contrib.auth.models import User
from django.test import Client
class UserListTestCase(TestCase):
    def setUp(self):
        self.user1_email = 'test_user1@example.com'
        self.user1_name = 'test_user1'
        self.user2_email = 'test_user2@example.com'
        self.user2_name = 'test_user2'

        user1 = User.objects.create_user(self.user1_name, self.user1_email, 'password')
        user1.save()

        user2 = User.objects.create_user(self.user2_name, self.user2_email, 'password')
        user2.save()

        shopuser1_list = UserList(user_id=user1.id, list_id=uuid.uuid4())
        shopuser1_list.save()

        shopuser2_list = UserList(user_id=user2.id, list_id=uuid.uuid4())
        shopuser2_list.save()
        self.user1_id = user1.id
        self.user2_id = user2.id


    def test_user_list(self):
        c = Client()
        c.login(username=self.user1_name, password='password')
        responce = c.post('/user/invite', {'email': self.user2_email})
        responce.status_code
        self.assertEqual(responce.status_code, 200)
        shopuser1_list = UserList.objects.filter(user_id=self.user1_id).first()
        shopuser2_list = UserList.objects.filter(user_id=self.user2_id).first()
        self.assertEqual(shopuser2_list.list_id, shopuser1_list.list_id)

    def test_user_not_exist(self):
        c = Client()
        c.login(username=self.user1_name, password='password')
        responce = c.post('/user/invite', {'email': 'user3@example.com'})
        self.assertEqual(responce.status_code, 404)


class UserRegister(TestCase):
    def createuser(self):
        c = Client()

        response = c.post('/user/register', {'username': 'user3', 'email': 'user3@gmail.com', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        user3 = User.objects.filter(username='user3').first()
        self.assertIsNotNone(user3)
        userlist3 = UserList.objects.filter(user_id=user3.id).first()
        self.assertIsNotNone(userlist3)

        response = c.post('/user/register', {'username': 'user4', 'email': 'user4@gmail.com', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        user4 = User.objects.filter(username='user4').first()
        self.assertIsNotNone(user4)
        userlist4 = UserList.objects.filter(user_id=user4.id).first()
        self.assertIsNotNone(userlist4)

        self.assertNotEqual(userlist3.list_id, userlist4.list_id)

class TestBuyItem(TestCase):
    fixtures = ['buy_item_fixture.json']
    def test_buy_item(self):
        shopinglist = Shoppinglist.objects.filter(list_id='2ae182f5-4029-43b1-a890-ea765a5a2c45').all()
        self.assertEqual(len(shopinglist), 2)

        c = Client()
        c.login(username='user1', password='1234')
        response = c.post('/shopping_list/1/buy', {'item': 1})

        shopinglist2 = Shoppinglist.objects.filter(list_id='2ae182f5-4029-43b1-a890-ea765a5a2c45').all()
        self.assertEqual(len(shopinglist), 2)
        self.assertEqual('bought', shopinglist2[1].status)
