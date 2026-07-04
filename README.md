# TechGamer Brasil - Agente de Conteudo Automatizado

Agente Python que gera automaticamente artigos de afiliados sobre tecnologia gamer, publicando conteudo em um site com HTTPS hospedado em infraestrutura cloud gratuita.

## Como funciona

O agente usa a API da Groq (LLaMA 3.1) para gerar artigos completos em portugues sobre produtos de tecnologia gamer, insere automaticamente links de afiliado da Amazon, e publica as paginas HTML em um servidor Nginx.

## Stack utilizada

- **Infraestrutura**: Oracle Cloud Infrastructure (Free Tier) - VM Ubuntu
- **Servidor Web**: Nginx com certificado SSL via Let's Encrypt
- **IA**: Groq API (modelo LLaMA 3.1 8B)
- **Automacao**: Python 3 + cron job diario
- **Analytics**: Google Analytics 4
- **SEO**: Google Search Console + sitemap.xml
- **Monetizacao**: Programa de Associados Amazon

## Funcionalidades

- Geracao automatica de artigos com IA
- Insercao automatica de links de afiliado especificos por produto
- Template HTML responsivo com tema dark
- Imagens de produtos via Unsplash
- SEO on-page (meta tags, sitemap, robots.txt)
- Execucao diaria automatizada via cron
- Deploy 100%% em infraestrutura gratuita

## Configuracao

A chave da API e lida via variavel de ambiente:

```bash
export GROQ_API_KEY="sua_chave_aqui"
python3 agente.py
```

## Autor

Patrick Camargo
