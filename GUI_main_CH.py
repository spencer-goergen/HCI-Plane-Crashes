from unicodedata import category
import PySimpleGUI as sg            # For GUI
import pandas as pd                 # For Graphs
import matplotlib.pyplot as plt     # ...
import numpy as np                  # ...
import seaborn as sns               # ...
import os                           # For directory movement


# System Top menu

menu_def = [['File', ['Open', 'Save', 'Exit']],
            ['Edit', ['Paste', ['Special', 'Normal'], 'Undo']],
            ['Help', 'About...']]

# Menus for GUI

button_menu_def_graph = ['', ['Line Graph', 'Bar Graph']]
button_menu_def_countries = ['', ['All Countries', 'United States of America', 'China']]
button_menu_def_cause = ['', ['All Causes', 'Technical Failure', 'Terrorism']]
button_menu_def_survivors = ['', ['Yes', 'No', 'Both']]
button_menu_def_type = ['', ['Something', 'Bar Graph']]
button_menu_def_phase = ['', ['All', 'Bar Graph']]

# Default Graphs
# Please never ever hardcode folder names, just use relative path!
# Otherwise how would somebody else run your code?
default_line = 'images/Deaths_By_Year_Line.png'
default_bar = 'images/Deaths_By_Year_Bar.png'


# Top Variables
t_graph = 'Line Graph'
t_country = 'All Countries'
t_cause = 'All Causes'
t_survivors = 'All Survivors'
t_type = 'All Types'
t_phase = 'all Phases'


# Bottom Variables
b_graph = 'Bar Graph'
b_country = 'All Countries'
b_cause = 'All Causes'
b_survivors = 'both survivors'
b_type = 'all types'
b_phase = 'all phases'

country = 'initiate'


# GUI Layout
# CH this looks very confusing. Can this be visually better structured?
layout = [
        [sg.Menu(menu_def,text_color='black', font="SYSTEM_DEFAULT", pad=(10,10)),],
        [sg.Text('                                                                       '), sg.ButtonMenu('Graph Type', menu_def=button_menu_def_graph, border_width=5, key='t_graph_menu'),sg.ButtonMenu('Countries', menu_def=button_menu_def_countries, border_width=5, key='t_country_menu'), sg.ButtonMenu('Crash Cause', menu_def=button_menu_def_cause, border_width=5, key='t_cause_menu'), sg.ButtonMenu('Survivors', menu_def=button_menu_def_survivors, border_width=5, key='-B_MENU-'),sg.ButtonMenu('Flight Type', menu_def=button_menu_def_type, border_width=5, key='-B_MENU-'),sg.ButtonMenu('Flight Phase', menu_def=button_menu_def_phase, border_width=5, key='-B_MENU-'), sg.Button('Refresh Top Image'),sg.Text('                                                                          '),sg.Button('Exit')],
        [sg.Text('                                                                       '), sg.pin(sg.Text(t_graph, key='t_graph')), sg.pin(sg.Text(t_country, key='t_country')), sg.pin(sg.Text(t_cause, key='t_cause')), sg.pin(sg.Text(t_survivors, key='t_survivors')), sg.pin(sg.Text(t_type, key='t_type')), sg.pin(sg.Text(t_phase, key='t_phase'))],
        [sg.pin(sg.Image(filename=default_line, key='top_graph'))],
        [sg.Text('                                                                                                             '),sg.Text('Last Top Settings: '),sg.pin(sg.Text('Default Setup', key='t_output'))],
        [sg.Text(' ')], #Space between outputs
        [sg.Text('                                                                       '), sg.ButtonMenu('Graph Type', menu_def=button_menu_def_graph, border_width=5, key='b_graph_menu'),sg.ButtonMenu('Countries', menu_def=button_menu_def_countries, border_width=5, key='b_country_menu'), sg.ButtonMenu('Crash Cause', menu_def=button_menu_def_cause, border_width=5, key='b_cause_menu'), sg.ButtonMenu('Survivors', menu_def=button_menu_def_survivors, border_width=5, key='-B_MENU-'),sg.ButtonMenu('Flight Type', menu_def=button_menu_def_type, border_width=5, key='-B_MENU-'),sg.ButtonMenu('Flight Phase', menu_def=button_menu_def_phase, border_width=5, key='-B_MENU-'), sg.Button('Refresh Bottom Image')],
        [sg.Text('                                                                       '), sg.pin(sg.Text(b_graph, key='b_graph')), sg.pin(sg.Text(b_country, key='b_country')), sg.pin(sg.Text(b_cause, key='b_cause')), sg.pin(sg.Text(b_survivors, key='b_survivors')), sg.pin(sg.Text(b_type, key='b_type')), sg.pin(sg.Text(b_phase, key='b_phase'))],
        [sg.pin(sg.Image(filename=default_bar, key='bottom_graph'))],
        [sg.Text('                                                                                                             '),sg.Text('Last Bottom Settings: '),sg.pin(sg.Text('Default Setup', key='b_output'))],       
    ]


# GUI Function
#GUI_run(df, t_country, b_country, t_cause):
def GUI_run():
    window =sg.Window('Plane Crashes from 1970-2022',layout)
    while True:

        # Bring in Global Variables
        global t_country
        global b_country
        global t_cause

        # Why can these not be normal args to GUI_run()?

        event, values = window.read()

        # Close on Exit
        if event in (sg.WIN_CLOSED, 'Exit'):
                break


        # Top Graph Update Variables
        if values['t_graph_menu'] == "Line Graph":
            print("Now Line Graph")
            t_graph = 'Line graph'
            window['t_graph'].Update(t_graph)

        if values['t_graph_menu'] == "Bar Graph":
            print("Bar Graph")
            t_graph = 'Bar graph'
            window['t_graph'].Update(t_graph)
        
        if values['t_country_menu'] == "China":
            t_country = 'China'
            window['t_country'].Update(t_country)

        if values['t_country_menu'] == "All Countries":
            t_country = 'All Countries'
            window['t_country'].Update(t_country)
        
        if values['t_country_menu'] == "United States of America":
            t_country = 'United States of America'
            window['t_country'].Update(t_country)

        if values['t_cause_menu'] == 'Technical Failure':
            t_cause = 'Technical Failure'
            window['t_cause'].Update(t_cause)

        if values['t_cause_menu'] == 'All Causes':
            t_cause = 'All Causes'
            window['t_cause'].Update(t_cause)




        # Bottom Graph Update Variables
        if values['b_country_menu'] == "China":
            b_country = 'China'
            window['b_country'].Update(b_country)
        
        if values['b_country_menu'] == "United States of America":
            b_country = 'United States of America'
            window['b_country'].Update(b_country)



        if values['b_graph_menu'] == "Line Graph":
            print("Now Line Graph")
            b_graph = 'Line graph'
            window['b_graph'].Update(b_graph)

        if values['b_graph_menu'] == "Bar Graph":
            print("Bar Graph")
            b_graph = 'Bar graph'
            window['b_graph'].Update(b_graph)

        if values['b_cause_menu'] == 'Technical Failure':
            b_cause = 'Technical Failure'
            window['t_cause'].Update(b_cause)

        if values['b_cause_menu'] == 'All Causes':
            b_cause = 'All Causes'
            window['b_cause'].Update(b_cause)




        # Refresh Top Graph
        if event=='Refresh Top Image':
            if values['t_graph_menu'] == "Bar Graph":
                if values['t_country_menu'] == 'All Countries':
                    t_graph = 'Bar Graph'
                    window['t_graph'].Update(t_graph)

                    barPlot_causes()
                    print('success')
                    #window['top_graph'].Update(filename='images/output.png')
                elif values['t_country_menu'] != 'All Countries':
                    t_graph = 'Bar Graph'
                    window['t_graph'].Update(t_graph)

                    barPlot_t()
                    print('success')
                    #window['top_graph'].Update(filename='images/output.png')
            
            if values['t_graph_menu'] == "Line Graph":
                if values['t_country_menu'] == 'All Countries':
                    t_graph = 'Line Graph'
                    window['t_graph'].Update(t_graph)

                    linePlot_all()
                    print('success')
                    #window['top_graph'].Update(filename='images/output.png')
                elif values['t_country_menu'] != 'All Countries':
                    t_graph = 'Line Graph'
                    window['t_graph'].Update(t_graph)

                    linePlot_t()
                    print('success')
                    #window['top_graph'].Update(filename='images/output.png')

        # Refresh Bottom Graph

        if event=='Refresh Bottom Image':
            if values['b_graph_menu'] == "Bar Graph":
                if values['b_country_menu'] == 'All Countries':
                    b_graph = 'Bar Graph'
                    window['b_graph'].Update(b_graph)

                    barPlot_causes()
                    print('success')
                    #window['bottom_graph'].Update(filename='images/output.png')
                elif values['b_country_menu'] != 'All Countries':
                    b_graph = 'Bar Graph'
                    window['b_graph'].Update(b_graph)

                    barPlot_b()
                    print('success')
                    #window['bottom_graph'].Update(filename='images/output.png')
            
            if values['b_graph_menu'] == "Line Graph":
                if values['b_country_menu'] == 'All Countries':
                    b_graph = 'Line Graph'
                    window['b_graph'].Update(b_graph)

                    linePlot_all()
                    print('success')
                    #window['bottom_graph'].Update(filename='images/output.png')
                elif values['b_country_menu'] != 'All Countries':
                    b_graph = 'Line Graph'
                    window['b_graph'].Update(b_graph)

                    linePlot_b()
                    print('success')
                    #window['bottom_graph'].Update(filename='images/output.png')
                

            
        #if t_array == line_all_graph:
             #window['top_graph'].Update(filename=default_line)

        #window['top_graph'].Update(filename=default_bar)
        #window['t_output'].Update(' Top Refreshed to ' + t_graph + ', ' + t_country + ', ' + t_cause + ', ' + t_survivors + ', ' + t_type + ', ' + t_phase, 'red')
        


    # End of GUI_run()

    window.close()



# Top Graphs

def linePlot_t():
    df_line = pd.read_csv("Plane Crash dataset.csv")    
    from GUI_main import GUI_run

    df0 = df_line[df_line.Country == t_country]

    #Total Fatalities
    print("all fatalities", df0["Total fatalities"].sum())

    print(t_cause)

    category = 'Year'

    numeric = 'Total fatalities'

    print(t_cause)

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb0 = df0.groupby(category)[numeric].sum()

    print(gb0)


    print("groupby as Series:") 
    print(gb0, type(gb0))




      # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
      # is its index (which can be non-numeric) and the right (unnamed) column has
      # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
      # I'll create a new, separate df for plotting:

    d0 = {category: gb0.index,
        numeric: gb0.values}
    dfgb0 = pd.DataFrame(d0)
    #dfgb0




    #Graph Total Deaths By Year
    name = "Deaths_By_Year_Line"
    fig, ax = plt.subplots(figsize=(12.75,3.5))  # new plot
    x = 'Year'
    y = 'Total fatalities'

    ax = sns.lineplot(x=x, y=y, # which columns for x and y
                    data=dfgb0, # in which dataframe
                    ci=0, # no error bars (much faster!)
                    ) 


    plt.xticks(rotation=90)
    ax.tick_params(axis='x', which='both', labelsize=8)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    ax.set_title("Total Deaths by Year for " + t_country, fontsize='22')
    ax.set_ylabel(ax.get_ylabel(), fontsize='18')
    ax.set_xlabel(ax.get_xlabel(), fontsize='18')
    sns.set(rc={'figure.figsize':(.2,.1)})

    fig = ax.get_figure()
    #os. chdir("images/")
    #print(os.getcwd())

    #fig.savefig("output.png") 

#def barPlot_t(df): # better?
def barPlot_t():
    from GUI_main import GUI_run

    # Maybe this is silly b/c the files are not that large but why not make a dataframe outside
    # this function and give it to both rather re-reading it in again?
    df_bar = pd.read_csv("Plane Crash dataset.csv") 

    df1 = df_bar[df_bar.Country == t_country]

    #Total Fatalities
    print("all fatalities", df_bar["Total fatalities"].sum())

    category = 'Year'
    numeric = 'Total fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb1 = df1.groupby(category)[numeric].sum()

    print(gb1)


    print("groupby as Series:") 
    print(gb1, type(gb1))


    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d1 = {category: gb1.index,
        numeric: gb1.values}
    dfgb1 = pd.DataFrame(d1)
    dfgb1

    # Plot Graph
    fig, ax = plt.subplots(figsize=(12.75,3.5))  # new plot

    ax = sns.barplot(x="Year", y="Total fatalities", # which columns for x and y
                        data=dfgb1, # in which dataframe
                        ci=0, # no error bars (much faster!)
                        ) 


    plt.xticks(rotation=90)

    ax.set_title("Fatalities by Year for " + t_country, fontsize='22')

    ax.set_ylim(0,1000)
    ax.set_ylabel(ax.get_ylabel(), fontsize='18')
    ax.set_xlabel(ax.get_xlabel(), fontsize='18')
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)

    #fig = ax.get_figure()
    #os. chdir("images/")
    #print(os.getcwd())

    #fig.savefig("output.png") 


#def barPlot_causes(df):
def barPlot_causes():
    from GUI_main import GUI_run

    df = pd.read_csv("Plane Crash dataset.csv")

    #Total Fatalities
    print("all fatalities", df["Total fatalities"].sum())

    category0 = 'Crash cause'
    numeric0 = 'Total fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb = df.groupby(category0)[numeric0].sum()
    print("groupby as Series:") 
    print(gb, type(gb))

    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d = {category0: gb.index,
        numeric0: gb.values}
    dfgb0 = pd.DataFrame(d)
    dfgb0
    print(dfgb0)

    dfgb0.insert(2, "Fatalities", dfgb0['Total fatalities'], True)
    numeric01 = 'Fatalities'

    print(dfgb0)

    #Crew Fatalities
    print("all fatalities", df["Crew fatalities"].sum())

    category1 = 'Crash cause'
    numeric1 = 'Crew fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb = df.groupby(category1)[numeric1].sum()
    print("groupby as Series:") 
    print(gb, type(gb))

    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d = {category1: gb.index,
        numeric1: gb.values}
    dfgb1 = pd.DataFrame(d)
    dfgb1

    dfgb1.insert(2, "Fatalities", dfgb1['Crew fatalities'], True)
    numeric01 = 'Fatalities'

    print(dfgb1)

    #Passenger Fatalities
    print("all fatalities", df["PAX fatalities"].sum())

    category2 = 'Crash cause'
    numeric2 = 'PAX fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb = df.groupby(category2)[numeric2].sum()
    print("groupby as Series:") 
    print(gb, type(gb))

    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d = {category2: gb.index,
        numeric2: gb.values}
    dfgb2 = pd.DataFrame(d)
    dfgb2

    dfgb2.insert(2, "Fatalities", dfgb2['PAX fatalities'], True)
    numeric2 = 'Fatalities'

    print(dfgb2)

    #Other Fatalities
    print("all fatalities", df["Other fatalities"].sum())

    category3 = 'Crash cause'
    numeric3 = 'Other fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb = df.groupby(category3)[numeric3].sum()
    print("groupby as Series:") 
    print(gb, type(gb))

    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d = {category3: gb.index,
        numeric3: gb.values}
    dfgb3 = pd.DataFrame(d)
    dfgb3

    dfgb3.insert(2, "Fatalities", dfgb3['Other fatalities'], True)
    numeric01 = 'Fatalities'

    print(dfgb0)
    # 1 graph working
    name = 'Crash_Cause_By_Fatalities_Bar'

    aa=dict(zip(dfgb0['Crash cause'],dfgb0['Fatalities']))
    bb=dict(zip(dfgb1['Crash cause'],dfgb1['Fatalities']))
    cc=dict(zip(dfgb2['Crash cause'],dfgb2['Fatalities']))
    dd=dict(zip(dfgb3['Crash cause'],dfgb3['Fatalities']))

    dfbar = pd.DataFrame({'Total Fatalities': aa, 'Crew Fatalities': bb, 'Passenger Fatalities': cc,'Other Fatalities': dd})

    # Non-stacked bar plot
    graph = dfbar.plot.bar(figsize=(12.75,3.5))

    plt.title("Fatalities by Crash Cause")
    plt.legend(title="Fatalitiy Type")
    plt.xticks(rotation=0)

    # Save Graph
    #os. chdir("images/")
    #print(os.getcwd())


    #fig = graph.get_figure()
    #fig.savefig('output.png') 

#def linePlot_all(df):
def linePlot_all():
    df = pd.read_csv("Plane Crash dataset.csv")    # CH always use relative paths
    from GUI_main import GUI_run  # CH put ALL import on top!
    #Total Fatalities
    print("all fatalities", df["Total fatalities"].sum())

    category = 'Year'
    numeric = 'Total fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb = df.groupby(category)[numeric].sum()
    print("groupby as Series:") 
    print(gb, type(gb))

    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d = {category: gb.index,
        numeric: gb.values}
    dfgb = pd.DataFrame(d)
    dfgb
    #Graph Total Deaths By Year
    name = "Deaths_By_Year_Line"
    fig, ax = plt.subplots(figsize=(12.75,3.5))  # new plot
    x = 'Year'
    y = 'Total fatalities'

    ax = sns.lineplot(x=x, y=y, # which columns for x and y
                        data=dfgb, # in which dataframe
                        ci=0, # no error bars (much faster!)
                        ) 


    plt.xticks(rotation=90)
    ax.tick_params(axis='x', which='both', labelsize=8)

    ax.set(ylim=(0, 5000))

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    ax.set_title("Total Deaths by Year", fontsize='22')
    ax.set_ylabel(ax.get_ylabel(), fontsize='18')
    ax.set_xlabel(ax.get_xlabel(), fontsize='18')
    sns.set(rc={'figure.figsize':(.2,.1)})

    #fig = ax.get_figure()
    #os. chdir("images/")
    #print(os.getcwd())

    #fig.savefig("output.png") 








# Bottom Graphs
#def linePlot_b(df):
def linePlot_b():
    df_line = pd.read_csv("Plane Crash dataset.csv")    
    from GUI_main import GUI_run

    df0 = df_line[df_line.Country == b_country]

    print("DKSJFNDSJIFSDFHKSDFJSFSNDF ---" + b_country)

    #Total Fatalities
    print("all fatalities", df0["Total fatalities"].sum())

    category = 'Year'
    numeric = 'Total fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb0 = df0.groupby(category)[numeric].sum()

    print(gb0)


    print("groupby as Series:") 
    print(gb0, type(gb0))




      # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
      # is its index (which can be non-numeric) and the right (unnamed) column has
      # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
      # I'll create a new, separate df for plotting:

    d0 = {category: gb0.index,
        numeric: gb0.values}
    dfgb0 = pd.DataFrame(d0)
    dfgb0




    #Graph Total Deaths By Year
    name = "Deaths_By_Year_Line"
    fig, ax = plt.subplots(figsize=(12.75,3.5))  # new plot
    x = 'Year'
    y = 'Total fatalities'

    ax = sns.lineplot(x=x, y=y, # which columns for x and y
                    data=dfgb0, # in which dataframe
                    ci=0, # no error bars (much faster!)
                    ) 


    plt.xticks(rotation=90)
    ax.tick_params(axis='x', which='both', labelsize=8)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    ax.set_title("Total Deaths by Year for " + b_country, fontsize='22')
    ax.set_ylabel(ax.get_ylabel(), fontsize='18')
    ax.set_xlabel(ax.get_xlabel(), fontsize='18')
    sns.set(rc={'figure.figsize':(.2,.1)})

    #fig = ax.get_figure()
    #os. chdir("images/")
    #print(os.getcwd())

    #fig.savefig("output.png") 


def barPlot_b():
    from GUI_main import GUI_run

    df_bar = pd.read_csv("Plane Crash dataset.csv")

    df1 = df_bar[df_bar.Country == b_country]

    #Total Fatalities
    print("all fatalities", df_bar["Total fatalities"].sum())

    category = 'Year'
    numeric = 'Total fatalities'

    # group fatalities by cause:  https://datagy.io/pandas-groupby/
    gb1 = df1.groupby(category)[numeric].sum()

    print(gb1)


    print("groupby as Series:") 
    print(gb1, type(gb1))


    # The issue (for me anyway) is that gb is not a dataframe, the left most "column"
    # is its index (which can be non-numeric) and the right (unnamed) column has
    # the actual values. Thing is you can't plot with that (x=index y=unnamed) so
    # I'll create a new, separate df for plotting:

    d1 = {category: gb1.index,
        numeric: gb1.values}
    dfgb1 = pd.DataFrame(d1)
    dfgb1

    # Plot Graph
    fig, ax = plt.subplots(figsize=(12.75, 3.5))  # new plot

    ax = sns.barplot(x="Year", y="Total fatalities", # which columns for x and y
                        data=dfgb1, # in which dataframe
                        ci=0, # no error bars (much faster!)
                        ) 


    plt.xticks(rotation=90)

    ax.set_title("Fatalities by Year for " + b_country, fontsize='22')

    ax.set_ylim(0, 1000)
    ax.set_ylabel(ax.get_ylabel(), fontsize='18')
    ax.set_xlabel(ax.get_xlabel(), fontsize='18')
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)

    #fig = ax.get_figure()
    #os. chdir("images/")
    #print(os.getcwd())

    #fig.savefig("output.png")

#df = pd.read_csv("Plane Crash dataset.csv")
#GUI_run(df, t_country, b_country, t_cause)


GUI_run()