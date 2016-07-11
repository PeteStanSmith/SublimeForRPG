

# Sarge would kill me for naming it this
class Utils():

    @staticmethod
    def getRetrievalTarget(fileExtension):
        sourceFileDictionary = {'sqlrpgle': Utils.qrpglesrc,
                                'rpgleref': Utils.qrpgleref,
                                'rpgle': Utils.qrpglesrc,
                                'rpg': Utils.qrpgsrc,
                                'clle': Utils.qcllesrc,
                                'cl': Utils.qclsrc,
                                'pf': Utils.qddssrc,
                                'lf': Utils.qddssrc,
                                'dspf': Utils.qddssrc,
                                'ddl': Utils.sqltblsrc,
                                'sql': Utils.sqlfuncsrc,
                                'bnd': Utils.qsrvsrc,
                                'ind': Utils.sqlindsrc,
                                'proc': Utils.sqlprocsrc,
                                'trigger': Utils.sqltrgsrc,
                                'view': Utils.sqlviewsrc,
                                'cmd': Utils.qcmdsrc}

# except KeyError:
# logger.log('File extension not valid. ' +
# 'Please enter sqlrpgle, rpgle, ' +
# 'clle, cl, dds, dspf or ddl ')
# logger.close()
# return

        return sourceFileDictionary[fileExtension.lower()]()

    @staticmethod
    def qrpglesrc():
        return 'qrpglesrc'

    @staticmethod
    def qrpgsrc():
        return 'qrpgsrc'

    @staticmethod
    def qcllesrc():
        return 'qcllesrc'

    @staticmethod
    def qclsrc():
        return 'qclsrc'

    @staticmethod
    def qddssrc():
        return 'qddssrc'

    @staticmethod
    def sqlfuncsrc():
        return 'sqlfuncsrc'

    @staticmethod
    def qcmdsrc():
        return 'qcmdsrc'

    @staticmethod
    def qsrvsrc():
        return 'qsrvsrc'

    @staticmethod
    def sqltblsrc():
        return 'sqltblsrc'

    @staticmethod
    def qrpgleref():
        return 'qrpgleref'

    @staticmethod
    def sqlindsrc():
        return 'sqlindsrc'

    @staticmethod
    def sqlprocsrc():
        return 'sqlprocsrc'

    @staticmethod
    def sqlviewsrc():
        return 'sqlviewsrc'

    @staticmethod
    def sqltrgsrc():
        return 'sqltrgsrc'


