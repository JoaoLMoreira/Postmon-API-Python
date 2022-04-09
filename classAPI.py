class jsonclass:   
    def __init__(self, JSON):
        self.Estado = JSON['estado']
        self.Cidade = JSON['cidade']
        self.Bairro = JSON['bairro']
        self.Logradouro = JSON['logradouro']
        self.Estado_area_km2 = JSON['estado_info']['area_km2']
        self.Cidade_area_km2 = JSON['cidade_info']['area_km2']
        self.Cidade_codigo_ibge = JSON['cidade_info']['codigo_ibge']