# ChatBot-Using-NLTK
The name of the ChatBot is PyBot because I love to do anything with python and made the whole project with it.This PyBot can learn reply from you intially and can reply to you on the next occurence .The main feature is it is a BlogBot where it contains a blogpage Database and it can reply to user query regarding to their blog.

## Python Library Dependencies ##
  
+ [pymysql](http://pymysql.readthedocs.io/en/latest/)  
+ [nltk](http://www.nltk.org/install.html) 
+ [numpy](http://www.numpy.org/)
+ [pandas](http://pandas.pydata.org/)

## LINK FOR TECHCRUNCH CSV FILE ##

https://mega.nz/#!L8ghkQRT!peinMO5Rtc8tSnjz3FGWVbRF7jr2dva8yqSFYuHblAI


## Files and Components ##


**Core Functionality**
+ `chatbot.py` - main ChatBot library (Command Center)
+ `utils.py` - generic function utilities used by ChatBot (config, DB conn etc) 
+ `setupdatabse.py` - Initially setting the Database for the bot in your machine
+ `dataload.py` - Loading the blogpage csv file and used to extract data from it
+ `techcrunch.csv`- Techcrunch Blogpages user blogs data in CSV Format


## Install and Setup ##

Details of installing dependancies for the NLPBot 

In summary, for a new install, the following steps are required:
1. Install Python 3.5
2. Install pyMySQL 
3. Install NLTK
4. MySQL Database Server Configuration
5. Install Bot Code and Configure
6. Configure the botuser ./config/config.ini file
7. Start BotServer

# Sample Conversation #
This is sample conversation between me and the bot.Initially I have to train with base commands and then it learn from me.When ask the question next time it replies me with answer.The main feature is we can ask blog query which it fetches from database and reply us with that.

# Configuring Database #
```
Configuring Tables for database configuration: 
        Server: localhost 
        DB-User: botuser1 
        DB-Name: blogbot

** ALL EXISTING TABLES AND DATA WILL BE LOST **

Continue? [Y/n] 
Y
Connecting to database... connected.

Creating sentences table:
DROP TABLE IF EXISTS sentences
CREATE TABLE sentences (hashid VARCHAR(16) COLLATE utf8_general_ci , sentence VARCHAR(768) COLLATE utf8_general_ci , result VARCHAR(768) COLLATE utf8_general_ci ) 

Done.
```

# TRAIN - TO TRAIN THE BOT #
# SEARCH - TO SEARCH THE ANSWER BY THE BOT ITSELF #
# CHATTING WITH BOT #
```
BOT ONLINE...
Connecting to database...
...connected
BOT>>  PyBot Online.Ready To Serve You
>>>Hai How are you?
BOT>> TRAIN OR SEARCH
>>>train
BOT>> Please  enter the answer to train me
>>>I am fine what about you?
BOT>>  Thankyou For Training Me
>>>Hai How are you?
BOT>>  I am fine what about you?
Show me the url of the post 1401293
BOT>> TRAIN OR SEARCH
>>>search
BOT>>  https://techcrunch.com/2016/10/13/soylent-bars-recalled-after-some-customers-get-sick/
>>>content of Ajay
BOT>> TRAIN OR SEARCH
>>>search
BOT>>  
Despite what some politicians say, no country is an island in today’s rapidly changing world. In the same way, no company can survive as an island, either.
Most won’t have noticed a recent $6.5 million Series A for a company called Mobilize, but it’s indicative of a major change occurring in businesses today. Companies’ growing reliance on a distributed workforce have been occupying headlines and podcasts for the past couple of years. However, these conversations must now turn to how companies increasingly depend on partnerships as their force multiplier.
The most successful companies today live or die based upon their business partners, whether they be channel partners, technology partners, suppliers or outsourced operations partners. Some of the wisest business leaders realize that the only way to scale and remain competitive is to stick to their core competency — then, work collaboratively with other groups whose complementary core competencies can make a business process more efficient than by trying (and largely failing) to create such disparate capabilities themselves.
The result? A business that is more nimble, while remaining focused on building greater value for shareholders, employees and customers. When each party does what it is expert at, everyone can add value efficiently up and down the value chain.
Furthermore, by working with a broad demographic of partners externally, companies are able to be far more responsive to market and perception changes. Integrated partners are able to relay changes back to the core company more quickly, and, when there is a response the partners are involved in developing or supportive of, they provide a sizable ambassadorship that would’ve otherwise taken huge investments of time and effort to rally organically.
It’s no wonder, then, that the largest hotel company in the world, Airbnb, does not own any hotels, relying instead on a network of accommodation provider partners. Fun fact: This network includes more than 1,400 castles, which I doubt they would have had access to otherwise. And the largest “taxi” company in the world, Uber, doesn’t own any cabs. Instead, they rely on an expansive network of driving partners.
For companies like Airbnb, Uber, ClassPass, Thumbtack and countless others, partners are mission-critical to their operation and value proposition. They would not exist without these partnerships working seamlessly to help them execute their core competency and vision.
And the partnership trend isn’t limited to just consumer companies. Significant open-source software companies, starting with Red Hat years ago and Docker more recently, would cease to exist without the partner communities on which they were built.
The networks of partnerships that all kinds of companies are acknowledging as essential to their businesses are growing and becoming more diverse in terms of their purpose, size, type and geographies. In the same fashion, in light of recent changes in the economy, traditional companies are rethinking and re-investing more in their partner programs, too — relying even more on affiliates, resellers, franchisers and any external network that can broaden their reach and impact.
Naturally, as with any business development, this new paradigm is creating other business opportunities. There’s come a growing need for companies to quickly and coherently communicate with and manage fluid relationships with these partner communities. Good-old emails no longer need apply. Just raise your hand if you think that would be the best way to send a mission critical message to a Lyft driver about surge pricing in New Orleans at 6pm tonight!
Furthermore, the tracking and engagement of ever-growing groups of partners across their actions and milestones can result in significant internal team demands. Some companies have long offered group communication tools that go beyond emailing to more dynamic communication, but they’ve largely been left for people to adopt to their own needs. Google Groups, Facebook Messenger and others weren’t built around the specific needs of managing sizable groups of people like on-demand workers or a city’s-worth of dinner hosts.
Slack and HipChat provide a good hub for informal conversation and the sharing of materials, though targeted toward internal teams. Mobilize provides a more developed platform for communicating, scheduling and driving impact with regard for diverse partner contexts.
Companies large and small — from MasterCard to Maker Faire — are already migrating to Mobilize’s platform from other solutions so they can better manage their growing external partnerships without having to grow internal teams. There are already internal job titles and consultants lining up to help manage these groups, so the need for platforms focused on managing these networks of partner groups is only growing.
As these partnerships grow and the platforms that support them develop, rhythms for partner relationship management will evolve. Today, these rhythms are more a tap on the drum set. Someday they’ll become fluid jam sessions. This will require focused attention and understanding of how different groups live, behave and what they want from these partnerships, as well. But the companies that engage in the partnered economy will be rewarded with the strongest ties with these groups, through to their customers, and become the most adept at working through market and other changes beyond their control. This in turn will allow them continued growth and tenure at the top of their industries.
BOT>> Content Displayed
>>>posts id of Anthony
BOT>> TRAIN OR SEARCH
>>>search
BOT>>  1401193
BOT>>  1400891
BOT>>  1401629
BOT>>  1399984
BOT>>  1397811
BOT>>  1399087
BOT>>  1399040
BOT>>  1398357
BOT>>  1393887
BOT>>  1397811
BOT>>  1397659
BOT>>  1394698
BOT>>  1393887
BOT>> Content Displayed
>>> exit
BOT>> Thankyou For Using Me
```
These are the sample commands for the bot .You try your own commands.
