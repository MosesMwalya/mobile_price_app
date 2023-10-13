
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

This deployment was possible through use of [Streamlight](https://streamlit.io/) and [Heroku](https://www.heroku.com/)


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

     - Estimating optimal number of Decision Trees. This well articulated by [Avi Chwala](https://www.blog.dailydoseofds.com/p/your-random-forest-is-underperforming)
      
     - Popular [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) 

      After tuning the model, Accuracy has slightly increased from 87%; with the model generalizing fairly well to 88%
   
1. Decision Trees
   
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/DTrees%20of%20RF%20estimators.png)
    
1. Decision Boundary
   
   ![](https://github.com/MosesMwalya/mobile_price_app/blob/main/images/Decision%20boundary%20of%20RF%20using%20t-SNE.png)


## Key Libraries used
![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fc3.klipartz.com%2Fpngpicture%2F401%2F742%2Fsticker-png-alternative-python-icons-and-folder-icon-python-2-thumbnail.png&tbnid=1HCoZd54UlvxNM&vet=12ahUKEwjc8oDV6vKBAxUFrycCHcBiDo4QMygJegQIARB_..i&imgrefurl=https%3A%2F%2Fwww.klipartz.com%2Fen%2Fsearch%3Fq%3Dpython&docid=PrSdE_mOE_VI3M&w=370&h=370&q=icon%20for%20python&ved=2ahUKEwjc8oDV6vKBAxUFrycCHcBiDo4QMygJegQIARB_)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F0%2F05%2FScikit_learn_logo_small.svg%2F2560px-Scikit_learn_logo_small.svg.png&tbnid=6beLvrlelDhObM&vet=12ahUKEwi4pdPr6vKBAxVnV6QEHXyrBXQQMygAegQIARBI..i&imgrefurl=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3AScikit_learn_logo_small.svg&docid=ZasF_RP8GlBo-M&w=2560&h=1378&q=icon%20for%20sklearn&ved=2ahUKEwi4pdPr6vKBAxVnV6QEHXyrBXQQMygAegQIARBI)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fstreamlit.io%2Fimages%2Fbrand%2Fstreamlit-logo-secondary-colormark-darktext.png&tbnid=_l3WkM3jQpymsM&vet=12ahUKEwjOvqXq6_KBAxWfticCHUH9DBgQMygAegQIARBM..i&imgrefurl=https%3A%2F%2Fstreamlit.io%2Fbrand&docid=vnWK2tMrGVX_0M&w=2921&h=811&q=icon%20for%20streamlit&ved=2ahUKEwjOvqXq6_KBAxWfticCHUH9DBgQMygAegQIARBM)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.iconscout.com%2Ficon%2Ffree%2Fpng-256%2Ffree-heroku-11-1175214.png&tbnid=5cUhCMeCmqmY5M&vet=12ahUKEwjumcv46_KBAxXbmicCHWzGDP4QMygDegQIARBR..i&imgrefurl=https%3A%2F%2Ficonscout.com%2Ficons%2Fheroku&docid=5zvTLwWQDEM8xM&w=256&h=256&q=icon%20for%20heroku&ved=2ahUKEwjumcv46_KBAxXbmicCHWzGDP4QMygDegQIARBR)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2F1.bp.blogspot.com%2F-1VKv6Sq1WDw%2FXmc1Cy-UWtI%2FAAAAAAAAD-I%2Fye3uFBx8D6MEGEgbtzCLD5rzx7A44Pz-ACNcBGAsYHQ%2Fs1600%2Fpython-pickle-800x2001.png&tbnid=y1vFAb4iEJuh4M&vet=12ahUKEwirgt_A7PKBAxW4rycCHd2MCNMQMygAegQIARAt..i&imgrefurl=https%3A%2F%2Fwww.infinitycodex.in%2F2020%2F03%2Fdata-science-ss-107python-pickle.html&docid=zoam8Z2mSdq9CM&w=570&h=196&q=icon%20for%20pickle%20python%20documentation&hl=en&ved=2ahUKEwirgt_A7PKBAxW4rycCHd2MCNMQMygAegQIARAt)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F3%2F31%2FNumPy_logo_2020.svg%2F2560px-NumPy_logo_2020.svg.png&tbnid=_USeIIo97vUGrM&vet=12ahUKEwiHsviN6_KBAxVyW6QEHdbbBUUQMygCegQIARBH..i&imgrefurl=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3ANumPy_logo_2020.svg&docid=2szkTYJOYt7fEM&w=2560&h=1152&q=icon%20for%20numpy&ved=2ahUKEwiHsviN6_KBAxVyW6QEHdbbBUUQMygCegQIARBH)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fe%2Fed%2FPandas_logo.svg%2F1280px-Pandas_logo.svg.png&tbnid=MQyOBeq811GD5M&vet=12ahUKEwjyiN2c6_KBAxUdnCcCHdRGCJAQMygCegQIARBK..i&imgrefurl=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3APandas_logo.svg&docid=jK6kcNRt9RgIqM&w=1280&h=517&q=icon%20for%20pandas&ved=2ahUKEwjyiN2c6_KBAxUdnCcCHdRGCJAQMygCegQIARBK)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fmatplotlib.org%2Fstable%2F_images%2Fsphx_glr_logos2_003.png&tbnid=-gUoUQ7YcievqM&vet=12ahUKEwjE9ZCu6_KBAxVtV6QEHdyuBiQQMygDegQIARBL..i&imgrefurl=https%3A%2F%2Fmatplotlib.org%2Fstable%2Fgallery%2Fmisc%2Flogos2.html&docid=bRmdr0PbayjZRM&w=550&h=110&q=icon%20for%20matplotlib&ved=2ahUKEwjE9ZCu6_KBAxVtV6QEHdyuBiQQMygDegQIARBL)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fuser-images.githubusercontent.com%2F315810%2F92255284-156f1180-eea0-11ea-9d2d-be8262670e8c.png&tbnid=s_ocSxDsnTkjZM&vet=12ahUKEwjd1MTO6_KBAxU3kicCHXAECvkQMygGegQIARBV..i&imgrefurl=https%3A%2F%2Fgithub.com%2Fmwaskom%2Fseaborn%2Fissues%2F2243&docid=vhVYirNQjejZJM&w=819&h=248&q=icon%20for%20seaborn&ved=2ahUKEwjd1MTO6_KBAxU3kicCHXAECvkQMygGegQIARBV)

![](https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F8%2F8a%2FPlotly-logo.png&tbnid=Amymi2H4BenB9M&vet=12ahUKEwjiv9q96_KBAxXDVKQEHXQGAmAQMygCegQIARAx..i&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPlotly&docid=5YCcidvLDTOu8M&w=1250&h=417&q=icon%20for%20plotly.express&ved=2ahUKEwjiv9q96_KBAxXDVKQEHXQGAmAQMygCegQIARAx)


## License
This project is licensed under the [MIT License](https://github.com/MosesMwalya/mobile_price_app/blob/main/LICENSE.md). You are free to use the code and resources for educational or personal purposes.

## Contributions
Contributions are welcome! If you would like to contribute to this repository, please follow the guidelines outlined in [CONTRIBUTING.md](https://github.com/MosesMwalya/mobile_price_app/blob/main/Contributions.md). Any improvements, bug fixes, or additional projects are greatly appreciated

## Feedback and Contact
I welcome any feedback, suggestions, or questions you may have about the projects or the repository. Feel free to reach out to me via email at moses.mutua@gmail.com

Enjoy exploring my data science projects!

