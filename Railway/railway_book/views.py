from django.shortcuts import render,HttpResponse
from .models import search

file_in = open('search.txt','wt')


#BULLSHIT
CHEM_S = ['0600', '0622', '0644', '0706', '0728', '0750', '0812', '0834', '0856', '0918', '0940', '1002', '1024', '1046', '1108', '1130', '1152', '1214', '1236', '1258', '1320', '1342', '1404', '1426', '1448', '1510', '1532', '1554', '1616', '1638', '1700', '1722', '1744', '1806', '1828', '1850', '1912', '1934', '1956', '2018', '2040', '2102', '2124', '2146', '2208']

VNP_S = ['0603', '0625', '0647', '0709', '0731', '0753', '0815', '0837', '0859', '0921', '0943', '1005', '1027', '1049', '1111', '1133', '1155', '1217', '1239', '1301', '1323', '1345', '1407', '1429', '1451', '1513', '1535', '1557', '1619', '1641', '1703', '1725', '1747', '1809', '1831', '1853', '1915', '1937', '1959', '2021', '2043', '2105', '2127', '2149', '2211']

FER_S = ['0605', '0627', '0649', '0711', '0733', '0755', '0817', '0839', '0901', '0923', '0945', '1007', '1029', '1051', '1113', '1135', '1157', '1219', '1241', '1303', '1325', '1347', '1409', '1431', '1453', '1515', '1537', '1559', '1621', '1643', '1705', '1727', '1749', '1811', '1833', '1855', '1917', '1939', '2001', '2023', '2045', '2107', '2129', '2151', '2213']

BHARAT_S = ['0606', '0628', '0650', '0712', '0734', '0756', '0818', '0840', '0902', '0924', '0946', '1008', '1030', '1052', '1114', '1136', '1158', '1220', '1242', '1304', '1326', '1348', '1410', '1432', '1454', '1516', '1538', '1600', '1622', '1644', '1706', '1728', '1750', '1812', '1834', '1856', '1918', '1940', '2002', '2024', '2046', '2108', '2130', '2152', '2214']

MYSORE_S = ['0609', '0631', '0653', '0715', '0737', '0759', '0821', '0843', '0905', '0927', '0949', '1011', '1033', '1055', '1117', '1139', '1201', '1223', '1245', '1307', '1329', '1351', '1413', '1435', '1457', '1519', '1541', '1603', '1625', '1647', '1709', '1731', '1753', '1815', '1837', '1859', '1921', '1943', '2005', '2027', '2049', '2111', '2133', '2155', '2217']

BHAKTI_S = ['0614', '0636', '0658', '0720', '0742', '0804', '0826', '0848', '0910', '0932', '0954', '1016', '1038', '1100', '1122', '1144', '1206', '1228', '1250', '1312', '1334', '1356', '1418', '1440', '1502', '1524', '1546', '1608', '1630', '1652', '1714', '1736', '1758', '1820', '1842', '1904', '1926', '1948', '2010', '2032', '2054', '2116', '2138', '2200', '2222']

WADALA_S = ['0617', '0639', '0701', '0723', '0745', '0807', '0829', '0851', '0913', '0935', '0957', '1019', '1041', '1103', '1125', '1147', '1209', '1231', '1253', '1315', '1337', '1359', '1421', '1443', '1505', '1527', '1549', '1611', '1633', '1655', '1717', '1739', '1801', '1823', '1845', '1907', '1929', '1951', '2013', '2035', '2057', '2119', '2141', '2203', '2225']

GTB_S = ['0619', '0641', '0703', '0725', '0747', '0809', '0831', '0853', '0915', '0937', '0959', '1021', '1043', '1105', '1127', '1149', '1211', '1233', '1255', '1317', '1339', '1401', '1423', '1445', '1507', '1529', '1551', '1613', '1635', '1657', '1719', '1741', '1803', '1825', '1847', '1909', '1931', '1953', '2015', '2037', '2059', '2121', '2143', '2205', '2227']

ANTOP_S = ['0621', '0643', '0705', '0727', '0749', '0811', '0833', '0855', '0917', '0939', '1001', '1023', '1045', '1107', '1129', '1151', '1213', '1235', '1257', '1319', '1341', '1403', '1425', '1447', '1509', '1531', '1553', '1615', '1637', '1659', '1721', '1743', '1805', '1827', '1849', '1911', '1933', '1955', '2017', '2039', '2101', '2123', '2145', '2207', '2229']

ACHARYA_S = ['0624', '0646', '0708', '0730', '0752', '0814', '0836', '0858', '0920', '0942', '1004', '1026', '1048', '1110', '1132', '1154', '1216', '1238', '1300', '1322', '1344', '1406', '1428', '1450', '1512', '1534', '1556', '1618', '1640', '1702', '1724', '1746', '1808', '1830', '1852', '1914', '1936', '1958', '2020', '2042', '2104', '2126', '2148', '2210', '2232']

WADALAB_S = ['0629', '0651', '0713', '0735', '0757', '0819', '0841', '0903', '0925', '0947', '1009', '1031', '1053', '1115', '1137', '1159', '1221', '1243', '1305', '1327', '1349', '1411', '1433', '1455', '1517', '1539', '1601', '1623', '1645', '1707', '1729', '1751', '1813', '1835', '1857', '1919', '1941', '2003', '2025', '2047', '2109', '2131', '2153', '2215', '2237']

DADAR_S = ['0631', '0653', '0715', '0737', '0759', '0821', '0843', '0905', '0927', '0949', '1011', '1033', '1055', '1117', '1139', '1201', '1223', '1245', '1307', '1329', '1351', '1413', '1435', '1457', '1519', '1541', '1603', '1625', '1647', '1709', '1731', '1753', '1815', '1837', '1859', '1921', '1943', '2005', '2027', '2049', '2111', '2133', '2155', '2217', '2239']

NAIGAON_S = ['0634', '0656', '0718', '0740', '0802', '0824', '0846', '0908', '0930', '0952', '1014', '1036', '1058', '1120', '1142', '1204', '1226', '1248', '1310', '1332', '1354', '1416', '1438', '1500', '1522', '1544', '1606', '1628', '1650', '1712', '1734', '1756', '1818', '1840', '1902', '1924', '1946', '2008', '2030', '2052', '2114', '2136', '2158', '2220', '2242']

AMBEDKAR_S =['0638', '0700', '0722', '0744', '0806', '0828', '0850', '0912', '0934', '0956', '1018', '1040', '1102', '1124', '1146', '1208', '1230', '1252', '1314', '1336', '1358', '1420', '1442', '1504', '1526', '1548', '1610', '1632', '1654', '1716', '1738', '1800', '1822', '1844', '1906', '1928', '1950', '2012', '2034', '2056', '2118', '2140', '2202', '2224', '2246']

MINT_S =  ['0641', '0703', '0725', '0747', '0809', '0831', '0853', '0915', '0937', '0959', '1021', '1043', '1105', '1127', '1149', '1211', '1233', '1255', '1317', '1339', '1401', '1423', '1445', '1507', '1529', '1551', '1613', '1635', '1657', '1719', '1741', '1803', '1825', '1847', '1909', '1931', '1953', '2015', '2037', '2059', '2121', '2143', '2205', '2227', '2249']

LOWER_S = ['0644', '0706', '0728', '0750', '0812', '0834', '0856', '0918', '0940', '1002', '1024', '1046', '1108', '1130', '1152', '1214', '1236', '1258', '1320', '1342', '1404', '1426', '1448', '1510', '1532', '1554', '1616', '1638', '1700', '1722', '1744', '1806', '1828', '1850', '1912', '1934', '1956', '2018', '2040', '2102', '2124', '2146', '2208', '2230', '2252']

SANT_S = ['0646', '0708', '0730', '0752', '0814', '0836', '0858', '0920', '0942', '1004', '1026', '1048', '1110', '1132', '1154', '1216', '1238', '1300', '1322', '1344', '1406', '1428', '1450', '1512', '1534', '1556', '1618', '1640', '1702', '1724', '1746', '1808', '1830', '1852', '1914', '1936', '1958', '2020', '2042', '2104', '2126', '2148', '2210', '2232', '2254']

CHEM_N = ['0647', '0709', '0731', '0753', '0815', '0837', '0859', '0921', '0943', '1005', '1027', '1049', '1111', '1133', '1155', '1217', '1239', '1301', '1323', '1345', '1407', '1429', '1451', '1513', '1535', '1557', '1619', '1641', '1703', '1725', '1747', '1809', '1831', '1853', '1915', '1937', '1959', '2021', '2043', '2105', '2127', '2149', '2211', '2233', '2255']

VNP_N = ['0644', '0706', '0728', '0750', '0812', '0834', '0856', '0918', '0940', '1002', '1024', '1046', '1108', '1130', '1152', '1214', '1236', '1258', '1320', '1342', '1404', '1426', '1448', '1510', '1532', '1554', '1616', '1638', '1700', '1722', '1744', '1806', '1828', '1850', '1912', '1934', '1956', '2018', '2040', '2102', '2124', '2146', '2208', '2230', '2252']

FER_N = ['0640', '0702', '0724', '0746', '0808', '0830', '0852', '0914', '0936', '0958', '1020', '1042', '1104', '1126', '1148', '1210', '1232', '1254', '1316', '1338', '1400', '1422', '1444', '1506', '1528', '1550', '1612', '1634', '1656', '1718', '1740', '1802', '1824', '1846', '1908', '1930', '1952', '2014', '2036', '2058', '2120', '2142', '2204', '2226', '2248']

MYSORE_N = ['0637', '0659', '0721', '0743', '0805', '0827', '0849', '0911', '0933', '0955', '1017', '1039', '1101', '1123', '1145', '1207', '1229', '1251', '1313', '1335', '1357', '1419', '1441', '1503', '1525', '1547', '1609', '1631', '1653', '1715', '1737', '1759', '1821', '1843', '1905', '1927', '1949', '2011', '2033', '2055', '2117', '2139', '2201', '2223', '2245']

BHARAT_N = ['0634', '0656', '0718', '0740', '0802', '0824', '0846', '0908', '0930', '0952', '1014', '1036', '1058', '1120', '1142', '1204', '1226', '1248', '1310', '1332', '1354', '1416', '1438', '1500', '1522', '1544', '1606', '1628', '1650', '1712', '1734', '1756', '1818', '1840', '1902', '1924', '1946', '2008', '2030', '2052', '2114', '2136', '2158', '2220', '2242']

WADALA_N = ['0627', '0649', '0711', '0733', '0755', '0817', '0839', '0901', '0923', '0945', '1007', '1029', '1051', '1113', '1135', '1157', '1219', '1241', '1303', '1325', '1347', '1409', '1431', '1453', '1515', '1537', '1559', '1621', '1643', '1705', '1727', '1749', '1811', '1833', '1855', '1917', '1939', '2001', '2023', '2045', '2107', '2129', '2151', '2213', '2235']
ANTOP_N = ['0620', '0642', '0704', '0726', '0748', '0810', '0832', '0854', '0916', '0938', '1000', '1022', '1044', '1106', '1128', '1150', '1212', '1234', '1256', '1318', '1340', '1402', '1424', '1446', '1508', '1530', '1552', '1614', '1636', '1658', '1720', '1742', '1804', '1826', '1848', '1910', '1932', '1954', '2016', '2038', '2100', '2122', '2144', '2206', '2228']

GTB_N = ['0623', '0645', '0707', '0729', '0751', '0813', '0835', '0857', '0919', '0941', '1003', '1025', '1047', '1109', '1131', '1153', '1215', '1237', '1259', '1321', '1343', '1405', '1427', '1449', '1511', '1533', '1555', '1617', '1639', '1701', '1723', '1745', '1807', '1829', '1851', '1913', '1935', '1957', '2019', '2041', '2103', '2125', '2147', '2209', '2231']

WADALAB_N = ['0615', '0637', '0659', '0721', '0743', '0805', '0827', '0849', '0911', '0933', '0955', '1017', '1039', '1101', '1123', '1145', '1207', '1229', '1251', '1313', '1335', '1357', '1419', '1441', '1503', '1525', '1547', '1609', '1631', '1653', '1715', '1737', '1759', '1821', '1843', '1905', '1927', '1949', '2011', '2033', '2055', '2117', '2139', '2201', '2223']
AMBEDKAR_N= ['0606', '0628', '0650', '0712', '0734', '0756', '0818', '0840', '0902', '0924', '0946', '1008', '1030', '1052', '1114', '1136', '1158', '1220', '1242', '1304', '1326', '1348', '1410', '1432', '1454', '1516', '1538', '1600', '1622', '1644', '1706', '1728', '1750', '1812', '1834', '1856', '1918', '1940', '2002', '2024', '2046', '2108', '2130', '2152', '2214']

ACHARYA_N = ['0616', '0638', '0700', '0722', '0744', '0806', '0828', '0850', '0912', '0934', '0956', '1018', '1040', '1102', '1124', '1146', '1208', '1230', '1252', '1314', '1336', '1358', '1420', '1442', '1504', '1526', '1548', '1610', '1632', '1654', '1716', '1738', '1800', '1822', '1844', '1906', '1928', '1950', '2012', '2034', '2056', '2118', '2140', '2202', '2224']

DADAR_N = ['0613', '0635', '0657', '0719', '0741', '0803', '0825', '0847', '0909', '0931', '0953', '1015', '1037', '1059', '1121', '1143', '1205', '1227', '1249', '1311', '1333', '1355', '1417', '1439', '1501', '1523', '1545', '1607', '1629', '1651', '1713', '1735', '1757', '1819', '1841', '1903', '1925', '1947', '2009', '2031', '2053', '2115', '2137', '2159', '2221']

NAIGAON_N =['0612', '0634', '0656', '0718', '0740', '0802', '0824', '0846', '0908', '0930', '0952', '1014', '1036', '1058', '1120', '1142', '1204', '1226', '1248', '1310', '1332', '1354', '1416', '1438', '1500', '1522', '1544', '1606', '1628', '1650', '1712', '1734', '1756', '1818', '1840', '1902', '1924', '1946', '2008', '2030', '2052', '2114', '2136', '2158', '2220'] 
MINT_N = ['0605', '0627', '0649', '0711', '0733', '0755', '0817', '0839', '0901', '0923', '0945', '1007', '1029', '1051', '1113', '1135', '1157', '1219', '1241', '1303', '1325', '1347', '1409', '1431', '1453', '1515', '1537', '1559', '1621', '1643', '1705', '1727', '1749', '1811', '1833', '1855', '1917', '1939', '2001', '2023', '2045', '2107', '2129', '2151', '2213']

LOWER_N = ['0604', '0626', '0648', '0710', '0732', '0754', '0816', '0838', '0900', '0922', '0944', '1006', '1028', '1050', '1112', '1134', '1156', '1218', '1240', '1302', '1324', '1346', '1408', '1430', '1452', '1514', '1536', '1558', '1620', '1642', '1704', '1726', '1748', '1810', '1832', '1854', '1916', '1938', '2000', '2022', '2044', '2106', '2128', '2150', '2212']

SANT_N = ['0600', '0622', '0644', '0706', '0728', '0750', '0812', '0834', '0856', '0918', '0940', '1002', '1024', '1046', '1108', '1130', '1152', '1214', '1236', '1258', '1320', '1342', '1404', '1426', '1448', '1510', '1532', '1554', '1616', '1638', '1700', '1722', '1744', '1806', '1828', '1850', '1912', '1934', '1956', '2018', '2040', '2102', '2124', '2146', '2208']
# Create your views here.
def main(request):
	return render(request,'index.html')

def recent(request):
    db = search.objects.all()
    return render(request,'recent.html',{'search_a':db})

def delete(request):
    search.objects.all().delete()
    db = search.objects.all()
    return render(request,'recent.html',{'search_a':db})



def choice(request):
    arrival = request.GET['Arrival']
    depart = request.GET['Deparutre']
    station = ['CHEMBUR','VNP MARG','FERTILIZER TOWNSHIP','BHARAT PETROLEUM','MYSORE COLONY','BHAKTI PARK','WADALA','GTB NAGAR','ANTOP HILL','ACHARYA ATRE NAGAR','WADALA BRIDGE','DADAR EAST','NAIGAON','AMBEDKAR COLONY','MINT COLONY','LOWER PAREL',"SANT GADGE CHOWK"]
    req_time = request.GET['time']    
    a = None
    req_time = req_time.replace(':', '')
    direction = None
    info = arrival + " TO " + depart + " at " + req_time[0:2] + ":" + req_time[2:4]
    db = search.objects.all()
    a = search(searches = info).save()

    for element in station:
    	
    	if element == arrival:
    		direction = 'North'
    		break
    	elif element == depart:
    		direction = 'South'
    		break
    	else:
    		continue
    print(arrival,direction,a)
   


    if direction == 'North' and arrival == 'CHEMBUR':
        for time in CHEM_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'VNP MARG':
        for time in VNP_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'FERTILIZER TOWNSHIP':
        for time in FER_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'BHARAT PETROLEUM':
        for time in BHARAT_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'MYSORE COLONY':
        for time in MYSORE_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'BHAKTI PARK':
        for time in BHAKTI_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break

    elif direction == 'North' and arrival == 'WADALA':
        for time in WADALA_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'GTB NAGAR' :
        for time in GTB_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'ANTOP HILL':
        for time in ANTOP_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'ACHARYA ATRE NAGAR':
        for time in ACHARYA_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'WADALA BRIDGE':
        for time in WADALAB_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'DADAR EAST':
        for time in DADAR_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'NAIGAON':
        for time in NAIGAON_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'AMBEDKAR NAGAR':
        for time in AMBEDKAR_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'MINT COLONY':
        for time in MINT_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break

    elif direction == 'North' and arrival == 'LOWER PAREL':
        for time in LOWER_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'North' and arrival == 'SANT GADGE':
        for time in SANT_S:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'CHEMBUR':
        for time in CHEM_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'VNP MARG':
        for time in VNP_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'FERTILIZER TOWNSHIP':
        for time in FER_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'BHARAT PETROLEUM':
        for time in BHARAT_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'MYSORE COLONY':
        for time in MYSORE_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'BHAKTI PARK':
        for time in BHAKTI_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break

    elif direction == 'South' and arrival == 'WADALA':
        for time in WADALA_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'GTB NAGAR' :
        for time in GTB_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'ANTOP HILL':
        for time in ANTOP_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'ACHARYA ATRE NAGAR':
        for time in ACHARYA_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'WADALA BRIDGE':
        for time in WADALAB_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'DADAR EAST':
        for time in DADAR_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'NAIGAON':
        for time in NAIGAON_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'AMBEDKAR NAGAR':
        for time in AMBEDKAR_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'MINT COLONY':
        for time in MINT_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break

    elif direction == 'South' and arrival == 'LOWER PAREL':
        for time in LOWER_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    elif direction == 'South' and arrival == 'SANT GADGE':
        for time in SANT_N:
            if int(time) >= int(req_time):
                a = time
                
                m = a[3:4]
               
                break
    
    position = ['FROM : ' + str(arrival),'TO : '+ str(depart)]
    final_time = [a[0:1],a[1:2],':',a[2:3],a[3:4]]
    return render(request,'result.html',{'time':final_time,'position':position})


   