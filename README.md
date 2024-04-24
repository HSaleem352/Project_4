# Breast Cancer Research Group

## Description of Project

In Project 4, our team expands upon the groundwork laid by Projects 1 and 3, which focused on breast cancer data from the COVID-19 and Cancer Consortium (CCC19). Our primary aim in this final project is to develop machine learning-based risk assessment models tailored to predicting the likelihood of women with breast cancer experiencing moderate or severe COVID-19 symptoms.

To ensure real-time predictive capabilities, we enhance our existing web platform by introducing a "COVID-19 Risk Wizard" page. This feature allows individuals to input various parameters such as race, age, smoking status, and more. These parameters provided by users undergo analysis by four machine learning models, culminating in a weighted average number that reflects their COVID-19 risk level. This tool serves as a guideline for users to assess their COVID-19 risk and receive immediate feedback.

Click here for more information about [Project 3](https://github.com/HSaleem352/Bootcamp_Project_3)


## Members of the Group
- Hamza Saleem - @HSaleem352
- Mina Bagheri - @minalbm
- Dean Ninalga - @Ninalgad 
- Fozia - @FoziaY
- Shan Lian - @Lians03
- Alejandra - @AlejandraFeatherston

## Work Breakdown
- Developing 4 unique machine learning model on individual colab files with python : Dean, Shan, Alex, Fozia
- Developing the app.py and flask app connection: Hamza
- Developing the user interface with HTML and CSS and integrating it to our already-existing website: Mina
- Deploy fly.io : Shan, Hamza


## Instructions on How to Use and Interact with the Project
### Method 1: Accessing the Web Application Directly
Visit our hosted web application by navigating to https://breastcancerproject3.fly.dev/

### Method 2: Running the Code Locally
- Open app.py and run the application.
- Open the local host server: http://127.0.0.1:5000
- Use the navigation bar to move through the webapp
- Scroll down to view the page contents
- Use the buttons in the home page to access the question pages
- Use the navigation bar to return to homepage
- Follow directions on the pages to interact with elements



## Efforts for Ethical Considerations Made in the Project
The dataset that we are using is associated with a Creative Commons Attribution 4.0 International License. This allows for the re-distribution and re-use of the dataset as long as the creators are porperly cited. We made sure to cite the creators of the dataset both in this ReadMe and on the Website - thus adhering to the Data License.

Our website doesn't collect any user information like name or contact information, thus we did not have to deploy additional security measures to ensure we were safely storing and using the information.

We made sure to make the website easy to use and interpret, and engaging so that it is accessible to the general public. In this way, we are also making scientific research more accessible to the lay audience.

## Dataset:
[Nagaraj, G., Khaki, A., & Shah, D. (2023). Covid-19 and Cancer Consortium (CCC19) breast cancer and racial disparities outcomes study. Zenodo](https://doi.org/10.5281/zenodo.7644334). 


## Code Snippets
**Mina**

Modal Example:
```python
<div class="modal fade" id="welcomeModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" data-bs-backdrop="static">
        <div class="modal-dialog modal-dialog-centered modal-scale">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Welcome to COVID-19 Risk Wizard!</h5>
            </div>
            <div class="modal-body" style="text-align: center; background-color: #E5DFCF;">
            <p>We're excited to introduce you to our predictive model designed to assess the risk of moderate to severe COVID-19 in breast cancer 
            patients. Leveraging a comprehensive dataset, we've developed an algorithm that analyzes various patient factors to provide valuable insights.</p>
            <p> </p>
            <p><span style="font-weight: bold; color: #4C5D6A;">Important Note:</span> It's essential to recognize that while our model offers valuable predictions, it's not infallible. Like any tool, it has limitations,
            primarily due to the constraints of our dataset. Therefore, the results should be interpreted with caution and not solely relied upon for medical decision-making.</p>
            <p> </p>
            <p>Press "Continue" to begin the prediction process.</p>
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-success" data-bs-dismiss="modal">Continue</button>
            </div>
        </div>
        </div>
    </div>
```
Tooltip Initialization:
```python
       <script>
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    </script>
```
Checking if all questions are answered:
```python
    <script>
        var formData = {};
        document.addEventListener("DOMContentLoaded", function() {
            function checkAllQuestionsAnswered() {
                var selects = document.querySelectorAll("select");
                var radios = document.querySelectorAll("input[type='radio']");
                var allAnswered = true;
                selects.forEach(function(select) {
                    if (select.value === "") {
                        allAnswered = false;
                    }
                });
                radios.forEach(function(radio) {
                    var name = radio.getAttribute("name");
                    if (!document.querySelector("input[name='" + name + "']:checked")) {
                        allAnswered = false;
                    }
                });
                return allAnswered;
            }


            // Function to handle predict button click
            function handlePredictButtonClick() {
                var selects = document.querySelectorAll("select");
                var radios = document.querySelectorAll("input[type='radio']");
                if (checkAllQuestionsAnswered()) {
                    // All questions answered, proceed with prediction
                    console.log("All questions answered. Proceeding with prediction...");

                    document.getElementById("errorMessage").style.display = "none"; // Hide error message
                    selects.forEach(function(select) {
                        select.classList.remove("unanswered");
                    });
                    radios.forEach(function(radio) {
                        var name = radio.getAttribute("name");
                        var questionRadioButtons = document.querySelectorAll("input[name='" + name + "']");
                        var isAnswered = false;
                        questionRadioButtons.forEach(function(radioButton) {
                            if (radioButton.checked) {
                                isAnswered = true;
                            }
                        });
                        if (!isAnswered) {
                            questionRadioButtons.forEach(function(radioButton) {
                                radioButton.classList.add("unanswered");
                            });
                        } else {
                            // Remove the highlight if the question is answered
                            questionRadioButtons.forEach(function(radioButton) {
                                radioButton.classList.remove("unanswered");
                            });
                        }
```



**Hamza**

Ajax handler
```javascript

// Send Data
                    
$.ajax({
url: '/predictor',
type: 'POST',
contentType: 'application/json',
data: JSON.stringify(formData),
dataType: "json",
success: function(response) {

    console.log("Response received:", response.value);
    percentage_value = response.value*100

    
    $('#output-popup').text("This individual has an estimated risk of " + percentage_value + "% for moderate-to-severe COVID-19.");
    $('#outputModal').modal('show');

},
error: function(xhr, status, error) {
    console.error('Error:', error);
    }
});
```


Flask app
```python
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
```


**Shan** 
Using Keras Tuner to find the optimal hyperparameters for the best neural network model through a hyperparameter search using the Hyperband algorithm.
```
def create_model(hp):
    nn_model = tf.keras.models.Sequential()

    # Allow kerastuner to decide which activation function to use in hidden layers
    activation = hp.Choice('activation',['relu','tanh','softmax'])

    # Allow kerastuner to decide number of neurons in first layer
    nn_model.add(tf.keras.layers.Dense(units=hp.Int('first_units',
        min_value=1,
        max_value=30,
        step=5), activation=activation, input_dim=29))

    # Allow kerastuner to decide number of hidden layers and neurons in hidden layers
    for i in range(hp.Int('num_layers', 1, 10)):
        nn_model.add(tf.keras.layers.Dense(units=hp.Int('units_' + str(i),
            min_value=1,
            max_value=30,
            step=5),
            activation=activation))

    nn_model.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

    # Compile the model
    nn_model.compile(loss="binary_crossentropy", optimizer='adam', metrics=['accuracy', tf.keras.metrics.AUC(name='auc')])

    return nn_model
     

tuner = kt.Hyperband(
    create_model,
    objective="val_accuracy",
    max_epochs=20,
    hyperband_iterations=2)
     

tuner.search(X_train, y_train,
             epochs=20,
             validation_data=(X_test, y_test))
```

**Alex**
```
from keras.layers import Dropout

nn_model = tf.keras.models.Sequential()

nn_model.add(tf.keras.layers.Dense(128, activation="tanh", input_dim=X_train.shape[1]))
nn_model.add(Dropout(0.2))
nn_model.add(tf.keras.layers.Dense(64, activation="tanh"))
nn_model.add(Dropout(0.2))
nn_model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

nn_model.summary()

```

## References

**Hamza**
* [Creating postgresql engine](https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre)
* [Listing all tables in postgres using SQLAlchemy](https://www.pythonsheets.com/notes/python-sqlalchemy.html)  
* [Visual for amcharts](https://www.amcharts.com/demos/donut-with-radial-gradient/)
* [Pic for home page](https://healthcare.utah.edu/huntsmancancerinstitute/sites/g/files/zrelqx336/files/styles/freeform_phone/public/migrate_images/mammo-mask.jpg?h=bdbe9ddb&itok=VPDk9U4v)
* [Animations](https://animate.style/)

**Alejandra**
* [Information on the license applied to the dataset](https://creativecommons.org/licenses/by/4.0/legalcode)
* [Information on ethical web design](https://capacityinteractive.com/blog/the-principles-of-ethical-web-design/)
* [Creating the carousel](https://www.w3schools.com/howto/howto_js_slideshow.asp)
* [Creating the flip cards](https://www.w3schools.com/howto/howto_css_flip_card.asp)
* [Aranging text vertically](https://www.shecodes.io/athena/38295-how-to-make-h1-on-two-lines-with-different-colors)
* [Text alignment in css](https://www.w3schools.com/css/css_text_align.asp)


**Mina**
* [Page structures](https://getbootstrap.com) , ChatGPT


**Dean**
* [Density plot with several groups in d3.js](https://d3-graph-gallery.com/graph/density_double.html)
* [Animations in JavaScript](https://plotly.com/javascript/animations/)
* [Dot Plots in JavaScript](https://plotly.com/javascript/animations/)












