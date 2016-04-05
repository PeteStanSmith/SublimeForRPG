import sublime_plugin
from ftplib import FTP
import os
from Systemitools.logger import Logger
from Systemitools.fileExtension import Utils


class checkoutFromTracey(sublime_plugin.TextCommand):

    def run(self, edit):
        global logger
        global ir
        logger = Logger('log')
        logger.log("Retrieval operation initiated")
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
                           'defaulted to ' + library)

            self.view.window() \
                .show_input_panel("Enter the file extension: ",
                                  "", self.set_fileExtension,
                                  None, self.exit)
        return

    def set_cr(self, text):
        global cr
        cr = text
        logger.log('User entered CR: ' + cr)
        self.view.window() \
            .show_input_panel("Enter the file extension: ",
                              "", self.set_fileExtension,
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

        retrievalTarget = Utils.getRetrievalTarget(fileExtension)

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
                           program + ' successfully retrieved')
                os.startfile(fileName)
                file.close()
            except:
                logger.log('Could not find source file')
                file.close()
                os.remove(fileName)
        except:
            logger.log('Library does not exist')
            file.close()
            os.remove(fileName)

        ftp.quit()

        logger.close()
        return

    def exit(self):
        logger.log('User connection reset by peer')
        logger.close()

    def writeFile(self, line):
        try:
            file.write(line + "\n")
        except UnicodeEncodeError:
            line = line.replace('\x82', '\x20')
            line = line.replace('\x80', '\x20')
            line = line.replace('\xA6', '\x20')
            line = line.replace('\x9A', '\x20')
            line = line.replace('\xA2', '\x20')
            line = line.replace('\xA3', '\x20')

            file.write(line + "\n")
