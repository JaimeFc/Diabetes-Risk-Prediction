from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# ======================================
# CARGAR MODELO Y ARCHIVOS
# ======================================

modelo = joblib.load("modelo_diabetes.pkl")
escalador = joblib.load("escalador.pkl")
columnas = joblib.load("columnas_modelo.pkl")

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None

    if request.method == "POST":

        # ==========================
        # VARIABLES NUMÉRICAS
        # ==========================

        datos = {col: 0 for col in columnas}

        datos["age"] = float(request.form["age"])
        datos["bmi"] = float(request.form["bmi"])
        datos["hours_sleep_per_night"] = float(request.form["hours_sleep_per_night"])
        datos["stress_level"] = float(request.form["stress_level"])
        datos["fasting_blood_sugar"] = float(request.form["fasting_blood_sugar"])
        datos["hba1c_level"] = float(request.form["hba1c_level"])
        datos["blood_pressure_systolic"] = float(request.form["blood_pressure_systolic"])
        datos["blood_pressure_diastolic"] = float(request.form["blood_pressure_diastolic"])
        datos["waist_circumference_cm"] = float(request.form["waist_circumference_cm"])

        # ==========================
        # GÉNERO
        # ==========================

        gender = request.form["gender"]

        if gender == "Male":
            datos["gender_Male"] = 1

        elif gender == "Other":
            datos["gender_Other"] = 1

        # ==========================
        # ANTECEDENTES FAMILIARES
        # ==========================

        family_history = request.form["family_history_diabetes"]

        if family_history == "Yes":
            datos["family_history_diabetes_Yes"] = 1

        # ==========================
        # ACTIVIDAD FÍSICA
        # ==========================

        activity = request.form["physical_activity_level"]

        if activity == "Moderate":
            datos["physical_activity_level_Moderate"] = 1

        elif activity == "Sedentary":
            datos["physical_activity_level_Sedentary"] = 1

        # ==========================
        # TABAQUISMO
        # ==========================

        smoking = request.form["smoking_status"]

        if smoking == "Former":
            datos["smoking_status_Former"] = 1

        elif smoking == "Never":
            datos["smoking_status_Never"] = 1

        elif smoking == "Unknown":
            datos["smoking_status_Unknown"] = 1

        # ==========================
        # DATAFRAME
        # ==========================

        df_pred = pd.DataFrame([datos])

        # Escalar

        datos_escalados = escalador.transform(df_pred)

        # Predicción

        resultado = modelo.predict(datos_escalados)[0]

    return render_template(
        "index.html",
        resultado=resultado
    )


if __name__ == "__main__":
    app.run(debug=True)