import glob

replacements = {
    ">Funcionalidades <span": ">Features <span",
    ">Ajuda &amp; Legal <span": ">Help &amp; Legal <span",
    ">Ajuda & Legal <span": ">Help & Legal <span",
    ">Coach IA<": ">AI Coach<",
    ">Ecossistema<": ">Ecosystem<",
    ">Jornadas<": ">Journeys<",
    ">Configurações<": ">Settings<",
    ">Suporte<": ">Support<",
    ">Termos de Uso<": ">Terms of Use<",
    ">Privacidade<": ">Privacy Policy<"
}

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        content = f.read()
        
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(file, 'w') as f:
        f.write(content)

print("Menu translated successfully.")
