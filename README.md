Condo Comparison with Convolutional Neural Network (CNN)
===
![picture](/img/finalplan.png)
Database Schema
---
![picture](/img/schema.png)

The database schema will be refined through completing use cases on the application implementation.

USE CASE Example: Getting the User to Filter and Upload the Picture for Prediction
---

class models
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
The output in Flask will be 5 images from the database, derived by the CNN.

The Neural Network 
---
![picture](/img/vgg.png)
The CNN will use the pre-trained model VGG16 using Keras. 

* Convolutions layers (i.e. 3*3 size)
* Max pooling layers (i.e. 2*2 size)
* Fully connected layers at end
* Total 16 layers


The Recommendation Method
---
![picture](/img/knn.png)
The CNN will create an output value to all of the images.
The recommendation system will take the input image and predict by KNN.

Math behind implementation of K-Nearest Neighbor (KNN)
---
![picture](/img/euclidmath.png)
The prediction will output 5 images from the database based on KNN values.


