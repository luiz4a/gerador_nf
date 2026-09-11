import json
import qrcode
from datetime import datetime
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

ARQUIVO = "banco.json"

# Criar banco se não existir
if not Path(ARQUIVO).exists():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump([], f)

# Carregar banco
with open(ARQUIVO, "r", encoding="utf-8") as f:
    notas = json.load(f)

numero_nf = len(notas) + 1

print("\n=== GERADOR DE NOTA FISCAL ===\n")

cliente = input("Nome do Cliente: ")
cpf = input("CPF/CNPJ: ")

produtos = []
total = 0

while True:

    produto = input("\nProduto: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(
        input("Valor Unitário: ").replace(",", ".")
    )

    subtotal = quantidade * valor_unitario

    produtos.append({
        "nome": produto,
        "qtd": quantidade,
        "valor": valor_unitario,
        "subtotal": subtotal
    })

    total += subtotal

    continuar = input(
        "\nAdicionar outro produto? (S/N): "
    ).upper()

    if continuar != "S":
        break

nota = {
    "numero": numero_nf,
    "cliente": cliente,
    "cpf": cpf,
    "produtos": produtos,
    "total": total,
    "data": datetime.now().strftime("%d/%m/%Y")
}

# Salva nota
notas.append(nota)

with open(ARQUIVO, "w", encoding="utf-8") as f:
    json.dump(
        notas,
        f,
        indent=4,
        ensure_ascii=False
    )

arquivo_pdf = f"NF_{numero_nf:06}.pdf"
arquivo_qr = f"QR_NF_{numero_nf:06}.png"

# Dados QR
dados_qr = (
    f"NF: {numero_nf:06}\n"
    f"Cliente: {cliente}\n"
    f"CPF/CNPJ: {cpf}\n"
    f"Total: R$ {total:.2f}"
)

img = qrcode.make(dados_qr)
img.save(arquivo_qr)

# PDF
pdf = canvas.Canvas(
    arquivo_pdf,
    pagesize=A4
)

pdf.setTitle(
    f"NF_{numero_nf:06}"
)

# Moldura
pdf.rect(
    20,
    20,
    555,
    800
)

# Cabeçalho
pdf.setFont(
    "Helvetica-Bold",
    18
)

pdf.drawCentredString(
    297,
    810,
    "NFC-e"
)

pdf.setFont(
    "Helvetica",
    10
)

pdf.drawCentredString(
    297,
    790,
    "Documento Auxiliar da Nota Fiscal"
)

pdf.line(
    30,
    770,
    565,
    770
)

# Cliente
pdf.setFont(
    "Helvetica-Bold",
    12
)

pdf.drawString(
    40,
    740,
    "CONSUMIDOR"
)

pdf.setFont(
    "Helvetica",
    10
)

pdf.drawString(
    40,
    720,
    f"Cliente: {cliente}"
)

pdf.drawString(
    40,
    705,
    f"CPF/CNPJ: {cpf}"
)

# Tabela
pdf.line(
    30,
    680,
    565,
    680
)

pdf.setFont(
    "Helvetica-Bold",
    10
)

pdf.drawString(40, 660, "ITEM")
pdf.drawString(80, 660, "DESCRIÇÃO")
pdf.drawString(300, 660, "QTD")
pdf.drawString(380, 660, "VL.UN")
pdf.drawString(470, 660, "TOTAL")

y = 640

pdf.setFont(
    "Helvetica",
    9
)

for i, item in enumerate(produtos, start=1):

    pdf.drawString(
        40,
        y,
        str(i)
    )

    pdf.drawString(
        80,
        y,
        item["nome"][:30]
    )

    pdf.drawString(
        300,
        y,
        str(item["qtd"])
    )

    pdf.drawString(
        380,
        y,
        f"{item['valor']:.2f}"
    )

    pdf.drawString(
        470,
        y,
        f"{item['subtotal']:.2f}"
    )

    y -= 20

# Total
pdf.line(
    30,
    y,
    565,
    y
)

y -= 30

pdf.setFont(
    "Helvetica-Bold",
    12
)

pdf.drawString(
    330,
    y,
    f"TOTAL: R$ {total:.2f}"
)

y -= 30

pdf.setFont(
    "Helvetica",
    10
)

pdf.drawString(
    40,
    y,
    f"Data de Emissão: {nota['data']}"
)

pdf.drawString(
    320,
    y,
    f"NF: {numero_nf:06}"
)

# QR abaixo dos produtos
y -= 180

pdf.drawImage(
    arquivo_qr,
    220,
    y,
    width=130,
    height=130
)

pdf.drawCentredString(
    285,
    y - 15,
    "Consulte esta nota via QR Code"
)

pdf.save()

print("\n✅ Nota emitida com sucesso!")
print(f"PDF: {arquivo_pdf}")
print(f"QR Code: {arquivo_qr}")