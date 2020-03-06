import csv

#  ========================================================

file_name = "2020calndata"
output_title = ["Team", "Auto Init Points", "Auto Cells", "Tele Cells", "Control Panel", "End Game Points", "Score"]

# List of weights for each corresponding column
auto_init_wt = 5
auto_cell_wt = 4
tele_cell_wt = 2
control_panel_wt = 15
end_game_wt = 25
score = 0

weights = [auto_init_wt, auto_cell_wt, tele_cell_wt, control_panel_wt, end_game_wt]

#  ========================================================

title = []
team_data = []

# Open File
with open(file_name + ".csv") as csv_file:
    # Use csv to parse the file
    csv_file = csv.reader(csv_file, delimiter=',')

    counter = 0
    # row is an iterable
    for row in csv_file:
        # first row is title
        if counter == 0:
            title = row
            counter += 1
        else:
            # Get rid of 'frc' in 'frcX' and add the rest of the data
            team_data.append([row[0][3:]] + row[1:])

# Manipulate data here, team data is list of team data

for i in range(0,len(team_data)):
    score = 0
    for j in range(0,len(team_data[i])):
        if j != 0:
            team_data[j] = team_data[j] * weights[j-1]
            score += team_data[j]
    team_data.append(score)




# Write to an output file
with open(file_name + "_output.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(output_title)

