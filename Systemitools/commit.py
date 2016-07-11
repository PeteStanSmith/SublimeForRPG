import sublime_plugin
from ftplib import FTP
import datetime
from Systemitools.logger import Logger
from Systemitools.fileExtension import Utils


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

                fileName = 'C:\\jhc\\src\\RPG\\CR\\' + program + '.' + \
                           fileExtension

                try:
                    retrievalTarget = Utils.getRetrievalTarget(fileExtension)
                except KeyError:
                    self.view.set_status('task', 'Last commit failed')
                    raise

                # putOperation = ('STOR ' + retrievalTarget +
                #                 '.' + program)
                # logger.log(putOperation)

                # global file
                # file = open(fileName, 'rb')
                # ftp = FTP('tracey')

                # ftp.login('PSDEV', 'PSDEV')
                # ftp.cwd(library)
                # ftp.storlines(putOperation, file)
                # ftp.quit()
                # file.close()
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
