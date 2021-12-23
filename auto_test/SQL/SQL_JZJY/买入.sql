   SELECT CUST_NO  FROM KS.CUST_BASE_INFO WHERE CUST_NO IN (
		SELECT AA.CUST_NO FROM (SELECT A.CUST_NO,A.CUST_STATUS FROM KS.CUST_BASE_INFO A
			LEFT JOIN
			(SELECT CUST_NO FROM KS.VIP_CUST_LIST)B
			 ON A.CUST_NO = B.CUST_NO
			 WHERE B.CUST_NO IS NULL AND A.ATTRIBUTE = '{attribute}' )AA
			 LEFT JOIN
			 (SELECT D1.CUST_NO,sum(a.THIS_BAL+a.DEPOSIT-a.WITHDRAW-a.ABNORMAL_FRZN_AMT-a.BUY_FROZEN_AMT-a.FORBID_AMT) AS total
			  FROM KS.HOLDER_ACC D1 LEFT JOIN KS.FUND a ON D1.CUST_NO = a.CUST_NO WHERE  D1.MARKET_CODE = '{market}' AND D1.HOLDER_TYPE IN ('00','04')
			 AND D1.CUST_NO NOT IN {disabled_cust_no} AND D1.STATUS = '0' {allow_seat_no}{disabled_seat_no} AND a.CUST_NO IS NOT NULL  {allow_branch_code}{disabled_branch_code}
			 GROUP BY D1.CUST_NO
			 )BB
			 ON AA.CUST_NO = BB.CUST_NO
			 WHERE BB.CUST_NO IS NOT NULL AND AA.CUST_STATUS = '0'
			 ORDER BY BB.total DESC FETCH FIRST 20 ROWS ONLY WITH UR)
			 ORDER BY rand() FETCH FIRST 1 ROWS ONLY WITH UR


