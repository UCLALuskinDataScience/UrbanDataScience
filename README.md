# UP229 Urban Data Science
Spring 2021: Tues/Thurs 9.30-10.45

**Instructor:** [Adam Millard-Ball](https://luskin.ucla.edu/person/adam-millard-ball), he/him

**Office hours:** Mondays 2.30-4.30. [Sign up here](https://goo.gl/X7vFOD)

**About this course:** New data sources are a potential goldmine for urban planners and policy makers. But sometimes they are large, sometimes they are messy, sometimes they are awkward to access, and often they are all of these things. In this hands-on course, we’ll develop skills in scraping, processing, and managing urban data, and using tools such as natural language processing, geospatial analysis, and machine learning. We’ll use examples from transit, housing, and equity planning, and build competence in open-source tools and languages such as Python and SQL. We’ll also consider the limits to data science, and the biases and pitfalls that "big data" can entail.

**Prerequisites:** Basic Python programming experience, for example through the 2020-21 version of 206A (Introduction to Geographic Information Systems and Spatial Data Science), or an introductory Python course. One good, free option is offered by [Data Carpentry](https://datacarpentry.org/python-socialsci/index.html). Another is the University of Michigan [Introduction to Data Science in Python](https://www.coursera.org/learn/python-data-analysis) course; if you have no prior knowledge, you should take [Programming for Everyone](https://www.coursera.org/learn/python) first. (You can take these for free if you choose the "audit" option.) Whichever option you choose, *before* starting this course you should be familiar with Python syntax, Jupyter notebooks, plotting via `matplotlib`, and `pandas` and `geopandas` dataframes.

## Learning objectives
* Expand your urban data analysis, visualization, and Python skills, regardless of your starting point
* Identify applications of these techniques to urban planning challenges
* Know how to read API documentation and where to get more information
* Understand how to collaborate using git and other software tools
* Critically analyze the constraints to data science methods, particularly in terms of ethics and causal inference

## Course tools
All the readings, assignments, and lecture notebooks will be posted on this GitHub site.

I ask you to do the assignments using a Jupyter Notebook in [Anconda](https://www.anaconda.com/products/individual). That helps make sure that we all have a consistent Python setup across different computers (Mac, Windows, etc.). If you are unable to install Anaconda or are uncomfortable doing so, please talk to me about alternatives before the quarter starts.

Each class will be held synchronously via Zoom. Login details are on CCLE. Class sessions will be recorded and posted to CCLE.

We will primarily use Slack to maintain communication outside of scheduled class times. In particular, it provides a space for problem solving and for you to help each other. You’ll receive an email invitation from me to join our Slack workspace. If you have not used Slack before, please familiarize yourself with the tool using the [resources here](https://www.it.ucla.edu/support-training/tutorials/how-use-slack).

## Textbook
There is no textbook for the class. All required readings will be posted here on GitHub. However, you may find some of the following books helpful.
* [Python for Data Analysis, 2nd edition](https://bookshop.org/books/python-for-data-analysis-data-wrangling-with-pandas-numpy-and-ipython-9781491957660/9781491957660). This focuses on the `pandas` library. The UCLA Library has a copy.
* [Think Python, 2nd edition](https://greenteapress.com/wp/think-python-2e/). This is a free ebook and is an excellent general refresher on Python syntax and data structures.

## Class participation
Your active participation is essential to making this course successful and enjoyable. I expect you to:

* Actively follow the examples in class through your own copy of the Jupyter notebook posted in advance. Tweak and experiment with the examples. If you don't follow an example, let me know in the Zoom chat—others will undoubtedly have the same question.
* Discuss the substantive readings on Slack. Post a question, idea, or comment by 8.30am on the day of class.  Please engage with the posts of others as well as writing your own—this is a discussion board, not a repository of essays.  
* Use Slack to help each other out with questions on the assignments and projects.

## Graded assignments
**Weekly homeworks** (25%). Each homework will be posted on Monday and due at 5pm on the following Monday. You must submit at least 4 out of 5 homeworks on time (but please do them all). *We'll spend time in class on Thursday working through the assignment, so please make a start on it before then.*

**Challenge problems** (25%). Most homeworks will include a challenge problem, which is more open ended. You must do at least 2 of these, and present one in class.

**Final project** (35%). Working in groups of 2-3, you'll conceptualize and implement an urban data science project. You'll submit a proposal (Week 3), and make lightening presentations of your interim (Weeks 6-7) and final analysis (Weeks 9-10).

**Class participation** (15%). Your class participation grade will consider attendance and active participation in class and on Slack.

## Course Policies

### Accessibility and Disabilities
If you require any accommodations because of a disability, please talk to me within the first two weeks of the quarter if possible. The sooner that I am aware of any accessibility needs, the quicker I can try and accommodate them.

### Late Submission of Assignments
Students can make a formal request to the instructor for special consideration
for an extension to an assignment due date. This request should be received at least 48 hours in advance. Otherwise, one partial grade will be deducted for every 24-hour period an assignment is late. For example, an A- will go to a B+. Note that no extensions are possible for the weekly homeworks (because I post the solutions promptly)—that's why only 7 out of 9 homeworks are required.

## Academic Integrity
UCLA’s policy about plagiarism is clear: the sources of all ideas, text, pictures, or graphics that are not your (or your team’s) own must be fully cited, all passages copied from other sources must be in quotation marks with the source cited, and you absolutely cannot submit materials that have previously been submitted by other students in previous iterations of this course, even if you have re-worked this material for your submission. Being in this class constitutes an acknowledgment and willingness to abide by UCLA’s academic integrity policies.1 Should you have any questions about these policies, [see here](http://www.studentgroups.ucla.edu/dos/students/integrity/). (Thanks to Prof. Mike Manville for permission to use this text.)

The same principles of academic integrity apply to your code. If you borrow any code snippets or ideas, acknoweldge them with a comment in the code. E.g.

```
# Iteration code from: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
``` 

# Weekly schedule
The schedule is preliminary and subject to change, depending on how quickly or slowly we move through the material. In general, class on Tuesdays will cover the theory and worked examples, and discuss applications from the readings. Class on Thursdays will be more hands-on, and devote time to working through the weekly homework assignment.

A Jupyter notebook will be posted on GitHub. The course readings are all posted on CCLE.

Pre-course:

* Please fill out the [pre-course survey](https://forms.gle/w28sJpUZZ3CubCZG8)
* Create a [GitHub account](https://github.com/) if you don't have one
* Download and install [Anaconda](https://www.anaconda.com/products/individual)

[Week 1: Introduction. APIs](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/week1)
* [Homework](https://classroom.github.com/a/QnMFJCbo) due 9.30am, Apr 8
* [How to submit your homework on GitHub](https://github.com/UCLALuskinDataScience/UrbanDataScience/blob/main/Assignment_submission.pdf)

[Week 2: Web scraping](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/week2)
* [Homework](https://classroom.github.com/a/X2EWdWqj), due 5pm, Apr 19

[Weeks 3 and 4: Data wrangling](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/week3)
* [Homework](https://classroom.github.com/a/G2rJhEwp), due 5pm, May 3

[Week 5: Natural language processing (1): parsing](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/weeks5-6)
* *Guest: Zachary Steinert-Threlkeld, Department of Public Policy, UCLA (April 27)*

Week 6: Natural language processing (2): [topic modeling and sentiment analysis](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/weeks5-6)
* *Guest: Claudia Preciado, Remix (May 4)*
* [Homework](https://classroom.github.com/a/HpWxYxUR), due 5pm, May 17

[Week 7: Machine learning (1): supervised algorithms](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/weeks7-8)

[Week 8: Machine learning (2): unsupervised algorithms](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/weeks7-8)
* [Homework](https://classroom.github.com/a/ZGuDnzmW), due 5pm, June 2

[Week 9: Databases](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/weeks9-10)

[Week 10: Big data, privacy, and ethics](https://github.com/UCLALuskinDataScience/UrbanDataScience/tree/main/weeks9-10)
