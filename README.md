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
