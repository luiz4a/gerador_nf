# gerador_nf
codigo que gera nota fiscal e seus qr codes (notas meramente ilustrativas ) 

# Instalação do Python e Dependências

## 1. Verificar se o Python está instalado

Abra o terminal (CMD ou PowerShell) e execute:

```bash
python --version
```

Se aparecer algo semelhante a:

```text
Python 3.13.7
```

o Python já está instalado.

Caso não esteja instalado:

1. Acesse:
   https://www.python.org/downloads/

2. Baixe a versão mais recente do Python.

3. Durante a instalação marque:

```text
✅ Add Python to PATH
```

4. Conclua a instalação e reinicie o terminal.

---

## 2. Verificar o gerenciador de pacotes

Execute:

```bash
python -m pip --version
```

Se aparecer a versão do pip, prossiga para a instalação das dependências.

---

## 3. Instalar as dependências do projeto

### Instalar ReportLab (geração de PDFs)

```bash
python -m pip install reportlab
```

### Instalar QRCode (geração de QR Code)

```bash
python -m pip install qrcode
```

### Instalar Pillow (tratamento de imagens)

```bash
python -m pip install pillow
```

---

## 4. Instalar todas as dependências de uma única vez

```bash
python -m pip install reportlab qrcode pillow
```

---

## 5. Verificar se as bibliotecas foram instaladas corretamente

Listar bibliotecas instaladas:

```bash
python -m pip list
```

Verificar individualmente:

```bash
python -m pip show reportlab
```

```bash
python -m pip show qrcode
```

```bash
python -m pip show pillow
```

---

## 6. Executar o projeto

Acesse a pasta do projeto:

```bash
cd caminho/do/projeto
```

Execute:

```bash
python gerador-nf-completa.py
```

---

## Bibliotecas Utilizadas

### reportlab
Responsável pela geração de arquivos PDF.

```python
from reportlab.pdfgen import canvas
```

### reportlab.platypus
Responsável pela criação de tabelas e elementos avançados do PDF.

```python
from reportlab.platypus import Table, TableStyle
```

### qrcode
Responsável pela geração do QR Code da nota.

```python
import qrcode
```

### pillow
Biblioteca utilizada internamente para manipulação das imagens do QR Code.

```python
python -m pip install pillow
```

---

## Dependências Nativas do Python

As bibliotecas abaixo já vêm instaladas com o Python e não precisam de instalação:

```python
import json
from datetime import datetime
from pathlib import Path
```

---

## Comando Completo de Instalação

```bash
python -m pip install reportlab qrcode pillow
```

## Comando Completo para Executar

```bash
python gerador-nf-completa.py
```

