SELECT CUST_NO FROM KS.STOCK where CUST_NO not in ('00002303','00002306') 
and CUST_NO in (SELECT  CUST_NO FROM KS.CUST_BASE_INFO where BRANCH_CODE='001' )  GROUP BY CUST_NO order by count(1) desc fetch first 1 rows only;