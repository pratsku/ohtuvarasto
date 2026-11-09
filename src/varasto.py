
"""Sisältää Varasto-luokan."""


class Varasto:
    """Edustaa säilytystilaa."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Luo uuden varaston."""
        self.tilavuus = max(0.0, tilavuus)
        self.saldo = max(0.0, min(alku_saldo, self.tilavuus))

    def paljonko_mahtuu(self):
        """Palauttaa varastossa olevan vapaan tilan."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon tavaroita."""
        if maara < 0:
            return

        self.saldo = min(
            self.saldo + maara,
            self.tilavuus
        )

    def ota_varastosta(self, maara):
        """Ottaa varastosta tavaroita ja palauttaa otetun määrän."""
        if maara < 0:
            return 0.0

        saatiin = min(maara, self.saldo)
        self.saldo -= saatiin

        return saatiin

    def __str__(self):
        """Palauttaa varaston tiedot merkkijonona."""
        return (
            f"saldo = {self.saldo}, "
            f"vielä tilaa {self.paljonko_mahtuu()}"
        )
