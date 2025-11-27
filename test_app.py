import unittest
from app import app

class TestUygulama(unittest.TestCase):
    
    def setUp(self):
        # Test için sanal bir istemci oluşturuyoruz
        self.app = app.test_client()
        self.app.testing = True

    def test_anasayfa_status_kodu(self):
        # '/' adresine istek atıyoruz
        response = self.app.get('/')
        # Cevabın 200 (Başarılı) olup olmadığını kontrol ediyoruz
        self.assertEqual(response.status_code, 200)

    def test_anasayfa_icerigi(self):
        response = self.app.get('/')
        # Cevabın içinde "Merhaba" kelimesi geçiyor mu?
        # (app.py'deki mesajınızda Merhaba geçmeli)
        context= response.data.tolower()
        self.assertIn(b'merhaba', context)

if __name__ == '__main__':
    unittest.main()