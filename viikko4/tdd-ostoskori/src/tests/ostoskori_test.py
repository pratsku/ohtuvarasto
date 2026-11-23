import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipa", 4)
    #1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    # 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    # 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)
    # 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    # 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_yhteensa_tuotteiden_hinnat(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.hinta(), 7)
    # 6
    def test_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    # 7
    def test_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_kaksinkertaistuu(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 6)
    # 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)
    # 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoksen_nimi_oikea_ja_lukumaaran_1(self):
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
    # 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(len(self.kori.ostokset()), 2)
    # 11
    def test_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)
    # 12
    def test_saman_tuotteen_lisaamisen_jalkeen_ostoksen_nimi_oikea_ja_lukumaara_2(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)
    # 13
    def test_saman_tuotteen_kaksi_jalkeen_yhden_poisto_jattaa_yhden(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        ostos = ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
    # 14
    def test_tuotteen_lisaamisen_jalkeen_saman_tuotteen_poisto_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
    # 15
    def test_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)