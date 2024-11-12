import time
import unittest

# Função para recuperar os serviços
def obter_servicos():
    servicos = [
        {"nome": "Desenvolvimento de Aplicativo", "descricao": "Desenvolvimento de sistemas móveis.", "preco": 1000, "prazo": "15 dias", "categoria": "Programação"},
        {"nome": "Manutenção de Software", "descricao": "Manutenção e atualização de sistemas.", "preco": 500, "prazo": "7 dias", "categoria": "Manutenção"},
        {"nome": "Campanha de Google Ads", "descricao": "Gestão de anúncios no Google.", "preco": 700, "prazo": "10 dias", "categoria": "Marketing"},
        {"nome": "Consultoria de TI", "descricao": "Consultoria para melhorias em infraestrutura de TI.", "preco": 1500, "prazo": "20 dias", "categoria": "Consultoria de TI"},
        {"nome": "Desenvolvimento Web", "descricao": "Desenvolvimento de websites responsivos.", "preco": 1200, "prazo": "30 dias", "categoria": "Programação"},
        {"nome": "SEO para Sites", "descricao": "Otimização de sites para buscadores.", "preco": 600, "prazo": "15 dias", "categoria": "Marketing"},
        {"nome": "Suporte Técnico", "descricao": "Suporte remoto para sistemas e infraestrutura.", "preco": 300, "prazo": "5 dias", "categoria": "Manutenção"},
        {"nome": "Análise de Segurança", "descricao": "Análise de vulnerabilidades de sistemas e redes.", "preco": 800, "prazo": "10 dias", "categoria": "Consultoria de TI"},
        {"nome": "Gestão de Redes Sociais", "descricao": "Gestão de redes sociais para empresas.", "preco": 900, "prazo": "25 dias", "categoria": "Marketing"},
        {"nome": "Reparo de Hardware", "descricao": "Reparo de computadores e outros dispositivos.", "preco": 400, "prazo": "7 dias", "categoria": "Manutenção"}
    ]
    return servicos

# Função para categorizar os serviços
def categorizar_servicos(servicos, categoria):
    return [servico for servico in servicos if categoria.lower() in servico['categoria'].lower()]

class TestDesempenho(unittest.TestCase):
    
    def test_desempenho_obter_servicos(self):
        # Medindo o tempo de execução da função obter_servicos
        start_time = time.time()
        servicos = obter_servicos()  # Chama a função que recupera os serviços
        end_time = time.time()
        
        tempo_execucao = end_time - start_time
        print(f"Tempo para recuperar serviços: {tempo_execucao:.6f} segundos")
        
        # Verifica se o número de serviços está correto
        self.assertEqual(len(servicos), 10)

    def test_desempenho_categorizar_servicos_programacao(self):
        # Prepara os dados
        servicos = obter_servicos()
        
        # Medindo o tempo de execução da função categorizar_servicos para "Programação"
        start_time = time.time()
        programacao = categorizar_servicos(servicos, "Programação")
        end_time = time.time()
        
        tempo_execucao = end_time - start_time
        print(f"Tempo para categorizar serviços (Programação): {tempo_execucao:.6f} segundos")
        
        # Verifica se a categorização retornou o número correto de serviços
        self.assertEqual(len(programacao), 2)  # Espera-se 2 serviços na categoria "Programação"

    def test_desempenho_categorizar_servicos_marketing(self):
        # Prepara os dados
        servicos = obter_servicos()
        
        # Medindo o tempo de execução da função categorizar_servicos para "Marketing"
        start_time = time.time()
        marketing = categorizar_servicos(servicos, "Marketing")
        end_time = time.time()
        
        tempo_execucao = end_time - start_time
        print(f"Tempo para categorizar serviços (Marketing): {tempo_execucao:.6f} segundos")
        
        # Verifica se a categorização retornou o número correto de serviços
        self.assertEqual(len(marketing), 3)  # Espera-se 3 serviços na categoria "Marketing"

if __name__ == '__main__':
    unittest.main()
