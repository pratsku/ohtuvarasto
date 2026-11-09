
"""Testit Varasto-luokalle."""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testaa varaston toimivuutta."""

    def setUp(self):
        """Luo uuden varaston ennen jokaista testiä."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa tyhjän varaston luomista."""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa varaston tilavuuden."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa saldon kasvamista."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_pienentaa_vapaata_tilaa(self):
        """Testaa vapaan tilan vähenemistä."""
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa otetun määrän palauttamista."""
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa vapaan tilan kasvamista."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_nolla_tilavuus(self):
        """Testaa nollatilavuuksista varastoa."""
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_alkusaldo(self):
        """Testaa negatiivista alkusaldoa."""
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alkusaldo_yli_tilavuuden(self):
        """Testaa alkusaldoa, joka ylittää tilavuuden."""
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        """Testaa negatiivisen lisäyksen käsittelyä."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_suuri_lisays_tayttaa_varaston(self):
        """Testaa liian suuren lisäyksen käsittelyä."""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        """Testaa negatiivisen oton käsittelyä."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liian_suuri_otto_tyhjentaa_varaston(self):
        """Testaa liian suuren oton käsittelyä."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
