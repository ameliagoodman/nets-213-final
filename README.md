# nets-213-final
Amelia Goodman, Andrew Graffy, Andrea Baric

###Module 1: Interaction
We will make a Crowdflower hit that first surveys the participant's demographic information like age range, gender, and location. We will then ask the contributors to rate 7 personal attributes (i.e., intelligence, wealth, physical appearance) on a 1-7 scale based on how important it is to them when selecting a romantic partner. Then, we will ask them to rate the same attributes based on what they think people in their home country would "generally" believe. 

###Module 2: Quality Control
Because we are soliciting subjective information from the crowdworkers, our quality control mechanism simply needs to check whether the crowdworkers are paying attention or else simply clicking randomly. To do this, we incorporate a subtle instruction, requiring the workers to mark a certain attribute ("affability") which we do not care about with an importance of 2. Once we collect the crowd data, we have written a python script that will check each contribution for whether it got this "golden" question correct - if not, we scratch it from the data set.  

###Module 3: Aggregation
We will collect our responses via Crowdflower. To aggregate and analyze this data, we have a python script that finds the average importance rating for each attribute according to location. We can also easily adjust the script to output the average rating according to age range or gender. 

###Module 4: Results and Analysis
We will organize the data based on age, gender, and location. We will observe and compare patterns in responses: how do different ethnicities, gender, or young/old people differ when it comes to rating the importance of these attributes? When estimating their own country's general rating, how do these differ according to location? Find an effective and interesting way to organize and display our findings.


##High Level Milestones
* [3 points] Designing and posting the HIT
* [2 points] Writing the python script for quality control
* [2 points] Writing the python script for aggregation
* [2 points] Download crowd data and run through quality control module
* [3 points] Use aggregation script to organize/sort data based on different demographics: age, gender, location of the crowd worker
* [2 points] Generating aesthetically pleasing ways to display our analyzed results, like a word cloud.
