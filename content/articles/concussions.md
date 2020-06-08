Title: Have NFL Rules Affected Concussion Rates?
Date: 2020-06-08 15:30
Author: Cameron Malloy
Category: Data Science
Tags: Permutation Testing
Slug: concussions
Summary: What is the overall sentiment of the bay area? What is the distribution of this sentiment? What are people happy or sad about in a given area? The San Francisco Bay Area is home to a very diverse population. There are many different people from different racial profiles.
Postid: 1

*Have the new NFL rules significantly reduced the number of concussions in a season? Or has the decrease just been random chance?*

## Introduction

After the discovery of [CTE](https://en.wikipedia.org/wiki/Chronic_traumatic_encephalopathy){target="_blank"} by [Dr. Bennet Omalu](https://en.wikipedia.org/wiki/Bennet_Omalu){target="_blank"}, the NFL has been under scrutiny for dismissing the effects of concussions and it's relationship to CTE. Over the past couple of years, the league has started to make rules to help defend players in an attempt to decrease the number of concussions. In 2017 the implemented the [targeting](https://en.wikipedia.org/wiki/Helmet-to-helmet_collision#:~:text=In%20the%20NFL%2C%20helmet%2Dto,of%2015%20yards%20for%20violations.&text=In%202017%2C%20the%20NFL%20adopted,offenders%20out%20from%20the%20game.){target="_blank"} rule which fines and throws players out of the game for purposeful helmet-to-helmet collisions. After that they changed the [rules for kick offs](https://www.sbnation.com/2018/5/22/17369774/nfl-kickoff-rule-change-explained){target="_blank"} to make them safer, there was a pretty big decrease in the number of concussions in 2018. There have been some [articles](https://www.nfl.com/news/nfl-sees-significant-drop-in-concussions-during-2018-season-0ap3000001013041){"target=_blank"} touting this progress, but is this deserved? After a slight increase in 2019, it's not clear cut as to whether these changes had any effect at all. We'll discuss how effective these rules have been and how well the NFL has done with these rules.

There have been rules put in place before 2017, however, the NFl only gives us data from 2012. Data before then may not be so great because concussion protocols and documenting concussions were more relaxed before then, so this is all the data I'm comfortable with analyzing.

Download the [R-Notebook for the statistical tests in this blog posts. There are only code blocks for permutation and multivariate regression tests, no explanations/comments]({static}/assets/concussions_assets/tests.Rmd){}

Download the <a href=./assets/concussions_assets/get_supplement_data.ipynb>Python Jupyter notebook to obtain supplemental data (see data section) for multivariate regression tests</a>

## Data

The NFL only has concussion data dating back to 2012 which can be found at [playsmartplaysafe.com](https://www.playsmartplaysafe.com/newsroom/reports/injury-data/){target="_blank"}. We'll only be working with the regular season totals shown below.

![img not found]({static}/assets/concussions_assets/concussions_table.png){}
<figcaption markdown="span">
Screenshot from [playsmartplaysafe in 2020](https://www.playsmartplaysafe.com/newsroom/reports/injury-data/){target="_blank"}
</figcaption>

Later in the post will analyze possible confounding variables. Data for that analysis were statistics from [pro football reference](https://www.pro-football-reference.com/){target="_blank"}

## A/B Testing

<ul markdown="1">
<li>
**Null Hypothesis:** *The rules implemented post 2017 and post 2018 had no effect on the number of concussions in a regular season. Any differences are due to random chance*
</li>
<li>
**Alternative Hypothesis:** *The rules were statistically significant in decreasing the number of concussions in the regular season*
</li>
<li>
**Statistic:** *The statistic we'll be measuring is the average number of concussions before the rule changes minus the average number of concussions after the rule changes*
</li>
</ul>

I chose to carry out the A/B Test with a permutation tests. For those not familiar, we set up the null and alternative as above. Under the null, we assume that no matter the rule changes in any year, it doesn't effect the number of concussions, so we can permute the concussion numbers and associate them with different years, then compute the statistic. We repeat this 10,000 times and then we have an accurate distribution of the statistics look like under the null hypothesis. Then we can plot the actual statistic. If it's far off from the distribution created, then we can say that the null hypothesis is very unlikely and we'll sway toward the alternative.

Since targeting was one of the first major rules to address concussions, we'll start there. The control group are the concussion values for the years 2012 to 2016, and the treatment is 2017 to 2019 (the treatment being rules to help mitigate concussions). Here's the resulting permutation test visualization.

![img not found]({static}/assets/concussions_assets/2017_ab_test.jpg){}
<figcaption>
Permutation test for concussions pre and post 2017 (2017 included in post). The blue line is the observed statistic
</figcaption>

The blue line is the observed statistic found with the real NFl data. The graph clearly shows that reality is quite in line with the null hypothesis distribution created. In addition it has a *p-value of 0.39*. It's clear that we fail to reject the null hypothesis here.

The NFL stated the concussion rule changes a great success after a pretty steep decrease in concussions in 2018, so I decided to see if the new rules they implemented for the 2018 season had any significant effect. Here's the permutation test visualization.

![img not found]({static}/assets/concussions_assets/2018_ab_test.jpg){}
<figcaption>
Permutation test for concussions pre and post 2018 (2018 included in post). The blue line is the observed statistic
</figcaption>

Again, the blue line is the observed statistic. And while this fairs much better than the previous test, a *p-value of 0.147* doesn't meet the 90% or 95% confidence threshold. Again, we fail to reject the null hypothesis.

This quick analysis shows that on the surface level, the change in concussions over recent years have been due to random chance. However, there is one caveate that we haven't given the NFL enough credit for.

## Data Augmentation

![img not found]({static}/assets/concussions_assets/time_series.jpg){}

Above is the data we've been working with plotted as a time series. Notice the large dip in 2014. 2014 actually had by far, the largest number of unique players designated as "out" (injured and did not play for at least a game) of all the years analyzed at 605 players. The next closest year comes in at 470. It also had about the same number of kickoffs and plays as the other years. This huge drop in concussions is unprecedented. This is likely because of rule changes that resulted in players needing time to learn them, effecting their tackling. It could also be because player's were just more cautious (also because of rule changes or personal reasons), or teams were overly cautious. There could be more reasons or none of these reasons it's hard to tell, however, this dip in concussions is quite strange. Thus, I re-ran the A/B tests, but I changed the 2014 value to the mean of the concussions from 2012 to 2017 (the control and including 2014). This is a large change that doesn't necessarily reflect reality, but I think it's fun to see how this changes the statistical tests. I only ran the statistical test where the treatment were the years 2018 and 2019. It had a *p-value of 0.035* and its visualization is below.

![img not found]({static}/assets/concussions_assets/2018_ab_test_augmented.jpg){}

So now it seems like the NFL rules had a big change, only if 2014 was a more normal year. But this comes with it's own challenges. Before I brushed over some of the assumptions A/B tests follow. They require that the only difference between the control and treatment groups is the treatment itself. In other words, no confounding variables. This wasn't necessary to state before because we didn't find anything statistically significant even with possible confounding variables present.

3 notable confounding variables come to mind. The number of unique players who were injured, number of plays, and number of kickoffs over the course of the regular season.

## Multivariate Regression

In multivariate regression, we can include the confounding variables and see if the variable we're analyzing really is a strong predictor of the number of concussions. Without the data augmentation, we find that no matter the combination of indicator variables for years (pre-exclusive and post-inclusive 2018) and confounding variables, we still don't find that the rules put in place are statisticallly significant in reducing the number of concussions.

![img not found]({static}/assets/concussions_assets/lm_res.png){}
<figcaption>
Result of R's Linear Model summary function on concussions data with the year indicator variable along with confounding variables. unique_outs: Unique players classified as "out" and did not play in a game because of injury, plays: number of plays, scores: number of scores (TDs and kickoffs) meant to resemble the number of kickoffs. All variables are regular season stats from pro-football-reference [see Data section above].
</figcaption>

The `year_indicator` variable is what we're most interested in. It has a large standard error, so it's hard to say whether the estimate for this linear model is as estimated or should be 0. So in these terms, the NFL rules did not have much of an effect (if any at all) on the number of concussions in the regular season. However, how does it perform on the data with the outlier removed?

As expected, it does much better. Combined with some confounding variables, such as only the unique number of players classified as "out" once in a season, it's a statistically significant predictor. However, when faced with mutliple confounding variables, it continues to miss the mark (i.e. it's hard to differentiate the estimate with 0 like before). So, depending on the confounding variables in reality, we can't say that the rules have significantly affected the decrease in concussions considering the data we have.

![img not found]({static}/assets/concussions_assets/lm_res_aug.png){}
<figcaption>
Result of R's Linear Model summary function on augmented concussions data with the year indicator variable along with confounding variables. unique_outs: Unique players classified as "out" and did not play in a game because of injury, plays: number of plays, scores: number of scores (TDs and kickoffs) meant to resemble the number of kickoffs. All variables are regular season stats from pro-football-reference [see Data section above].
</figcaption>

## Conclusion

The short answer to this question is no, the NFL's rules haven't done enough to say that they are the reason concussions were down in recent years. There is an argument to be made for the NFL that the data we have is very small and it's hard to come to statistical conclusions with this little data. However, when dealing with something as big as CTE and protecting the players that make the league money, the NFL should be doing something with extreme noticeable impact to help them. I hope to see a larger drop in concussions soon. I hope this post is shown to be wrong in the near future.
