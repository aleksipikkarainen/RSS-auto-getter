from rssconnector import Rssparser

t = Rssparser()
while True:
    option = input("Please select option:")
    if option == '1':
        t.setRss()
    elif option == '2':
        t.getRss()
    elif option == '3':
        t.parseTest()
    elif option == '4':
        t.addShows()
    else:
        break
