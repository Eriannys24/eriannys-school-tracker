function calcularMinutosFora(isoString) {
  const saida = new Date(isoString);
  const agora = new Date();
  const diff = Math.floor((agora - saida) /  60000); // converte ms para minutos
return diff;
}

function renderizarDashboard(movimentacoes) {
  const grid = document.getElementById('grid-alunos');
  grid.innerHTML = ''; // Limpa para atualizar

movimentacoes.forEach(m => {
  if (m.status === 'em_andamento') {
    const minutos = calcularMinutosFora(m.data_hora_saida);
    const isCritical = minutos > 10; // Regra de Negocio; 10 minutos 

  const card = `
    <div class="student-card ${isCritical ? 'critical' : ''}">
    <span class="name">${m.nome}</span>
    <span class="location">Destino: ${m.local_destino}</span>
    <span class="time-elapsed">${minutos} min fora</span>
    </div>
    `;
    grid.innerHTML += card;
  }
});
}
