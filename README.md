# ScoutingAppDataAnalysis
Programs for sorting through scouting data and using weights to find a ranking of teams. 

### 2019 Scouting Data Analysis 
------
#### DataAnalysisProgram.py
Takes in an Excel file containing data from a regional and outputs an Excel file that ranks the teams by a score calculated from performance in the regional. 
```
score = hatches * 2 + cargo * 3 + climb_level * 3
```
On the output file, an overall sheet shows the ranking of teams as well as their avg hatches, cargo, climb. Each following sheet has detailed info on a team, including amount scored per match.

### 2020 Scouting Data Analysis
------
Using data from thebluealliance API, rank teams based upon performance in previous matches.  
#### CSVDataAnalysis.py
Takes in CSV file with avg data on each team and multiplies each avg by a weight to obtain a score for ranking the teams at the regional. Outputs a CSV with the ranked teams and their associated weights and score.

To modify per regional/year:
`file_name` is the input CSV file name (ex. "2020calndata")
`output_title` is the first row header for the output CSV file
`weights` is a list of weights to multiply each game score by