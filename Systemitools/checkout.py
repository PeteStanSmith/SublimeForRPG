import sublime_plugin
from ftplib import FTP
import os
from Systemitools.logger import Logger
from Systemitools.fileExtension import Utils


class checkoutFromTracey(sublime_plugin.TextCommand):

    def run(self, edit):
        global logger
        global ir
        self.view.set_status('task', 'Checking out source code')
        logger = Logger('log')
        logger.log("Retrieval operation initiated.")
        self.set_variables()

    def set_variables(self):
        global count
        count = 0
        global ir
        ir = ''
        global fileExtension

        currentprogramWithFile = ""
        filename = str(self.view.file_name())
        tokens = filename.split("\\")

        for token in tokens:
            if token != "None":
                currentprogramWithFile = token

        tokens = currentprogramWithFile.split(".")
        for token in tokens:
            if token != "None":
                fileExtension = token

        currentprogram = str.replace(currentprogramWithFile, "." + fileExtension, "")

        self.view.window() \
            .show_input_panel("Enter the program name: ",
                              currentprogram, self.set_program,
                              None, self.exit)
        return

    def set_program(self, text):
        global program
        program = text
        logger.log('User entered program: ' + program)
        self.view.window() \
            .show_input_panel("Enter the IR or Figaro library: ",
                              "", self.set_ir,
                              None, self.exit)
        return

    def set_ir(self, text):
        global ir
        global library
        if (text[:1]) == '0':
            ir = text
            logger.log('User entered IR: ' + ir)
            self.view.window() \
                .show_input_panel("Enter the CR: ",
                                  "", self.set_cr,
                                  None, self.exit)
        else:
            library = text
            if library != '':
                logger.log('User entered Figaro library: ' + library)
            else:
                library = 'F63FIGARO'
                logger.log('User did not enter a library, ' +
                           'defaulted to ' + library + '.')

            self.view.window() \
                .show_input_panel("Enter the file extension: ",
                                  fileExtension, self.set_fileExtension,
                                  None, self.exit)
        return

    def set_cr(self, text):
        global cr
        cr = text
        logger.log('User entered CR: ' + cr)
        self.view.window() \
            .show_input_panel("Enter the file extension: ",
                              fileExtension, self.set_fileExtension,
                              None, self.exit)
        return

    def set_fileExtension(self, text):
        global fileExtension
        global logFile
        global library

        fileExtension = text
        logger.log('User entered file extension: ' + fileExtension)

        # if the ir isn't blank construct the library
        if ir != '':
            library = ('o#' + ir + cr)

        fileName = 'C:\\jhc\\src\\RPG\\CR\\' + program + '.' + \
                   fileExtension
        try:
            retrievalTarget = Utils.getRetrievalTarget(fileExtension)
        except KeyError:
            self.view.erase_status('task')
            raise

        getOperation = ('RETR ' + retrievalTarget + '.' + program)
        logger.log(getOperation)

        global file
        file = open(fileName, 'w', encoding='ascii')
        ftp = FTP('tracey')

        ftp.login('PSDEV', 'PSDEV')
        try:
            ftp.cwd(library)
            try:
                ftp.retrlines(getOperation, self.writeFile)
                logger.log('Source code for ' + library + '/' +
                           program + ' successfully retrieved.')
                os.startfile(fileName)
                file.close()
                ftp.quit()
            except:
                logger.log('Could not find source file or ' +
                           'file could not be parsed.')
                ftp.quit()
                file.close()
        except:
            logger.log('Library does not exist.')
            ftp.quit()
            file.close()
            os.remove(fileName)

        logger.close()
        self.view.erase_status('task')
        return

    def exit(self):
        logger.log('User connection reset by peer.')
        logger.close()

    # Should extract this to a file writer when I get the chance.
    # Should also pull out what chracter has been replaced
    def writeFile(self, line):
        global count
        count = count + 1
        try:
            file.write(line + "\n")
        except UnicodeEncodeError:
            # This section will replace the none acsii
            # characters with a blank space.
            try:
                # see-change header character
                line = line.replace('\x80', '\x20')
                #  ¦ Alt Gr pipe
                line = line.replace('\xA6', '\x20')
                # ¬ not sign
                line = line.replace('\xAC', '\x20')

                # white hex colour
                line = line.replace('\x82', '\x20')
                # blue hex colour
                line = line.replace('\x9A', '\x20')
                # Purple hex colour
                line = line.replace('\x98', '\x20')
                # Red hex colour
                line = line.replace('\x88', '\x20')
                # Yellow hex colour
                line = line.replace('\x96', '\x20')

                # [ open square bracket - replaced with ^.
                line = line.replace('\xA3', '\x5E')

                file.write(line + "\n")

            except UnicodeEncodeError:
                # This section is for those characters
                # that we should log as replaced.

                # incase we need the hex value
                # newline = ":".join("{:02x}".format(ord(c)) for c in line)

                # dollar sign - not an ascii character
                line = line.replace('\xA2', '\x20')

                file.write(line + "\n")
                logger.log('Unable to parse line ' +
                           str(count) + '. Take care when editing ' +
                           'this! Printed: ' + line)
