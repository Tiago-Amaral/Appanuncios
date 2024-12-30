# Projeto em Python Utilizando a Biblioteca FastAPI

## Descrição do Projeto

Este projeto foi desenvolvido com o objetivo de **estudar e aprimorar conhecimentos em Python no contexto de Backend**, utilizando a biblioteca **FastAPI** e o banco de dados **SQL**. Ele inclui funcionalidades básicas de manipulação de produtos no banco de dados, como:

- Cadastrar um produto.
- Listar todos os produtos cadastrados.
- Buscar e editar produtos a partir do **ID**.
- Deletar produtos utilizando o **ID**.

Embora seja um projeto em evolução, ele representa um bom ponto de partida para consolidar conhecimentos em backend.

---

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção de APIs rápidas e modernas.
- **SQLAlchemy**: Biblioteca para interação com bancos de dados SQL.
- **SQLite**: Banco de dados utilizado durante o desenvolvimento.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.

---

## Como Executar o Projeto

1. **Clonar o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. **Criar um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows, use venv\Scripts\activate
   ```

3. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o servidor**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Acessar a documentação interativa**:
   - Abra o navegador e acesse: `http://127.0.0.1:8000/docs`

---

## Funcionalidades

### 1. Cadastrar um Produto
- **Endpoint**: `POST /produtos`
- **Descrição**: Permite cadastrar um novo produto no banco de dados.
- **Exemplo de Payload**:
  ```json
  {
    "nome": "Produto Exemplo",
    "descricao": "Uma descrição simples",
    "preco": 100.0
  }
  ```

### 2. Listar Produtos
- **Endpoint**: `GET /produtos`
- **Descrição**: Retorna todos os produtos cadastrados.

### 3. Buscar Produto pelo ID
- **Endpoint**: `GET /produtos/{id}`
- **Descrição**: Retorna os detalhes de um produto específico.

### 4. Editar Produto pelo ID
- **Endpoint**: `PUT /produtos/{id}`
- **Descrição**: Atualiza as informações de um produto.
- **Exemplo de Payload**:
  ```json
  {
    "nome": "Produto Atualizado",
    "descricao": "Nova descrição",
    "preco": 150.0
  }
  ```

### 5. Deletar Produto pelo ID
- **Endpoint**: `DELETE /produtos/{id}`
- **Descrição**: Remove um produto do banco de dados.

---

## Estrutura do Projeto
```
/
|-- app/
|   |-- main.py          # Ponto de entrada da aplicação
|   |-- models.py        # Definição das tabelas do banco de dados
|   |-- schemas.py       # Estruturas para validação de dados
|   |-- database.py      # Conexão com o banco de dados
|   |-- routes/
|       |-- produtos.py  # Rotas relacionadas aos produtos
|-- requirements.txt     # Dependências do projeto
```

---

## Melhorias Futuras

- Implementar autenticação e autorização.
- Adicionar testes unitários para os endpoints.
- Substituir o SQLite por um banco de dados mais robusto, como PostgreSQL.
- Criar um sistema de paginação para a listagem de produtos.
- Desenvolver uma interface frontend para interagir com a API.

---

## Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests. Qualquer feedback ou sugestão será muito bem-vinda!

---

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

