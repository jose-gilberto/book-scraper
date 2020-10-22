# Desafio Data Engineering

## Contexto:

A Book Club é uma Startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários, cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele não queira oferecer outro livro em troca.

Umas das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Você é um Data Scientist contrato pela empresa para construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários. Porém, a Book Club não coleta e nem armazena os livros enviados pelos usuários.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

- Nome do livro
- Categoria do livro
- Número de estrelas que o livro recebeu
- Preço do livro
- Se o livro está em estoque ou não

## Dados do desafio:

Os dados para serem coletados e armazenados, estão disponíveis neste site. http://books.toscrape.com/

Esse site foi desenvolvido e disponibilizado especialmente para praticar web scraping. Não existe nenhum tipo de problema legal ao fazer a coleta de dados.

## Solução:

- [ ] Criar um web scraper, usando Python.
- [ ] Utilizar o selenium para navegar entre as categorias e páginas.
- [ ] Utilizar a biblioteca BeautifulSoup do Python para coletar os dados.
- [ ] Configurar um banco de dados postgres.
- [ ] Agendar um script para rodar todos os dias no mesmo horário. (Não tem problema armazenar dados repetidos).
- [ ] Garantir que o script lide com erros e não pare de funcionar por qualquer problema (internet lenta, página não encontrada, objeto não carregado, etc).

## Extras:
- [ ] Modularizar a solução.
  - Script -> scraper -> csv
  - Script -> load_db -> csv -> postgres
- [ ] Sincronizar os dois scripts.
- [ ] Gerenciamento de jobs usando Airflow. Um script só pode rodar quando o outro terminar.
- [ ] Paralelizar o script de coleta, cada um coleta e armazena dados de uma página.
