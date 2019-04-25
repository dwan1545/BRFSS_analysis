# BRFSS Analysis
### Exploratory Data Analysis of Substance Use and Social Determinants of Health Using the BRFSS Data Set
-----
**Overview and Reproducibility**

I conducted this project as part of the K2 Data Science bootcamp within a 1 - 2 week timeframe. My primary goal was to answer how has tobacco, alcohol, and Marijuana use are related to a variety of demographic, social, mental, and behavioral factors, and how, if at all, this has evolved over the years.

This project was conducted using BRFSS datasets from 2013 to 2017, Python 3.6.5, and a variety of packages as detailed in requirements.txt.

In order to replicate this project, you can follow along in the Jupyter Notbooks in the notebooks folder of this repo, which walk through data acquisition, cleaning, and exploration.

-----

# An Exploratory Analysis of Substance Use Across Social Determinants of Health

Given the current climate around substance use, marijuana legalization, and the general focus around social determinants of health, I wanted to use my newly acquired data-science skills to take a deeper look at the current state of these factors. The CDC conducts an annual survey of over 400,000 interviews every year by phone, called the Behavioral Risk Factor Surveillance System (BRFSS), which provides an excellent source of data to understand trends and differences in substance use across several different factors, including mental health, social determinants of health (e.g., ability to pay rent), and a variety of demographic factors. This project explores this rich dataset, in an attempt to further understand how substance use varies across our society.

## Key Findings

- The BRFSS data set provides a rich source of information to profile tobacco use, alcohol consumption, and marijuana use across demographic, geographic, social, and mental health factors
- Binge drinking and marijuana use for pleasure tend to occur more in younger age groups, students, and individuals who have never been married and is generally unassociated with income levels
- On the other hand, every-day tobacco usage tends to occur more in middle age groups and individuals who are separated / divorced, unemployed, and from lower income levels
- Almost all substance use is significantly higher in individuals with higher stress, poor living situations, poor financial health, and generally poor mental health
- Every-day tobacco usage has declined across a majority of states since 2013
- In the same time frame, mental health has also deteriorated across a majority of states, with a higher proportion of individuals indicating greater than 10 poor mental health days in the past 30
- States with greater deterioration of mental health saw less significant reductions in every-day tobacco usage

## Data Overview

The BRFSS is an annual survey conducted by the CDC across all states in the U.S. It includes over 400,000 interviews of adults (>18 yrs) conducted over landlines or mobile phones. Further information [can be found here.](https://www.cdc.gov/brfss/about/index.htm)

The questionnaires used in the survey encompass a broad array of topics, from basic demographic, census-style questions to questions around chronic health, substance use, diet, and mental health. There are a core set of questions asked to every respondent as well as rotating optional sections asked to a sample of respondents. The optional sections change every year and include topics such as marijuana use and social determinants of health.

This project focuses on the 2017 BRFSS. Below is an overview of the variables used for analysis in this project.

#### Demographic:
These variables describe basic characteristics of the respondents, such as age and gender.
![alt text](./reports/figures/demographics.png)

#### Environmental:
These variables describe advanced characteristics of respondents, including self-assessments of mental health, financial / social situations, etc. These variables are only available for a selection of respondents.
![alt text](./reports/figures/environmental.png)

#### Target Variables:
These are variables we are interested in exploring further, including tobacco use, alcohol consumption, and marijuana use. We will explore the association of these variables with the demographic and environmental variables below, but briefly, the target variables are self-assessments that include:

- Smoking Frequency: How often a respondent smokes tobacco (e.g., never, some days, or every day)
- Binge Drinking Frequency: How often a respondent has had more than 5 drinks on an occasion in the past 30 days
- Marijuana Use: Whether or not a respondent smokes marijuana for pleasure (as opposed to medical reasons)

Importantly, smoking and marijuana use are categorical variables and will be presented below as a proportion of all respondents, while binge drinking frequency is a numerical variable and will be presented with standard error bars in the analysis below. There are also other variables available in the links below, including the maximum number of drinks in one occasion in the past 30 days, and the number of days that a respondent smoked marijuana in the past 30 days. But for the purpose of this analysis, we will keep things simple and confined to these three variables.

## Analysis

### Alcohol, Tobacco, and Marijuana Use in 2017

As an initial pass, below are several plots of substance use across different demographic factors. While all plots can be found in the links at the bottom of this article, these are a selection of interesting trends that I've pulled out from the pack:

#### Age:
The analysis shows interesting differences in substance use across age groups, with marijuana and binge drinking more skewed towards younger age groups, while heavy, every-day smoking evenly distributed across middle age groups.
![alt text](./reports/figures/age.png)

#### Marital:
Use of all three substances seems to be higher among divorced and separated respondents relative to married respondents. While the difference appears to be less pronounced in marijuana use, statistical tests (linked in appendix) show a statistically significant difference in the groups, nonetheless.
![alt text](./reports/figures/marital.png)

#### Employment:
Smoking appears to be more pronounced among respondents who are unemployed or unable to work, while marijuana use is more concentrated in students.
![alt text](./reports/figures/employment.png)

#### Income:
Strikingly, smoking shows a clear trend across narrowly defined income brackets, with every-day smoking incidence increasing as income decreases. Interestingly, similar trends are not exhibited for binge drinking or marijuana use.
![alt text](./reports/figures/income.png)

#### State:
A heat map across the nation suggests a higher proportion of every-day smokers in Tennessee, Kentucky, and Oklahoma.
![alt text](./reports/figures/smoke_state_2017.svg)

### Relation to Social Determinants of Health and Mental Factors

Now for the more interesting part. How does substance use relate to a variety of social and mental health risk factors? Once again, a selection of graphs are shown here, with the full set available in the appendix links.

#### Satisfaction with Life:
Every-day smoking shows a clear trend, with higher incidence among respondents indicating dissatisfaction with their lives. Binge drinking shows a similar trend, however the error bars indicate high variablilty, particularly among those who are "very dissatisfied". Marijuana usage underscores this idea also, perhaps suggesting that those with a mild level of dissatisfaction are more amenable to binge drinking and using marijuana for pleasure.
![alt text](./reports/figures/satisfied_life.png)

#### Inability to Pay Bills:
This variable asks respondents whether there was an occasion in the last 12 months where respondents were not able to pay their mortgage, rent, or utility bills. Interestingly, substance use was higher for all three substances among respondents who indicated yes. These trends were also corroborated across other finance related questions, including how much money respondents have left after paying bills and respondents' ability to afford balanced meals.
![alt text](./reports/figures/cannot_pay_bills.png)

#### Safe Living Situations:
This variable asks how safe respondents feel their neighborhoods to be. Once again, across all three substance variables, there is a higher incidence of usage in more unsafe neighborhoods. Unfortunately, a similar trend is seen in relation to the number of times respondents' have moved in the last year.
![alt text](./reports/figures/safe_living.png)
![alt text](./reports/figures/times_moved_bins.png)

#### Stress:
Smoking and binge drinking appear to be correlated with higher levels of stress, with the highest use among those indicating stress "all the time". Interestingly, marijuana use drops between "most of the time" and "all the time" stress groups.
![alt text](./reports/figures/stress.png)

### Substance Use Over Time

Given the annual nature of the survey, I was curious to see if there were any trends in substance use across the years. Unfortunately, the analysis was not as fruitful as the above plots, as several of the environmental variables were not available for all 5 years due to the survey design. Nevertheless, here are a couple interesting plots to consider:

#### Change in Every-day Smoking:

On a more positive note, it appears that the proportion of every-day smokers has decreased in a majority of states relative to 2013 (e.g., 5 years prior to the above analysis).

![alt text](./reports/figures/smoking_change.png)

#### Change in Mental Health:

However, the data suggests that mental health has deteriorated across most states relative to 2013. This plot shows the percent change (2013 to 2017) in number of respondents who indicated that they had >10 days of poor mental health in the past 30 days.

![alt text](./reports/figures/mh_change.png)

I wanted to explore whether there might be some correlation between changes in mental health and every-day smoking. While there are admittedly a variety of factors at play here, and of course correlation does NOT imply causation, the below graph suggests an interesting but mild correlation. States with improved mental health (e.g., lower proportion of respondents indicating >10 poor mental health days in last 30) tended to have greater decreases in proportion of every-day smokers.

![alt text](./reports/figures/smoking_mh_change.png)

## Discussion

This analysis explored substance use across a variety of factors, including demographics, geography, mental health, and social determinants of health. The data revealed several interesting (and disturbing) trends, including the higher use of tobacco, alochol, and marijuana among individuals with high levels of stress, unsafe living situations, poor financial health, and generally lower satisfaction with life. Combined with the higher incidence of poor mental health from 2013 to 2017, the data suggests difficult circumstances for a significant proportion of the country despite the economic growth over the past 5 - 10 years.

While this analysis is preliminary and could use several improvements (some of which I've highlighted below), it emphasizes the importance of the BRFSS data and the continuous measurement of population mental health and substance use. Analysis such as this can help to stratify and identify populations and areas at higher risk of substance use, leading to more effective resource allocation and policies directed at community support.

Thank you for reading, and I look forward to your comments!

## Future Work and Improvements

I undertook this project as part of the K2 Data Science bootcamp in a limited time frame. There are several areas of potential improvement and future work to extract more knowledge out of this rich dataset. Most importantly, while Python is great for several data science applications, to the best of my knowledge, it does not have as many features to handle complex survey design and analysis relative to other statistical applications such as SAS and SPSS. Future work should attempt to analyze this data using clustering and weights as described in the BRFSS documentation. This will also help with the sampling differences across years and analysis of trends over time.

For additional questions, I would also be interested in assessing substances beyond tobacco, alcohol, and marijuana. One could argue that the substances analyzed in this project aren't "substances" in colloquial use of the word, and we should analyze opioids and heroin as well. Another question I would be interested in answering based on this dataset is how substance use varies across number of social risk factors (e.g., poor financial health, unsafe neighborhood, etc.). This information could be useful to stratify populations and identify areas and individuals at higher risk of substance use.
