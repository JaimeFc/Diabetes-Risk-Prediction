# Sistema Predictivo de Riesgo de Diabetes

## Descripción

Proyecto desarrollado para la asignatura de Minería de Datos utilizando técnicas de Machine Learning para clasificar el riesgo de diabetes.

## Dataset

Diabetes Risk Prediction Dataset.

## Objetivo

Predecir el nivel de riesgo de diabetes de un paciente utilizando información médica, antecedentes familiares y hábitos de vida.

## Categorías de riesgo

- Low
- Moderate
- High

## Etapas desarrolladas

- Exploración de datos
- Estadística descriptiva
- Visualización de datos
- Limpieza de datos
- Tratamiento de valores nulos
- Codificación de variables categóricas
- Escalamiento de variables
- Entrenamiento de modelos
- Evaluación del desempeño
- Guardado del modelo predictivo

## Modelos evaluados

- Regresión Logística
- Random Forest
- Árbol de Decisión

## Mejor modelo seleccionado

Regresión Logística

### Accuracy obtenido

79.37%

## Variables más importantes

- fasting_blood_sugar
- hba1c_level
- age
- bmi
- family_history_diabetes

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib
- GitHub

## Autor

Jaime Faustino Castillo Guaman

## Repositorio GitHub

Este repositorio contiene el notebook desarrollado durante la práctica, el modelo entrenado, el escalador utilizado en el preprocesamiento y los archivos necesarios para futuras implementaciones mediante API REST.

## Resultados obtenidos

Accuracy final: 79.37 %

Clase Low:
- Precision: 0.86
- Recall: 0.91

Clase Moderate:
- Precision: 0.60
- Recall: 0.56

Clase High:
- Precision: 0.82
- Recall: 0.72
