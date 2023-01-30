# Desafio 2 (Leitor de CNAB)

Este projeto foca em receber arquivos do tipo CNAB decodifica-los, guardas suas informaçoes em um banco de dados
e devolver o total de cada loja e suas respectivas transaçoes.
O Arquivo CNAB pode ser enviador por meio de uma interface em HTML e a API para decodificaçao é toda feita em Python 3.11.0, utilizando junto a ele o DJANGO rest_framework.
Temos apenas uma rota POST para envio dos arquivos CNAB, a rota faz todo uma análise dos dados e retorna um relatório de cada loja com o seu total junto das transaçoes feitas por
aquela loja.

ROTA POST: URL = /api/operations/
body: Array de strings, exemplo: {
	"data": ["3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       ","5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ", "3201903010000012200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA","2201903010000011200096206760173648****0099234234JOÃO MACEDO   BAR DO JOÃO       ","1201903010000015200096206760171234****7890233000JOÃO MACEDO   BAR DO JOÃO       ","2201903010000010700845152540738723****9987123333MARCOS PEREIRAMERCADO DA AVENIDA","2201903010000050200845152540738473****1231231233MARCOS PEREIRAMERCADO DA AVENIDA",
"3201903010000060200232702980566777****1313172712JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"1201903010000020000556418150631234****3324090002MARIA JOSEFINALOJA DO Ó - MATRIZ"
,"5201903010000080200845152540733123****7687145607MARCOS PEREIRAMERCADO DA AVENIDA"
,"2201903010000010200232702980568473****1231231233JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"3201903010000610200232702980566777****1313172712JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"4201903010000015232556418150631234****6678100000MARIA JOSEFINALOJA DO Ó - FILIAL"
,"8201903010000010203845152540732344****1222123222MARCOS PEREIRAMERCADO DA AVENIDA"
,"3201903010000010300232702980566777****1313172712JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"9201903010000010200556418150636228****9090000000MARIA JOSEFINALOJA DO Ó - MATRIZ"
,"4201906010000050617845152540731234****2231100000MARCOS PEREIRAMERCADO DA AVENIDA" 
,"2201903010000010900232702980568723****9987123333JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"8201903010000000200845152540732344****1222123222MARCOS PEREIRAMERCADO DA AVENIDA" 
,"2201903010000000500232702980567677****8778141808JOSÉ COSTA    MERCEARIA 3 IRMÃOS" 
,"3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA"]
}

Retorno esperado: Status 200 OK
body: [
	{
		"Name": "BAR DO JOÃO",
		"Owner": "JOÃO MACEDO",
		"Total": "R$13938.0",
		"Transactions": [
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$14200,00",
				"CPF": "096.206.760-17",
				"Card": "4753****3153",
				"Time": "15:34:53",
				"Owner": "JOÃO MACEDO",
				"Shop_name": "BAR DO JOÃO"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$11200,00",
				"CPF": "096.206.760-17",
				"Card": "3648****0099",
				"Time": "23:42:34",
				"Owner": "JOÃO MACEDO",
				"Shop_name": "BAR DO JOÃO"
			},
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$15200,00",
				"CPF": "096.206.760-17",
				"Card": "1234****7890",
				"Time": "23:30:00",
				"Owner": "JOÃO MACEDO",
				"Shop_name": "BAR DO JOÃO"
			}
		]
	},
	{
		"Name": "LOJA DO Ó - MATRIZ",
		"Owner": "MARIA JOSEFINA",
		"Total": "R$-8068.0",
		"Transactions": [
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$13200,00",
				"CPF": "556.418.150-63",
				"Card": "3123****7687",
				"Time": "14:56:07",
				"Owner": "MARIA JOSEFINA",
				"Shop_name": "LOJA DO Ó - MATRIZ"
			},
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$20000,00",
				"CPF": "556.418.150-63",
				"Card": "1234****3324",
				"Time": "09:00:02",
				"Owner": "MARIA JOSEFINA",
				"Shop_name": "LOJA DO Ó - MATRIZ"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$10200,00",
				"CPF": "556.418.150-63",
				"Card": "6228****9090",
				"Time": "00:00:00",
				"Owner": "MARIA JOSEFINA",
				"Shop_name": "LOJA DO Ó - MATRIZ"
			}
		]
	},
	{
		"Name": "MERCADO DA AVENIDA",
		"Owner": "MARCOS PEREIRA",
		"Total": "R$-18657.0",
		"Transactions": [
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$12200,00",
				"CPF": "845.152.540-73",
				"Card": "6777****1313",
				"Time": "17:27:12",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$10700,00",
				"CPF": "845.152.540-73",
				"Card": "8723****9987",
				"Time": "12:33:33",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$50200,00",
				"CPF": "845.152.540-73",
				"Card": "8473****1231",
				"Time": "23:12:33",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$80200,00",
				"CPF": "845.152.540-73",
				"Card": "3123****7687",
				"Time": "14:56:07",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$10203,00",
				"CPF": "845.152.540-73",
				"Card": "2344****1222",
				"Time": "12:32:22",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Entrada",
				"Data": "01/06/2019",
				"Value": "R$50617,00",
				"CPF": "845.152.540-73",
				"Card": "1234****2231",
				"Time": "10:00:00",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$200,00",
				"CPF": "845.152.540-73",
				"Card": "2344****1222",
				"Time": "12:32:22",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$19200,00",
				"CPF": "845.152.540-73",
				"Card": "6777****1313",
				"Time": "17:27:12",
				"Owner": "MARCOS PEREIRA",
				"Shop_name": "MERCADO DA AVENIDA"
			}
		]
	},
	{
		"Name": "MERCEARIA 3 IRMÃOS",
		"Owner": "JOSÉ COSTA",
		"Total": "R$-2304.0",
		"Transactions": [
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$60200,00",
				"CPF": "232.702.980-56",
				"Card": "6777****1313",
				"Time": "17:27:12",
				"Owner": "JOSÉ COSTA",
				"Shop_name": "MERCEARIA 3 IRMÃOS"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$10200,00",
				"CPF": "232.702.980-56",
				"Card": "8473****1231",
				"Time": "23:12:33",
				"Owner": "JOSÉ COSTA",
				"Shop_name": "MERCEARIA 3 IRMÃOS"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$610200,00",
				"CPF": "232.702.980-56",
				"Card": "6777****1313",
				"Time": "17:27:12",
				"Owner": "JOSÉ COSTA",
				"Shop_name": "MERCEARIA 3 IRMÃOS"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$10300,00",
				"CPF": "232.702.980-56",
				"Card": "6777****1313",
				"Time": "17:27:12",
				"Owner": "JOSÉ COSTA",
				"Shop_name": "MERCEARIA 3 IRMÃOS"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$10900,00",
				"CPF": "232.702.980-56",
				"Card": "8723****9987",
				"Time": "12:33:33",
				"Owner": "JOSÉ COSTA",
				"Shop_name": "MERCEARIA 3 IRMÃOS"
			},
			{
				"Transaction_type": "Saída",
				"Data": "01/03/2019",
				"Value": "R$500,00",
				"CPF": "232.702.980-56",
				"Card": "7677****8778",
				"Time": "14:18:08",
				"Owner": "JOSÉ COSTA",
				"Shop_name": "MERCEARIA 3 IRMÃOS"
			}
		]
	},
	{
		"Name": "LOJA DO Ó - FILIAL",
		"Owner": "MARIA JOSEFINA",
		"Total": "R$15232.0",
		"Transactions": [
			{
				"Transaction_type": "Entrada",
				"Data": "01/03/2019",
				"Value": "R$15232,00",
				"CPF": "556.418.150-63",
				"Card": "1234****6678",
				"Time": "10:00:00",
				"Owner": "MARIA JOSEFINA",
				"Shop_name": "LOJA DO Ó - FILIAL"
			}
		]
	}
]



Para instalar a aplicação siga o passo a passo:

1- De o git clone em uma pasta na sua máquina;

2- Utilize o comando pip install -r requirements.txt

3- Após a instalação das dependencias crie seu .env e preencha com suas informaçoes

4- Utilize o python manage.py makemigrations e o migrate para fazer as migrations localmente

5- Para iniciar a aplicação localmente utilize o python manage.py runserver

6- Caso queira iniciar em ambiente de desenvolvimento, após colocar suas informaçoes no .env, utilize o docker-compose up para iniciar com o docker e poder testar usando um database PostgresSQL


**AVISO PARA KENZIE**

Minha interface HTML está dando um erro de CORS, não entendi o erro e procurei bastante sobre na internet, infelizmente não consegui achar nada a respeito.
Fiz dentro do JS para ele decodificar o CNAB e fazer um array onde cada elemento é uma linha do CNAB, na ideia inicial ele enviaria esse array com as strings do CNAB para
a API que iria tratar todo esse array e devolveria as informaçoes em questao, como ocorreu esse erro do CORS, no html apenas fiz ele retornar o array, entao caso queira testar
com um arquivo CNAB seu, envie no HTML e copie e cole no insomnia, caso queira testar a aplicaçao sem usar a interface aqui vai um array que usei pra testar.

P.S: Mesmo com o docker funcionando o erro continua acontecendo não sei se é um problema na minha máquina.

{
	"data": ["3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       ","5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ", "3201903010000012200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA","2201903010000011200096206760173648****0099234234JOÃO MACEDO   BAR DO JOÃO       ","1201903010000015200096206760171234****7890233000JOÃO MACEDO   BAR DO JOÃO       ","2201903010000010700845152540738723****9987123333MARCOS PEREIRAMERCADO DA AVENIDA","2201903010000050200845152540738473****1231231233MARCOS PEREIRAMERCADO DA AVENIDA",
"3201903010000060200232702980566777****1313172712JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"1201903010000020000556418150631234****3324090002MARIA JOSEFINALOJA DO Ó - MATRIZ"
,"5201903010000080200845152540733123****7687145607MARCOS PEREIRAMERCADO DA AVENIDA"
,"2201903010000010200232702980568473****1231231233JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"3201903010000610200232702980566777****1313172712JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"4201903010000015232556418150631234****6678100000MARIA JOSEFINALOJA DO Ó - FILIAL"
,"8201903010000010203845152540732344****1222123222MARCOS PEREIRAMERCADO DA AVENIDA"
,"3201903010000010300232702980566777****1313172712JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"9201903010000010200556418150636228****9090000000MARIA JOSEFINALOJA DO Ó - MATRIZ"
,"4201906010000050617845152540731234****2231100000MARCOS PEREIRAMERCADO DA AVENIDA" 
,"2201903010000010900232702980568723****9987123333JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
,"8201903010000000200845152540732344****1222123222MARCOS PEREIRAMERCADO DA AVENIDA" 
,"2201903010000000500232702980567677****8778141808JOSÉ COSTA    MERCEARIA 3 IRMÃOS" 
,"3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA"]
}

