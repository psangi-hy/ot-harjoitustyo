import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.tyhja_kortti = Maksukortti(0)
        self.taysi_kortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_ja_myyntien_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_riittava_edullinen_kateismaksu_toimii(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_riittamaton_edullinen_kateismaksu_toimii(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_riittava_maukas_kateismaksu_toimii(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_riittamaton_maukas_kateismaksu_toimii(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_riittava_edullinen_korttimaksu_toimii(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.taysi_kortti))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.taysi_kortti.saldo, 760)

    def test_riittamaton_edullinen_korttimaksu_toimii(self):
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.tyhja_kortti))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.tyhja_kortti.saldo, 0)

    def test_riittava_maukas_korttimaksu_toimii(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.taysi_kortti))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.taysi_kortti.saldo, 600)

    def test_riittamaton_maukas_korttimaksu_toimii(self):
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.tyhja_kortti))
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.tyhja_kortti.saldo, 0)

    def test_kortille_lataaminen_toimii(self):
        self.kassa.lataa_rahaa_kortille(self.tyhja_kortti, 1000)
        self.assertEqual(self.tyhja_kortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortille_ei_voi_ladata_negatiivista_maaraa_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.tyhja_kortti, -100)
        self.assertEqual(self.tyhja_kortti.saldo, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
