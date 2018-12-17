A Data Driven Web Application with Machine Learning in Keras to Image Search the Boston Real Estate Condo Market
===
![picture](/img/glass.jpg)


Application
---

- Flask: Python web application

- Keras: convolutional neural network

- Numpy: nearest neighbor algorithm

- Postgres: SQL database

This application will allow users to input condo images and output similar images by feature extraction from a pre-trained model using a convolutional neural network and retrieval classification algorithm. 


URL:        http://faspeculator.herokuapp.com/

Screencast: https://www.youtube.com/watch?v=2-ZgUKFmphw

Github:     [GitHub Pages](https://github.com/fimhub/speculator/)



CODE NAVIGATION
---
```
1. Open .ipynb and run in Jupyter
   - **condo.csv** (condo data) and **condo_images.csv** (picture array) are created
```

```
2. Create database 'speculator_db' in Postgres 
   - use **model.sql** to create tables and relationship
```

```
3. Run scripts to import data from .csv files into Postgres
   - use scripts **import_condos.py** and **import_images.py**
```

```
4. Run Flask 
   - python3 **routes.py** in command line
```


USER NAVIGATION
---
-functionality picture upload, predict, results, favorites, account.
picture

results

favorites

account

index (no idea) - results and idea of app.










