Condo Comparison with Convolutional Neural Network (CNN)
===
![picture](/img/finalplan.png)
Database Schema
---
1. During the start of development all of the condo data elements will be put into one table.
![picture](/img/condostable.png)

USE CASE Example: Getting the User to Filter and Upload the Picture for Prediction
---

2. The database schema will be refined by completing use cases on each implementation to the application.


class models to filter and upload USE CASE example
![picture](/img/model.png)

PostgreSQL implementation to USE CASE example:

```
Table: public."Users"

-- DROP TABLE public."Users";

CREATE TABLE public."Users"
(
  uid integer NOT NULL DEFAULT nextval('"Users_uid_seq"'::regclass),
  username character varying(255),
  password character varying(255),
  "createdAt" timestamp with time zone NOT NULL,

  CONSTRAINT "Users_pkey" PRIMARY KEY (username)
)
WITH (
  OIDS=FALSE
);
```

```
-- Table: public."Filters"

-- DROP TABLE public."Filters";

CREATE TABLE public."Filters"
(
  id integer NOT NULL DEFAULT nextval('"Filters_id_seq"'::regclass),
  "beds" integer NOT NULL,
  “baths” integer NOT NULL,
  “zip” integer NOT NULL,
  “photourl" character varying(255),
  "createdAt" timestamp with time zone NOT NULL,
  "username" character varying(255),

  CONSTRAINT "Filters_pkey" PRIMARY KEY (id),
  CONSTRAINT "Filters_username_fkey" FOREIGN KEY ("username")
      REFERENCES public."Users" (username) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE SET NULL
)
```

The next use case will be implement the favorites function to the application
---

class models to favorites USE CASE example
![picture](/img/followmodel.png)

Focusing from the perspective of how the data is being stored in the database provides clarity on how the functions in the model should be called.   
![picture](/img/followhow.png)

As a result, the database schema can incrementally be refined one use case at a time.
![picture](/img/followsschema.png)

3. The final schema will adhere to 1NF, 2NF, 3NF, and BCNF (NF - normal form)
![picture](/img/schema.png)

Once all use cases have been completed will the database schema be able to finalize.




Teamwork
---
A parable on making full use of a team to make a great product:

[![Teamwork](https://i.imgur.com/OORFH52.jpg)](https://www.youtube.com/watch?v=K-Yv-UdsmSo "Teamwork")

![alt text][logo] We are avoiding the path to least resistance: 
```
Less of this - "You do your thing. I will do my own thing. Let's meet up later."  "Okay."

We want to avoid building a scaled-down version limited by integration headaches.  
However, this does not mean we want to avoid difficult challenges.
```

![alt text][logo] We are going into the rock tumbler instead: 
```
More of this - "See my classification system to identify beds, kithen, etc?"
"Okay. Wait. No. Let's not train the model. Vector image output only."   

We are focused on working on the code set together as a team,
to polish the application and make the best product possible.
```
[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text"


The Web Stack
---
![picture](/img/stack.png)

We will focus on the Flask and Postgres components to the web stack.
A user should be able to logon and upload an image in Flask.  
The output in Flask will contain 5 images from the database, 
which will be derived by prediction from the CNN.

The Neural Network 
---
Please refer to the Python Notebook to see how the CNN was implemented.

![picture](/img/vgg.png)

The CNN will use the pre-trained model VGG16 for feature extraction through Keras. 

* Convolutions layers (i.e. 3*3 size)
* Max pooling layers (i.e. 2*2 size)
* 16+ layers


The Recommendation Method
---
![picture](/img/knn.png)
As a basis for similarity search, the CNN collects features from the input image to enable the k-Nearest Neighbors (kNN) algorithm by classifying it against other images in the database.

Math behind implementation of K-Nearest Neighbor
---
![picture](/img/euclidmath.png)
The quality of the prediction will be based on the kNN values.  Other classification algorithms will be evaluated to improve the recommendation.


