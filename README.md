
# Empowering Agile Marketing with Data-Driven Insights: My Mobile Phone Price Prediction Project.

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


![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Price_simulation%20Model.png)


### Role phone features play in determining price range

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Features%20Importance.png)


### Understanding Mobile Phone market ecosystem 
#### Distribution of mobile phone features in the market

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Distribution%20of%20Numeric%20Vars.png)

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Target%20Features%20distribution.png)

      We note that
      - 
      - 
        
#### How Features relate with Price Range

![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Categoricals%20Vars%20against%20Target.png)


![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Numeric%20Vars%20agaist%20Target.png)

   
#### Relationship between Features

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Price_range%20relationship%20with%20other%20features.png)

   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/features%20relationship.png)


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

     - Estimating optimal number of Decision Trees. This well articulated by [Avi Chwala](https://www.blog.dailydoseofds.com/p/your-random-forest-is-underperforming)
      
     - GridSearchCV

      After tuning the model, Accuracy has slightly increased from 87%; with the model generalizing fairly well to 88%
   
1. Decision Trees
   
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/DTrees%20of%20RF%20estimators.png)
    
1. Decision Boundary
   
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Decision%20boundary%20of%20RF%20using%20t-SNE.png)



## License
This project is licensed under the [MIT License](https://github.com/MosesMwalya/mobile_price_app/blob/main/LICENSE.md). You are free to use the code and resources for educational or personal purposes.

## Contributions
Contributions are welcome! If you would like to contribute to this repository, please follow the guidelines outlined in [CONTRIBUTING.md](https://github.com/MosesMwalya/mobile_price_app/blob/main/Contributions.md). Any improvements, bug fixes, or additional projects are greatly appreciated

## Feedback and Contact
I welcome any feedback, suggestions, or questions you may have about the projects or the repository. Feel free to reach out to me via email at moses.mutua@gmail.com

Enjoy exploring my data science projects!

