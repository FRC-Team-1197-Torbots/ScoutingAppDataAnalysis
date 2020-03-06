import csv

#  ========================================================
# Edit variables here

# Input file name
file_name = "2020calndata"

# Output file first row header
output_title = ["Team", "Auto Init Points", "Auto Cells", "Tele Cells", "Control Panel", "End Game Points", "Score"]

# List of weights for each corresponding column
auto_init_wt = 5
auto_cell_wt = 4
tele_cell_wt = 2
control_panel_wt = 15
end_game_wt = 25

weights = [auto_init_wt, auto_cell_wt, tele_cell_wt, control_panel_wt, end_game_wt]

#  ========================================================

title = []
team_data = []
output_teams = []
lowestScore = float("inf")


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
for i in range(0, len(team_data)):
    score = 0
    for j in range(0, len(team_data[i])):
        if j != 0:
            team_data[i][j] = float(team_data[i][j]) * weights[j-1]
            score += float(team_data[i][j])
    team_data[i].append(score)

    # sort by score
    if score < lowestScore:
        output_teams.append(team_data[i])
        lowestScore = score
    else:
        k = 0
        while score < output_teams[k][len(output_title) - 1]:
            k += 1
        output_teams.insert(k, team_data[i])


# Write to an output file
with open(file_name + "_output.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Write header for output file
    writer.writerow(output_title)

    # Write team rows for output file
    for i in range(0, len(output_teams)):
        writer.writerow(output_teams[i])


