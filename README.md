# data-collection-pipeline782
Brief Description of the project


In this project I scrape Waterstones.com to obtain information of my favourite genre of books (crime) and used various technologies to make my data accessible in multiple forms. These include converting my dictioary to JSON which could then be uploaded to S3 and converted my dictionary into a pandas dataframe that could be loaded into my RDS cloud SQL database. With the use of Docker I containerised my scraper to allow me to ....

Milestone 1 

-Why did I choose waterstones? 

Milestone


Created Scraper class
I began my project by creating my Scraper class that I named "WaterScraper" and then began to add methods so I could initialise an instance of the class and use it to scrape the Waterstones website.

Created methods that will navigate webpage

It did not take long to encouter my first barrier to accessing the webpage that required the data I wanted to scrape. A cookies pop up stood in my way. By finding the Xpath of the element that contained the cookies button and adding the click() command to the end of the "find_element" method, I was able to by pass the cookies button a make my way past the first hurdle. A time.sleep function needed to be added before the action of clicking the cookies button could be used as it took the cookies pop up a few seconds before it appeared.

Navigating to the crime books page
Because my favourite genre of books are crime books , it was only right that I gain as much data as possible from the books that I love the most. But first I had to get there. Though making use of the websites drop down boxes I was able to find and get to the crime books page in seconds.

-Then adding a method that will allow me to scraper more data.
Now after making it to the page where my beloved crime books were, I encountered another problem. There were books, a good number, but not the amount that I was looking for. I was looking to access at least 100 and in order to get the webpage to show me that many , I created the extend_webpage method. This included three lines of code that would scroll to the bottom of the webpage, allowing access to more books and then 2 lines that would lead to a "Show More" button being clicked to allow even more books into the view of my scraper.

Creating a method to get links to each page where the details can be found and stored in a list
Now that I had access to all of the books, it was time to obtain all of the links to the webpages of each individual book and then store these in a list. This list would come in handy when I need to obtain the data I need on each book available to me. After find the container of the books and discovering the common place where each element contained the link to each individual bookpage , I was able to append these all to a list and really get started with gathering the information I need.

Run the main body of code only within if__name__ == "__main__" block

Milestone

Create a function to retrieve text and image data from a single details page.
Before emabarking on my very ambitious feat of gathering all the data I needed from 100 books, I started small. Very small. One to be exact. 

Determinsically generate a unique ID


Extract data and stror in dictionary which maps feature name to feature value


Save the raw data dictionaries locally
