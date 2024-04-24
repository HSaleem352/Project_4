# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,text
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template
from flask import request
import tensorflow as tf
from flask_cors import CORS
import pickle
import numpy as np
import json

engine = create_engine('postgresql+psycopg2://breast_cancer_dataset_user:UnSNEeECgY7ky2i5KAPC2WtQn9XrRpvc@dpg-cnbvjf779t8c73epbb3g-a.oregon-postgres.render.com/breast_cancer_dataset')

app = Flask(__name__)
CORS(app) #enables all
#################################################################################################################
##                                            Home Page                                                        ##
#################################################################################################################

@app.route('/')
def main():
    return render_template("index.html")

#################################################################################################################
##                                            Our Team Page                                                    ##
#################################################################################################################

@app.route('/OurTeam')
def ourteam():
    return render_template("ourteam.html")

#################################################################################################################
##                                            References Page                                                  ##
#################################################################################################################

@app.route('/Limitations_References')
def Limitations_References():
    return render_template("limitations_references.html")

#################################################################################################################
##                                            COVID-19 Risk Wizard Page                                        ##
#################################################################################################################


##################################################################################################
####################################    Covid Page      ##########################################
##################################################################################################

@app.route('/COVID_Predictor', methods=['GET'])
def COVID_page():
    return render_template("COVID_Predictor.html")


##################################################################################################
################################       Ajax Communication      ###################################
##################################################################################################

@app.route('/predictor', methods=['POST'])
def COVID_Predictor():
    
        # Check if the request contains JSON data
        if request.is_json:
            data = request.json

            result = process_input(data)
            return result
        else:
            return jsonify({'error': 'Request must be JSON'}), 400
        
        
def process_input(data_dict):
    
    # Mapping for data transformation
    _yesno_map = {"yes": 1, "no": 0}
    _smoking_map = {"Current or Former": 1, "Never": 0}


    # Deriving values based on the provided template
    der_age_trunc = float(data_dict['age'])
    der_obesity = _yesno_map[data_dict['Obesity']]
    der_smoking2 = _smoking_map[data_dict['Smoking Status']]
    der_race_v2 = data_dict['Race/Ethnicity']
    urban_rural = data_dict['Residential Area Type']
    der_cancertr_none = _yesno_map[data_dict['cancer treatment']]
    der_cancer_status_v4 = data_dict['Cancer Status']
    der_dm2 = _yesno_map[data_dict['Diabetes Mellitus']]
    der_card = _yesno_map[data_dict['Cardiovascular Comorbidity']]
    der_pulm = _yesno_map[data_dict['Pulmonary Comorbidities']]
    der_renal = _yesno_map[data_dict['Renal Comorbidities']]

    # Constructing the Pandas Series
    series = pd.Series({
        'der_age_trunc': der_age_trunc,
        'der_obesity': der_obesity,
        'der_smoking2': der_smoking2,
        'der_race_v2': der_race_v2,
        'urban_rural': urban_rural,
        'der_cancertr_none': der_cancertr_none,
        'der_cancer_status_v4': der_cancer_status_v4,
        'der_dm2': der_dm2,
        'der_card': der_card,
        'der_pulm': der_pulm,
        'der_renal': der_renal
    })

    ####### Calling Model Functions

    dean_model = predict_model_dn(series)
    shan_model = predict_model_sh(series)
    alex_model = predict_model_afr(series)
    fozia_model = predict_model_fz(series)

    avg_model = (dean_model + shan_model + alex_model + fozia_model) / 4.0

    output_result = {'value': str(round(avg_model, 2))}    
    
    return jsonify(output_result)

##################################################################################################
####################################### Model Functions ##########################################
##################################################################################################

################ Dean's model

def preprocess_inp_dn(data):
    with open('assets/dn/ohe.pkl', 'rb') as f:
        one_hot_enc = pickle.load(f)
    with open('assets/dn/scaler.pkl', 'rb') as f:
        standard_scaler = pickle.load(f)
    multi_categorical = ['der_race_v2', 'der_smoking2', 'urban_rural', 'der_cancer_status_v4']
    binary = ['der_obesity', 'der_cancertr_none', 'der_dm2', 'der_card', 'der_pulm', 'der_renal']
    continuous = ['der_age_trunc']

    x_continous = standard_scaler.transform(data[continuous].values.reshape(1, -1))
    x_categorical = one_hot_enc.transform(data[multi_categorical + binary].values.reshape(1, -1))
    x = np.concatenate([x_continous, x_categorical], axis=-1)

    return x


def predict_model_dn(data):
    x = preprocess_inp_dn(data)
    model = tf.keras.models.load_model('assets/dn/model.h5')
    p = model.predict(x, verbose=0)[0][0]
    return p

################################################################################################

################ Shan's model

def preprocess_inp_sh(data):
    with open('assets/shan/ohe.pkl', 'rb') as f:
        one_hot_enc = pickle.load(f)
    with open('assets/shan/scaler.pkl', 'rb') as f:
        standard_scaler = pickle.load(f)
    multi_categorical = ['der_race_v2', 'der_smoking2', 'urban_rural', 'der_cancer_status_v4']
    binary = ['der_obesity', 'der_cancertr_none', 'der_dm2', 'der_card', 'der_pulm', 'der_renal']
    continuous = ['der_age_trunc']

    x_continous = standard_scaler.transform(data[continuous].values.reshape(1, -1))
    x_categorical = one_hot_enc.transform(data[multi_categorical + binary].values.reshape(1, -1))
    x = np.concatenate([x_continous, x_categorical], axis=-1)

    return x


def predict_model_sh(data):
    x = preprocess_inp_sh(data)
    model = tf.keras.models.load_model('assets/shan/model_shan.h5')
    p = model.predict(x, verbose=0)[0][0]
    return p

################################################################################################

############### Alejandra's Model

def preprocess_inp_afr(data):
    with open('assets/afr/ohe.pkl', 'rb') as f:
        one_hot_enc = pickle.load(f)
    with open('assets/afr/scaler.pkl', 'rb') as f:
        standard_scaler = pickle.load(f)
    multi_categorical = ['der_race_v2', 'der_smoking2', 'urban_rural', 'der_cancer_status_v4']
    binary = ['der_obesity', 'der_cancertr_none', 'der_dm2', 'der_card', 'der_pulm', 'der_renal']
    continuous = ['der_age_trunc']

    x_continous = standard_scaler.transform(data[continuous].values.reshape(1, -1))
    x_categorical = one_hot_enc.transform(data[multi_categorical + binary].values.reshape(1, -1))
    x = np.concatenate([x_continous, x_categorical], axis=-1)

    return x


def predict_model_afr(data):
    x = preprocess_inp_afr(data)
    model = tf.keras.models.load_model("assets/afr/model_afr.h5")
    p = model.predict(x, verbose=0)[0][0]
    return p

################################################################################################

############### Fozia's Model

def preprocess_fz(raw_inp):
    categorical_cols = ['der_obesity', 'der_race_v2', 'der_smoking2', 'urban_rural', 'der_cancertr_none', 'der_cancer_status_v4', 'der_dm2', 'der_card', 'der_pulm', 'der_renal']
    numeric_cols = ['der_age_trunc']

    with open('assets/fz/ohe.pkl', 'rb') as f:
      encoder = pickle.load(f)

    with open('assets/fz/mm.pkl', 'rb') as f:
      scaler = pickle.load(f)

    categorical = encoder.transform(raw_inp[categorical_cols].values.reshape(1, -1))
    numeric = scaler.transform(raw_inp[numeric_cols].values.reshape(-1, 1))

    x = np.concatenate([numeric, categorical], axis=-1)
    return x


def predict_model_fz(inp):

    # Load the model from the file
    with open('assets/fz/model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    x = preprocess_fz(inp)
    return loaded_model.predict_proba(x)[0][1]
    

#################################################################################################################
##                                                Mina                                                         ##
#################################################################################################################

@app.route('/smoking_effect')
def mina_q1():
    return render_template("smoking.html")

@app.route('/smoking_race_effect')
def mina_q2():
    return render_template("smoking_race.html")


@app.route('/api/v1/Smoker&BC_VS_Non-Smoker&BC', methods=['GET'])
def get_data_MB1():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('Smoker&BC_VS_Non-Smoker&BC',connection)
   
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route('/api/v1/Smoker_NonSmoker_Covid_DF', methods=['GET'])
def get_data_MB2():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('Smoker_NonSmoker_Covid_DF',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route('/api/v1/MildCov_BC_Smoker_NonSmoker_DF', methods=['GET'])
def gget_data_MB3():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('MildCov_BC_Smoker_NonSmoker_DF',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route('/api/v1/ModerateCov_BC_Smoker_NonSmoker_DF', methods=['GET'])
def get_data_MB4():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('ModerateCov_BC_Smoker_NonSmoker_DF',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


@app.route('/api/v1/SevereCov_BC_Smoker_NonSmoker_DF', methods=['GET'])
def get_data_MB5():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('SevereCov_BC_Smoker_NonSmoker_DF',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


@app.route('/api/v1/A_Res_BC_Smoker_NonSmoker_DF', methods=['GET'])
def get_data_MB6():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('A_Res_BC_Smoker_NonSmoker_DF',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route('/api/v1/A_St_BC_Smoker_NonSmoker_DF', methods=['GET'])
def get_data_MB7():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('A_St_BC_Smoker_NonSmoker_DF',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route('/api/v1/A_Prog_BC_Smoker_NonSmoker_DF', methods=['GET'])
def get_data_MB8():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('A_Prog_BC_Smoker_NonSmoker_DF',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data
 

#################################################################################################################
##                                                Hamza                                                        ##
#################################################################################################################

@app.route('/residence_type_effects')
def hamza_page():
    return render_template("hamza.html")


@app.route('/api/v1/residence_counts', methods=['GET'])
def HS_residenceCounts():

    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('residence_counts',connection)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


@app.route('/api/v1/severity_residence_HS', methods=['GET'])
def severity_residence_HS():

    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('severity_residence_HS',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


@app.route('/api/v1/cancer_residence_HS', methods=['GET'])
def cancer_residence():

    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('cancer_residence_HS',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


#################################################################################################################
##                                                Alejandra                                                    ##
#################################################################################################################

@app.route('/api/v1/AFR_timing_df', methods=['GET'])
def AFR_timing_df():

    
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('AFR_timing_df',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route("/api/v1/afr_treatment_type_df", methods=["GET"])
def afr_treatment_type_df():

    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('afr_treatment_type_df',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient="records")

    return json_data

@app.route('/afr_treatment_timing_page')
def afr_page():
    return render_template("alejandra.html")


#################################################################################################################
##                                                  Shan                                                       ##
#################################################################################################################

@app.route('/race_affect_COVID_breast_cancer')
def shan_page():
    return render_template("shan.html")


@app.route('/api/v1/race_counts', methods=['GET'])
def get_data1_shan():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('race_counts',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


@app.route('/api/v1/cancer_status_sum', methods=['GET'])
def get_data2_shan():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('cancer_status_sum',connection)
   
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

@app.route('/api/v1/covid_severity_count_by_race', methods=['GET'])
def get_data3_shan():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('covid_severity_count_by_race',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


#################################################################################################################
##                                                  Dean                                                       ##
#################################################################################################################

@app.route('/severe_outcomes_by_age')
def dean_page():
    return render_template("dean_q.html")


@app.route('/api/v1/age_status_severity', methods=['GET'])
def age_v_cancer_covid_data():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('age_status_severity',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data


@app.route("/api/v1/outcome_rates", methods=["GET"])
def outcome_rates():

    # Read CSV file using pandas
    
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('outcome_rates',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient="records")

    return json_data


#################################################################################################################
##                                                  Fozia                                                      ##
#################################################################################################################

@app.route('/obesity&age')
def fozia_page():
    return render_template("FY.html")

# A function to display the data from the sql server in json
@app.route('/api/v1/FYinit_data',methods=['GET'])
def FY_get_data():
    # Read Dataframe using SQL
    with engine.connect() as connection:
        df = pd.read_sql('FYinit_data',connection)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return  jsonify(json_data)


@app.route('/obesity_distribution_active_responding')
def obesity_distribution_active_responding():
    # Connect to the database and retrieve data
    with engine.connect() as connection:
        # Adjust the SQL query based on your database schema and structure
        query = "SELECT der_obesity, COUNT(*) as count FROM obesity_age_effect WHERE der_cancer_status_v4 = 'Active and responding' GROUP BY der_obesity"
        result = connection.execute(query)
        data = [{"der_obesity": row[0], "count": row[1]} for row in result]

    # Convert the data to JSON
    json_data = jsonify(data)
   
    return json_data

@app.route('/FYcancer_status_percentage')
def cancer_percentage():
    with engine.connect() as connection:
        # Query data for cancer percentage
        query = text("""
            SELECT
                COUNT(*) FILTER (WHERE der_cancer_status_v4 = 'Active and stable' OR der_cancer_status_v4 = 'Active and responding') / COUNT(*)::float * 100 AS cancer_percentage,
                COUNT(*) FILTER (WHERE der_cancer_status_v4 = 'Remission or no evidence of disease, >5 years' OR der_cancer_status_v4 = 'Remission or no evidence of disease, <5 years') / COUNT(*)::float * 100 AS no_cancer_percentage
                FROM obesity_age_effect
                """)
        result = connection.execute(query)

        # Convert the result to a DataFrame
        cancer_percentage_df = pd.DataFrame(result.fetchall(), columns=["cancer_percentage", "no_cancer_percentage"])

    # Convert the DataFrame to JSON
    cancer_percentage_json = cancer_percentage_df.to_json(orient='records')

    return cancer_percentage_json


@app.route("/obesity_distribution")
def obesity_distribution():
    with engine.connect() as connection:
        # Query data for obesity distribution
        query = text("""
            SELECT
                der_obesity,
                COUNT(*) AS count
            FROM obesity_age_effect
            GROUP BY der_obesity
        """)
        result = connection.execute(query)

        # Convert the result to a DataFrame
        obesity_distribution_df = pd.DataFrame(result.fetchall(), columns=["der_obesity", "count"])

    # Convert the DataFrame to JSON
    obesity_distribution_json = obesity_distribution_df.to_json(orient='records')

    return obesity_distribution_json


@app.route('/covid_severity_distribution')
def covid_severity_distribution():
    with engine.connect() as connection:
        # Query data for COVID-19 severity distribution by obesity status
        query = text("""
            SELECT
                der_obesity,
                severity_of_covid_19_v2,
                COUNT(*) AS count
            FROM obesity_age_effect
            GROUP BY der_obesity, severity_of_covid_19_v2
        """)
        result = connection.execute(query)

        # Convert the result to a DataFrame
        covid_severity_distribution_df = pd.DataFrame(result.fetchall(), columns=["der_obesity", "severity_of_covid_19_v2", "count"])

    # Convert the DataFrame to JSON
    covid_severity_distribution_json = covid_severity_distribution_df.to_json(orient='records')

    return covid_severity_distribution_json


@app.route('/age_distribution_by_covid_severity')
def age_distribution_by_covid_severity():
    with engine.connect() as connection:
        query = text("""SELECT der_age_trunc, severity_of_covid_19_v2 FROM obesity_age_effect WHERE der_cancer_status_v4 IS NOT NULL""")
        data = pd.read_sql(query, connection)

    # Clean the data if needed and filter out null values
    data = data.dropna()

    # Convert the data to JSON
    age_distribution_data = data.to_json(orient='records')

    return age_distribution_data

#################################################################################################################
##                                                  Debug                                                      ##
#################################################################################################################


if __name__ == '__main__':
    app.run(debug=True)

