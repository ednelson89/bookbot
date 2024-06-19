# bookbot

Boot.Dev - command-line application in Python that does static analysis on text files

In order for this application to work, you will need to have a .txt file available to run. I recommend placing it in the books directory of this project, but relative pathing should work.

For ex.

Both test.txt and the project folder are placed in the user folder within /home. The correct path to input would be:
`../test.txt`

The test.txt file is placed at the root of the project folder:
`./test.txt`

Note: the application does not allow for system aliases such as root: '/' or user: '~'
