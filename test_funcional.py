import unittest
from funcional import obter_servicos, obter_detalhes_servico

class TestFuncional(unittest.TestCase):

    def test_visualizar_servicos(self):
        # A função obter_servicos deve retornar a lista completa de serviços
        servicos = obter_servicos()
        
        # Verificando se o número de serviços está correto (esperamos 10 serviços)
        self.assertEqual(len(servicos), 10)
        
        # Verificando se alguns serviços específicos estão na lista
        nomes_servicos = [servico['nome'] for servico in servicos]
        self.assertIn("Desenvolvimento de Aplicativo", nomes_servicos)
        self.assertIn("Consultoria de TI", nomes_servicos)
        self.assertIn("SEO para Sites", nomes_servicos)

    def test_consultar_detalhes_servico(self):
        # Consultando detalhes do serviço "Desenvolvimento de Aplicativo"
        servico = obter_detalhes_servico("Desenvolvimento de Aplicativo")
        
        # Verificando se o serviço foi encontrado e se os detalhes estão corretos
        self.assertIsNotNone(servico)
        self.assertEqual(servico['nome'], "Desenvolvimento de Aplicativo")
        self.assertEqual(servico['preco'], 1000)
        self.assertEqual(servico['prazo'], "15 dias")

        # Consultando um serviço inexistente
        servico_inexistente = obter_detalhes_servico("Serviço Inexistente")
        self.assertIsNone(servico_inexistente)

if __name__ == '__main__':
    unittest.main()
