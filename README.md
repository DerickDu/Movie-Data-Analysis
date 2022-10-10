# Movie-Data-Analysis

Introduction:
Nowadays, watching movie is a good way to kill time and entertain ourselves. In terms of audience, they want to know what kind of movie is great and popular. On the other hand, if some investors want to get into the movie business, but they have no prior experience in the field and will need assistance to make their movie studio a success. They may pay more attention to what factors is significant to the revenue or popularity. Therefore, this movie metadata is sufficient to make us figure out the haziness and doubt mentioned above. In addition, the data here is with enough size and type. In the csv file of movie metadata, we have records more than 45,000 records. Moreover, there are many kinds of data in this data set. There are categorical feature and continuous feature in the dataset. According to the reasons above, this dataset is perfect for us to engage in.
The purpose of this report is to address the questions below.

1.	We wanted to discover if a film's initial budget had an influence on its ultimate revenues and, if so, what the impact trend was.
2.	Are there substantial differences between English-language films and those in other languages in certain variables? Can we determine a film's linguistic kind based on these differences?
3.	In which month of the year will the most films be released? Are there any clear changes in the cost and advantages of movies released at different times, as well as their ratings? This can assist us in determining when the best moment to release a film is.
In terms of the predictive models, we 
1.	In order to figure out what features or variables have significant impact on the popularity, we need to make a regression model to predict the popularity of movies. There is no question that this model is considerable and beneficial to filmmakers.
2.	To some extent, the rating of audience has a strong influence on the revenue or the popularity of a movie. Therefore, we plan to make a regression model to predict the rating of voting by observer.
3.	Return on Investment is the one of the most significant index for filmmakers and investors. We plan to make a classification model to predict what kind of features have strong impact of getting high ROI level.
The exploratory data analysis will be carried out initially in order to reveal some interesting data and address the questions attached above. The dataset will then be used to create a Lasso Regression, a Gradient Boosting Regression, a Random Forest, and a Decision Tree Classification model to answer the four questions given.

 
Exploratory Data Analysis:
Data Extraction:	
The dataset we chose to set out this capstone project is about 45,466 movies. There are 24 features in this database, including cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts, vote averages and so on.

Data Cleaning:
	First of all, we drop the duplicate data. In terms of the numeric variables, we fill the null value with the average of each feature. In addition, the NAs in object variables which doesn’t affect the analysis, are filled with a space. After dropping another not useful rows and columns, we use budget and revenue to create two new features to better analyze latter, including profit and ROI.   
	Because the data of genres and production countries are stored as like a dictionary, which were scaped from the websites. Therefore, we need to extract the useful information from those variables. In order to make the later analysis feasible and meaningful, after extracting the data from genres and production countries, we create a new data frame with the genres stacked, due to that each movies have many genres.  
	The first model of Lasso regression filters out the movies budget less than $1,000. In addition, in order to analyze the impact of release month, we create a new feature is_holiday to set Month Jan, April, May, Sep, Nov, and Dec as holiday month. In terms of the languages and the countries, we select 4 main value and set rest of them as other.

Data Visualization:
	Here is the Word cloud of overview of movie. We can clearly notice that the movies with topic life or find or love enjoys great numbers. 
 
According to the density graph of average rating, there are many voting rate centered around 5-7. In terms of how long the movie is, most movies are 120mins.
     
	Revenue is worthy of consideration for filmakers and investors. The distribution plot of the revenue tells us that most of the movies only have around 10 millions revenue. But there are very profitable movies, but very few.
 
	In terms of the genres of movies, there is a great number of movies in Drama (20,244), followed by Comedy (13,178). Other kinds of the movie are much fewer than those two main genres.
 
	
	This graph attached below give us some information about the possible relationship between revenue and budget. When the budget increase, the revenue will rise, which shows the positive relationship between those two features.
 
	Here is a correlation matrix of those numeric data. According to the graph, we can notice that revenue and budget indeed have positive relationships. The popularity do not have that strong relationships between other features. In terms of the vote count, there are many possible relationships we can focus on and dive into.
 
Question 1: 
	We take these two features into consideration and make a regression model. In accordance with the results of the OLS regression, the R2 is 0.53, which is not bad. In addition, the coefficient of the budget is 3.02 with 0.000 p-value, which is highly confident and creditable. 
    
	Therefore, we can conclude that the more budget you invest, the more revenue you gonna get. When the budget increase 1,000 dollars, the revenue will rise by 3,020 dollars. 

Question 2: 
In this problem we want to know the language in the film the other properties of the films on what is reflected, the data set we have a total of more than 80 kinds of film language, this analysis does not make sense and takes a long time, so we will film language into English and non-English, on this basis to explore difference between English movies and English movies.

Then we look at some basic data of movies according to their language classification.
   
   

Figure. The gap between films in different languages

It can be found that in terms of budget, revenue and net profit, English films have higher figures, while non-English films reflect the characteristics of low cost and low profit. This is logical, because English films are the mainstream in the world, and in terms of film investment, English films also have obvious advantages, which naturally have the characteristics of high investment and high return.
However, there is no obvious difference in the length of films between the two. In terms of the average score of films, the average score of English films is slightly lower than that of non-English films. The average number of votes cast for English films is much higher than that for non-English films, which shows that English films can reach more audiences.
When we study the difference in the release time of the two kinds of films, we find that the release time of both English and non-English films is concentrated in the second half of the year, and there is no significant difference in the trend of release time between the two.
  
Figure. The distribution of the release time of the two kinds of movies

Question 3: 
In question 3, we first want to know in which month of the year the most films will be released. We can know the most popular movie month and find why so many movie choose to be release in such a time. Here is the plot that show the number of movies released in each month:


 

We can see that January is the most popular month to release a movie. After September, which is during September, October, November, December, many movies are also released at this time. The reason may be there are many holidays and new year during these months. 

Then we also compared the budget, revenue, as well as their ratings during the different months. The following three plots show the relative change:
 

We have the following findings based on previous results:
1. Budget and revenue are highly related, which are both highest in the May, June and July (Summer).
2. During the January, there are many movies released at this time, but the budget and revenue are not high for these movies. A possible reason is these movies are for the new year, and most of them may be comedy or the type that could be watched by the whole family.
3. There are no obvious difference of the ratings of the movies in each month.

 
Predictive Models:
Model 1:
In order to figure out what features or variables have significant impact on the popularity, we need to make a regression model to predict the popularity of movies. There is no question that this model is considerable and beneficial to filmmakers.
	First of all, we did a simple regression with 4 numerical variables budget, runtime, vote_average, and 4 categorical variables country, language, genres and is_holiday. However, the R2 is only 0.12, which indicates the regression results is really bad. Therefore, we try to use Lasso regression to avoid the overfitting. 
	 After building the Lasso regression model, we got RMSE 9.27 but the R-square still very low (0.16), which indicates that this regression model is bad. The coefficients of the variables are shown in the plot below. In addition, the lines of MSE of Lasso are not converged. Therefore, popularity is hard to predict by these variables in our data.
 
 
Model 2:
To some extent, the rating of audience has a strong influence on the revenue or the popularity of a movie. Therefore, we plan to make a regression model to predict the rating of voting by observer
For the evaluation of a film, the average score of the film is a very important factor. We try to predict the average score a movie is likely to receive using known variables, such as the movie market, the movie budget and profit, the release month and the movie genre.
Different from ordinary movie rating levels, the score in the data set is a continuous variable between 0 and 10, so we will use regression model to predict movie scores in this problem.
We first divided the data into training set and test set and used the simplest regression curve model for the first step of prediction. We can see that under the result of fitting, there is a big gap between the predicted data and actual data, and the R squared is 0.4.
  
Figure. The parameters of linear regression.

Then we made a fitting comparison diagram between the predicted data and real data and found that the predicted data would have some extreme prediction results with greater fluctuations, but the data were distributed in the high score range as a whole, while the low score data in real data made it difficult for the prediction model to predict success.
 
Figure. Comparison of forecast and actual value.
By checking the normality and independence of the model, we found that there was no problem with the model, which indicated that in this model, the effect of the model was not good, so we need to use other models to see the results.
 
Figure. The normality of the linear regression

Then we use the more complicated machine learning model to forecast the film scores, we first use the decision tree, by changing the depth of the tree, we found that the fitting accuracy score increased significantly, and the decision tree to get closer to 0.5 points in this problem when the depth is 20, this is great progress compared with the linear regression, but we still want to try other model, See if there's a model that gets better results.
We then tried the gradient model, the popular machine model, and tried to test the predictive power using the same data set without changing any parameters. It was found that the gradient model performed better than the decision tree, with a model score of more than 0.5.
Finally, we try to use of random forests for modeling and forecasting, which is one of the most commonly used machine model, we by changing the number of random tree, to adjust the model prediction efficiency can get closer to 0.8 model score, the score has been very good, through the random forest we can rely on and properties of the film itself to forecast the film scores, And this has given us a very close approximation of the trend in the original data. 

Model 3:
Return on Investment is the one of the most significant index for filmmakers and investors. We plan to make a Decision Tree classification model to predict what kind of features have strong impact of getting high ROI level. Therefore, we create a new feature roi_level to indicates high positive ROI, low positive ROI and negative ROI. 
In this model, we put features budget, language, country, and genres into the classification. For those categorical variables, we create dummy variables to make the model feasible to run. 
Gini is used as the loss function in the decision tree to show the degree of chaos. To avoid overfitting, the maximum depth is set to 4. The decision tree's accuracy is calculated as 0.7153 by creating classifications for the test set. That means our model is perfect to use to classify the ROI level.

  
Conclusion:
Summary:
In this project, we compared the films with different characteristics, such as the released month, the language of the movie, the genre and the budget. In the EDA, we can conclude that the more budget you invest, the more revenue you gonna get. In addition, Comedies, thrillers, fantasies, and romances, which are normally more popular, do not score so well, particularly horror films. Moreover, we discovered that both English and non-English films release in the second part of the year, with no significant defference in release time trends between the two. 
After that, we got a general idea about what make a movie successful. Then focused on some key features, we built models to predict the popularity, the rating, and the revenue of a movie. The Random Forest model given us a very close approximation of the trend in the original data. The Gradient Boosting Regression is perfect to perform a reasonable solution to predict revenue. In terms of the Decision Tree model, the accuracy 0.71 indicates that we are confident to classify what kind of movie will get high ROI or negative ROI. 
Recommendation:
Through the study of the movie data set, we predict some of the attributes of the movie through the characteristics of the movie itself, and at the same time deeply understand the trend of the movie in some aspect. Such as movie theaters in let's guidance in the movie of the year is usually concentrated in the second half of the year and the January of the next year because those time have more holiday time, and the quality of the film in this period is generally higher, we suggest that the viewing audience without clear goals, so in September, October, November, December and January are good viewing time. At the same time, although non-English films are not accepted by everyone, there are many excellent films worth enjoying.
In terms of film types, many films that are not accepted by everyone, such as non-fiction films and musicals, can often produce good films that make a profound impact on people. We recommend audiences to try different types of films.
Finally, it is possible to use the basic information of a movie to predict the success of a movie (including the movie's evaluation, score and income, etc.). This kind of prediction can give the audience some psychological expectations before releasing of movies and give the developer more opportunities to prepare and improve the movie, which is also a good application of data analysis.
 
Reference:
[1] The Movies Dataset. (2017, November 10). [Dataset]. https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv 
[2] Kirenz, J. (2021, December 27). Lasso Regression with Python. Jan Kirenz. https://www.kirenz.com/post/2019-08-12-python-lasso-regression-auto/ 
[3] Python Decision Tree Classification Tutorial: Scikit-Learn DecisionTreeClassifier. (n.d.). DataCamp Community. https://www.datacamp.com/community/tutorials/decision-tree-classification-python 
[4] Eric Matthes (2019), Python Crash Course, 2nd Edition: A Hands-on, Project-Based 
Introduction to Programming, ISBN 978-1-59327-928-8, published by No Starch 
Press.
[5] Haijun (2019.1.29), Classification Algorithm -- KNN Algorithm (theory and Python 
Implementation)[Website], Retrieved from: 
https://blog.csdn.net/weixin_43216017/article/details/86679334 

