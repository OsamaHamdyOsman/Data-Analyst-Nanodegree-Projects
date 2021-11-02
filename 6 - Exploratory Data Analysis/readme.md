# EDA of Loan Data with Python
## by *Osama Hamdy Osman*

## Prosper’s Story:

[**Prosper**](https://www.prosper.com/about) was founded in 2005 as the first **peer-to-peer** lending marketplace in the United States. Since then, Prosper has facilitated more than **$13 billion in loans** to more than **850,000** people.

Through Prosper, people can invest in each other in a way that is financially and socially rewarding. Borrowers apply online for a fixed-rate, fixed-term loan between \\$2,000 and \\$40,000. Individuals and institutions can invest in the loans and earn attractive returns. Prosper handles all loan servicing on behalf of the matched borrowers and investors.

Prosper Marketplace is backed by leading investors including Sequoia Capital, Francisco Partners, Institutional Venture Partners, and Credit Suisse NEXT Fund.

<!-- #region -->
## Dataset

***What is the structure of The dataset?***

This data set comprises **113,937 loans** with **81 attributes** on each loan, including *loan amount, borrower rate (or interest rate), current loan status, borrower income, borrower employment status, borrower credit history, and the latest payment information*.


***Important notes***

* Before 2009 credit rating named `"CreditGrade"` “The Credit rating that was assigned at the time the listing went live. Applicable for listings pre-2009 period and will only be populated for those listings.


* After **July 2009**, there’s another measure `“ProsperRating (Alpha)”` The Prosper Rating assigned at the time the listing was created between AA - HR. Applicable for loans originated after **July 2009**.

Both variables are imported as object datatype in the dataframe. Yet, It’s more sensible to exhibit them as ordered categorical variables, the matter that will come in handy if any modeling that involves such variables is pondered.

worth noting that the dataset was last updated 03/11/2014


**Note:** This [data dictionary](https://www.google.com/url?q=https://docs.google.com/spreadsheet/ccc?key%3D0AllIqIyvWZdadDd5NTlqZ1pBMHlsUjdrOTZHaVBuSlE%26usp%3Dsharing&sa=D&ust=1608172512599000&usg=AOvVaw3pTqUqYfvigl_FWgtIlTcE) explains the variables in the data set.
<!-- #endregion -->

## Summary of Findings

* he variation of loan amounts within different income ranges within each year showed us a change in the borrowers granted loans by Prosper and how thay shifted their targeting criteria and redefined the income range in a way that’s more transparent and achieves lower risks with time. This highlights how the company strategy was evolving over years. 

* The loan listings breakup by years and loan status, there was an observation that might be realted to the financial crisis hit in late 2008, these observations highlight a lead up to the financial crisis by the soaring proportion of loans either went defaulted or chargedoff in some point in time in 2007 and 2008. Following that period, a gradual increase in the number of listings concomitently with a notable decline in the chargedoff and defaulted loans propotions prevailed the subsequent years to early 2014.

*  A potential association between the Estimated loss and each of the Borrower Rate, the Prosper Rating and the Lender Yield. It shows this association through the use of a comination of graphing aesthetics like color and faceting.



<!-- #region -->
## Key Insights for Presentation

Intrigued by the affluence of the dataset and its wide range of variables, i will explore it to glean some insights and refine my understanding of the lending market in the US. In this journey i will try to cover the following points:

### Learn about borrowers:
> * An Overview of the Loan Original Amount Distributions through histrograms to learn about the typical amounts the aim at. This is done through histograms and entailed spcifying the bins, x and y axis labels and plot titles. 
> * The credit terms for the loans. A discrete variable that is better plotted using part chart. Hence the number of groups is 3 and there's stark differences between their frequency, i opted to employ a pie chart as well. 
> * The two Credit ratings, another set of categorical variables that have two slightly different levels. One was employed before July, 2009 and the other was employed after that date. 
> * Borrowers' states, Here things got really interesting as i got to learn about using the geopandas library
> * Investigating Loan Status, plotting this variable as a horizontal barchart due to the numereous categories and their lenthy names. 
> * Rates of borrowing:There were two of them with slightly different definition that is highlighted in the relevant part of the notebook. A historgram with the appropriate binning was used to distinguish both definitions.  
> * "ListingCategory" is another categorical variable that informs us about the likely reasons for people to borrow for.
> * Borrowers' Income Range, another categorical variable that was depicted as an horizontal barchart for the same reasons mentioned earlier for using this kind of chart. 
> * Debt to Income Ratio, a continuous variable, so histograms was the appropriate choice. A decision was made to split the data into two groups, one for those records with debt/income ratio equal to or greater than 1 and the other less than 1 to zoom in into the distribution of each and try to glean some insights

### Investors’ Insights:
> * The Lender Yield: By plotting the histogram, we can see the actual variable’s distribution - with its peaks and vallies - the yeild of 31% is the most common with some very rare cases of negative 10% yield. Meanwhile most of the yields are around the 15% mark.

### Loan Market - How is it going? 
> * An Overview of the overall Loan Market - Listings’ count over time: First and foremost, an overview of the trend of loan listings across the dataset time span sheds light on the general direction of the loans market; either growing, declining or going steady. Through the following time series graphs, it seems that there’s an upward trend in the number of listing through the dataset period from late 2005 to early 2014. I have used several to explore this aspect.
    * Bar Plot for Yearly listings count was used to give a general sense of the data.
    * A time series plot was employed 'How the Listings Count growing on Quarterly basis' 
    
> * Loan Original amount and delinquency:
I wanted to look into the pattern of the different delinquency levels across the different loan original amount. 
    * So, i resorted to using faceted histograms.
    * Another variation, stacked histogram shows the proportions of chargedoff & defaulted loans and how they behave over the different ranges of loan amounts.
    
> * The association between Loan Amount and Listing Category: Boxplots was used to illustrate the relation between those aspects. 

> * The Debt to Income ratio and Income Range: An eye-catching observation is that large number of not employed borrowers are selecting really high debt to income ratios. May be because they had been expecting to have a job soon. A facetgrid with the income range variable and plotting histogram from the Debt/income ratio revealed some important insights.
    * One important note, is the use of the argument `sharey=False` to spot each income range graph with clarity. 
    
> * Loan Amount & Loan Term using boxplot and violin plots, showed that the median loan amount of the 60 months term loan are typically higher than that of the 36 months which in turn higher than the 12 months term loans.

> * Credit Ratings and Lender Yield: Risk-Return Tradeoff is really apparant here using boxplots and violin plots again

> * Income range & Prosper rating: The two categorical variables are associated to each other, as expected, as the income increases the credit ratings gets higher. A Stacked barchart along with their prospective Prosper ratings yields a very interesting step-wise graphic. Then heatmap used to emphasis the finding.

> * Borrower Annual Percentage Rate and Lender Yield: a scatter plot to show the strong relationship beween them. 

> * Borrower rate and Estimated Loss: Investigating the association between the borrower interest rate and the Estimated loss (which is the estimated principal loss on charge-offs. Applicable for loans originated after July 2009.). A positive relationship seems to exist between the 2 variables.

> * Rates of borrowing: The "BorrowerAPR" and the "BorrowerRate" are two nuemrical variables the measures the The Borrower's Annual Percentage Rate (APR) for the loan and The Borrower's interest rate for this loan respectively. Using a timeseries line chart shows the difference between them at glance 
    
    
> * How Loan listings across different Income Levels behave accross years, using facetgrid with pointplots gives us a really interesting insights on the strategy that have been steered by Prosper to deminish risks and grow thier business. 

> * Total number of listings partitioned by delinquency (loan status) over Time. Stacked barcharts and line plots was a nice choice to highlight what happened in 2007 and 2008 (the period leading to the financial crisis)

> * Plotting the Estimated loss vs BorrowerRate vs Lender Yield with ProsperRatings: Last but not least, Using pariplot hued by the Prosper rating as a categorical variable. 
<!-- #endregion -->
