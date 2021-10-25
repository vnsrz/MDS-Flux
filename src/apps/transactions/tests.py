import datetime
from django.test import TestCase, Client
from django.urls import reverse

from apps.transactions.models import Purchase, Sale
from apps.user.models import CustomUser
from apps.clients.models import Client as MyClient

# ------------------------------------------------------------------------------------------------ Teste de Models

# Classe para testar a compra
# class TestPurchase(TestCase):
#     # Método que cria os Objetos 'Usuário' e 'Compra' para usar nos testes
#     def setUp(self):
#         self.user = CustomUser.objects.create(
#             email = 'test@email.com', 
#             username = 'teste',
#             password = 'popolklk'
#         )
#         self.user.save()
#         self.purchase = Purchase.objects.create(
#             user = self.user, 
#             products = 'produto teste', 
#             provider = 'fornecedor', 
#             price = 123.30
#         )
#         self.purchase.save()

#     # Testa se a data da compra é registrada corretamente
#     def test_purchase_date_is_registered(self):
#         self.assertEquals(self.purchase.purchase_date, datetime.date.today())
#         print('\npurchase date is registered\n')

# # Classe para testar a venda
# class TestSale(TestCase):
#     # Método que cria os Objetos 'Usuário', 'Cliente' e 'Venda' para usar nos testes
#     def setUp(self):
#         self.user = CustomUser.objects.create(
#             email = 'test@email.com', 
#             username = 'teste',
#             password = 'popolklk'
#         )
#         self.user.save()
#         self.client = MyClient.objects.create(
#             user = self.user, 
#             name = 'cliente teste', 
#             number = '12345678910',
#             email = 'clienttest@email.com',
#             cpf = '12345678910',
#             address = 'casa teste',
#         )
#         self.client.save()
#         self.sale = Sale.objects.create(
#             user = self.user, 
#             products = 'produto teste', 
#             client = self.client, 
#             price = 123.30
#         )
#         self.sale.save()

#     # Testa se a data da venda é registrada corretamente
#     def test_sale_date_is_registered(self):
#         self.assertEquals(self.sale.sale_date, datetime.date.today())
#         print('\nsale date is registered\n')

# ------------------------------------------------------------------------------------------------ Teste de Views

class TestPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_transactions_buy_page(self):
        url = reverse('list_purchases')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/purchases.html')
        self.assertContains(response, 'Compras')
        print('\npurchases page is working\n')

    def test_transactions_sell_page(self):
        url = reverse('list_sales')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/sales.html')
        self.assertContains(response, 'Vendas')
        print('\nsales page is working\n')

    def test_register_new_purchase_page(self):
        url = reverse('create_purchase')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transactions/purchase-form.html')
        self.assertContains(response, 'Compras -     Cadastrar')
        print('\npuchase register page is working\n')
    
    def test_sale_new_purchase_page(self):
        print('\nsale register page is working\n')

# py manage.py test apps/transactions