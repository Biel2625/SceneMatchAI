# SceneMatchAI

SceneMatchAI é uma aplicação web que transforma roteiros em vídeos incríveis automaticamente, utilizando inteligência artificial para análise de cenas e envio de resultados.

## Demonstração

Acesse a versão online: [https://scenematchai.onrender.com](https://scenematchai.onrender.com)

## Funcionalidades

- Upload de roteiros (.txt)
- Processamento automático do conteúdo
- Visualização, download e exclusão de arquivos processados
- Painel com login protegido
- Envio automático por e-mail (em breve)

## Tecnologias Utilizadas

- Python 3.11
- Flask
- Jinja2
- Gunicorn
- HTML/CSS (puro)
- Deploy: Render.com
- Versionamento: GitHub

## Instalação Local

```bash
git clone https://github.com/SEU_USUARIO/SceneMatchAI.git
cd SceneMatchAI
pip install -r requirements.txt
python server.py


Acesse no navegador: http://127.0.0.1:5000


Estrutura do Projeto
csharp
Copiar
Editar
SceneMatchAI/
│
├── static/                # Arquivos CSS
├── templates/             # HTML (login, dashboard, upload, etc.)
├── uploads/               # Arquivos enviados
├── processados/           # Arquivos gerados
│
├── server.py              # Servidor Flask principal
├── processar_roteiro.py   # Lógica de processamento
├── enviar_email.py        # (em breve) envio de resultados
├── requirements.txt       # Dependências
├── README.md              # Este arquivo


**Desenvolvido com dedicação por Gabriel Martins Da Silva.**