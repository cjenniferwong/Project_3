## Project Design Summary
For project 3, I was interested in if I was able to predict whether or not two people would match. To answer this question, I found a dataset on Kaggle from Columbia University in which they conducted a Speed Dating Experiement, and released the data in a csv. Upon inspect the dataset, I realized that there were many categorical columns, as well as missing data that I would need to impute. 

I hope to be able to use this model for future application in larger companies that have more data for me to train on. From then, I hope to use it to make recommendations to introduce users to each other based on their probability of match.

However, I have to keep in mind the bias in my data. This study was done on traditional college population at Columbia University--majority people in their early to mid twenties. In fact, one of the questions that the survey asked was about their goals and intentions going into this experiement. By far, the most popular answer was "it seemed like something fun to do" and "i wanted to meet someone new". These are not reflective of someone interested in long-term/serious commit relationships in the traditional/explicit sense. This helps to explain why my model.

## Data

#### Cleaning and Imputing Data
I systematically imputed the data of the different time stamps beginning with the inital time stamp (survey conducted prior to the speed dating event). I tried to match the results to see if they were listed in the partner's feature attributes, and perhaps match it to the iid and then impute it that way. If that was not possible, then I would have imputed the data from taking the median value for each attribute from the entire dataset, after grouping by age and sex as I think that would refine my results to be a little more accurate.

Time s obtained their values during the middle of the survey. I made the assumption that there would be no difference between the middle of the speeding dating event, and the survey results collected before the event, so I just imputed the data from time 1 of the same person, and if they were missing the results there I took the median of time s from that person's sex and age.

Please note that time 2 feature results were taking a day after the speed dating experiement. Naturally, we can expect that there is a drop off in participation the longer it's been since the intial interaction. This was confirmed by the increase in the number of missing cells for the time 2. I impute the data from the median of the person's age and sex. I was interested to see if there was a change in these values from the different time stamps between time 1 and time 2 so I kept those values separate.

This was again done the same way for time 3.

#### Exploring the data
I created a heatmap of the correlation of the dataset to see if there would be any insights that I could glean from the visual representation. I did notice that there were several clusters of high heat/correlation, and kept that in mind during further exploration and analysis.

## Tools Used

I utilized many sklearn models (Bagging, Decision, Random, SVC, Logistic). I also tried to use PCA to reduce the number of columns that I had from 305 to something more managable.

For visualization, I created an interactive flask app that tried to predict whether or not two people would match based on how much they each valued 6 attributes in a partner: attractiveness, intelligence, sincerity, ambition, fun, and shared interests.

These features were determined to be of importance from a Random Forrest Classifier and the feature_importance_ property that it had.


