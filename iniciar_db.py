#coding=utf8
import sqlite3

conexao = sqlite3.connect('blog.db')

with open('schema.sql') as f:
    conexao.executescript(f.read())

cur = conexao.cursor()

cur.execute("INSERT INTO posts (titulo, conteudo, frase, link_imagem, autor) VALUES (?, ?, ?, ?, ?)", ('Anne de Green Gables', 'Quando os irmãos Marilla e Matthew Cuthbert, de Green Gables, na Prince Edward Island, no Canadá, decidem adotar um órfão para ajudá-los nos trabalhos da fazenda, não estão preparados para o “erro” que mudará suas vidas: Anne Shirley, uma menina ruiva de 11 anos, acaba sendo enviada, por engano, pelo orfanato.', 'Não é o que o mundo reserva para você, mas o que você traz para o mundo.', 'https://m.media-amazon.com/images/I/51wmbuhRAaL._SX331_BO1,204,203,200_.jpg', 'Lucy Maud Montgomery'))
cur.execute("INSERT INTO posts (titulo, conteudo, frase, link_imagem, autor) VALUES (?, ?, ?, ?, ?)", ('Flores para Algernon', 'Com excesso de erros no início do romance, os relatos de Charlie revelam sua condição limitada, consequência de uma grave deficiência intelectual, que ao menos o mantém protegido dentro de um “mundo” particular – indiferente às gozações dos colegas de trabalho e intocado por tragédias familiares. Porém, ao participar de uma cirurgia revolucionária que aumenta o seu QI, ele não apenas se torna mais inteligente que os próprios médicos que o operaram, como também vira testemunha de uma nova realidade: ácida, crua e problemática. Se o conhecimento é uma benção, Daniel Keyes constrói um personagem complexo e intrigante, que questiona essa sorte e reflete sobre suas relações sociais e a própria existência. E tudo isso ao lado de Algernon, seu rato de estimação e a primeira cobaia bem-sucedida no processo cirúrgico.', 'Inteligência e educação sem doses de afeto humano não valem droga nenhuma.', 'https://m.media-amazon.com/images/I/41tpztfvPML._SY344_BO1,204,203,200_QL70_ML2_.jpg', 'Daniel Keyes'))
cur.execute("INSERT INTO posts (titulo, conteudo, frase, link_imagem, autor) VALUES (?, ?, ?, ?, ?)", ('O morro dos ventos uivantes', 'Único romance da escritora inglesa Emily Bronte, O morro dos ventos uivantes retrata uma trágica historia de amor e obsessão em que os personagens principais são a obstinada e geniosa Catherine Earnshaw e seu irmão adotivo, Heathcliff. Grosseiro, humilhado e rejeitado, ele guarda apenas rancor no coração, mas tem com Catherine um relacionamento marcado por amor e, ao mesmo tempo, ódio.', 'Há, ou deveria haver, uma existência sua além de você mesmo.', 'https://m.media-amazon.com/images/I/51sz0nn7u9L._SY344_BO1,204,203,200_QL70_ML2_.jpg', 'Emily Bronte'))

conexao.commit()
conexao.close()
