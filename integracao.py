# Função para recuperar a lista de serviços oferecidos
def obter_servicos():
    return [
        {"nome": "Programação", "descricao": "Desenvolvimento de sistemas", "preco": 100, "prazo": "2 dias", "categoria": "Programação"},
        {"nome": "Manutenção", "descricao": "Manutenção de sistemas", "preco": 50, "prazo": "1 dia", "categoria": "Manutenção"},
        {"nome": "Marketing", "descricao": "Gestão de campanhas digitais", "preco": 200, "prazo": "5 dias", "categoria": "Marketing"},
        {"nome": "Consultoria de TI", "descricao": "Consultoria em soluções de TI", "preco": 300, "prazo": "3 dias", "categoria": "Consultoria de TI"}
    ]

# Função para categorizar os serviços
def categorizar_servicos(servicos, categoria):
    return [servico for servico in servicos if categoria.lower() in servico['categoria'].lower()]
