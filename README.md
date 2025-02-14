# API_FLASK_Websockets# Payment API

A **Payment API** é uma aplicação backend desenvolvida em Python com o framework Flask. Ela permite a criação e confirmação de pagamentos via Pix, utilizando WebSockets para notificações em tempo real.

## Funcionalidades

### Pagamentos via Pix
- Criação de pagamentos Pix com QR Code.
- Confirmação de pagamento.
- Recuperação de imagens de QR Code.
- WebSockets para atualização em tempo real.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para desenvolvimento da API.
- **Flask-SQLAlchemy**: Integração com banco de dados.
- **Flask-SocketIO**: Implementação de WebSockets.
- **SQLite**: Banco de dados utilizado para armazenar os pagamentos.
- **QR Code**: Geração de QR Codes para pagamentos.

## Estrutura do Projeto

```
/payment-api
  /repository
    - database.py      # Configuração do SQLAlchemy
  /db_models
    - payment.py       # Modelo de dados para pagamentos
  /payments
    - pix.py           # Lógica para criação de pagamentos Pix
  - app.py             # Aplicação Flask (rotas e lógica)
  - requirements.txt   # Dependências do projeto
  - README.md          # Documentação do projeto
```

## Como Executar o Projeto

### Pré-requisitos

- **Python 3.x**: Para executar a aplicação Flask.
- **Pip**: Para instalar as dependências.

### Passos para Execução

#### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

#### 2. Executar a Aplicação
```bash
python app.py
```
A API estará disponível em `http://localhost:5000`.

## Rotas da API

### Criar Pagamento via Pix

#### **POST /payments/pix**
Cria um novo pagamento via Pix.

**Body (JSON):**
```json
{
  "value": 100.50
}
```
**Resposta:**
```json
{
  "message": "The payment has been created",
  "payment": {
    "id": 1,
    "value": 100.50,
    "paid": false,
    "bank_payment_id": "abc123",
    "qr_code": "qr_code_payment_abc123",
    "expiration_date": "2023-10-01T12:30:00"
  }
}
```

### Obter QR Code do Pagamento

#### **GET /payments/pix/qr_code/<file_name>**
Retorna a imagem do QR Code correspondente ao pagamento.

**Exemplo de Uso:**
```bash
GET /payments/pix/qr_code/qr_code_payment_abc123
```

### Confirmar Pagamento

#### **POST /payments/pix/confirmation**
Confirma um pagamento via Pix.

**Body (JSON):**
```json
{
  "bank_payment_id": "abc123",
  "value": 100.50
}
```
**Resposta:**
```json
{
  "message": "The payment has been confirmed"
}
```

### Obter Status do Pagamento

#### **GET /payments/pix/<int:payment_id>**
Retorna o status do pagamento e a página correspondente.

**Exemplo de Uso:**
```bash
GET /payments/pix/1
```

## WebSockets

A API utiliza WebSockets para notificar clientes sobre confirmação de pagamento.

### Eventos:
- **Conexão:** `connect`
- **Desconexão:** `disconnect`
- **Confirmação de Pagamento:** `payment-confirmed=<payment_id>`

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um **fork** do projeto.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona nova feature'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um **Pull Request**.

## Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](./LICENSE) para mais informações.

