@echo off
@echo.
@echo Preparing for import!
@echo.

rem file name changes

if exist extract_payment_gl*.csv (
ren extract_payment_gl*.csv Invoice.csv
)

if exist extract_dl_inv_pay*.csv (
  ren extract_dl_inv_pay*.csv input.csv
)



rem begin imports

if exist Invoice.csv (
 

  @echo Importing Bills!
  "Transaction Pro Importer 8.0.exe" /ACTIVATED /AUTORUN /TEXT_FILE=E:\D\QB$\Concur\Mapping\Automation\Invoice.csv /DELIMITER=Comma /TXN_TYPE=Bill /MAP_FILE=E:\D\QB$\Concur\Mapping\APInvoiceMap.dat
  
  @echo Deleting Bills CSV file... 
  del Invoice.csv 
  @echo Invoices imported!
  @echo.
) else (
  @echo No Invoices file, moving to expenses...
  @echo.
)


if exist Expenses.csv (

  @echo Importing Expenses! 
  "Transaction Pro Importer 8.0.exe" /ACTIVATED /AUTORUN /TEXT_FILE=E:\D\QB$\Concur\Mapping\Automation\Expenses.csv /DELIMITER=Comma /TXN_TYPE=Bill /MAP_FILE=E:\D\QB$\Concur\Mapping\ExpenseMap.dat

  @echo Deleting Expenses CSV file...
  del Expenses.csv
  @echo. 
  @echo Expenses imported!
  @echo. 
) else (
  @echo No Expenses file, moving to bill payments...
  @echo.
)




if exist input.csv (

  @echo Converting Payment file to QB format..
  csdcc.exe

  @echo Importing Bill Payments!
  "Transaction Pro Importer 8.0.exe" /ACTIVATED /AUTORUN /TEXT_FILE=E:\D\QB$\Concur\Mapping\Automation\zBillPayReady.csv /DELIMITER=Comma /TXN_TYPE=Bill Payment /MAP_FILE=E:\D\QB$\Concur\Mapping\PaymentMap.dat

  @echo Deleting Input & Bill Payment CSV file. 
  del input.csv
  del zBillPayReady.csv
  @echo.
  @echo Bill Payments imported!
  @echo.
) else (
  @echo No Bill Payments file, wrapping up importing...
  @echo.
)



@echo.
@echo.
@echo Operations completed successfully!
@echo.
@echo.
 


