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

Home page question cards animation:
```python
.card-link .card {
    transition: transform 0.3s ease-in-out;
    width: 100%; /* Set a fixed width for the card */
}

.card-link:hover .card {
    transform: scale(1.08); /* Increase the size on hover, adjust as needed */
    transition: 0.7s;
    box-shadow: 0px 0px 2px 2px darkgrey;     
}
```
Removing the blue color hyperlink:
```python
.icon-link:hover {
    color: inherit;
}
```
Flip cards:
```python
    <script>
        function flipCard(card) {
            card.classList.toggle('flipped');
        }
    </script>
//css//
.card.flipped {
    transform: rotateY(180deg);
}
```
Card click expand:
```python
    <script>
        document.querySelectorAll('.card').forEach(function(card) {
            card.addEventListener('click', function() {
                var targetCollapse = card.getAttribute('data-target');
                var isExpanded = $(targetCollapse).hasClass('show');
    
                // If the explanation is not expanded, expand it
                if (!isExpanded) {
                    $(targetCollapse).collapse('show');
                }
            });
        });
    </script>
```


**Alejandra**

html code for the carousel displaying the pie charts with the timing of BC treatment for each covid outcome 
  <!-- Timing Carousel -->
  
  <!-- Slideshow container -->
  <div class="timing-slideshow-container">
  
    <!-- Bar Charts with caption text -->
    <div class="myTimingSlides">
      <div id="afr_mild_timing_pie" style ="width:100%"></div>
      <div class="timingtext" style = "width:100%"> The most number of patients experienced mild covid outcomes when they had ATC within the first 4 weeks of developing covid</div>
    </div>
  
    <div class="myTimingSlides">
      <div id="afr_moderate_timing_pie" style ="width:100%"></div>
      <div class="timingtext" style = "width:100%"> The most number of patients experienced moderate covid outcomes when they had ATC within the first 4 weeks of developing covid</div>
    </div>
  
    <div class="myTimingSlides">
      <div id="afr_severe_timing_pie" style ="width:100%"></div>
      <div class="timingtext" style = "width:100%"> The most number of patients experienced severe covid outcomes when they had ATC 3 months after of developing covid</div>
    </div>
  
    <!-- Next and previous buttons -->
    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
  
  </div>
  
  <br>
  
  <!-- The dots/circles -->
  <div style="text-align:center">
    <span class="dot" onclick="currentSlide(1)"></span> 
    <span class="dot" onclick="currentSlide(2)"></span> 
    <span class="dot" onclick="currentSlide(3)"></span> 
  </div>

css code for the carousel displaying the pie charts with the timing of BC treatment for each covid outcome 
```python
* {box-sizing:border-box}

/* Slideshow container */
.timing-slideshow-container {
  max-width: 700px;
  height: 600px;
  position: relative;
  margin:auto;
  overflow: hidden;
}

/* Hide the images by default */
.myTimingSlides {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: black;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
  transform: rgba(214, 206, 206, 0.8);
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
  color: white;
}

/* Caption text */
.timingtext {
  color: black;
  font-size: 15px;
  padding: 8px 12px;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
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



**Dean** \
Functions to compute densities
```python
// Function to compute density
function kernelDensityEstimator(kernel, X) {
    return function(V) {
        return X.map(function(x) {
            return [x, d3.mean(V, function(v) {
                return kernel(x - v);
            })];
        });
    };
}

function kernelEpanechnikov(k) {
    return function(v) {
        return Math.abs(v /= k) <= 1 ? 0.75 * (1 - v * v) / k : 0;
    };
}

function plotCancerDensity() {
    d3.json("/api/v1/age_status_severity").then(function(data) {
        let traces = []
        let density = null,
            dat = null

        for (i in canHueOrder) {
            dat = data
                .filter((d) => d.der_cancer_status_v4 === canHueOrder[i])
                .map((d) => d.der_age_trunc)
            density = kde(dat)
            traces.push({
                x: density.map((d) => d[0]),
                y: density.map((d) => 100 * (dat.length / data.length) * d[1]),
                line: {
                    color: canColors[i]
                },
                mode: "lines",
                name: canNames[i],
                type: "scatter",
                hovermode: false
            })
        }

        Plotly.newPlot('density-cancer', traces);
    })
}
```
Custom hover template for stacked densities
```python
            hovertemplate = 'Relative:%{customdata:.3f})%<extra>%{fullData.name}</extra>'
            if (i == (covHueOrder.length - 1)) {
                hovertemplate = 'Overall Density:%{y:.3f}% | Relative:%{customdata:.3f})%<extra>%{fullData.name}</extra>'
            }
            max_ = Math.max(max_, Math.max(...y))
            traces.push({
                x: x,
                y: y,
                line: {
                    color: covColors[i],
                },
                fill: "tonexty",
                fillcolor: covColors[i],
                mode: "lines",
                name: covNames[i],
                type: "scatter",
                customdata: subvector(y, y_last),
                hovertemplate: hovertemplate,
                hoverlabel: {
                    font: {
                        color: 'white',
                        size: 18
                    }
                }
            })
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
* [Uploading images from GoogleDrive to Our Team page](https://stackoverflow.com/questions/77851898/using-google-drive-link-as-img-src-on-react-app-not-working)
* [Home page navbar](https://tachyons.io/components/nav/logo-titles-links-centered/index.html)


**Dean**
* [Density plot with several groups in d3.js](https://d3-graph-gallery.com/graph/density_double.html)
* [Animations in JavaScript](https://plotly.com/javascript/animations/)
* [Dot Plots in JavaScript](https://plotly.com/javascript/animations/)












