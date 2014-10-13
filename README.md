Python-stock-analysis
=====================

- All output is within folder: 'data_and_output'
--- one month company yahoo finance data for:
----- AAPL.csv
----- AMZN.csv
----- EBAY.csv
----- GOOG.csv
----- MSFT.csv
--- Data analysis output:
----- AAPL_baseline141011.png
      normalized closing price data for apple
----- AMZN_baseline141011.png
      normalized closing price data for amazon
----- GOOG_baseline141011.png
      normalized closing price data for google
----- MSFT_baseline141011.png
      normalized closing price data for microsoft
----- TSLA_related_exuberance_141011.png
      normalized closing price data for tesla showing that it does not 
      seem to be following the usual trend owning to D series news event
----- goog_amzn_corr_141012
      shows that goog and amzn trending in similar way during this once 
      month stable period.


- Subroutine description:
--- one_company_stock_pull_1.py : 
    pulls single company one month data from yahoo finance
--- one_company_stock_pull_and_save_to_file_2.py :
    pulls as above and puts it into a file with company name in csv format
