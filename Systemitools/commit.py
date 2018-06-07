import sublime_plugin
from ftplib import FTP
import datetime
from Systemitools.logger import Logger
from Systemitools.fileExtension import Utils

from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


class commitToTracey(sublime_plugin.TextCommand):

    def run(self, edit):
        global logger
        global ir
        self.view.set_status('task', 'Committing source code to CR')
        logger = Logger('log')
        logger.log('Commit operation initiated')
        self.set_variables()

    def set_variables(self):
        global ir
        global fileExtension
        ir = ''
        global currentIR
        global currentCR

        currentprogramWithFile = ""
        currentIR = ""
        currentCR = ""
        filename = str(self.view.file_name())

        tokens = filename.split("\\")

        if len(tokens) > 1:
            currentprogramWithFile = tokens[-1]
            currentIR = tokens[-2]

        tokens = currentIR.rsplit(".")
        if len(tokens) > 1:
            currentIR = tokens[-2]
            currentCR = tokens[-1]

        tokens = currentprogramWithFile.rsplit(".")
        fileExtension = tokens[-1]

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
            .show_input_panel("Enter the IR: ",
                              currentIR, self.set_ir,
                              None, self.exit)
        return

    def set_ir(self, text):
        global ir
        ir = text
        logger.log('User entered IR: ' + ir)
        self.view.window() \
            .show_input_panel("Enter the CR: ",
                              currentCR, self.set_cr,
                              None, self.exit)
        return

    def set_cr(self, text):
        global cr
        cr = text
        logger.log('User entered CR: ' + cr)
        self.view.window() \
            .show_input_panel("Enter the file entension file: ",
                              fileExtension, self.set_fileExtension,
                              None, self.exit)
        return

    def set_fileExtension(self, text):
        global fileExtension

        fileExtension = text
        logger.log('User entered file extension: ' + fileExtension)

        opentabs = self.view.window().views()
        for opentab in opentabs :
            if opentab.is_dirty():

                paneltext = "There are open unsaved changes, " \
                     "would you like to continue, Y or N:"

                self.view.window() \
                    .show_input_panel(paneltext, "",
                    self.commitfile, None, self.exit)
                return

        self.commitfile("No unsaved changes")
        return

    def commitfile(self, text):
        global fileExtension
        logger.log('Proceed with unsaved changes: ' + text)

        if text.lower() == 'y' or text == 'No unsaved changes':

            # if the ir isn't blank construct the library
            if ir != '':
                library = ('o#' + ir + cr)

                fileName = 'C:\\jhc\\src\\RPG\\CR\\' + ir + '.' + cr + '\\'+ program + '.' + \
                           fileExtension

                try:
                    retrievalTarget = Utils.getRetrievalTarget(fileExtension)
                except KeyError:
                    self.view.set_status('task', 'Last commit failed')
                    raise

                putOperation = ('STOR ' + retrievalTarget +
                                '.' + program)
                logger.log(putOperation)

                self.characterConversion(fileName)
                global file
                file = open(fileName, 'rb')
                ftp = FTP('tracey')

                ftp.login('SMITHP', 'qsdw99co')
                ftp.cwd(library)

                #undo replacements
                #for line in file:
                #    line = line.replace('\x24', '\xA2')

                ftp.storlines(putOperation, file)
                ftp.quit()
                file.close()
                logger.log('Source code for ' + library + '/' +
                            program + ' successfully committed')
                self.view.erase_status('task')

            else:
                logger.log('No IR was entered, commit aborted')
                self.view.set_status('task', 'Last commit failed')

        else:
            logger.log('Abort for unsaved file changes')
            self.view.erase_status('task')

        logger.close()
        return

    def exit(self):
        logger.log('User connection reset by peer')
        self.view.erase_status('task')
        logger.close()

    def characterConversion(self, file_path):
        #Create temp file
        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    # dollar sign
                    line = line.replace('\x24', '\xA2')
                    # left square bracket
                    line = line.replace('\x5B', '\xA3')
                    # not sign ¬
                    line = line.replace('\x5F', '\xAC')
                    new_file.write(line)
        #Remove original file
        remove(file_path)
        #Move new file
        move(abs_path, file_path)
