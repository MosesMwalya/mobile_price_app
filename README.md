
# Beyond the Specs: Understanding the Hidden Influences on Mobile Phone Prices Through Data-driven Modeling and Predictive Analysis.

My organization decided to venture into mobile phone business as a way of extending our product portfolio in our expansion plan. We worked on all aspects of marketing but one challenge remained unresolved! - how do we price our product considering that we always strive to price optimally; underpricing or overpricing is a risk we never consider

The main goal of the project is therefore to develop a model that estimates ideal price given a set of product characteristics.
## Objectives
1. Firstly, seek to understand mobile phone market ecosystem by 
    - Identifying characteristics of mobile features in the market
    -  And then establishing any relationship between features of a mobile phone and its selling price. 

    
2. Secondly, to determine the role the phone features play in determining their price.

3. Finally, develop and avail a simulation model that our marketers would use to determine ideal mobile price for a given combination of phone features.

## About Dataset
 *I used fictitious data from [Kaggle](https://www.kaggle.com/datasets/ybifoundation/mobile-price-range?select=MobilePriceRange.csv) but I try as much as possible to demonstrate the steps that one can use to generate similar set.*

There are two steps involved:-
1. generating list of features that customers always ask for when buying a mobile phone.
   
   I did immersions with phone sellers and through this process, I was able to generate a list of features that customers consider important when buying phone. The list is as shown
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Phone%20Features.png)

3. Collected quantitative data of mobile phones
   
   Using features identified in Step 1 above, I developed a questionnaire and visited randomly selected phone shop sellers and for each phone that they stocked, recorded the features and corresponding price range. During this exercise, I collected data for 2000 different mobile phones on sale.
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/quant_data.png)
   
## The Finding

### Mobile Price Point Simulator
   
To enable marketers play with different combination of features and resultant ideal price range, I developed a [simulator model](https://mobileprice-f4464c53c2d6.herokuapp.com/).

This deployment was possible through use of [Streamlight](https://streamlit.io/) and [Heroku](https://mobileprice-f4464c53c2d6.herokuapp.com/)


![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Price_simulation%20Model.png)


### Role phone features play in determining price range

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Features%20Importance.png)


### Understanding Mobile Phone market ecosystem 
#### Distribution of mobile phone features in the market

    1. In terms of the price range, how does the distribution look like for mobile phones being sold?
    
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Target%20Features%20distribution.png)

       We note that there is equal popularity in terms of phone price ranges

   2. In terms of other features, which features are popular?
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Distribution%20of%20Numeric%20Vars.png)

      We note the following:-
      
              - *battery_power* - % of phones with battery power from lowest capacity (min=501 mAh) to highest capacity (max=1998 mAh) is the same. No particular capacity is higher than another.
      
              - Phones with *bluetooth, dual SIM, 4G, touch screen, and wifi* have same share as those without
      
              - Phones with *lower clock speed* are more than those with more speeds
      
              - Phones with lower *front camera megapixels* are more than those with higher megapixels
      
              - Market has phones in varying level of *internal memory* and none is a clear leader
      
              - The market has more phones with lower *front camera megapixels, pixel resolution height px_height, screen width* as compared to higher levels of the same features.
      
              - Nearly 75% of phones in the market are supporting *3G technology*.
      
              - Interestingly, all phones supporting *4G* also supports *3G*
  

        
#### How Features relate with Price Range

![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Categoricals%20Vars%20against%20Target.png)


![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Numeric%20Vars%20agaist%20Target.png)


Observations:-

    - Phones with *blue tooth* capability tend to cost higher.
    - Phones with *dual SIM* functionality tend to cost higher.
    - Phones with *3G or 4G* technology are likely to cost higher.
    - Generally, *touch_screen* phones cost higher.
    - Phones with *wifi* support costs higher.
    - Increase in phone *Battery_power power* as well as *ram* results in direct increase in price range
    - Other phone features that have slight impact in cost includes *pc, px_height, px_width, sc_h and sc_w*
   
#### Relationship between Features

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Price_range%20relationship%20with%20other%20features.png)

       We notice that while some features have a positive correlation with mobile price range, others have equally significant negative relationship with price range


   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/features%20relationship.png)

       It is noted that different features have significant relationship amongst themselves but there are those with relatively high correlation


## The Model

1. I used Random Forest classifier because it satisfied the following conditions identified during Exploratory Data Analysis

       - Understanding that some features have outliers
       - The data contains a mix of both numerical and categorical features
       - The data contains a fairly large number of features i.e. 20 features
       - The output feature has 4-classes; so classifier must be able to work for multiclassification problem
       - As part of the output, the user wants to establish the features importance in determing price range
       - The size of data being 2000 instances isnt big enough for a large model training
       - Obviously a model good enough to generalize; giving a relatively good accuracy, precision and recall.
   
1. Hyperparameter tuning

     - The base model was [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) 
      
     - [Bayesian Optimization](https://github.com/bayesian-optimization/BayesianOptimization)
       
     - [RandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)

      After tuning the model, Accuracy has slightly increased from 87%; with the model generalizing fairly well to 88%
   
1. Decision Trees
   
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/DTrees%20of%20RF%20estimators.png)
    
1. Decision Boundary
   
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Decision%20boundary%20of%20RF%20using%20t-SNE.png)


## Key Libraries used

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/scitkit.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/matplotlib.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/numpy.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/pandas.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/MLxtend.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/plotly.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/seaborn.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/streamlit.png" width="100" height="100" /> 

<img src="https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Libraries/heroku.png" width="100" height="100" /> 


## References
1. (https://www.kaggle.com/code/alifarahmandfar/mobile-price-prediction-classification-models)
   ``` By ALI FARAHMANDFAR```
   
3. [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
   
5. [RandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)

6. [Bayesian Optimizer](https://github.com/bayesian-optimization/BayesianOptimization)

7. [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

8. [Streamlit](https://docs.streamlit.io/library/get-started/main-concepts)

9. [Pickle](https://docs.python.org/3/library/pickle.html)

## License
This project is licensed under the [MIT License](https://github.com/MosesMwalya/mobile_price_app/blob/main/LICENSE.md). You are free to use the code and resources for educational or personal purposes.

## Contributions
Contributions are welcome! If you would like to contribute to this repository, please follow the guidelines outlined in [CONTRIBUTING.md](https://github.com/MosesMwalya/mobile_price_app/blob/main/Contributions.md). Any improvements, bug fixes, or additional projects are greatly appreciated

## Feedback and Contact
I welcome any feedback, suggestions, or questions you may have about the projects or the repository. Feel free to reach out to me via email at moses.mutua@gmail.com

Enjoy exploring my data science projects!

