from mjml import mjml2html

import os
import webbrowser

import lib.constant as const



def openInBrowser( handle: str ):
    cwd = os.getcwd()
    if handle.endswith('.mjml'):
        handle = handle.replace('.mjml', '')
    path = f"file://{ cwd }/{ const.TEMPLATE_DIR }/{ handle }.html"
    webbrowser.open(path)

#####################################
#             HELPERS               #
#####################################

def readSource( handle: str ) -> str:
    # Take a string as input and return the read file text string.
    if not handle.endswith('.mjml'):
        handle = f"{ handle }.mjml"

    return open( f"{ const.MJML_DIR }/{ handle }", "r" ).read()

def parseMJML( mjml: str ) -> str:
    # Take a string of MJML and return the corresponding HTML representation.
    return mjml2html( mjml )


def writeHTML( html: str, handle: str ):
    # Take a string and handle as input and write it to the template folder as a .html file.
    if handle.endswith('.mjml'):
        handle = handle.replace('.mjml', '')

    with open( f"{ const.TEMPLATE_DIR }/{ handle }.html", "w" ) as file:
        file.write( html )

#####################################
#             /HELPERS              #
#####################################

def main( templates_to_handle: list ):
    for template in templates_to_handle:
        file_contents = readSource( handle = template )
        html = parseMJML( mjml = file_contents )
        writeHTML( html = html, handle = template )
        openInBrowser( handle = template )

if __name__ == "__main__":
    # templates_to_handle = ['source_1','source_2','source_3']
    templates_to_handle = None
    if not templates_to_handle:
        templates_to_handle = next(os.walk( const.MJML_DIR ), (None, None, []))[2]
    main( templates_to_handle = templates_to_handle )