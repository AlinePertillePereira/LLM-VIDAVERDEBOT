<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Vida Verde Bot</title>
  <link href="file:///C:/Users/Aline/OneDrive/Desktop/Chatbot/Chat.html" rel="stylesheet" />
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
 
    :root {
      --green-dark: #1a3d2b;
      --green-mid: #2d6a4f;
      --green-accent: #52b788;
      --green-light: #d8f3dc;
      --cream: #f8f5ee;
      --text-main: #1a1a1a;
      --text-muted: #6b7c6e;
      --white: #ffffff;
      --shadow: 0 4px 24px rgba(26,61,43,0.10);
    }
 
    body {
      font-family: 'DM Sans', sans-serif;
      background: var(--cream);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }
 
    .chatbot-wrap {
      display: flex;
      flex-direction: column;
      min-height: 580px;
      width: 100%;
      max-width: 440px;
      background: var(--white);
      border-radius: 20px;
      box-shadow: var(--shadow);
      overflow: hidden;
    }
 
    .chat-header {
      background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-mid) 100%);
      padding: 1.1rem 1.25rem 1rem;
      display: flex;
      align-items: center;
      gap: 12px;
    }
 
     .avatar {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      overflow: hidden;
      background: white;
      display: flex;
      align-items: center;
      justify-content: center;
   }

     .avatar img {
       width: 100%;
       height: 100%;
       object-fit: cover;
   }
 
    .header-info h2 {
      font-family: 'Playfair Display', serif;
      font-size: 16px;
      font-weight: 500;
      color: #fff;
      letter-spacing: 0.3px;
    }
 
    .header-info span {
      font-size: 12px;
      color: var(--green-light);
      display: flex; align-items: center; gap: 5px;
    }
 
    .status-dot {
      width: 7px; height: 7px;
      background: #74c69d;
      border-radius: 50%;
      display: inline-block;
    }
 
    .chat-body {
      flex: 1;
      padding: 1.25rem 1rem 0.75rem;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
      min-height: 360px;
      max-height: 380px;
    }
 
    .msg {
      display: flex;
      gap: 8px;
      align-items: flex-end;
      animation: fadeUp 0.28s ease;
    }
 
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(8px); }
      to   { opacity: 1; transform: translateY(0); }
    }
 
    .msg.bot  { flex-direction: row; }
    .msg.user { flex-direction: row-reverse; }
 
    .msg-avatar {
     width: 28px;
     height: 28px;
     border-radius: 50%;
     overflow: hidden;
     background: white;
     display: flex;
     align-items: center;
     justify-content: center;
    }

    .msg-avatar img {
     width: 100%;
     height: 100%;
     object-fit: cover;
    }
 
    .bubble {
      max-width: 82%;
      padding: 10px 14px;
      border-radius: 16px;
      font-size: 14px;
      line-height: 1.55;
      color: var(--text-main);
    }
 
    .msg.bot  .bubble {
      background: var(--green-light);
      border-bottom-left-radius: 4px;
      color: var(--green-dark);
    }
 
    .msg.user .bubble {
      background: var(--green-mid);
      border-bottom-right-radius: 4px;
      color: var(--white);
    }
 
    .options-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      padding: 0 1rem 1rem;
    }
 
    .opt-btn {
      background: var(--white);
      border: 1.5px solid var(--green-accent);
      color: var(--green-mid);
      padding: 8px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-family: 'DM Sans', sans-serif;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.18s, color 0.18s, transform 0.1s;
      display: flex; align-items: center; gap: 6px;
    }
 
    .opt-btn:hover  { background: var(--green-accent); color: var(--white); transform: scale(1.03); }
    .opt-btn:active { transform: scale(0.97); }
 
    .opt-btn.danger             { border-color: #e07070; color: #b04040; }
    .opt-btn.danger:hover       { background: #e07070; color: var(--white); }
 
    .chat-footer {
      border-top: 1px solid #eef3ec;
      padding: 0.65rem 1rem 0.75rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }
 
    .chat-input {
      flex: 1;
      padding: 9px 14px;
      border-radius: 20px;
      border: 1.5px solid #c6e5d3;
      font-family: 'DM Sans', sans-serif;
      font-size: 13.5px;
      background: var(--cream);
      color: var(--text-main);
      outline: none;
      transition: border 0.18s;
    }
 
    .chat-input:focus       { border-color: var(--green-accent); }
    .chat-input::placeholder { color: var(--text-muted); }
 
    .send-btn {
      width: 36px; height: 36px;
      border-radius: 50%;
      background: var(--green-mid);
      border: none;
      cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: background 0.18s, transform 0.1s;
      flex-shrink: 0;
    }
 
    .send-btn:hover  { background: var(--green-dark); transform: scale(1.06); }
    .send-btn:active { transform: scale(0.94); }
    .send-btn svg    { width: 17px; height: 17px; fill: white; }
 
    .timestamp {
      font-size: 10px;
      color: var(--text-muted);
      text-align: center;
      margin: 2px 0 4px;
      letter-spacing: 0.2px;
    }
 
    .typing { display: flex; gap: 4px; align-items: center; padding: 4px 0; }
 
    .dot {
      width: 7px; height: 7px;
      background: var(--green-accent);
      border-radius: 50%;
      animation: bounce 1s infinite;
    }
 
    .dot:nth-child(2) { animation-delay: 0.15s; }
    .dot:nth-child(3) { animation-delay: 0.3s; }
 
    @keyframes bounce {
      0%, 80%, 100% { transform: translateY(0); }
      40%            { transform: translateY(-6px); }
    }
 
    .state-selector { display: flex; flex-wrap: wrap; gap: 6px; padding: 0.2rem 0; }
 
    .state-btn {
      background: var(--white);
      border: 1.5px solid #b7ddc7;
      color: var(--green-mid);
      padding: 5px 12px;
      border-radius: 14px;
      font-size: 12.5px;
      font-family: 'DM Sans', sans-serif;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }
 
    .state-btn:hover { background: var(--green-mid); color: white; }
  </style>
</head>
<body>
 
<div class="chatbot-wrap" role="main">
  <div class="chat-header">
    <div class="avatar">
     <img src="logo.png" alt="Logo">
     </div>

    <div class="header-info">
      <h2>Vida Verde Bot</h2>
      <span><span class="status-dot"></span> Online agora · Atendimento 24h</span>
    </div>
  </div>
 
  <div class="chat-body" id="chatBody"></div>
 
  <div class="options-grid" id="optionsGrid"></div>
 
  <div class="chat-footer">
    <input class="chat-input" id="chatInput" type="text" placeholder="Digite uma mensagem..." maxlength="120" />
    <button class="send-btn" id="sendBtn" aria-label="Enviar">
      <svg viewBox="0 0 24 24"><path d="M2 21L23 12 2 3v7l15 2-15 2z"/></svg>
    </button>
  </div>
</div>
 
<script>
  /* ── Base de Conhecimento ── */
  const KB = {
    pedido_minimo: {
      pr: 'R$ 500,00',
      sc: 'R$ 800,00',
      mg: 'R$ 900,00',
      sp: 'R$ 1.000,00',
      rj: 'R$ 1.500,00',
      rs: 'R$ 700,00',
      ba: 'R$ 850,00',
      go: 'R$ 950,00',
    },
    estados: {
      pr: 'Paraná',
      sc: 'Santa Catarina',
      mg: 'Minas Gerais',
      sp: 'São Paulo',
      rj: 'Rio de Janeiro',
      rs: 'Rio Grande do Sul',
      ba: 'Bahia',
      go: 'Goiás',
    },
    prazo: '15 a 20 dias após a a confirmação do pedido.',
    pagamento: ['Pix', 'Dinheiro', 'Cheque', 'Boleto Bancário'],
    boleto_dias: ['21 Dias', '25/40/55/80 Dias', '28/35/42 Dias', '28/35/42/49 Dias', '28/35/42/49/56/63 Dias', '28/42/56 Dias', '28/45/60 Dias', '28/56 Dias', '30 Dias', 
    '30/45 Dias', '30/45/60 Dias', '30/45/60/75 Dias', '30/45/60/75/90 Dias', '30/50/70 Dias', '30/50/70/90 Dias', '30/50/75 Dias', '30/60 Dias', '30/60/90 Dias', 
    '35/55/75 Dias', '45 Dias', 'A Vista'],
  };
 
  /* ── Elementos DOM ── */
  const body    = document.getElementById('chatBody');
  const opts    = document.getElementById('optionsGrid');
  const input   = document.getElementById('chatInput');
  const sendBtn = document.getElementById('sendBtn');
 
  let state = 'menu';
 
  /* ── Utilitários ── */
  function scrollBot() { body.scrollTop = body.scrollHeight; }
 
  function addMsg(text, from = 'bot', delay = 0) {
    return new Promise(res => {
      setTimeout(() => {
        const wrap = document.createElement('div');
        wrap.className = msg ${from};
 
        if (from === 'bot') {
         const av = document.createElement('div');
         av.className = 'msg-avatar';
         av.innerHTML = '<img src="logo.png" alt="Logo">';
         wrap.appendChild(av);
      }
 
        const b = document.createElement('div');
        b.className = 'bubble';
        b.innerHTML = text;
        wrap.appendChild(b);
        body.appendChild(wrap);
        scrollBot();
        res();
      }, delay);
    });
  }
 
  function addTimestamp(label = 'agora') {
    const t = document.createElement('div');
    t.className = 'timestamp';
    t.textContent = label;
    body.appendChild(t);
  }
 
  function showTyping() {
    const wrap = document.createElement('div');
    wrap.className = 'msg bot';
    wrap.id = 'typingIndicator';
    const av = document.createElement('div');
    av.className = 'msg-avatar';
    av.innerHTML = '<img src="logo.png" alt="Logo">';
    const b = document.createElement('div');
    b.className = 'bubble';
    b.innerHTML = '<div class="typing"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>';
    wrap.appendChild(av);
    wrap.appendChild(b);
    body.appendChild(wrap);
    scrollBot();
  }
 
  function removeTyping() {
    const el = document.getElementById('typingIndicator');
    if (el) el.remove();
  }
 
  function setOptions(items) {
    opts.innerHTML = '';
    items.forEach(item => {
      const btn = document.createElement('button');
      btn.className = 'opt-btn' + (item.danger ? ' danger' : '');
      btn.innerHTML = (item.icon ? item.icon + ' ' : '') + item.label;
      btn.onclick = () => item.action();
      opts.appendChild(btn);
    });
  }
 
  function clearOptions() { opts.innerHTML = ''; }
 
  async function botRespond(text, delay = 600) {
    showTyping();
    await new Promise(r => setTimeout(r, delay));
    removeTyping();
    await addMsg(text, 'bot');
  }
 
  /* ── Fluxos ── */
  async function showMenu() {
    state = 'menu';
    clearOptions();
    await botRespond('Como posso ajudar você hoje?', 300);
    setOptions([
      { icon: '📦', label: 'Pedido mínimo',        action: () => askEstado()     },
      { icon: '🚚', label: 'Prazo de entrega',      action: () => showPrazo()     },
      { icon: '💳', label: 'Formas de pagamento',   action: () => showPagamento() },
      { icon: '❌', label: 'Encerrar',              action: () => encerrar(), danger: true },
    ]);
  }
 
  async function askEstado() {
    state = 'estado';
    clearOptions();
    await addMsg('Pedido mínimo 📦', 'user');
    await botRespond('Claro! Selecione seu <strong>estado</strong> para consultar o pedido mínimo correspondente:', 700);
 
    const stateGrid = document.createElement('div');
    stateGrid.className = 'state-selector';
 
    Object.entries(KB.estados).forEach(([code, name]) => {
      const btn = document.createElement('button');
      btn.className = 'state-btn';
      btn.textContent = name;
      btn.onclick = () => showPedidoMinimo(code, name);
      stateGrid.appendChild(btn);
    });
 
    opts.appendChild(stateGrid);
 
    const back = document.createElement('button');
    back.className = 'opt-btn';
    back.innerHTML = '← Voltar';
    back.onclick = () => showMenu();
    opts.appendChild(back);
  }
 
  async function showPedidoMinimo(code, name) {
    clearOptions();
    await addMsg(name, 'user');
    const valor = KB.pedido_minimo[code];
    await botRespond(Para entregas em <strong>${name}</strong>, o pedido mínimo é de <strong>${valor}</strong>., 800);
    await botRespond('Posso ajudar com mais alguma coisa?', 400);
    setOptions([
      { icon: '🔙', label: 'Voltar ao menu', action: () => showMenu() },
      { icon: '❌', label: 'Encerrar',       action: () => encerrar(), danger: true },
    ]);
  }
 
  async function showPrazo() {
    clearOptions();
    await addMsg('Prazo de entrega 🚚', 'user');
    await botRespond(O prazo de entrega padrão é de <strong>${KB.prazo}</strong> após a confirmação do pedido., 800);
    await botRespond('Posso ajudar com mais alguma coisa?', 400);
    setOptions([
      { icon: '🔙', label: 'Voltar ao menu', action: () => showMenu() },
      { icon: '❌', label: 'Encerrar',       action: () => encerrar(), danger: true },
    ]);
  }
 
async function showPagamento() {
  clearOptions();
  await addMsg('Formas de pagamento 💳', 'user');

  await botRespond(Escolha uma forma de pagamento:, 800);

  setOptions([
    { label: 'Pix', action: () => pagamentoSelecionado('Pix') },
    { label: 'Dinheiro', action: () => pagamentoSelecionado('Dinheiro') },
    { label: 'Cheque', action: () => pagamentoSelecionado('Cheque') },
    { label: 'Boleto Bancário', action: () => escolherBoleto() },
    { label: '← Voltar', action: () => showMenu() }
  ]);
}
 
  async function encerrar() {
    clearOptions();
    await addMsg('Encerrar ❌', 'user');
    await botRespond('Obrigado por entrar em contato com a <strong>Vida Verde</strong>! 🌿<br>Se precisar de mais ajuda, estamos disponíveis 24h. Até logo!', 700);
    state = 'encerrado';
    setTimeout(() => {
      setOptions([{ icon: '🔄', label: 'Nova conversa', action: () => iniciar() }]);
    }, 1000);
  }
 
  /* ── Input livre ── */
  async function handleInput(text) {
    if (!text.trim()) return;
    input.value = '';
 
    if (state === 'encerrado') {
      await addMsg(text, 'user');
      await botRespond('A conversa foi encerrada. Clique em <strong>Nova conversa</strong> para recomeçar.', 500);
      return;
    }
 
    await addMsg(text, 'user');
 
    const t = text.toLowerCase();
    if (t.includes('prazo') || t.includes('entrega'))                           { clearOptions(); await showPrazo();     return; }
    if (t.includes('pagamento') || t.includes('pagar') || t.includes('pix') || t.includes('boleto')) { clearOptions(); await showPagamento(); return; }
    if (t.includes('pedido') || t.includes('minimo') || t.includes('mínimo') || t.includes('valor')) { clearOptions(); await askEstado();     return; }
    if (t.includes('sair') || t.includes('tchau') || t.includes('encerrar') || t.includes('obrigado')) { clearOptions(); await encerrar();    return; }
 
    await botRespond('Entendi! Para te ajudar melhor, use as opções abaixo:', 600);
    if (state === 'menu') showMenu();
  }
 async function escolherBoleto() {
  clearOptions();
  await addMsg('Boleto Bancário', 'user');
  await botRespond('Em quantos dias você deseja o vencimento do boleto?', 600);

  setOptions(
    KB.boleto_dias.map(dia => ({
      label: dia,
      action: () => confirmarBoleto(dia)
    }))
  );
}

async function confirmarBoleto(dia) {
  clearOptions();
  await addMsg(dia, 'user');
  await botRespond(Perfeito! O boleto será emitido com vencimento em <strong>${dia}</strong>., 700);
  await botRespond('Posso ajudar com mais alguma coisa?', 400);

  setOptions([
    { label: '🔙 Voltar ao menu', action: () => showMenu() },
    { label: '❌ Encerrar', action: () => encerrar(), danger: true }
  ]);
}

async function pagamentoSelecionado(tipo) {
  clearOptions();
  await addMsg(tipo, 'user');
  await botRespond(Você escolheu <strong>${tipo}</strong> como forma de pagamento., 600);
  await botRespond('Posso ajudar com mais alguma coisa?', 400);

  setOptions([
    { label: '🔙 Voltar ao menu', action: () => showMenu() },
    { label: '❌ Encerrar', action: () => encerrar(), danger: true }
  ]);
}

  /* ── Inicialização ── */
  async function iniciar() {
    body.innerHTML = '';
    clearOptions();
    state = 'menu';
    addTimestamp('hoje');
    await addMsg('Olá! 👋 Seja bem-vindo ao atendimento da <strong>Vida Verde</strong>.<br>Sou o seu assistente virtual e estou aqui para ajudar!', 'bot');
    await showMenu();
  }
 
  input.addEventListener('keydown', e => { if (e.key === 'Enter') handleInput(input.value); });
  sendBtn.addEventListener('click', () => handleInput(input.value));
 
  iniciar();
</script>
 
</body>
</html>