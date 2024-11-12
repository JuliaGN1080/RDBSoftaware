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

def obter_detalhes_servico(nome_servico):
    # Simula a busca do serviço pelo nome
    servicos = obter_servicos()
    for servico in servicos:
        if servico['nome'] == nome_servico:
            return servico
    return None
