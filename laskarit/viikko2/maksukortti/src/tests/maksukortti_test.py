import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        vastaus = str(self.kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        vastaus = str(self.kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 7.50 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein_2(self):
        self.kortti.syo_edullisesti()
        saldo = self.kortti.saldo_euroina()

        self.assertEqual(saldo, 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        saldo = self.kortti.saldo_euroina()

        self.assertEqual(saldo, 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()
        saldo = kortti.saldo_euroina()

        self.assertEqual(saldo, 2.0)

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)
        saldo = self.kortti.saldo_euroina()

        self.assertEqual(saldo, 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)
        saldo = self.kortti.saldo_euroina()

        self.assertEqual(saldo, 150.0)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(300)
        kortti.syo_maukkaasti()
        saldo = kortti.saldo_euroina()

        self.assertEqual(saldo, 3.0)

    def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
        self.kortti.lataa_rahaa(-200)
        saldo = self.kortti.saldo_euroina()

        self.assertEqual(saldo, 10.0)

    def test_edullisen_lounaan_voi_ostaa_edullisen_lounaan_hinnalla(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()
        saldo = kortti.saldo_euroina()

        self.assertEqual(saldo, 0.0)

    def test_maukkaan_lounaan_voi_ostaa_maukkaan_lounaan_hinnalla(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()
        saldo = kortti.saldo_euroina()

        self.assertEqual(saldo, 0.0)
