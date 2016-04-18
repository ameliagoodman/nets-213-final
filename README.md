# nets-213-final
Amelia Goodman, Andrew Graffy, Andrea Baric

##Layout of our Repo
* Raw data (HIT screenshots) in Deliverable\ 2/data/hit-screenshot*
* Sample input/output for QC in Deliverable\ 2/data/QC\ Input.csv and /data/QC\ Input.csv
* Sample input/output for aggregation in Deliverable\ 2/data/Aggregation\ Input.csv and Deliverable\ 2/data/Aggregation\ Output.csv
* Code for QC in Deliverable\ 2/src/qc_module.py
* Code for aggregation in Deliverable\ 2/src/aggregation_module.py


###Module 1: Interaction (screenshots in Deliverable\ 2/data/)
We have a Crowdflower hit that first surveys the participant's demographic information like age range, gender, location, and ethnicity. We will then ask the contributors to rate 7 personal attributes (i.e., intelligence, wealth, physical appearance) on a 1-7 scale based on how important it is to them when selecting a romantic partner. Then, we will ask them to rate the same attributes based on what they think people in their home country would prefer on average. Also, we will have them rate hand-selected photos of different ethnicities in order to observe their preference for race when it comes to physical attraction. The input for the HIT will be hand-selected pictures of South Asian, East Asian, American, African, and Middle Eastern men and women. The output will be a CSV file containing the contributors' demographic information, ratings for themselves, perceived "average" ratings for their home country, and their ratings of the photos. 

###Module 2: Quality Control (Deliverable\ 2/src/qc_module.py)
Because we are soliciting subjective information from the crowdworkers, our quality control mechanism simply needs to check whether the crowdworkers are paying attention or else simply clicking randomly. To do this, we incorporate a subtle instruction, requiring the workers to mark a certain attribute ("affability") which we do not care about with an importance of 2 for their raiting and another attribute ("health") a rating of 3 for their country's rating. When we have collected the crowd data, we will run a python script that will check each contribution for whether it got this "golden" question correct - if not, we scratch it from the data set. The input for this module will be the crowdflower output in CSV format, and the output will be a "cleaned" CSV file that excludes the contributions that missed the gold question. 

###Module 3: Aggregation (Deliverable\ 2/src/aggregation_module.py)
We will collect our responses via Crowdflower. To aggregate and analyze this data, we have a python script that finds the average importance rating for each attribute according to location. We can also easily adjust the script to output the average rating according to age range or gender. Our input here will be a cleaned CSV file, and the output will be a text file displaying average results according to country. The script can easily be augmented/adjusted to sort by age or gender as well - this will need to be done going forward, as well as ensuring that the headers and rows used in the script match with the finalized headers that we will extract from the HIT data.

###Module 4: Results and Analysis
We will organize the data based on age, gender, ethnicity, and location. We will observe and compare patterns in responses: how do different ethnicities, gender, or young/old people differ when it comes to rating the importance of these attributes? When estimating their own country's general rating, how do these differ according to location? We will then find an effective and interesting way to organize and display our findings.


##High Level Milestones
* [3 points] Designing and posting the HIT
* [2 points] Writing the python script for quality control
* [2 points] Writing the python script for aggregation
* [2 points] Download crowd data and run through quality control module
* [3 points] Use aggregation script to organize/sort data based on different demographics: age, gender, location of the crowd worker
* [3 points] Generating aesthetically pleasing ways to display our analyzed results, like a word cloud.
