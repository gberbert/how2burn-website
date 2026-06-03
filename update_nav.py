import glob
import re

nav_html = """    <nav class="clean-nav">
        <div class="nav-content">
            <a href="index.html" class="logo"><img src="assets/logo.png" alt="How2Burn Logo"> How2Burn</a>
            <div class="nav-links">
                <a href="index.html#dashboard">Dashboard</a>
                <a href="index.html#coach">Coach IA</a>
                <a href="index.html#logger">Logger</a>
                <a href="index.html#ecosystem">Ecossistema</a>
                <a href="index.html#journeys">Jornadas</a>
                <a href="index.html#settings">Configurações</a>
                <a href="index.html#faq">FAQ</a>
                <a href="support.html">Suporte</a>
                <a href="terms.html">Termos</a>
                <a href="privacy.html">Privacidade</a>
            </div>
            <a href="/app" class="nav-button">Download</a>
            <button class="menu-toggle" aria-label="Abrir menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>"""

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    # Replace the <nav> block
    content = re.sub(r'<nav class="clean-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    # Check if script.js is referenced. If not, add inline JS for the menu before </body>
    js_logic = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const menuToggle = document.querySelector('.menu-toggle');
            const navLinks = document.querySelector('.nav-links');
            if(menuToggle && navLinks) {
                menuToggle.addEventListener('click', () => {
                    menuToggle.classList.toggle('active');
                    navLinks.classList.toggle('active');
                });
                
                // Close menu when a link is clicked
                document.querySelectorAll('.nav-links a').forEach(link => {
                    link.addEventListener('click', () => {
                        menuToggle.classList.remove('active');
                        navLinks.classList.remove('active');
                    });
                });
            }
        });
    </script>
"""
    if "menuToggle" not in content:
        content = content.replace("</body>", js_logic + "</body>")
    
    with open(file, "w") as f:
        f.write(content)
print("Nav updated in all HTML files.")
