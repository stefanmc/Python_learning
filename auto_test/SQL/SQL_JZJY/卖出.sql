SELECT AA.CUST_NO,AA.SEC_CODE FROM(
  SELECT A.CUST_NO,A.SEC_CODE,A.VOL_BAL,A.HOLDER_ACC_NO FROM (
    SELECT  a1.CUST_NO,a1.HOLDER_ACC_NO,a1.SEC_CODE,a1.VOL_BAL FROM (
		SELECT a.CUST_NO,a.SEC_CODE,a.HOLDER_ACC_NO,a.THIS_VOL_BAL-a.ABNORMAL_FRZN_VOL-a.SELL_FROZEN_VOL-a.ETF_FROZEN_VOL-a.NOT_CIRC_VOL-a.MANUAL_FROZEN_VOL AS VOL_BAL
		FROM KS.STOCK a
             LEFT JOIN KS.B_SEC_CODE b ON a.MARKET_CODE = b.MARKET_CODE AND a.SEC_CODE = b.SEC_CODE
             WHERE a.MARKET_CODE = '{market}' AND a.SEC_TYPE = '{sec_type}' AND a.CUST_NO NOT IN {disabled_cust_no} AND b.SEC_VARIETY = '{sec_variety}'
              AND b.TX_STATUS = 'N'  AND b.SEC_LEVEL = '{sec_level}'
             AND b.RAISE_FALL_LIMIT_TYPE IN ( 'N','','R')  AND substr(b.sec_status,9,6) != '100001'
             {allow_branch_code}{disabled_branch_code}
             AND a.CUR_BUY_VOL = '0' AND a.CUR_SELL_VOL = '0'
             )a1
                LEFT JOIN (
                    SELECT HOLDER_ACC_NO
                    FROM KS.REDUCE_STOCK_INFO
     )b1 ON a1.HOLDER_ACC_NO =b1.HOLDER_ACC_NO
        WHERE a1.CUST_NO NOT IN {disabled_cust_no} AND b1.HOLDER_ACC_NO IS NULL
     )A LEFT JOIN (
                    SELECT D1.HOLDER_ACC_NO ,D1.CUST_NO FROM KS.HOLDER_ACC D1 LEFT JOIN KS.CUST_BASE_INFO BB1 ON D1.CUST_NO = BB1.CUST_NO
                    WHERE D1.HOLDER_ACC_NO !='' AND BB1.CUST_STATUS = '0'   AND D1.STATUS = '0' {allow_seat_no}{disabled_seat_no}
                    AND BB1.ATTRIBUTE = '{attribute}' AND BB1.CUST_NO NOT IN {disabled_cust_no} AND D1.HOLDER_TYPE IN ('00','04')
     )B ON A.HOLDER_ACC_NO = B.HOLDER_ACC_NO
            WHERE A.CUST_NO = B.CUST_NO AND B.HOLDER_ACC_NO IS NOT NULL
             )AA
    LEFT JOIN (
                SELECT CUST_NO  FROM KS.VIP_CUST_LIST) BB
    ON AA.CUST_NO = BB.CUST_NO
        WHERE BB.CUST_NO IS NULL
    ORDER BY AA.VOL_BAL DESC  FETCH FIRST 1 ROWS ONLY WITH UR