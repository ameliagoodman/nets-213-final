# nets-213-final
Amelia Goodman, Andrew Graffy, Andrea Baric

###Module 1: Interaction
We will make a Crowdflower hit that takes the participant's information like age range, gender, and location. We will ask the participant to provide a link to a picture of a person they find attractive. We will ask them to list three adjectives that they find most attractive in this person. 

###Module 2: Quality Control
To ensure quality from our HITs, we will put a lot of emphasis on honesty and truthful answers as requirements for payment. Of course, there is no real way we can ensure that the user is honest, since it is a very subjective question. It will be difficult to distinguish between a dishonest response and an unusual one, for example if someone writes that they find smelliness attractive. This could be a language/translation error, as in someone could just find it attractive when someone smells nice, or it could be an honest answer, as in someone is attracted to a person who is fragrant no matter what smell, or it could be a dishonest answer, as in the participant just wanted to fill the blank with something. We will have to go through each adjective by hand to ensure that they are legitimate adjectives--or perhaps we will train a classifier to do this work.

###Module 3: Aggregation
We will collect our responses via Crowdflower. We will ensure that participant's feedback of their information (age-range, location, gender) match their user profile on Crowdflower.

###Module 4: Results and Analysis
We will organize the data based on age, gender, and location. We will observe patterns in responses of both the person they linked to and their chosen adjectives. 


##High Level Milestones
* [2 points] Designing and posting the HIT
* [2 points] Checking for quality among responses to user information (age range, gender, location)
* [3 points] Checking for quality among responses to adjective questions and linked URL.
* [1 point] Collecting information from Crowdflower
* [4 points] Sorting data based on different qualities: age, gender, location, gender of person in linked URL, etc.
* [4 points] Sorting data based on the adjectives (i.e. do women list emotional attributes as attractive more often than men do?)
* [1 point] Generating aesthetically pleasing ways to display our analyzed results, like a word cloud.