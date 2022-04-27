import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


try:
		# uri de origem do .csv
    uri = 'https://raw.githubusercontent.com/MicrosoftLearning/mslearn-dp100/main/data/diabetes.csv'
		
		# lê o .csv com o auxílio da lib pandas e renomeia os campos.
    dataset = pd.read_csv(uri).rename(columns={'PatientID': 'PacienteID', 
                                            'Pregnancies' : 'Gravidez', 
                                            'PlasmaGlucose' : 'ÍndiceGlicêmico', 
                                            'DiastolicBloodPressure':'PressãoDiastólicaSanguínea', 
                                            'TricepsThickness':'EspessuraTríceps',
                                            'SerumInsulin':'Insulina',
                                            'BIM':'IMC',
                                            'DiabetesPedigree':'DiabetesAscendente',
                                            'Age':'Idade',
                                            'Diabetic':'Diabético'
                                            }
                                    )
		
		# seleciona os campos que correspondem às features, que predirão a resposta.
    x = dados[['PacienteID',	'Gravidez',	'ÍndiceGlicêmico',	'PressãoDiastólicaSanguínea',	'EspessuraTríceps',	'Insulina',	'BMI',	'DiabetesAscendente',	'Idade']]
		# seleciona o campo que corresponde à resposta.
    y = dados[['Diabético']]
		
		# seleciona os dados de treino, para y e para x. 75% para treino.
    train_x = x[:7500]
    train_y = y[:7500]

		# seleciona os dados de teste. 25% para teste.
    test_x = x[7500:]
    test_y = y[7500:]
		
		
    model = LinearSVC()
		
    model.fit(train_x, train_y)
		
		
    y_pred = model.predict(test_x)
		
		# calcula a acurácia(taxa de acerto).
    accuracy = accuracy_score(test_y, y_pred, normalize=True)

    print(f'A acurácia foi {accuracy*100:.2f}%.')

except Exception as e:
    print(e)
