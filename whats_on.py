
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10329935
#    Student name: DO VIET HOANG
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  What's On?: Online Entertainment Planning Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for planning an entertainment schedule.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it as a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'


# Import an exception raised when a web server denies access
# to a document
from urllib.error import HTTPError

#some standard libraries support the program
import webbrowser
import datetime


music_url = 'https://www.eventbrite.com.au/d/australia--brisbane-city/music/'
film_url = 'https://www.eventbrite.com.au/d/australia--brisbane-city/film/'
politics_url = 'https://www.eventbrite.com.au/d/australia--brisbane-city/politics/'

months_dict = {
    'Jan': 0
}
months_dict['Feb'] = months_dict['Jan'] + 31
months_dict['Mar'] = months_dict['Feb'] + 29
months_dict['Apr'] = months_dict['Mar'] + 31
months_dict['May'] = months_dict['Apr'] + 30
months_dict['Jun'] = months_dict['May'] + 31
months_dict['Jul'] = months_dict['Jun'] + 30
months_dict['Aug'] = months_dict['Jul'] + 31
months_dict['Sep'] = months_dict['Aug'] + 31
months_dict['Oct'] = months_dict['Sep'] + 30
months_dict['Nov'] = months_dict['Oct'] + 31
months_dict['Dec'] = months_dict['Nov'] + 30

currentDT = datetime.datetime.now()
now = currentDT.strftime("%a, %b %d, %I:%M%p")
now = now.replace('AM', 'am')
now = now.replace('PM', 'pm')

#turn the date into a value for comparison
def get_value_date(text):
    day, date, stuff = text.split(',')
    blank, month, month_date = date.split(' ')
    date_value = months_dict[month] + int(month_date)
    for i in range(len(stuff)):
        if stuff[i] == 'm':
            stuff = stuff[slice(0, i + 1)].replace(' ', '')
            break
    stuff = stuff.replace('p', ' p')
    stuff = stuff.replace('a', ' a')

    clock, meridiem = stuff.split(' ')
    hour, minute = clock.split(':')
    if int(hour) == 12 and meridiem == 'am':
        return date_value * 3600 + int(minute)
    elif int(hour) == 12 and meridiem == 'pm':
        return date_value * 3600 + 12 * 60 + int(minute)
    elif meridiem == 'pm':
        return date_value * 3600 + (int(hour) + 12) * 60 + int(minute)
    elif meridiem == 'am':
        return date_value * 3600 + int(hour) * 60 + int(minute)

#sort the event date
def bubleSort(alist):
    temp = []
    for i in range(len(alist)):
        temp.append([])
    for passnum in range(len(alist[len(alist) - 1]) - 1, 0, -1):
        for i in range(passnum):
            if alist[3][i] > alist[3][i + 1]:
                for j in range(len(alist)):
                    temp[j] = alist[j][i]
                    alist[j][i] = alist[j][i + 1]
                    alist[j][i + 1] = temp[j]
    return alist


# function to get and return a list of online events, date, images that retrieved from online websites
def get_online(isOffline=1, web_content='music'):
    date = []
    event = []
    image = []
    date_value = []

    if isOffline == 1:
        if web_content == 'music':
            text = open('archive/music.html').read()
        elif web_content == 'film':
            text = open('archive/film.html').read()
        elif web_content == 'politics':
            text = open('archive/politics.html').read()
    else:
        if web_content == 'music':
            download(url=music_url, target_filename='music_onl')
            text = open('music_onl.html', encoding="utf-8").read()
        elif web_content == 'film':
            download(url=film_url, target_filename='film_onl')
            text = open('film_onl.html', encoding="utf-8").read()
        elif web_content == 'politics':
            download(url=politics_url, target_filename='politics_onl')
            text = open('politics_onl.html', encoding="utf-8").read()

    #use regex to find events information and store it in a list
    music_event = findall(
        '<div class=\"event-card__formatted-name--is-clamped\" aria-hidden=\"true\" role=\"presentation\" data-spec=\"event-card__formatted-name--content\" data-reactid=\"\d*\">([^<]+)</\w*>',
        text)
    date_event = findall(
        '<div class=\"eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1\" data-reactid=\"\d*\">([^$<]+)</div>',
        text)
    image_event = findall('<img class=\"eds-media-card-content__image eds-max-img\" src=\"([^\"]+)',
                          text)

    #replace some unusual characters
    for i in range(len(music_event)):
        music_event[i] = music_event[i].replace('&quot;', '\"')
        music_event[i] = music_event[i].replace('&amp;', '&')
        music_event[i] = music_event[i].replace('&#x27;', '\'')

    for i in range(len(music_event) // 2):
        event.append(music_event[i])

    for i in range(len(date_event)):
        date_event[i] = date_event[i].replace('&quot;', '\"')
        date_event[i] = date_event[i].replace('&amp;', '&')
        date_event[i] = date_event[i].replace('&#x27;', '\'')

    for i in range(len(date_event) // 2):
        date.append(date_event[i])

    for i in range(len(date)):
        date_value.append(get_value_date(date[i]))

    for i in range(len(image_event)):
        image_event[i] = image_event[i].replace('&quot;', '\"')
        image_event[i] = image_event[i].replace('&amp;', '&')
        image_event[i] = image_event[i].replace('&#x27;', '\'')

    for i in range(len(image_event) // 2):
        image.append(image_event[i])

    #sort event based on date
    list_print = bubleSort([event, date, image, date_value])

    for i in range(len(list_print[3])):

        # Only return the list of events that will occure after current date
        # You DO NOT need to edit the HTML file for checking my code, just use other parameter in get_value_date()
        # For example: using 'if list_print[3][i]  > get_value_date('blabla, Jul 7, 7:00pm blabla'):'
        # to check if there are any events after Jul 7, 7:00pm. Make sure you type the correct format for parameter.
        # if list_print[3][i]  > get_value_date('blabla, Jul 7, 7:00pm blabla'):
        if list_print[3][i] > get_value_date(now):
            for j in range(len(list_print)):
                list_print[j] = list_print[j][i:]
            break
    return list_print


# some useful variable. I store the Checkbutton in a dictionary with defined keys
music_variables = {'music_1', 'music_2', 'music_3', 'music_4', 'music_5', 'music_6', 'music_7', 'music_8', 'music_9',
                   'music_10'}
music_checkbutton = dict()

film_variables = {'film_1', 'film_2', 'film_3', 'film_4', 'film_5', 'film_6', 'film_7', 'film_8', 'film_9', 'film_10'}
film_checkbutton = dict()

politics_variables = {'pol_1', 'pol_2', 'pol_3', 'pol_4', 'pol_5', 'pol_6', 'pol_7', 'pol_8', 'pol_9', 'pol_10'}
politics_checkbutton = dict()

# variables to count the selected events
count_event = 0
count_music = 0
count_film = 0
count_politics = 0


# function to create the Music Page
def PageOne():  # new window definition
    global off_var, music_variables, music_checkbutton
    page_one = Toplevel(root)

    page_one['bg'] = '#6AB187'
    label = Label(page_one, text="Music events", font='Roboto 14 bold', bg='#6AB187')
    label.grid(row=0, pady=10)

    if off_var.get() != 1:
        list = get_online(isOffline=0, web_content='music')
    if off_var.get() == 1:
        list = get_online(isOffline=1, web_content='music')

    j = 0

    for i in music_variables:
        if j < len(list[0]):
            music_event = list[0][j]
            music_date = list[1][j]
            music_image = list[2][j]
            if 'placeholder' in music_image:
                music_image = 'http://www.dwphoto.com.au/wp-content/uploads/2012/09/brisbane-events-riverfire-dwphoto-03-670x390.jpg'
            music_checkbutton[i] = [
                Checkbutton(page_one, font='Roboto 11', activebackground='#6AB187', onvalue=1, bg='#6AB187',
                            command=update_print_music), music_event, music_date, music_image]
            music_checkbutton[i][0].var = IntVar()
            music_checkbutton[i][0]['variable'] = music_checkbutton[i][0].var
            music_checkbutton[i][0].grid(row=j + 1, sticky=W, pady=3)

            music_checkbutton[i][0]['text'] = str(j + 1) + ': ' + str(music_checkbutton[i][1]) + ' ( ' + str(
                music_checkbutton[i][2]) + ' )'
        else:
            music_checkbutton[i] = [Checkbutton(page_one, onvalue=1, bg='#6AB187', command=update_print_music),
                                    '', '', '']
            music_checkbutton[i][0].var = IntVar()
            music_checkbutton[i][0]['variable'] = music_checkbutton[i][0].var
        j += 1
    label_bottom = Label(page_one, text='         ' + music_url, font='Roboto 10 italic', bg='#6AB187')
    label_bottom.grid(row=11, column=0, ipady=5, sticky=W)


# function to create the Film Page
def PageTwo():
    # new window definition
    global off_var, film_variables, film_checkbutton
    page_two = Toplevel(root)
    page_two['bg'] = '#6200EE'
    label = Label(page_two, text="Film events", bg='#6200EE', font='Roboto 14 bold', fg='white')
    label.grid(row=0, pady=10)

    # check offline or online state to read information file
    if off_var.get() != 1:
        list = get_online(isOffline=0, web_content='film')
    if off_var.get() == 1:
        list = get_online(isOffline=1, web_content='film')

    # add check button
    j = 0
    for i in film_variables:
        if j < len(list[0]):
            film_event = list[0][j]
            film_date = list[1][j]
            film_image = list[2][j]
            if 'placeholder' in film_image:
                film_image = 'http://www.dwphoto.com.au/wp-content/uploads/2012/09/brisbane-events-riverfire-dwphoto-03-670x390.jpg'
            film_checkbutton[i] = [Checkbutton(page_two, onvalue=1, font='Roboto 11', fg='white',
                                               selectcolor='#6200EE', activebackground='#6200EE', bg='#6200EE',
                                               command=update_print_film), film_event, film_date, film_image]
            film_checkbutton[i][0].var = IntVar()
            film_checkbutton[i][0]['variable'] = film_checkbutton[i][0].var
            film_checkbutton[i][0].grid(row=j + 1, sticky=W, pady=3)
            film_checkbutton[i][0]['text'] = str(j + 1) + ': ' + str(film_checkbutton[i][1]) + ' ( ' + str(
                film_checkbutton[i][2]) + ' )'
        else:
            film_checkbutton[i] = [Checkbutton(page_two, onvalue=1, bg='#6200EE', command=update_print_film),
                                   '', '', '']
            film_checkbutton[i][0].var = IntVar()
            film_checkbutton[i][0]['variable'] = film_checkbutton[i][0].var

        j += 1
    label_bottom = Label(page_two, text='         ' + film_url, fg='white', font='Roboto 10 italic', bg='#6200EE')
    label_bottom.grid(row=11, column=0, ipady=5, sticky=W)


# function to create the Politics Page
def PageThree():  # new window definition
    global off_var, politics_variables, politics_checkbutton
    page_three = Toplevel(root)

    page_three['bg'] = '#333333'
    label = Label(page_three, text="Politics events", bg='#333333', font='Roboto 14 bold', fg='white')
    label.grid(row=0, pady=10)

    if off_var.get() != 1:
        list = get_online(isOffline=0, web_content='politics')
    if off_var.get() == 1:
        list = get_online(isOffline=1, web_content='politics')

    print_event = list[0]
    print_date = list[1]
    print_image = list[2]

    j = 0
    for i in politics_variables:
        if j < len(list[0]):
            politics_event = print_event[j]
            politics_date = print_date[j]
            politics_image = print_image[j]
            if 'placeholder' in politics_image:
                politics_image = 'http://www.dwphoto.com.au/wp-content/uploads/2012/09/brisbane-events-riverfire-dwphoto-03-670x390.jpg'

            politics_checkbutton[i] = [Checkbutton(page_three, onvalue=1, bg='#333333',
                                                   selectcolor='#333333', activebackground='#333333', fg='white',
                                                   font='Roboto 11', command=update_print_politics), politics_event,
                                       politics_date, politics_image]
            politics_checkbutton[i][0].var = IntVar()
            politics_checkbutton[i][0]['variable'] = politics_checkbutton[i][0].var
            politics_checkbutton[i][0].grid(row=j + 1, sticky=W, pady=3)

            politics_checkbutton[i][0]['text'] = str(j + 1) + ': ' + str(politics_checkbutton[i][1]) + ' ( ' + str(
                politics_checkbutton[i][2]) + ' )'
        else:
            politics_checkbutton[i] = [Checkbutton(page_three, onvalue=1, bg='#333333', command=update_print_politics),
                                       '', '', '']
            politics_checkbutton[i][0].var = IntVar()
            politics_checkbutton[i][0]['variable'] = politics_checkbutton[i][0].var

        j += 1
    label_bottom = Label(page_three, text='         ' + politics_url, font='Roboto 10 italic', bg='#333333', fg='white')
    label_bottom.grid(row=11, column=0, ipady=5, sticky=W)


# function to count the music events selected
def update_print_music():
    global count_event, count_music, count_film, count_politics
    list_check = []
    for i in music_variables:
        list_check.append(music_checkbutton[i][0].var.get())

    count_music = sum(list_check)
    count_event = count_music + count_film + count_politics
    if count_event >= 2:
        print_button['text'] = 'Print planner (' + str(count_event) + ' events selected)'
    else:
        print_button['text'] = 'Print planner (' + str(count_event) + ' event selected)'


# function to count the film events selected
def update_print_film():
    global count_event, count_music, count_film, count_politics
    check = []
    for i in film_variables:
        check.append(film_checkbutton[i][0].var.get())

    count_film = sum(check)
    count_event = count_music + count_film + count_politics
    if count_event >= 2:
        print_button['text'] = 'Print planner (' + str(count_event) + ' events selected)'
    else:
        print_button['text'] = 'Print planner (' + str(count_event) + ' event selected)'


# function to count the politics events selected
def update_print_politics():
    global count_event, count_music, count_film, count_politics
    check = []
    for i in politics_variables:
        check.append(politics_checkbutton[i][0].var.get())

    count_politics = sum(check)
    count_event = count_music + count_film + count_politics
    if count_event >= 2:
        print_button['text'] = 'Print planner (' + str(count_event) + ' events selected)'
    else:
        print_button['text'] = 'Print planner (' + str(count_event) + ' event selected)'


# Create the main page
root = Tk()
root['bg'] = '#0091D5'
off_var = IntVar()
save_var = IntVar()

photo = PhotoImage(file="2.gif")
label = Label(root, image=photo, bg='#0091D5', fg='#F1F1F1')
label.image = photo
label.grid(row=0, columnspan=2)

# Choosing categories
category_buttons = LabelFrame(root, text='Event categories')
category_buttons['bg'] = '#0091D5'

button1 = Button(category_buttons, text="Music Events",
                 command=PageOne)
button2 = Button(category_buttons, text="Film Events",
                 command=PageTwo)
button3 = Button(category_buttons, text="Politics Events",
                 command=PageThree)

button1.grid(row=0, column=0, padx=15, pady=10)
button2.grid(row=0, column=1, padx=15, pady=10)
button3.grid(row=0, column=2, padx=15, pady=10)

category_buttons.grid(row=1, columnspan=3, pady=5, sticky='N')

# Ofline Mode button
offline_checkbox = Frame(root)
offline_checkbox['bg'] = '#0091D5'

offline_label = Label(offline_checkbox, text='Option: ', fg='black', bg='#0091D5')
offline_button = Checkbutton(offline_checkbox, text="Work offline", fg='black', bg='#0091D5',
                             activebackground='#1C4E80',
                             variable=off_var)

# save data button
save_data_button = Checkbutton(offline_checkbox, text="Save data", fg='black', bg='#0091D5', activebackground='#1C4E80',
                               variable=save_var)

offline_label.grid(row=0, column=0, sticky='W')
offline_button.grid(row=1, column=0)
save_data_button.grid(row=2, column=0, sticky='W')

offline_checkbox.grid(row=0, column=2)

# Decoration
photo_1 = PhotoImage(file="3.gif")
label_1 = Label(root, image=photo_1, bg='#0091D5', fg='#F1F1F1')

label_1.grid(row=2, columnspan=3, sticky=W)
connection = connect(database='entertainment_planner.db')
planner_db = connection.cursor()


# function to generate event information as HTML based on selected events


def generate_html(variables, checkbutton, file, url=''):
    global count_event, save_var
    list_event = []

    # get a list of selected events by determining Checkbutton is on or not.
    for i in variables:
        if checkbutton[i][0].var.get() == 1:
            list_event.append(i)

    for i in list_event:
        # if the number of events <= 4, use "col-md-6 offset-sm-3 text-center" for better display in website
        delay_time = 100
        if count_event <= 4:
            file.write('''                                                                                                            
            <div class="col-md-6 offset-sm-3 text-center" data-aos="fade-up" data-aos-delay="%s">                                                
                        <a class="image-gradient" href="%s">                                                                 
                          <figure>                                                                                                    
                            <img src= %s alt="" class="img-fluid">                                                                    
                          </figure>                                                                                                   
                          <div class="text">                                                                                          
                            <h3>%s</h3>                                                                                               
                            <span>%s</span>                                                                                           
                          </div>                                                                                                      
                        </a>                                                                                                          
                      </div>                                                                                                          

            ''' % (str(delay_time), url, checkbutton[i][3], checkbutton[i][1], checkbutton[i][2]))

        # if the number of events > 4, use "col-md-6 col-lg-4" for better display in website
        else:
            file.write('''
            <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%s">
                        <a class="image-gradient" href="%s">
                          <figure>
                            <img src= %s alt="" class="img-fluid">
                          </figure>
                          <div class="text">
                            <h3>%s</h3>
                            <span>%s</span>
                          </div>
                        </a>
                      </div>


            ''' % (str(delay_time), url, checkbutton[i][3], checkbutton[i][1], checkbutton[i][2]))
        delay_time += 100

    if save_var.get() == 1:

        #Update database if the Save data is pressed
        connection = connect(database='entertainment_planner.db')
        planner_db = connection.cursor()

        for i in list_event:
            planner_db.execute('''
                            INSERT INTO events (event_name, event_date) VALUES ('%s', '%s'); 
                            ''' % (checkbutton[i][1].replace('\'', '\'\''), checkbutton[i][2]))
        connection.commit()

        planner_db.close()
        connection.close()


# command of Print Button. Create a HTML file showing chosen events and open it in browser
def get_value():
    #delete database before using
    connection = connect(database='entertainment_planner.db')
    planner_db = connection.cursor()
    planner_db.execute('DELETE FROM events;')
    connection.commit()
    planner_db.close()
    file = open('planner.html', 'w', encoding='utf-8')

    #write the HTML file
    file.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
  
    <!-- Website Title  -->
    <title>Brisbane Guide</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <!-- Bootstrap CSS  -->
    <link rel="stylesheet" href="https://dl.dropbox.com/s/4i57myoi5dzvw62/style.css">
    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300i,400,700" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/magnific-popup.css">    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.css">    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css">    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.theme.default.min.css">    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightgallery/1.6.12/css/lightgallery.min.css">         
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css">    
    <link rel="stylesheet" href="https://dl.dropbox.com/s/e1oy0zbf989ivql/icomoon_style.css">    
    <link rel="stylesheet" href="https://dl.dropbox.com/s/6w6xo41vcu6aqub/swiper.css">    
    <link rel="stylesheet" href="https://dl.dropbox.com/s/31ly708shp49b1q/aos.css">    
    <link rel="stylesheet" href="https://dl.dropbox.com/s/t0fbwhnk2olu8d5/style.css">    


  </head>
  <body>


<!-- Header of the webpage   -->
  <div class="site-wrap">


    <div class="site-mobile-menu">
      <div class="site-mobile-menu-header">
        <div class="site-mobile-menu-close mt-3">
          <span class="icon-close2 js-menu-toggle"></span>
        </div>
      </div>
      <div class="site-mobile-menu-body"></div>
    </div>


    <header class="site-navbar py-3" role="banner">




      <div class="container">
        <div class="row align-items-center">
            <h1 ><a href="planner.html" class="text-black h2">The Brisbane Guide<span class="text-primary">.</span></a></h1>

          <div class="col-10 col-md-8 d-none d-xl-block">
            <nav class="site-navigation position-relative text-right text-lg-center" role="navigation">
            </nav>
          </div>



        </div>
      </div>

    </header>

    <div class="site-blocks-cover overlay inner-page-cover" style="background-image: url('http://sites.ieee.org/wieils-aus-2018/files/2018/04/bri_2.jpg');" data-stellar-background-ratio="0.5">
      <div class="container">
        <div class="row align-items-center justify-content-center">
          <div class="col-md-7 text-center" data-aos="fade-up">
            <h1>Looking for things to do and events in Brisbane? Visit Brisbane is loaded with great ideas. This is Brisbane.</h1>
          </div>
        </div>
      </div>
    </div>


<!-- Events image and information -->
    <div class="site-section border-bottom">
      <div class="container">
        <div class="row text-center justify-content-center mb-5">
          <div class="col-md-7" data-aos="fade-up">
            <h2>My events</h2>
          </div>
        </div>

    <div class="row">    


    ''')
    # generate images in HTML based on the number of selected events
    if count_music > 0:
        generate_html(music_variables, music_checkbutton, file, music_url)

    if count_film > 0:
        generate_html(film_variables, film_checkbutton, file, film_url)

    if count_politics > 0:
        generate_html(politics_variables, politics_checkbutton, file, politics_url)
    elif count_event == 0:
        file.write('''                                                                                                            
        <div class="col-md-4 offset-sm-4" data-aos="fade-up" data-aos-delay="200">                                                
                    <a class="image-gradient" href="planner.html">                                                                 
                      <figure>                                                                                                    
                        <img src= 'https://i.redd.it/p50uynv5uzl11.jpg' alt="" class="img-fluid">                                                                    
                      </figure>                                                                                                   
                      <div class="text">                                                                                          
                        <h3>No Event Selected</h3>                                                                                               
                        <span>Have a look and enjoy some events!</span>                                                                                           
                      </div>                                                                                                      
                    </a>                                                                                                          
                  </div>                                                                                                          

        ''')

    file.write('''
            </div>
          </div>
        </div>

    <!-- Quotes by celebrity in music, politics and film aspects -->
        <div class="py-5 site-block-testimonial" style="background-image: url('https://dl.dropbox.com/s/pjy8zhdb8bjnwrb/hero_bg_1.jpg');" data-stellar-background-ratio="0.5">
         <div class="container">
           <div class="row block-13 mb-5">
             <div class="col-md-12 text-center" data-aos="fade">
               <div class="nonloop-block-13 owl-carousel">
                  <div class="block-testimony">
                    <img src="https://www.miamibookfair.com/wp-content/uploads/2016/09/Lowry_Lois.jpg">
                    <p>&ldquo;For the first time, he heard something that he knew to be music. He heard people singing. Behind him, across vast distances of space and time, from the place he had left, he thought he heard music too. But perhaps, it was only an echo.&rdquo;</p>
                    <p class="small">&mdash; Lois Lowry</p>
                  </div>
                  <div class="block-testimony">
                    <img src="https://pbs.twimg.com/profile_images/961333428120559616/Yi7tLP5r.jpg" alt="Image" class="img-fluid">
                    <p>&ldquo;The first step - especially for young people with energy and drive and talent, but not money - the first step to controlling your world is to control your culture. To model and demonstrate the kind of world you demand to live in. To write the books. Make the music. Shoot the films. Paint the art.&rdquo;</p>
                    <p class="small">&mdash; Chuck Palahniuk</p>
                  </div>
                  <div class="block-testimony">
                    <img src="http://quoteslab.net/contents/uploads/john-f-kennedy-400x400.jpg" alt="Image" class="img-fluid">
                    <p>&ldquo;Let us not seek the Republican answer or the Democratic answer, but the right answer. Let us not seek to fix the blame for the past. Let us accept our own responsibility for the future.&rdquo;</p>
                    <p class="small">&mdash; John F. Kennedy</p>
                  </div>
                </div>
             </div>
           </div>
         </div>
       </div>



       <div class="py-3 mb-5 mt-5">
         <div class="container">
           <div class="row">
             <div class="col-md-12 d-md-flex align-items-center" data-aos="fade">
               <h2 class="text-black mb-5 mb-md-0 text-center text-md-left"></h2>
               <div class="ml-auto text-center text-md-left">
               </div>
             </div>
           </div>
         </div>
       </div>

    <!-- Footer of the web page -->
      <footer class="site-footer">
          <div class="container">
            <div class="row">
              <div class="col-lg-4">
                <div class="mb-5">
                  <h3 class="footer-heading mb-4">About Brisbane Guide</h3>
                  <p>Whether you’re a newcomer or a seasoned native, let us guide you through the city’s brightest hotspots and share our local tips for making the most of casual-cool Brisbane. All event information is retrieved from www.eventbrite.com.au.</p>
                </div>
              </div>
              <div class="col-lg-4 mb-5 mb-lg-0">
                <div class="row mb-5">
                  <div class="col-md-12">
                    <h3 class="footer-heading mb-4">Navigations</h3>
                  </div>
                  <div class="col-md-6 col-lg-6">
                    <ul class="list-unstyled">
                      <li><a href="#">Home</a></li>
                      <li><a href="https://www.eventbrite.com.au/d/australia--brisbane-city/music/">Music</a></li>
                      <li><a href="https://www.eventbrite.com.au/d/australia--brisbane-city/film/">Film</a></li>
                      <li><a href="https://www.eventbrite.com.au/d/australia--brisbane-city/politics/">Politics</a></li>
                    </ul>
                  </div>

                  <div class="col-md-6 col-lg-6">
                    <ul class="list-unstyled">
                      <li><a href="#">About Me</a></li>
                      <li><a href="#">Privacy Policy</a></li>
                      <li><a href="#">Contact Me</a></li>
                      <li><a href="#">Terms</a></li>
                    </ul>
                  </div>
                </div>


              </div>

              <div class="col-lg-4 mb-5 mb-lg-0">
                <h3 class="footer-heading mb-4">Follow Me</h3>

                    <div>
                      <a href="#" class="pl-0 pr-3"><span class="icon-facebook"></span></a>
                      <a href="#" class="pl-3 pr-3"><span class="icon-twitter"></span></a>
                      <a href="#" class="pl-3 pr-3"><span class="icon-instagram"></span></a>
                      <a href="#" class="pl-3 pr-3"><span class="icon-linkedin"></span></a>
                    </div>



              </div>

            </div>
          </div>
        </footer>




      </div>
    <!-- JavaScript  -->
    <script src="https://dl.dropbox.com/s/9986shjjie0cuwz/jquery-3.3.1.min.js"></script>
    <script src="https://dl.dropbox.com/s/7dmm66sj7x5lhjg/jquery-migrate-3.0.1.min.js"></script>
    <script src="https://dl.dropbox.com/s/t041vpy5talsri5/jquery-ui.js"></script>
    <script src="https://dl.dropbox.com/s/o58uqbcnurnpuvn/popper.min.js"></script>
    <script src="https://dl.dropbox.com/s/0zootv57ai4ys6p/bootstrap.min.js"></script>
    <script src="https://dl.dropbox.com/s/qstiltyzjiz9nb7/owl.carousel.min.js"></script>
    <script src="https://dl.dropbox.com/s/nuyvyxpvpkv4s8l/jquery.stellar.min.js"></script>
    <script src="https://dl.dropbox.com/s/g0pmg2ulw2jz7yi/jquery.countdown.min.js"></script>
    <script src="https://dl.dropbox.com/s/ulwyvuxgo9dko9m/jquery.magnific-popup.min.js"></script>
    <script src="https://dl.dropbox.com/s/284byhj4fx359w9/bootstrap-datepicker.min.js"></script>
    <script src="https://dl.dropbox.com/s/ywkcwf1gl5dcopr/swiper.min.js"></script>
    <script src="https://dl.dropbox.com/s/hn5lbwwmhkof9oy/aos.js"></script>

    <script src="https://dl.dropbox.com/s/xlragx706bpo6pu/picturefill.min.js"></script>
    <script src="https://dl.dropbox.com/s/5ro86w9z9zp4i93/lightgallery-all.min.js"></script>
    <script src="https://dl.dropbox.com/s/ibpih04gn3qg611/jquery.mousewheel.min.js"></script>

    <script src="https://dl.dropbox.com/s/bvgbwsb3am6bc7d/main.js"></script>

      <script>
        $(document).ready(function(){
          $('#lightgallery').lightGallery();
        });
      </script>

      </body>
    </html> ''')
    webbrowser.open('planner.html', new=2)


# Print planer button
print_button = Button(root, text='Print planner (' + str(count_event) + ' event selected)', command=get_value)
print_button.grid(row=2, columnspan=3, pady=10, sticky=N)

root.mainloop()










































