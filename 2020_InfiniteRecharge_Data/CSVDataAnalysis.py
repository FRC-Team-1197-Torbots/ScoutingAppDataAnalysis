import csv

#  ========================================================

file_name = "2020calndata.csv"
output_title = ["Team", "Auto Init Points", "Auto Cells", "Tele Cells", "Control Panel", "End Game Points", "Score"]
# Should be a list of
auto_init_wt = 0
auto_cell_wt = 0
tele_cell_wt = 0
control_panel_wt = 0
end_game_wt = 0
weights = [auto_init_wt, auto_cell_wt, tele_cell_wt, control_panel_wt, end_game_wt]

#  ========================================================

title = []
team_data = []

# Open File
with open(file_name) as csv_file:
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




# Write to an output file
with open(file_name + "_output.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(output_title)

