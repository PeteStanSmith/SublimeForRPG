import sublime_plugin
from ftplib import FTP
import datetime
from Systemitools.logger import Logger
from Systemitools.fileExtension import Utils


class commitToTracey(sublime_plugin.TextCommand):

    def run(self, edit):
        global logger
        global ir
        logger = Logger('log')
        logger.log('Commit operation initiated')
        self.set_variables()

    def set_variables(self):
        global ir
        ir = ''
        self.view.window() \
            .show_input_panel("Enter the program name: ",
                              "", self.set_program,
                              None, self.exit)
        return

    def set_program(self, text):
        global program
        program = text
        logger.log('User entered program: ' + program)
        self.view.window() \
            .show_input_panel("Enter the IR: ",
                              "", self.set_ir,
                              None, self.exit)
        return

    def set_ir(self, text):
        global ir
        ir = text
        logger.log('User entered IR: ' + ir)
        self.view.window() \
            .show_input_panel("Enter the CR: ",
                              "", self.set_cr,
                              None, self.exit)
        return

    def set_cr(self, text):
        global cr
        cr = text
        logger.log('User entered CR: ' + cr)
        self.view.window() \
            .show_input_panel("Enter the file entension file: ",
                              "", self.set_fileExtension,
                              None, self.exit)
        return

    def set_fileExtension(self, text):
        global fileExtension
        global logFile

        fileExtension = text
        logger.log('User entered file extension: ' + fileExtension)

        # if the ir isn't blank construct the library
        if ir != '':
            library = ('o#' + ir + cr)

            fileName = 'C:\\jhc\\src\\RPG\\CR\\' + program + '.' + \
                       fileExtension

            retrievalTarget = Utils.getRetrievalTarget(fileExtension)

            putOperation = ('STOR ' + retrievalTarget +
                            '.' + program)
            logger.log(putOperation)

            global file
            file = open(fileName, 'rb')
            ftp = FTP('tracey')

            ftp.login('PSDEV', 'PSDEV')
            ftp.cwd(library)
            ftp.storlines(putOperation, file)
            ftp.quit()
            file.close()
            logger.log('Source code for ' + library + '/' +
                       program + ' successfully committed')

        else:
            logger.log('No IR was entered, commit aborted')

        logger.close()
        return

    def exit(self):
        logger.log('User connection reset by peer')

    def log(self, text):
        global logFile
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logFile.write(timestamp + ': ' + text + "\n")
        return
