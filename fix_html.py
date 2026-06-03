import glob
import re

nav_html = """    <nav class="clean-nav">
        <div class="nav-content">
            <a href="index.html" class="logo"><img src="assets/logo.png" alt="How2Burn Logo"> How2Burn</a>
            
            <div class="nav-links">
                <div class="dropdown">
                    <button class="dropbtn">Funcionalidades <span class="arrow">▾</span></button>
                    <div class="dropdown-content">
                        <a href="index.html#dashboard">Dashboard</a>
                        <a href="index.html#coach">Coach IA</a>
                        <a href="index.html#logger">Logger</a>
                        <a href="index.html#ecosystem">Ecossistema</a>
                        <a href="index.html#journeys">Jornadas</a>
                        <a href="index.html#settings">Configurações</a>
                    </div>
                </div>
                
                <div class="dropdown">
                    <button class="dropbtn">Ajuda & Legal <span class="arrow">▾</span></button>
                    <div class="dropdown-content">
                        <a href="index.html#faq">FAQ</a>
                        <a href="support.html">Suporte</a>
                        <a href="terms.html">Termos de Uso</a>
                        <a href="privacy.html">Privacidade</a>
                    </div>
                </div>
            </div>
            
            <div class="nav-actions-group">
                <a href="/app" class="nav-button">Download</a>
                <button class="menu-toggle" aria-label="Abrir menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>"""

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    # Replace the <nav> block
    content = re.sub(r'<nav class="clean-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(content)
print("Nav HTML updated for floating pill & dropdowns.")
