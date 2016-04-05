@set CHECKOUT_LOCATION=C:\jhc\src\RPG\CR

@set /p PROGRAM="Enter program:"
@set /p IR="Enter IR:"
@set /p CR="Enter CR number:"
@set /p SOURCEFILE="Enter source file name:"
@set /p SOURCETYPE="Enter source format:"

@REM @if %PROGRAM%= set PROGRAM=OR2#cm01

@set LIBRARY=o#%IR%%CR
@REM @if [%LIBRARY%]=[o#] set LIBRARY=o#06277901

@set GET_SOURCE=get %SOURCEFILE%.%PROGRAM%
@set NEW_NAME=%SOURCEFILE%.%PROGRAM% %PROGRAM%.%SOURCETYPE%

@cd %CHECKOUT_LOCATION%

@echo user <username> > ftpcmd.txt
@echo <password> >> ftpcmd.txt
@echo bin >>ftpcmd.txt
@echo ascii >>ftpcmd.txt
@echo quote site namefmt 0 >>ftpcmd.txt
@echo cd %LIBRARY% >>ftpcmd.txt
@echo %GET_SOURCE%  >> ftpcmd.txt

@echo quit >>ftpcmd.txt

ftp -n -s:ftpcmd.txt <systemnameorIp>
@del ftpcmd.txt

@del previous%PROGRAM%.%SOURCETYPE%
@ren %PROGRAM%.%SOURCETYPE% previous%PROGRAM%.%SOURCETYPE%
@ren %NEW_NAME%
@echo successfully copied source file
start %PROGRAM%.%SOURCETYPE%
exit


