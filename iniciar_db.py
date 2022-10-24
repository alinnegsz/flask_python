import sqlite3

conexao = sqlite3.connect('blog.db')

with open('exemplo_flask/schema.sql') as f:
    conexao.executescript(f.read())

cur = conexao.cursor()

cur.execute("INSERT INTO posts (titulo, conteudo, frase, link_imagem) VALUES (?, ?, ?, ?)", ('Anne da Ilha', 'Decidida a realizar o seu sonho, Anne se muda para Kingsport e vai morar com sua amiga Priscilla Grant para finalmente terminar os seus estudos em Redmond College. Gilbert Blythe, desejando estudar medicina, também parte para Kingsport e enxerga a oportunidade de revelar seus sentimentos a Anne. O novo ambiente e a vida adulta trazem novos desafios e perdas que mudam as perspectivas e amadurecem a forma como ela enxerga o mundo.', 'As pessoas não podem se dar bem nesse mundo sem uma pitadinha de amor.', 'https://m.media-amazon.com/images/I/51XbXhlDyHL.jpg'))
cur.execute("INSERT INTO posts (titulo, conteudo, frase, link_imagem) VALUES (?, ?, ?, ?)", ('Flores para Algernon', 'Decidida a realizar o seu sonho, Anne se muda para Kingsport e vai morar com sua amiga Priscilla Grant para finalmente terminar os seus estudos em Redmond College.', 'esafios e perdas que mudam as perspectivas', 'https://m.media-amazon.com/images/I/51XbXhlDyHL.jpg'))
cur.execute("INSERT INTO posts (titulo, conteudo, frase, link_imagem) VALUES (?, ?, ?, ?)", ('O morro dos ventos uivantes', 'Decidida a realizar o seu sonho, Anne se muda para Kingsport e vai morar com sua amiga Priscilla Grant para finalmente terminar os seus estudos em Redmond College.', 'esafios e perdas que mudam as perspectivas', 'https://m.media-amazon.com/images/I/51XbXhlDyHL.jpg'))

conexao.commit()
conexao.close()
