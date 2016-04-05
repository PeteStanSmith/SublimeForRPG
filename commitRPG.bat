@set CHECKOUT_LOCATION=C:\jhc\src\RPG\CR

@set /p PROGRAM="Enter program:"
@set /p IR="Enter IR:"
@set /p CR="Enter CR number:"
@set /p SOURCEFILE="Enter source file name:"
@set /p SOURCETYPE="Enter source format:"

@cd %CHECKOUT_LOCATION%

@set LIBRARY=o#%IR%%CR%

@set PUT_SOURCE=put %SOURCEFILE%.%PROGRAM%
@set NEW_NAME=%PROGRAM%.%SOURCETYPE% %SOURCEFILE%.%PROGRAM%
@ren %NEW_NAME%

@echo user <username> > ftpcmd.txt
@echo <password> >> ftpcmd.txt
@echo bin >>ftpcmd.txt
@echo ascii >>ftpcmd.txt
@echo quote site namefmt 0 >>ftpcmd.txt
@echo cd %LIBRARY% >>ftpcmd.txt
@echo %PUT_SOURCE%  >> ftpcmd.txt

@echo quit >>ftpcmd.txt

ftp -n -s:ftpcmd.txt <systemnameorIp>
@echo successfully uploaded source file
@del ftpcmd.txt

@del committed%PROGRAM%.%SOURCETYPE%
@ren %SOURCEFILE%.%PROGRAM% committed%PROGRAM%.%SOURCETYPE%
exit


