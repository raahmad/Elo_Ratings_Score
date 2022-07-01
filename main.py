"""

Partner Group: Raees Ahmad and Dave Thaker

"""

from tkinter import*
import csv

# Get File
filepath = '/Users/theRa/OneDrive/Documents/Computational Thinking Project/nba_elo_538.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])
print(Data)

# Get Column Information
list_of_games = []
for x in list(range(0, len(Data))):
    list_of_games.append(Data[x][0])

# Import Tkinter Roots
root = Tk()
root.title('NBA Elo Ratings')
root.geometry('1200x700')

# Title Labels
L1 = Label(root, text="Compare Over 67000 NBA Games from 1946 Through 2018")
L1.grid(row=1, column=40)
L2 = Label(root, text="And See a Graph of the Elo Ratings Involved in Lebron James Final Game for Cleveland")
L2.grid(row=2, column=40)
L3 = Label(root, text="*Close Window to See Graph")
L3.grid(row=60, column=0)
L4 = Label(root, text="*Click Exit to Close Everything")
L4.grid(row=70, column=0)

# Insert a Listbox
listbox1 = Listbox(root)
listbox1.config(width=25, height=15)
for x, y in enumerate(list_of_games):
    listbox1.insert(x, y)
listbox1.grid(row=0, column=0)

# Insert a Enter Button
def enter():
    index=listbox1.curselection()[0]
    gamelabel2.config(text=Data[index][0])
    datelabel2.config(text=Data[index][1])
    seasonlabel2.config(text=Data[index][2])
    HomeTeamlabel2.config(text=Data[index][3])
    AwayTeamlabel2.config(text=Data[index][4])
    HomeTeamEloPRElabel2.config(text=Data[index][5])
    AwayTeamEloPRElabel2.config(text=Data[index][6])
    HomeTeamEloProblabel2.config(text=Data[index][7])
    AwayTeamEloProblabel2.config(text=Data[index][8])
    HomeTeamEloPostlabel2.config(text=Data[index][9])
    AwayTeamEloPostlabel2.config(text=Data[index][10])
    HomeTeamScorelabel2.config(text=Data[index][11])
    AwayTeamScorelabel2.config(text=Data[index][12])
    return None

button1=Button(root, text="Enter", command=enter)
button1.grid(row=55, column=35)

# Inserting Labels
gamelabel = Label(root, text="Game").grid(row=1, column=0, sticky='w')
datelabel = Label(root, text="Date").grid(row=2, column=0, sticky='w')
seasonlabel = Label(root, text="Season").grid(row=3, column=0, sticky='w')
HomeTeamlabel = Label(root, text="Home Team").grid(row=4, column=0, sticky='w')
AwayTeamlabel = Label(root, text="Away Team").grid(row=5, column=0, sticky='w')
HomeTeamEloPRElabel = Label(root, text="Home Team elo_pre").grid(row=6, column=0, sticky='w')
AwayTeamEloPRElabel = Label(root, text="Away Team elo_pre").grid(row=7, column=0, sticky='w')
HomeTeamEloProblabel = Label(root, text="Home Team elo_prob").grid(row=8, column=0, sticky='w')
AwayTeamEloProblabel = Label(root, text="Away Team elo_prob").grid(row=9, column=0, sticky='w')
HomeTeamEloPostlabel = Label(root, text="Home Team elo_post").grid(row=10, column=0, sticky='w')
AwayTeamEloPostlabel = Label(root, text="Away Team elo_post").grid(row=11, column=0, sticky='w')
HomeTeamScorelabel = Label(root, text="Home Team Score").grid(row=12, column=0, sticky='w')
AwayTeamScorelabel = Label(root, text="Away Team Score").grid(row=13, column=0, sticky='w')

gamelabel2 = Label(root, text="")
gamelabel2.grid(row=1, column=1, sticky='w')
datelabel2 = Label(root, text="")
datelabel2.grid(row=2, column=1, sticky='w')
seasonlabel2 = Label(root, text="")
seasonlabel2.grid(row=3, column=1, sticky='w')
HomeTeamlabel2 = Label(root, text="")
HomeTeamlabel2.grid(row=4, column=1, sticky='w')
AwayTeamlabel2 = Label(root, text="")
AwayTeamlabel2.grid(row=5, column=1, sticky='w')
HomeTeamEloPRElabel2 = Label(root, text="")
HomeTeamEloPRElabel2.grid(row=6, column=1, sticky='w')
AwayTeamEloPRElabel2 = Label(root, text="")
AwayTeamEloPRElabel2.grid(row=7, column=1, sticky='w')
HomeTeamEloProblabel2 = Label(root, text="")
HomeTeamEloProblabel2.grid(row=8, column=1, sticky='w')
AwayTeamEloProblabel2 = Label(root, text="")
AwayTeamEloProblabel2.grid(row=9, column=1, sticky='w')
HomeTeamEloPostlabel2 = Label(root, text="")
HomeTeamEloPostlabel2.grid(row=10, column=1, sticky='w')
AwayTeamEloPostlabel2 = Label(root, text="")
AwayTeamEloPostlabel2.grid(row=11, column=1, sticky='w')
HomeTeamScorelabel2 = Label(root, text="")
HomeTeamScorelabel2.grid(row=12, column=1, sticky='w')
AwayTeamScorelabel2 = Label(root, text="")
AwayTeamScorelabel2.grid(row=13, column=1, sticky='w')

# Elo Ratings Definitions
elo_ratings = {
    'What does elo_pre mean?': 'The Elo Rating of a Team Prior to a Match Being Played',
    'What does elo_prob mean?': 'The Probability of a Team Winning That Match',
    'What does elo_post mean?': 'The Elo Rating of a Team After a Match Being Played',
}

# Create a listbox for Elo Ratings Information
listbox2 = Listbox(root)
listbox2.config(width=50, height=0)
for x, y, in enumerate(elo_ratings):
    listbox2.insert(x+1, y)
listbox2.grid(row=5, column=60)

# Create Elo Rating Button
def elorating():
    entry2.delete(0, 'end')
    elo = listbox2.get(ANCHOR)
    entry2.insert(0, elo_ratings[elo])
    pass

button1=Button(root, text="Elo Rating", command=elorating)
button1.grid(row=6, column=60)

# Create entry to get answers for Elo Ratings Information
label1=Label(root, text="Answer").grid(row=8, column=60)
entry2=Entry(root, width=50)
entry2.grid(row=7, column=60)

# Fun Facts Questions and Answers
fun_facts = {
    'What does a High Elo Rating Mean?': 'The Higher the Elo Rating the Better the Team',
    'Who had the Highest Elo Rating Ever?': '2017 GSW in June 2017 who had a Rating of 1846',
    'Who had the Highest Team Score Ever?': '1984 DET in Dec. 1983 who had a Score of 186',
}

# Create a listbox for Fun Facts Questions and Answers
listbox3 = Listbox(root)
listbox3.config(width=50, height=0)
for x, y, in enumerate(fun_facts):
    listbox3.insert(x+1, y)
listbox3.grid(row=10, column=60)

# Create Fun Facts Button
def funfacts():
    entry3.delete(0, 'end')
    facts = listbox3.get(ANCHOR)
    entry3.insert(0, fun_facts[facts])
    pass

button2=Button(root, text="Fun Facts", command=funfacts)
button2.grid(row=11, column=60)

# Create entry to place the answer for Fun Facts
label3=Label(root, text="Answer").grid(row=13, column=60)
entry3=Entry(root, width=50)
entry3.grid(row=12, column=60)


# Insert an Exit Button
# This is Our Error Handling Button
def Exit():
    exit()
button3=Button(root, text="Exit", command = Exit)
button3.grid(row=55, column=45)
mainloop()

# Bar Graph of Lebron James Game for Cleveland
import utilities as c

print(c)


root.mainloop()
