# Controle de Versão - Website

## v.1.0.2 (02 de Junho de 2026)
- Substituição das medidas `cqi` por variáveis nativas `--scale` e `calc()` para manter os tamanhos matematicamente imutáveis na escala de componentes do Apple Watch e iPhone, corrigindo a distorção do viewport (onde `cqi` lia a largura da tela do navegador em vez do mockup).

## v.1.0.1 (02 de Junho de 2026)
- Implementação de um sistema de versionamento visível no rodapé das páginas (`index.html`, `privacy.html`, `terms.html`, `support.html`).
- Refatoração profunda na responsividade dos mockups (iPhone/Watch) utilizando unidades `cqi` (Container Queries) para preservar a grossura exata dos contornos independentemente da tela.

## v.1.0.0
- Lançamento inicial da nova Landing Page (Clean Apple Style).
- Integração da política de RAG local.
- Adição dos mockups estáticos e micro-animações do site.
