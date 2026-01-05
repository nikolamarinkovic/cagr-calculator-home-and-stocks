import tkinter as tk
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List


class Price:
    def __init__(
            self,
            municipality: str,
            min_old_construction: int,
            max_old_construction: int,
            average_old_construction: int,
            min_new_construction: int,
            max_new_construction: int,
            average_new_construction: int):
    
        self.municipality: str = municipality # municipality name

        self.min_old_construction: int = min_old_construction  # not used anywhere but kept in for further improvements
        self.max_old_construction: int = max_old_construction  # not used anywhere but kept in for further improvements
        self.average_old_construction: int = average_old_construction  # average price per square meter for old construction

        self.min_new_construction: int = min_new_construction  # not used anywhere but kept in for further improvements
        self.max_new_construction: int = max_new_construction  # not used anywhere but kept in for further improvements
        self.average_new_construction: int = average_new_construction  # average price per square meter for new construction


home_prices = {
    # municipality,
    # min_old_construction, max_old_construction, average_old_construction
    # min_new_construction, max_new_construction, average_new_construction
    2024: [
        Price("Stari Grad", 1000, 7500, 3367, 2200, 6517, 4197),
        Price("Vračar", 806, 6000, 3039, 1151, 5830, 3178),
        Price("Savski venac", 818, 7529, 2852, 1194, 11811, 4508),
        Price("Novi Beograd", 758, 5294, 2561, 1331, 4983, 3233),
        Price("Zvezdara", 700, 5185, 2422, 1083, 4788, 2347),
        Price("Palilula", 755, 4600, 2301, 1118, 4209, 2577),
        Price("Voždovac", 742, 3902, 2254, 1000, 4188, 2616),
        Price("Zemun", 654, 3571, 2198, 909, 3535, 2378),
        Price("Čukarica", 649, 3690, 2085, 977, 4051, 2878),
        Price("Stara Rakovica", 702, 2893, 1835, 1134, 3044, 2284),
        Price("Beograd (svi gradovi)", 600, 7500, 2225, 800, 11811, 2435)
    ],
    2023: [
        Price("Stari Grad", 952, 6000, 3130, 1980, 5215, 3625),
        Price("Vračar", 645, 4650, 2822, 984, 6245, 2988),
        Price("Savski venac", 900, 4432, 2490, 945, 11475, 4213),
        Price("Novi Beograd", 732, 5032, 2415, 895, 4030, 2538),
        Price("Zvezdara", 600, 4298, 2212, 795, 3933, 2280),
        Price("Palilula", 690, 4367, 2185, 1000, 3888, 2150),
        Price("Zemun", 610, 4268, 2085, 605, 3707, 2320),
        Price("Voždovac", 515, 3930, 2052, 705, 3780, 2290),
        Price("Čukarica", 625, 3500, 1925, 605, 3470, 2110),
        Price("Stara Rakovica", 600, 2513, 1685, 1042, 2720, 1928),
        Price("Beograd (svi gradovi)", 400, 6000, 2060, 605, 11475, 2413)
    ],
    2022: [
        Price("Stari Grad", 715, 5238, 2628, 1010, 4765, 3265),
        Price("Vračar", 850, 4302, 2500, 875, 6162, 2575),
        Price("Savski venac", 833, 5195, 2248, 888, 10400, 3825),
        Price("Novi Beograd", 693, 4613, 2090, 875, 3995, 2522),
        Price("Zvezdara", 600, 3915, 1995, 625, 3362, 2150),
        Price("Palilula", 730, 4153, 1827, 1087, 3585, 2440),
        Price("Zemun", 517, 3500, 1805, 705, 3120, 2062),
        Price("Voždovac", 635, 3520, 1740, 737, 3492, 2132),
        Price("Čukarica", 500, 3500, 1657, 680, 4038, 1930),
        Price("Stara Rakovica", 705, 2260, 1427, 770, 2115, 1650),
        Price("Beograd (svi gradovi)", 400, 5238, 1815, 600, 10400, 2342)
    ],
    2021: [
        Price("Stari Grad", 882, 4500, 2328, 1325, 6493, 2755),
        Price("Vračar", 882, 4615, 2168, 845, 4292, 2224),
        Price("Savski venac", 870, 3420, 1866, 1200, 10068, 3155),
        Price("Novi Beograd", 715, 3083, 1770, 875, 3937, 2190),
        Price("Zvezdara", 773, 3208, 1702, 727, 3325, 1845),
        Price("Palilula", 587, 3000, 1572, 900, 3470, 2020),
        Price("Zemun", 632, 2625, 1563, 672, 2795, 1820),
        Price("Voždovac", 605, 2647, 1510, 675, 3287, 1958),
        Price("Čukarica", 570, 2442, 1430, 600, 2900, 1728),
        Price("Stara Rakovica", 522, 1880, 1180, 732, 1844, 1368),
        Price("Beograd (svi gradovi)", 400, 4615, 1530, 600, 10068, 2005)
    ],
    2020: [
        Price("Stari Grad", 1000, 4452, 2178, 962, 3836, 2636),
        Price("Vračar", 885, 4301, 1987, 1075, 3820, 2086),
        Price("Savski venac", 754, 3014, 1750, 1208, 9194, 3174),
        Price("Novi Beograd", 543, 3243, 1606, 900, 3731, 2258),
        Price("Palilula", 611, 2636, 1373, 882, 3060, 1629),
        Price("Zvezdara", 580, 2686, 1523, 768, 2763, 1691),
        Price("Voždovac", 555, 2390, 1316, 756, 2975, 1684),
        Price("Čukarica", 473, 2229, 1299, 947, 2787, 1695),
        Price("Zemun", 672, 2117, 1387, 732, 2505, 1728),
        Price("Stara Rakovica", 500, 1718, 1062, 612, 1662, 1278)
    ],
    2019: [
        Price("Stari Grad", 918, 3815, 2042, 1490, 2790, 2263),
        Price("Vračar", 905, 3125, 1840, 1221, 3019, 2002),
        Price("Savski venac", 842, 2851, 1634, 1400, 8683, 2979),
        Price("Novi Beograd", 652, 2936, 1500, 920, 3557, 2230),
        Price("Palilula", 500, 2358, 1264, 800, 2731, 1535),
        Price("Zvezdara", 619, 2441, 1426, 733, 2369, 1575),
        Price("Voždovac", 600, 2024, 1247, 739, 2226, 1640),
        Price("Čukarica", 605, 2089, 1200, 769, 2171, 1356),
        Price("Zemun", 500, 2190, 1274, 784, 2315, 1610),
        Price("Stara Rakovica", 500, 1519, 997, 850, 1194, 1077)
    ],
    2018: [
        Price("Stari Grad", 900, 2800, 1838, 1650, 2760, 2194),
        Price("Vračar", 920, 2500, 1712, 1200, 2987, 1859),
        Price("Savski venac", 912, 2979, 1572, 1522, 7777, 2739),
        Price("Novi Beograd", 500, 2843, 1334, 700, 3140, 1982),
        Price("Palilula", 500, 2860, 1194, 825, 2884, 1450),
        Price("Zvezdara", 606, 2286, 1346, 620, 2678, 1528),
        Price("Voždovac", 600, 2005, 1149, 645, 2044, 1534),
        Price("Čukarica", 500, 2418, 1115, 620, 2102, 1339),
        Price("Zemun", 500, 2090, 1160, 606, 1961, 1411)
    ],
    2017: [
        Price("Stari Grad", 800, 2800, 1750, 1300, 2310, 1918),
        Price("Vračar", 900, 2500, 1606, 1220, 2552, 1756),
        Price("Savski venac", 800, 2225, 1425, 1946, 7111, 2649),
        Price("Novi Beograd", 700, 2095, 1206, 611, 2450, 1643),
        Price("Palilula", 700, 1773, 1114, 1042, 2475, 1573),
        Price("Zvezdara", 606, 2099, 1226, 808, 2100, 1472),
        Price("Voždovac", 606, 1768, 1100, 814, 1884, 1520),
        Price("Čukarica", 600, 1698, 1052, 800, 1792, 1205),
        Price("Zemun", 600, 1700, 1113, 611, 1900, 1419)
    ]
}


# Calculates home cagr data between 2 years, returns a list strings that can be shown on UI
# Each string in the list should be divided by new lines (\n) before printing.
def calculate_cagr_homes(year_from: int, year_to: int, prices: Dict[int, List[Price]]) -> List[str]:
    if year_from not in prices or year_to not in prices:
        return ["Error! No home data for the chosen years."]

    output_lines = []
    years_diff = year_to - year_from

    data_from: Dict[str, Price] = {o.municipality: o for o in prices[year_from]}
    data_to: Dict[str, Price] = {o.municipality: o for o in prices[year_to]}

    # ---------- OLD CONSTRUCTION ----------
    output_lines.append("OLD CONSTRUCTION – CAGR (%)")
    output_lines.append("-" * 40)

    cagr_old_construction = []

    for municipality in sorted(data_from.keys()):
        if municipality not in data_to:
            continue

        start_price = data_from[municipality].average_old_construction
        end_price = data_to[municipality].average_old_construction

        if start_price <= 0:
            continue

        cagr = (end_price / start_price) ** (1 / years_diff) - 1
        cagr_old_construction.append(cagr * 100)

        output_lines.append(f"{municipality:20s} {cagr * 100:6.2f}%")

    if cagr_old_construction:
        output_lines.append(f"\nAVERAGE (old construction): {sum(cagr_old_construction) / len(cagr_old_construction):.2f}%\n")

    # ---------- NEW CONSTRUCTION ----------
    output_lines.append("NEW CONSTRUCTION – CAGR (%)")
    output_lines.append("-" * 40)

    cagr_new_construction = []

    for municipality in sorted(data_from.keys()):
        if municipality not in data_to:
            continue

        start_price = data_from[municipality].average_new_construction
        end_price = data_to[municipality].average_new_construction

        if start_price <= 0:
            continue

        cagr = (end_price / start_price) ** (1 / years_diff) - 1
        cagr_new_construction.append(cagr * 100)

        output_lines.append(f"{municipality:20s} {cagr * 100:6.2f}%")

    if cagr_new_construction:
        output_lines.append(f"\nAVERAGE (new construction): {sum(cagr_new_construction) / len(cagr_new_construction):.2f}%")

    return output_lines


# calculates sp500 cagr data between 2 years, returns string that can be shown on UI
def calculate_sp500_cagr(year_from: int, year_to: int, sp500_yearly_prices: any) -> str:
    data = sp500_yearly_prices[(sp500_yearly_prices.index.year >= year_from) &
                               (sp500_yearly_prices.index.year <= year_to)]

    if len(data) < 2:
        return "Not enough s&p500 data for these years!"

    start_price = data.iloc[0]["Close"]
    end_price = data.iloc[-1]["Close"]

    years = year_to - year_from

    cagr = (end_price / start_price) ** (1 / years) - 1

    return f"S&P 500 CAGR ({year_from}-{year_to}): {cagr * 100:.2f}%"


# calculate carg for stocks/homes and displays data
def calculate_cagr(text_output: tk.Text, entry_from: tk.Entry, entry_to: tk.Entry, sp500_yearly) -> None:
    # clear console
    text_output.delete("1.0", tk.END)

    # input validation
    try:
        year_from = int(entry_from.get())
        year_to = int(entry_to.get())
    except ValueError:
        text_output.insert(tk.END, "Error! Enter valid years.")
        return

    if year_from >= year_to:
        text_output.insert(tk.END, "Error! Year FROM must be less than year TO.")
        return

    # calculate and display cagr for stocks
    sp500_result: str = calculate_sp500_cagr(year_from, year_to, sp500_yearly)
    text_output.insert(tk.END, sp500_result)
    text_output.insert(tk.END, "\n" + "=" * 40 + "\n\n")

    # calculate and display cag for homes
    home_result: List[str] = calculate_cagr_homes(year_from, year_to, home_prices)
    for line in home_result:
        text_output.insert(tk.END, line + "\n")


# gets the sp500, groups them by years and takes only closing prices
def get_sp500_data():
    end_date = datetime.today()
    start_date = end_date - timedelta(days=50 * 365)

    sp500 = yf.download(
        "^GSPC",
        start=start_date,
        end=end_date,
        interval="1mo",
        auto_adjust=True
    )

    if isinstance(sp500.columns, pd.MultiIndex):
        sp500.columns = sp500.columns.get_level_values(0)

    sp500 = sp500[["Close"]].dropna()

    # Year-end portfolio values
    sp500_yearly = sp500.resample("Y").last()

    return sp500_yearly


def main():
    sp500_yearly = get_sp500_data()

    # ---- GUI ----
    root = tk.Tk()
    root.title("Compound annual growth rate for homes and stocks")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    tk.Label(frame, text="Note: supported years are 2017-2024 (inclusive)").grid(row=0, column=0, columnspan=2, pady=(0, 10))

    tk.Label(frame, text="Year FROM:").grid(row=1, column=0, sticky="e")
    entry_from = tk.Entry(frame, width=10)
    entry_from.grid(row=1, column=1)

    tk.Label(frame, text="Year TO:").grid(row=2, column=0, sticky="e")
    entry_to = tk.Entry(frame, width=10)
    entry_to.grid(row=2, column=1)

    btn = tk.Button(frame, text="Calculate",
                    command=lambda: calculate_cagr(text_output, entry_from, entry_to, sp500_yearly))
    btn.grid(row=3, column=0, columnspan=2, pady=5)

    text_output = tk.Text(root, width=70, height=30)
    text_output.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
