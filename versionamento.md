# Controle de Versão - Website

## v.1.0.7 (02 de Junho de 2026)
- Harmonização extrema do layout Mobile: todos os parágrafos de subtítulo, listas (bullets) e textos internos dos cartões (`.feature-item`) foram centralizados matematicamente para formarem um design 100% simétrico e balanceado, atendendo ao perfeccionismo do design.

## v.1.0.6 (02 de Junho de 2026)
- Redimensionamento e otimização geométrica da "Dynamic Island" (câmera frontal do iPhone). A altura e largura foram encolhidas para refletirem as proporções físicas reais de um iPhone 14/15 Pro, evitando que a ilha bloqueie o título e os botões superiores ("Journey Details" e "Close") nas screenshots do app.

## v.1.0.5 (02 de Junho de 2026)
- Correção de alinhamento visual em dispositivos móveis. A seção de conteúdo agora herda alinhamento à esquerda (`text-align: left; align-items: stretch;`) para remover a descentralização quebrada (h2 e ícones centralizados vs. cards alinhados à esquerda).
- Refatoração profunda na estética dos emojis (`.icon-large`), inserindo-os dentro de elegantes contêineres Glassmorphism, erradicando a aparência "crua" e não polida dos ícones soltos.

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
