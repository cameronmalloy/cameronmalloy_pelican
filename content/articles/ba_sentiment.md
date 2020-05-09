Title: Bay Area Twitter Sentiment During a Pandemic
Date: 2020-05-06 15:30
Author: Cameron Malloy
Category: Data Science
Tags: NLP, Deep Learning, Clustering
Slug: ba-sentiment
Summary: What is the overall sentiment of the bay area? What is the distribution of this sentiment? What are people happy or sad about in a given area? The San Francisco Bay Area is home to a very diverse population. There are many different people from different racial profiles.

*What is the overall sentiment of the bay area? What is the distribution of this sentiment? What are people happy or sad about in a given area?*

## Introduction

The San Francisco Bay Area is home to a very diverse population. There are many different people from different racial profiles.

<figure markdown="span">
![img not found]({static}/assets/ba_sentiment_assets/ba_race_demos.jpg){}
<figcaption>
Data taken from <http://www.bayareacensus.ca.gov/bayarea.htm>
Original data is from the *2010 United States Census Summary File 1*. United States Census Bureau
</figcaption>
</figure>

What's more interesting is that individuals of the same race tend to live around each other. The reasons behind this could be due to a multitude of reasons. One may be a want to be near social connections. Another may be housing, employment, and police discrimination, separating races.

**Race and Ethnicity 2010 - San Francisco Bay Area**

<center>
<figure markdown="span" id="ba_race_map">
![img not found]({static}/assets/ba_sentiment_assets/ba_race_map.png){}
<figcaption>
Data from the *2010 United States Census Summary File 1*. United States Census Bureau. Each dot is 25 people: <span id="red_color">White</span>, <span id="blue_color">African American</span>, <span id="green_color">Asian</span>, <span id="orange_color">Hispanic</span>, or Other (yellow)
Map by Eric Fischer: <https://www.flickr.com/photos/walkingsf/5560477152/>
</figcaption>
</figure>
</center>

Furthermore, these racial clusters tend to define the cities they are in. Despite being in close proximity with each other, each city has its own distinct culture. This is what provoked the question in the beginning of this post. What if we figure out which cities are happier than others at certain points in time? With this classification, we can possibly find out what people are happy or concerned about, something we can't do without surveys and directly interacting with people.


## Data Gathering

### Training Dataset

I used the Sentiment140 dataset. It has a large dataset of tweets which the algorithmically determined was either positive or negative based on emojis and keywords. This was the only dataset I found that was large enough to train a neural network.

### Test Dataset

I combined two test datasets. The first one is provided by [Sentiment140](http://help.sentiment140.com/for-students), the second is created by [Sanders Analytics](https://github.com/zfz/twitter_corpus). It's important to note that didn't use Sentiment140's neutral tweets, and instead relied on Sanders Analyitcs neutral tweets. Since I trained the model on only positive and negative tweets, having a large number of neutral tweets to adjust thresholds to classify neutrality isn't feasible. I looked over both datasets and I chose Sanders Analytics' neutral because the tweets were more diverse.

### Application Dataset

I had access to a large corpus of geotagged tweets, however, they didn't have the tweet's texts. Twitter's API couldn't find the tweets, likely because it was so long ago. So I decided to create my own dataset.

I gathered all data within 40 miles of the center of the San Francisco Bay from Twitter's API. Twitter has a way of reverse geocoding tweets even if the user doesn't share their location. I gathered 700,000 tweets from this area that were tweeted between April 25th and May 2nd of 2020.

Twitter allows users to set their location. They can set it to anything, it doesn't have to be their location at all. You could live in San Francisco but set your location to Kuala Lumpur. So I only took the tweets that had users who's location was a bay area city. The thought is that if they tweeted from within the bay area and their location is set to a bay area city, then there's a high likelihood that they live in that city. I ended up having about a quarter million tweets in my constructed dataset.

## Models

The goal is to build a classifier that takes in a tweet and outputs its sentiment, -1 for negative, 0 for neutral, and +1 for positive.

I started with a baseline model of Naive Bayes, however that showed that it was slightly better than guessing. Logistic regression didn't converge. I also didn't try an SVM because the training set had only positive and negative values, yet we also needed to compute the neutral tweets which would use thresholds on probabilites predicted by the classifier, which SVM's aren't necessarily great at. Then, I turned my attention toward neural networks, specifically LSTMs and GRUs. Due to financial and computational constraints, I was limited to Google Collaboratory for this part of the project, so BERT models didn't run well or else I would have fine tuned and compared those as well. Below are the accuracies for each model.

<figure markdown="span">
![img not found]({static}/assets/ba_sentiment_assets/model_comparison.jpg){.wp-image-104}
<figcaption>
Numbers in parentheses are the number of units associated to the layer. Each LSTM and GRU layer are bidirectional. Each neural network had a dense layer with 64 output units with a ReLU activation followed by another dense layer with 1 output unit with a sigmoid activation. Also, each neural network had a global spatial dropout of 0.5. Due to computational and time constraints, each network was trained for 3 epochs. Each model is based on the threshold criteria of predicting neutral if the prediction is between 0.3 and 0.7 (not inclusive).
</figcaption>
</figure>

I chose to go forward with the GRU and convolutional network in bold in the table. This had less parameters than the GRU with 128 units, so this likely had a slightly lower variance. I trained this model for 10 epochs. After analyzing ROC curves to find the best thresholds, the model gave the following confusion matrix.


![img not found]({static}/assets/ba_sentiment_assets/confusion_matrix_lstm_conv.png){.wp-image-105}


When you’re ready to publish, give your post three to five tags that describe your blog’s focus — writing, photography, fiction, parenting, food, cars, movies, sports, whatever. These tags will help others who care about your topics find you in the Reader. Make sure one of the tags is “zerotohero,” so other new bloggers can find you, too.


## Sentiment

Applying the model to the bay area tweets gives way to the following city sentiment map

<iframe width="100%" height="520" frameborder="0" src="https://cameronmalloy.carto.com/builder/436dbea1-daff-4fdd-b4ad-9dc1264360c3/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

The map shows an average of all the tweets sentiment values from each city. Comparing just positive and negative tweets versus the overall average including neutral tweets yields similar values. The large number of tweets from each city discouraged me from normalizing any values, since this average is likely to be close to the true average of the city. Almost all cities had large sample sizes (2,000 to 5,000) except a couple small ones like Yountville and St. Helena.

It's important to note that almost every city was positive to an extend on average aside from a couple cities. The bay area seems to be a very positive place! I chose this color scheme, not so that pink and red represents negativity, but rather because those cities are more negative on average compared to the rest of the bay area.

The stark contrast between the peninsula and East Bay is astonishing. The next section will be dedicated toward a way to extract what people are happy and sad about.

Given the data was over one week during the extension of the COVID-19 shelter in place order, it would be interesting to see the sentiment for tweets relating to corona virus and the quarantine.

<iframe width="100%" height="520" frameborder="0" src="https://cameronmalloy.carto.com/builder/2bf5c2c2-b229-4321-bc7e-35704761c585/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

Corona virus tweets accounted for 5% of the data and didn't effect the overall sentiments significantly. I had to plot this at the county level so the sample sizes were large enough to give a proper estimate of the sentiments. It's important to note though that Napa county only had 7 tweets relating to COVID-19.

Example corona virus tweets:

Negative tweet:
> ✔️ Largest wildfires in modern history <br />
> ✔️ Senate acquits of Donald Trump <br />
> ✔️ Death of Kobe Bryant <br />
> ✔️ Global Pandemic <br />
> ✔️ Financial Crisis <br />
> ✔️ "Murder Hornets" discovered in US <br /> <br />
> Whatchu cookin' up next, 2020? 🙃

Neutral tweet:
> My husband has been restaurant-phobic since this whole quarantine deal started up. I’ve *finally* convinced him to take a shot on some Chipotle takeout tonight. Nature is healing.

## Clustering

The theory behind clustering these tweets is stems from the thought that people who are tweeting about positive things are likely tweeting about similar things. Similarly for negative things. So, we can separate the groups positive and negative tweets, and cluster them into groups and see if they have any similarities.

If done correctly, this would give government and political officials a way of knowing what people are happy about and what people are unsatisifed with in their city or governing area. Previously, the only way of consolidating such information would be through surveys which are expensive and could have a low turnout depending on the location.

### Case Study: Berkeley

The first clustering algorithm I used was K-Means, however, the data showed to be unfit for K-Means. I switched to Agglomerative clustering. This type of clustering doesn't work well with large datasets, so I decided to take only Berkeley's tweets cluster those.

Below is the dendrogram for Agglomerative Clustering using [Ward's method](https://en.wikipedia.org/wiki/Ward%27s_method) with Berkeley's positive and negative tweets.

<figure markdown="span">
![img not found]({static}/assets/ba_sentiment_assets/dendrogram_styled.png){}
<figcaption>
I had to omit the x-axis values since there were so many samples, it looked like a thick black bar. With over 2,000 samples in each dendrogram, there was no way to fit it neatly on the x-axis.
</figcaption>
</figure>
