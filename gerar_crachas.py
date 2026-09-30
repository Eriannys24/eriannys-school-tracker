import json
impor qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# 1. Configurções e Pastas 
ARQUIVO_JSON = 'data/alunos.json'
PASTA_SAIDA = 'crachas_impressao'

if not os.path.exists(PASTA_SAIDA):
  os.makedirs(PASTA_SAIDA)

def gerar_cachas():
  try:
    with open(ARQUIVO_JSON,'r', encoding='utf-8') as f:
      alunos = json.load(f)
      execpt FileNotFoundError:
      print("Erro: Arquivo alunos.json não encontrado!")
      return

for aluno in alunos:
  nome = aluno['nome']
  turma = aluno['turma]
  tag = aluno['tag']

  print(f"Gerando crachápara: {nome}...")
  # 2. Criar o QR code
  qr = qrcode.QRCode(version=1, box_size=10, border=4)
  qr.add_data(tag)
  qr.make(fit=True)
  img_qr = qr.mke_image(fill_color="black", back_color="white").convert('RGB')

  # 3. Criar o fundo do Crachá (mais largo que o QR para caber o texto)
  largura_qr, altura_qr = img_qr.size
  altur_total = altura_qr + 100
  cracha = image.new('RGB', (largura_qr, altura_total), color='white')

  # Colar o QR Code no topo 
  cracha.paste(img_qr, (0, 0))

  # 4. Escrever o Nome e Turma (Texto centralizado)
  draw = ImageDraw.Draw(cracha)
  # Tenta carregar u,a fonte, se não tiver, usa a padrão
  try:
      fonte_nome = 
