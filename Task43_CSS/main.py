# CSS - Cascading Style Sheet
# Exist to separate the style from the structure
# property: value;

# Types of CSS:
# Inline for 1 element
# Internal for 1 webpage
# External for a website

# To add CSS with inline. It goes in the openening tag:
# <h1 style="color: blue;">Style in blue</h1>


# To add CSS you can add a tag called internal style (used for all the pages):
# Inside of the head element
# <head>
#   <style> 
#       html{
#           background: red;
#       } 
#       h1 {
#           color: red;
#       }
#   </style>
# </head>

# EXTERNAL AND COMMONLY USED. styles.css
# In the html:
# <head>
#   <link rel="stylesheet" href="./style.css"
# </head>
#
# In the CSS file (inside a folder into a file called style.css):
#
# h1 {
#   color: green;
# }


### CSS Selectors
# To understand which part of the html we are going to style
# Using a set of attributes:

# In the html
#<p draggable="true">Drag me</p> 
#<p draggable="false">Don't drag me</p> 

# In the CSS
#p[draggable]{
# color: red;
#}
#p[draggable="false"]{
# color: blue;
#}


# Class selector:
# In the html:
# <p class="note">
# In the CSS:
#.note{
#  font-size: 20px;
#} 

# Id selector. Only 1 item can have the same id.
# In the html:
#  id="id-selector-demo"
# In the css
##id-selector-demo{
#    color: green
#}