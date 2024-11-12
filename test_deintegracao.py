import unittest
from integracao import obter_servicos, categorizar_servicos

class TestIntegracaoServicos(unittest.TestCase):
    def test_categorizar_servicos(self):
        # Recupera a lista de serviços
        servicos = obter_servicos()
        
        # Teste 1: Filtrando serviços de "Programação"
        programacao = categorizar_servicos(servicos, "Programação")
        
        # Verifica se a lista filtrada de "Programação" tem apenas 1 serviço
        self.assertEqual(len(programacao), 1)
        self.assertEqual(programacao[0]["nome"], "Programação")
        self.assertEqual(programacao[0]["categoria"], "Programação")

        # Teste 2: Filtrando serviços de "Marketing"
        marketing = categorizar_servicos(servicos, "Marketing")
        
        # Verifica se a lista filtrada de "Marketing" tem apenas 1 serviço
        self.assertEqual(len(marketing), 1)
        self.assertEqual(marketing[0]["nome"], "Marketing")
        self.assertEqual(marketing[0]["categoria"], "Marketing")

        # Teste 3: Filtrando por uma categoria inexistente
        nao_encontrado = categorizar_servicos(servicos, "Design")
        
        # Verifica se a lista retornada é vazia
        self.assertEqual(len(nao_encontrado), 0)

if __name__ == '__main__':
    unittest.main()
