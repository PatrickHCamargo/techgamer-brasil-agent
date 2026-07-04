import os
from groq import Groq
import re
import time
from datetime import datetime

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
AMAZON_TAG = "techgamerbr-20"
GA_TAG = "G-K5FHSZ4H9D"
OUTPUT_DIR = "/var/www/assistentelocal"

TEMAS = [
    ("melhor-mouse-gamer-custo-beneficio-2026", "Melhor Mouse Gamer Custo-Benefício 2026", "mouse gamer"),
    ("melhor-headset-sem-fio-para-jogos-2026", "Melhor Headset Sem Fio Para Jogos 2026", "headset gamer"),
    ("melhor-teclado-mecanico-para-iniciantes-2026", "Melhor Teclado Mecânico Para Iniciantes 2026", "teclado mecanico gamer"),
    ("melhor-monitor-gamer-144hz-barato-2026", "Melhor Monitor Gamer 144Hz Barato 2026", "monitor gamer 144hz"),
    ("melhor-ssd-para-pc-gamer-2026", "Melhor SSD Para PC Gamer 2026", "ssd nvme gamer"),
    ("melhor-placa-de-video-para-1080p-2026", "Melhor Placa de Vídeo Para 1080p 2026", "placa de video gamer"),
    ("melhor-cadeira-gamer-custo-beneficio-2026", "Melhor Cadeira Gamer Custo-Benefício 2026", "cadeira gamer"),
    ("melhor-mousepad-gamer-grande-2026", "Melhor Mousepad Gamer Grande 2026", "mousepad gamer grande"),
]

UNSPLASH_QUERIES = {
    "mouse gamer": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=800&q=80",
    "headset gamer": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80",
    "teclado mecanico gamer": "https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=800&q=80",
    "monitor gamer 144hz": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&q=80",
    "ssd nvme gamer": "https://images.unsplash.com/photo-1591488320449-011701bb6704?w=800&q=80",
    "placa de video gamer": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=800&q=80",
    "cadeira gamer": "https://images.unsplash.com/photo-1598550476439-6847785fcea6?w=800&q=80",
    "mousepad gamer grande": "https://images.unsplash.com/photo-1616588589676-62b3bd4ff6d2?w=800&q=80",
}

GA_SCRIPT = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_TAG}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_TAG}');
    </script>"""

BANNER_ONNER = """
    <div class="banner-onner">
        <div class="banner-inner">
            <div class="banner-text">
                <span class="banner-tag">Parceiro</span>
                <h3>Precisa de software corporativo sob medida?</h3>
                <p>A <strong>Onner</strong> desenvolve sistemas personalizados para empresas de todos os tamanhos.</p>
            </div>
            <a href="https://onner.tech" target="_blank" class="banner-btn">Conhecer a Onner →</a>
        </div>
    </div>"""

HEADER = """
    <header>
        <div class="header-inner">
            <a href="/" class="logo">⚡ Tech<span>Gamer</span>Brasil</a>
            <nav>
                <a href="/">Home</a>
                <a href="/#artigos">Artigos</a>
            </nav>
        </div>
    </header>"""

FOOTER = f"""
    <footer>
        <div class="footer-inner">
            <p>⚡ TechGamerBrasil &copy; {datetime.now().year} — Conteúdo independente sobre tecnologia gamer</p>
            <p style="font-size:12px;margin-top:8px;color:#555;">Como Associado Amazon, ganho comissões em compras qualificadas.</p>
        </div>
    </footer>"""

CSS = """
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background: #0f0f13; color: #e0e0e0; line-height: 1.7; }
        a { color: #f97316; text-decoration: none; }
        a:hover { text-decoration: underline; }
        header { background: #1a1a2e; border-bottom: 2px solid #f97316; position: sticky; top: 0; z-index: 100; }
        .header-inner { max-width: 1100px; margin: 0 auto; padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 22px; font-weight: 900; color: #fff; }
        .logo span { color: #f97316; }
        nav a { color: #ccc; margin-left: 20px; font-size: 14px; font-weight: 600; }
        nav a:hover { color: #f97316; text-decoration: none; }
        .hero { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); padding: 60px 20px; text-align: center; border-bottom: 1px solid #222; }
        .hero h1 { font-size: 42px; font-weight: 900; color: #fff; margin-bottom: 12px; }
        .hero h1 span { color: #f97316; }
        .hero p { font-size: 18px; color: #aaa; max-width: 600px; margin: 0 auto; }
        .container { max-width: 1100px; margin: 0 auto; padding: 40px 20px; }
        .section-title { font-size: 24px; font-weight: 700; color: #fff; margin-bottom: 24px; padding-bottom: 10px; border-bottom: 2px solid #f97316; }
        .cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px; }
        .card { background: #1a1a2e; border-radius: 12px; overflow: hidden; border: 1px solid #222; transition: transform 0.2s, border-color 0.2s; }
        .card:hover { transform: translateY(-4px); border-color: #f97316; }
        .card img { width: 100%; height: 180px; object-fit: cover; }
        .card-body { padding: 20px; }
        .card-body h3 { font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 10px; line-height: 1.4; }
        .card-body p { font-size: 13px; color: #999; margin-bottom: 16px; }
        .card-body a.btn { display: inline-block; background: #f97316; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; }
        .card-body a.btn:hover { background: #ea6c0a; text-decoration: none; }
        .banner-onner { background: linear-gradient(135deg, #0f3460 0%, #16213e 100%); border: 1px solid #1e4d8c; border-radius: 12px; margin: 40px 0; }
        .banner-inner { max-width: 1100px; margin: 0 auto; padding: 30px 40px; display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap; }
        .banner-text .banner-tag { background: #f97316; color: #fff; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; }
        .banner-text h3 { font-size: 20px; font-weight: 700; color: #fff; margin: 10px 0 6px; }
        .banner-text p { color: #aaa; font-size: 14px; }
        .banner-text strong { color: #fff; }
        .banner-btn { background: #f97316; color: #fff !important; padding: 12px 24px; border-radius: 8px; font-weight: 700; font-size: 14px; white-space: nowrap; }
        .banner-btn:hover { background: #ea6c0a; text-decoration: none !important; }
        footer { background: #1a1a2e; border-top: 1px solid #222; padding: 30px 20px; text-align: center; color: #666; font-size: 13px; margin-top: 60px; }
        .footer-inner { max-width: 1100px; margin: 0 auto; }
        .article-container { max-width: 860px; margin: 40px auto; padding: 0 20px; }
        .article-hero { width: 100%; height: 350px; object-fit: cover; border-radius: 12px; margin-bottom: 30px; }
        .article-container h1 { font-size: 36px; font-weight: 900; color: #fff; margin-bottom: 16px; line-height: 1.3; }
        .article-meta { font-size: 13px; color: #666; margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #222; }
        .article-container h2 { font-size: 24px; font-weight: 700; color: #fff; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #222; }
        .article-container h3 { font-size: 20px; font-weight: 700; color: #f97316; margin: 28px 0 12px; }
        .article-container p { color: #ccc; margin-bottom: 16px; font-size: 16px; }
        .article-container ul { padding-left: 20px; margin-bottom: 16px; }
        .article-container li { color: #ccc; margin: 8px 0; font-size: 15px; }
        .article-container strong { color: #fff; }
        .btn-amazon { display: inline-block; background: #f97316; color: #fff !important; padding: 12px 24px; border-radius: 8px; font-weight: 700; font-size: 15px; margin: 16px 0 24px; }
        .btn-amazon:hover { background: #ea6c0a; text-decoration: none !important; }
        .product-card { background: #1a1a2e; border: 1px solid #222; border-radius: 12px; padding: 24px; margin: 24px 0; }
        .voltar { display: inline-block; color: #f97316; font-weight: 600; margin-top: 40px; }
        @media (max-width: 600px) {
            .hero h1 { font-size: 28px; }
            .article-container h1 { font-size: 26px; }
            .cards { grid-template-columns: 1fr; }
            .banner-inner { flex-direction: column; text-align: center; }
        }
    </style>"""

client = Groq(api_key=GROQ_API_KEY)

def markdown_para_html(texto):
    texto = re.sub(r'^#{1,6}\s*', '', texto, flags=re.MULTILINE)
    texto = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', texto)
    texto = re.sub(r'\*(.+?)\*', r'<em>\1</em>', texto)
    return texto

def gerar_artigo(titulo):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Voce e um redator brasileiro especialista em tecnologia e games. Escreva SEMPRE em portugues brasileiro correto. NUNCA use palavras em espanhol. NUNCA use markdown, asteriscos ou cerquilhas. Use APENAS HTML valido."},
            {"role": "user", "content": f"""Escreva um artigo HTML completo em portugues brasileiro sobre '{titulo}'.
Use APENAS tags HTML: h2, h3, p, ul, li, strong, a.
NAO inclua h1.
Estrutura:
- p com introducao de 2 paragrafos envolventes
- h2 'Os 5 Melhores Produtos'
- Para cada produto use div class='product-card', h3 com nome do produto, p com descricao, ul com especificacoes tecnicas, p com Pros e Contras
- Apos cada product-card adicione um link de busca da Amazon usando EXATAMENTE este formato, substituindo NOME+DO+PRODUTO pelo nome exato do produto com + entre palavras:
  <a href="https://www.amazon.com.br/s?k=NOME+DO+PRODUTO&tag=techgamerbr-20" target="_blank" class="btn-amazon">Ver na Amazon</a>
  Exemplo: <a href="https://www.amazon.com.br/s?k=Logitech+G502+Hero&tag=techgamerbr-20" target="_blank" class="btn-amazon">Ver na Amazon</a>
- h2 'Conclusao' com paragrafo final
NAO use markdown, asteriscos, cerquilhas ou links inventados."""}
        ]
    )
    conteudo = response.choices[0].message.content
    conteudo = markdown_para_html(conteudo)
    return conteudo

def salvar_artigo(slug, titulo, imagem_query, conteudo):
    imagem = UNSPLASH_QUERIES.get(imagem_query, "https://images.unsplash.com/photo-1593640408182-31c228b29a5b?w=800&q=80")
    filename = f"{OUTPUT_DIR}/{slug}.html"
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{titulo} - Guia completo com os melhores produtos e custo-beneficio para gamers brasileiros.">
    <meta property="og:title" content="{titulo} | TechGamerBrasil">
    <meta property="og:description" content="Guia completo com os melhores produtos para gamers brasileiros.">
    <meta property="og:url" content="https://assistentelocal.com.br/{slug}.html">
    <meta property="og:type" content="article">
    <link rel="canonical" href="https://assistentelocal.com.br/{slug}.html">
    <title>{titulo} | TechGamerBrasil</title>
{GA_SCRIPT}
{CSS}
</head>
<body>
{HEADER}
<div class="article-container">
    <img src="{imagem}" alt="{titulo}" class="article-hero">
    <h1>{titulo}</h1>
    <p class="article-meta">📅 Atualizado em {datetime.now().strftime('%d/%m/%Y')} &nbsp;|&nbsp; ⚡ TechGamerBrasil</p>
    {conteudo}
    {BANNER_ONNER}
    <a href="/" class="voltar">← Voltar ao início</a>
</div>
{FOOTER}
</body>
</html>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Salvo: {filename}")

def gerar_index():
    cards = ""
    for slug, titulo, imagem_query in TEMAS:
        imagem = UNSPLASH_QUERIES.get(imagem_query, "https://images.unsplash.com/photo-1593640408182-31c228b29a5b?w=800&q=80")
        cards += f"""
        <div class="card">
            <img src="{imagem}" alt="{titulo}" loading="lazy">
            <div class="card-body">
                <h3>{titulo}</h3>
                <p>Guia completo com os melhores produtos para o seu setup gamer.</p>
                <a href="/{slug}.html" class="btn">Ler artigo →</a>
            </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="TechGamerBrasil - Os melhores produtos tech e gamer com custo-beneficio para o mercado brasileiro.">
    <meta property="og:title" content="TechGamerBrasil - Setup Gamer com Custo-Benefício">
    <meta property="og:url" content="https://assistentelocal.com.br">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://assistentelocal.com.br">
    <title>TechGamerBrasil - Setup Gamer com Custo-Benefício</title>
{GA_SCRIPT}
{CSS}
</head>
<body>
{HEADER}
<div class="hero">
    <h1>Setup Gamer com <span>Custo-Benefício</span></h1>
    <p>Os melhores produtos tech para montar seu setup dos sonhos sem gastar uma fortuna.</p>
</div>
<div class="container">
    {BANNER_ONNER}
    <h2 class="section-title" id="artigos">📋 Últimos Artigos</h2>
    <div class="cards">
        {cards}
    </div>
</div>
{FOOTER}
</body>
</html>"""
    with open(f"{OUTPUT_DIR}/index.html", 'w', encoding='utf-8') as f:
        f.write(html)
    print("Index atualizado!")

if __name__ == "__main__":
    if not GROQ_API_KEY:
        print("ERRO: GROQ_API_KEY nao encontrada! Rode: source ~/.bashrc")
        exit(1)
    print("Agente iniciando...")
    for slug, titulo, imagem_query in TEMAS:
        print(f"Gerando: {titulo}")
        conteudo = gerar_artigo(titulo)
        salvar_artigo(slug, titulo, imagem_query, conteudo)
        print("Aguardando 15s...")
        time.sleep(15)
    gerar_index()
    print("Pronto!")
