day1_input = [1438, 781, 1917, 1371, 1336, 1802, 1566, 1878, 737, 1998, 1488, 1372, 1715, 1585, 1676, 1810, 1692, 1329, 1916, 1854, 1307, 1347, 1445, 1475, 1435, 1270, 1949, 1957, 1602, 1931, 1505, 1636, 1539, 1803, 1011, 1821, 1021, 1461, 1755, 1332, 1576, 1923, 1899, 1574, 1641, 1357, 1509, 1877, 1875, 1228, 1725, 1808, 1678, 1789, 1719, 1691, 1434, 1538, 2002, 1569, 1403, 1146, 1623, 1328, 1876, 520, 1930, 1633, 1990, 1330, 1402, 1880, 1984, 1938, 1898, 1908, 1661, 1335, 1424, 1833, 1731, 1568, 1659, 1554, 1323, 1344, 1999, 1716, 1851, 1313, 1531, 190, 1834, 1592, 1890, 1649, 1430, 1599, 869, 1460, 1009, 1771, 1818, 1853, 1544, 1279, 1997, 1896, 1272, 1772, 1375, 1373, 1689, 1249, 1840, 1528, 1749, 1364, 1670, 1361, 1408, 1828, 1864, 1826, 1499, 1507, 336, 1532, 1349, 1519, 1437, 1720, 1817, 1920, 1388, 1288, 1290, 1823, 1690, 1331, 1564, 1660, 1598, 1479, 1673, 1553, 1991, 66, 1571, 1453, 1398, 1814, 1679, 1652, 1687, 1951, 1334, 1319, 1605, 1757, 1517, 1724, 2008, 1601, 1909, 1286, 1780, 1901, 1961, 1798, 1628, 1831, 1277, 1297, 1744, 1946, 1407, 1856, 1922, 1476, 1836, 1240, 1591, 1572, 2000, 1813, 1695, 1723, 1238, 1588, 1881, 1850, 1298, 1411, 1496, 744, 1477, 1459, 1333, 1902]


def day1_part1(input_list):
    looking_for = {}
    for entry in input_list:
        if entry in looking_for:
            return entry * (2020 - entry)

        look_for = 2020 - entry
        looking_for[look_for] = 1

    print(f"No matches found")


def day1_part2(input_list):
    map_missing_value_to_used_indices = {}
    for index1, entry1 in enumerate(input_list):
        for index2, entry2 in enumerate(input_list):
            if index1 == index2:
                continue
            map_missing_value_to_used_indices[2020 - entry1 - entry2] = [index1, index2]

    for third_entry_index, third_entry in enumerate(input_list):
        if third_entry in map_missing_value_to_used_indices:
            used_indices = map_missing_value_to_used_indices[third_entry]
            if third_entry_index not in used_indices:
                return input_list[used_indices[0]] * input_list[used_indices[1]] * third_entry
    print(f"No matches found")
