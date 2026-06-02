# Controle de Versão - Website

## v.1.0.4 (02 de Junho de 2026)
- Atualização explícita de versão (Hotfix da tela preta na v.1.0.3). O usuário estava visualizando a v.1.0.3 cacheada sem o hotfix.

## v.1.0.3 (02 de Junho de 2026)
- Resolução do letterboxing no Safari Mobile. Transformação da `div.screen` de position relative para absoluta a fim de forçar o motor do WebKit a resolver a altura do `aspect-ratio` corretamente para o `object-fit: cover` das imagens internas.
- Alinhamento de todas as imagens com `object-position: top center` para impedir cortes na Status Bar nativa do iOS contida nas capturas.

## v.1.0.2 (02 de Junho de 2026)
- Substituição das medidas `cqi` por variáveis nativas `--scale` e `calc()` para manter os tamanhos matematicamente imutáveis na escala de componentes do Apple Watch e iPhone, corrigindo a distorção do viewport (onde `cqi` lia a largura da tela do navegador em vez do mockup).

## v.1.0.1 (02 de Junho de 2026)
- Implementação de um sistema de versionamento visível no rodapé das páginas (`index.html`, `privacy.html`, `terms.html`, `support.html`).
- Refatoração profunda na responsividade dos mockups (iPhone/Watch) utilizando unidades `cqi` (Container Queries) para preservar a grossura exata dos contornos independentemente da tela.

## v.1.0.0
- Lançamento inicial da nova Landing Page (Clean Apple Style).
- Integração da política de RAG local.
- Adição dos mockups estáticos e micro-animações do site.
