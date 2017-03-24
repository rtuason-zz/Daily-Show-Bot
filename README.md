## Motivation and Implementation Overview
In today's political climate, there's a sizable amount of anger and distrust from the right towards the left-leaning mainstream media because of accusations made by our... unorthodox president. Today, prominent talk show hosts like Stephen Colbert and Seth Meyers have unreservedly voiced constant streams of criticisms and comedic jabs directed against many Republican (and even a few Democratic) government officials. That said, we can't blindly follow one side over the other. Using a variety of sources, we should take the time to examine the views expressed by and the criticisms given to both sides of the political spectrum so that we can best form our own informed opinions. This bot takes one small slice of the mainstream media, The Daily Show with Jon Stewart, and presents different pieces of information about the show during Jon Stewart's run from 1999 to 2015. While looking at the information given by this bot is nowhere near the "thorough examination of both sides" that I mentioned above, it at least gives us a very rough lens to start with.

We must of course remember that The Daily Show is just one talk show, and that it does not necessarily represent many of the opinions of other "mainstream shows." That said, it has undoubtedly become a very popular part of the media, and it nevertheless can give us some insights on "what's hot" or "who's popular" over an extended time period.

This bot uses data aggregated by FiveThirtyEight, "a website that focuses on opinion poll analysis, politics, economics, and sports blogging" (Wikipedia). This data is in the form of a csv file with five headings. These descriptions were taken straight from FiveThirtyEight's own Github repository at https://github.com/fivethirtyeight/data/tree/master/daily-show-guests:

YEAR --- The year an episode aired.  
GoogleKnowlege_Occupation --- A guest's occupation or office, according to Google's Knowledge Graph or, if they're not in there, how Stewart introduced them on the program.  
Show --- Air date of episode. Not unique, as some shows had more than one guest.  
Group --- A larger group designation for the occupation. For instance, us senators, US presidents and former presidents are all under "politicians."  
Raw_Guest_List --- The person or list of people who appeared on the show, according to Wikipedia. The GoogleKnowlege_Occupation only refers to one of them in a given row.  

## Notes


## Links / Sample Output
#### /date/\<date\> ####


Bill Maher appeared on The Daily Show on 11/18/99 and is known to be a(n) comedian.  
This person has also appeared on the following dates:  
9/30/08  
6/23/14  
Learn more about Bill Maher at https://en.wikipedia.org/wiki/Bill Maher.  

#### /name/\<name\> ####


Paul Rudd appeared on The Daily Show on the following dates:  
12/6/99  
11/5/01  
8/8/02  
5/8/03  
2/11/04  
8/8/05  
6/5/07  
11/6/08  
3/11/09  
12/15/10  
2/23/12  
3/4/13  
7/20/15  
Learn more about Paul Rudd at https://en.wikipedia.org/wiki/Paul Rudd.  

#### /group/\<group\> ####


Within the 'business' group, the following guests appeared the most:  
Bill Gates (3) (https://en.wikipedia.org/wiki/Bill Gates)  
T. Boone Pickens (2) (https://en.wikipedia.org/wiki/T. Boone Pickens)  
Posh Spice & Baby Spice (1) (https://en.wikipedia.org/wiki/Posh Spice & Baby Spice)  
Donald Trump (1) (https://en.wikipedia.org/wiki/Donald Trump)  
Richard Branson (1) (https://en.wikipedia.org/wiki/Richard Branson)  

#### /year-groups/\<year\> ####


In 2014, guests from the following groups appeared:  
Media : 32.72%  
Acting : 29.01%  
Politician : 8.02%  
Comedy : 5.56%  
Academic : 5.56%  
Musician : 4.94%  
Government : 3.7%  
Misc : 3.09%  
Athletics : 2.47%  
Advocacy : 1.85%  
Political Aide : 1.23%  
Business : 0.62%  
Military : 0.62%  
Science : 0.62%  

#### /year-group-guests/\<year\>/\<group\> ####


In 2011, the following guests from the 'government' group appeared on The Daily Show:  
Lisa P. Jackson (5/19/11) (https://en.wikipedia.org/wiki/Lisa P. Jackson)  
Peter Tomsen (7/28/11) (https://en.wikipedia.org/wiki/Peter Tomsen)  
Melody Barnes (12/14/11) (https://en.wikipedia.org/wiki/Melody Barnes)  
