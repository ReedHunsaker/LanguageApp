from pathlib import Path

home = Path.home()
dir: Path = Path(__file__).parent / 'LanguageApp'

#window geometry
geometry = "600x400"
geometry_create = "350x200"
geometry_read = "1350x700"
geometry_translate_popup = "200x75"
app_title = "LanguageApp"
login_title = "Login - " + app_title
create_title = "Create Account - " + app_title

#fonts
text_font = "Arial 16"
button_font = "Helvetica"
readonly = 'readonly'

#buttons
button_big_height = 3
button_big_width = 25
button_background = 'grey'

# default lighting

bg_default = '#ffffff'
fg_default = '#030303'

#darkmode

bg_darkmode = '#1c1c1c'
fg_darkmode = "#cdcdcd"

#langages 

spanish = 'Spanish'
english = 'English'
tagalog = 'Tagalog'
korean = 'Korean'

naitive_all = [english]

foriegn_all = [spanish, tagalog, korean]

foriegn_all_length = len(foriegn_all)

#background images

#file paths
database =  'LanguageApp/secret/language-app-8e630-firebase-adminsdk-ureoj-4ac8e913d8.json'

#login screen
label_font_size = 32