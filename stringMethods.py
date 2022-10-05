highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

# creates a list from a string deliminating by ,
highlighted_poems_list = highlighted_poems.split(",")
# print(highlighted_poems_list)


# function that takes in a list of poems and strips the white space at the start and end of each entry
def strip_whitespace(poem_list):
    poem_stripped = []
    highlighted_poem_stripped = []
    for poem in poem_list:
        poem_stripped = poem.strip()
        highlighted_poem_stripped.append(poem_stripped)
    return highlighted_poem_stripped

# function that takes a list of poems and splits each entry further using the deliminator :


def split_poem_details(poem_list):
    return_list = []
    for poem in poem_list:
        split_poem = poem.split(":")
        return_list.append(split_poem)
    return return_list

# function that takes list of poem details, in each list saves the appropriate title, poet & date to the same named list


def sort_poems(poem_list):
    titles = []
    poets = []
    dates = []
    for poem in poem_list:
        titles.append(poem[0])
        poets.append(poem[1])
        dates.append(poem[2])
    return titles, poets, dates

# function that loops through the titles list and prints a formatted sentance to include the titel, poet and dates information for that entry.


def print_details(titles, poets, dates):
    for i in range(0, len(titles)):
        msg = "The poem {titles} was published by {poets} in {dates}."
        print(msg.format(titles=titles[i], poets=poets[i], dates=dates[i]))


# call whitespace strip
highlighted_poems_stripped = strip_whitespace(highlighted_poems_list)
# print(highlighted_poems_stripped)

#call : split
highlighted_poems_details = split_poem_details(highlighted_poems_stripped)
# print(split_poem_details(highlighted_poems_stripped))

# def varible lists
titles = []
poets = []
dates = []

# call sort poems to add title, poets, dates to lists
titles, poets, dates = sort_poems(highlighted_poems_details)
# print(sort_poems(highlighted_poems_details))
# print(titles)

# call print_details
printed_details = (print_details(titles, poets, dates))
