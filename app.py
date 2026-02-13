import pages.about as about
import pages.contact as contact
import pages.cv as cv
import pages.rwork as rwork
from pages.sidebar import sidebar


PAGES = {
    "About me": about,
    "Contact me": contact,
    "CV": cv,
    "Research works" : rwork
}


selection = sidebar(list(PAGES.keys()))
page = PAGES[selection]
page.content()

