# KNN with Iris dataset
Using Skitlearn to practice KNN

![feature-image](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

#Data
We use the dataset in this link https://www.kaggle.com/datasets/uciml/iris

# Idea
1. Choose a K(int) before we start
2. We will calculate the distance(Euclid or Minkosky) from all data_points to the point 'P' that i will predict it's label
3. Select K points that are the nearest base on distance we calculate
4. If the number of one label is the highest, this point 'P' is set this label
5. Compare from the test and we adjust K to increase the accuracy.
![feature-image](https://media.licdn.com/dms/image/C5112AQFY4bX3Y7jcHA/article-cover_image-shrink_600_2000/0/1565431496642?e=2147483647&v=beta&t=N2zhB7OhvdTrebqNkY2lxMaPHqPYpA4r3nj88msI-e0)


# Method
1.Preprocessing
2.Train with Sklearn Modulo

# Update
1. Built KNN - modulo by myself in **K_nearest.py**
2. Run and visulize sample dataset in **main.py**

