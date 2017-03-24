## Motivation and Project Overview
In today's political climate, there's a sizable amount of anger and distrust from the right towards the left-leaning mainstream media because of accusations made by our... unorthodox president. On the flipside, prominent talk show hosts like Stephen Colbert and Seth Meyers have been unreservedly voicing constant streams of criticisms and comedic jabs directed against many Republican (and even a few Democratic) government officials. That said, we can't blindly follow one side over the other. Using a variety of sources, we should take the time to examine the views expressed by and the criticisms given to both sides of the political spectrum so that we can best form our own informed opinions. This bot takes one small slice of the mainstream media, The Daily Show with Jon Stewart, and presents different pieces of information about the show during Jon Stewart's run from 1999 to 2015. While looking at the information given by this bot is nowhere near the "thorough examination of both sides" that I mentioned above, it at least gives us a very rough lens to start with.

We must of course remember that The Daily Show is just one talk show, and that it does not necessarily represent many of the opinions of other "mainstream shows." That said, it has undoubtedly become a very popular part of the media, and it nevertheless can give us some insights on "what's hot" or "who's popular" over an extended time period. And on a more technical note, the dataset used does not contain episode information during Trevor Noah's run. 

This bot uses data aggregated by FiveThirtyEight, "a website that focuses on opinion poll analysis, politics, economics, and sports blogging" (Wikipedia). This data is in the form of a csv file with five headings. Each row contains information about an episode by The Daily Show. The descriptions of what these rows contain are shown below and were taken straight from FiveThirtyEight's Github repository at https://github.com/fivethirtyeight/data/tree/master/daily-show-guests:

YEAR --- The year an episode aired.  
GoogleKnowlege_Occupation --- A guest's occupation or office, according to Google's Knowledge Graph or, if they're not in there, how Stewart introduced them on the program.  
Show --- Air date of episode. Not unique, as some shows had more than one guest.  
Group --- A larger group designation for the occupation. For instance, us senators, US presidents and former presidents are all under "politicians."  
Raw_Guest_List --- The person or list of people who appeared on the show, according to Wikipedia. The GoogleKnowlege_Occupation only refers to one of them in a given row.  

This bot runs on Flask, a micro web framework written in Python. When it is initialized in the terminal, it fetches the guest information described above straight from Github and executes the functionalities dictated by the link accessed by the user.


## Links / Sample Output
#### /date/\<date\> ####
Given a properly formatted date (e.g. 10-21-03), the bot presents the guest(s) for that day, what their occupation is, other dates in which they appeared on The Daily Show, and a Wikipedia URL for learning more about them. For example, the input "/date/11-18-99" gives us:

Bill Maher appeared on The Daily Show on 11/18/99 and is known to be a(n) comedian.  
This person has also appeared on the following dates:  
9/30/08  
6/23/14  
Learn more about Bill Maher at https://en.wikipedia.org/wiki/Bill Maher.  

#### /name/\<name\> ####
Given a name, the bot presents all the dates in which they appeared on The Daily Show, as well as a Wikipedia URL for learning more about them. For example, the input "/name/Paul Rudd" gives us:

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
Given a group name, the bot presents the five guests from that group who appeared on the show the most, how many times they each appeared, and Wikipedia URLs for learning more about them. If there are less than five guests to show, then the bot will simply give those fewer-than-five people. For example, the input "/group/business" gives us: 

Within the 'business' group, the following guests appeared the most:  
Bill Gates (3) (https://en.wikipedia.org/wiki/Bill Gates)  
T. Boone Pickens (2) (https://en.wikipedia.org/wiki/T. Boone Pickens)  
Posh Spice & Baby Spice (1) (https://en.wikipedia.org/wiki/Posh Spice & Baby Spice)  
Donald Trump (1) (https://en.wikipedia.org/wiki/Donald Trump)  
Richard Branson (1) (https://en.wikipedia.org/wiki/Richard Branson)  

#### /year-groups/\<year\> ####
Given a year, the bot presents the sorted breakdown of groups that appeared on the show for that year. Using the first entry in the example below, 32.72% of appearances in 2014 were by guests who fall under the "Media" category. The example below was generated using the input "/year-groups/2014". As a side note, this funcionality gives an interesting look at the types of people who appeared on The Daily Show over 16 years, especially since the show's early years seemed to lean more towards inviting actors.

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
Given a year and a group name, the bot presents all the guests falling under that group who appeared during that year. This also includes the dates in which these guests appeared, as well as Wikipedia URLs for learning more about them. For example, the input "/year-group-guests/2011/government" gives us:

In 2011, the following guests from the 'government' group appeared on The Daily Show:  
Lisa P. Jackson (5/19/11) (https://en.wikipedia.org/wiki/Lisa P. Jackson)  
Peter Tomsen (7/28/11) (https://en.wikipedia.org/wiki/Peter Tomsen)  
Melody Barnes (12/14/11) (https://en.wikipedia.org/wiki/Melody Barnes)  
