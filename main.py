import tkinter as tk
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List


class CenaStana:
    def __init__(
            self,
            naziv: str,
            min_starogradnja: int,
            max_starogradnja: int,
            average_starogradnja: int,
            min_novogradnja: int,
            max_novogradnja: int,
            average_novogradnja: int):
    
        self.naziv: str = naziv # name of opstina

        self.min_starogradnja: int = min_starogradnja  # not used anywhere but kept in for further improvements
        self.max_starogradnja: int = max_starogradnja  # not used anywhere but kept in for further improvements
        self.average_starogradnja: int = average_starogradnja

        self.min_novogradnja: int = min_novogradnja  # not used anywhere but kept in for further improvements
        self.max_novogradnja: int = max_novogradnja  # not used anywhere but kept in for further improvements
        self.average_novogradnja: int = average_novogradnja


home_prices = {
    # opstina, min_starogradnja, max_starogradnja, average_starogradnja, min_novogradnja, max_novogradnja, average_novogradnja
    2024: [
        CenaStana("Stari Grad", 1000, 7500, 3367, 2200, 6517, 4197),
        CenaStana("Vračar", 806, 6000, 3039, 1151, 5830, 3178),
        CenaStana("Savski venac", 818, 7529, 2852, 1194, 11811, 4508),
        CenaStana("Novi Beograd", 758, 5294, 2561, 1331, 4983, 3233),
        CenaStana("Zvezdara", 700, 5185, 2422, 1083, 4788, 2347),
        CenaStana("Palilula", 755, 4600, 2301, 1118, 4209, 2577),
        CenaStana("Voždovac", 742, 3902, 2254, 1000, 4188, 2616),
        CenaStana("Zemun", 654, 3571, 2198, 909, 3535, 2378),
        CenaStana("Čukarica", 649, 3690, 2085, 977, 4051, 2878),
        CenaStana("Stara Rakovica", 702, 2893, 1835, 1134, 3044, 2284),
        CenaStana("Beograd (svi gradovi)", 600, 7500, 2225, 800, 11811, 2435)
    ],
    2023: [
        CenaStana("Stari Grad", 952, 6000, 3130, 1980, 5215, 3625),
        CenaStana("Vračar", 645, 4650, 2822, 984, 6245, 2988),
        CenaStana("Savski venac", 900, 4432, 2490, 945, 11475, 4213),
        CenaStana("Novi Beograd", 732, 5032, 2415, 895, 4030, 2538),
        CenaStana("Zvezdara", 600, 4298, 2212, 795, 3933, 2280),
        CenaStana("Palilula", 690, 4367, 2185, 1000, 3888, 2150),
        CenaStana("Zemun", 610, 4268, 2085, 605, 3707, 2320),
        CenaStana("Voždovac", 515, 3930, 2052, 705, 3780, 2290),
        CenaStana("Čukarica", 625, 3500, 1925, 605, 3470, 2110),
        CenaStana("Stara Rakovica", 600, 2513, 1685, 1042, 2720, 1928),
        CenaStana("Beograd (svi gradovi)", 400, 6000, 2060, 605, 11475, 2413)
    ],
    2022: [
        CenaStana("Stari Grad", 715, 5238, 2628, 1010, 4765, 3265),
        CenaStana("Vračar", 850, 4302, 2500, 875, 6162, 2575),
        CenaStana("Savski venac", 833, 5195, 2248, 888, 10400, 3825),
        CenaStana("Novi Beograd", 693, 4613, 2090, 875, 3995, 2522),
        CenaStana("Zvezdara", 600, 3915, 1995, 625, 3362, 2150),
        CenaStana("Palilula", 730, 4153, 1827, 1087, 3585, 2440),
        CenaStana("Zemun", 517, 3500, 1805, 705, 3120, 2062),
        CenaStana("Voždovac", 635, 3520, 1740, 737, 3492, 2132),
        CenaStana("Čukarica", 500, 3500, 1657, 680, 4038, 1930),
        CenaStana("Stara Rakovica", 705, 2260, 1427, 770, 2115, 1650),
        CenaStana("Beograd (svi gradovi)", 400, 5238, 1815, 600, 10400, 2342)
    ],
    2021: [
        CenaStana("Stari Grad", 882, 4500, 2328, 1325, 6493, 2755),
        CenaStana("Vračar", 882, 4615, 2168, 845, 4292, 2224),
        CenaStana("Savski venac", 870, 3420, 1866, 1200, 10068, 3155),
        CenaStana("Novi Beograd", 715, 3083, 1770, 875, 3937, 2190),
        CenaStana("Zvezdara", 773, 3208, 1702, 727, 3325, 1845),
        CenaStana("Palilula", 587, 3000, 1572, 900, 3470, 2020),
        CenaStana("Zemun", 632, 2625, 1563, 672, 2795, 1820),
        CenaStana("Voždovac", 605, 2647, 1510, 675, 3287, 1958),
        CenaStana("Čukarica", 570, 2442, 1430, 600, 2900, 1728),
        CenaStana("Stara Rakovica", 522, 1880, 1180, 732, 1844, 1368),
        CenaStana("Beograd (svi gradovi)", 400, 4615, 1530, 600, 10068, 2005)
    ],
    2020: [
        CenaStana("Stari Grad", 1000, 4452, 2178, 962, 3836, 2636),
        CenaStana("Vračar", 885, 4301, 1987, 1075, 3820, 2086),
        CenaStana("Savski venac", 754, 3014, 1750, 1208, 9194, 3174),
        CenaStana("Novi Beograd", 543, 3243, 1606, 900, 3731, 2258),
        CenaStana("Palilula", 611, 2636, 1373, 882, 3060, 1629),
        CenaStana("Zvezdara", 580, 2686, 1523, 768, 2763, 1691),
        CenaStana("Voždovac", 555, 2390, 1316, 756, 2975, 1684),
        CenaStana("Čukarica", 473, 2229, 1299, 947, 2787, 1695),
        CenaStana("Zemun", 672, 2117, 1387, 732, 2505, 1728),
        CenaStana("Stara Rakovica", 500, 1718, 1062, 612, 1662, 1278)
    ],
    2019: [
        CenaStana("Stari Grad", 918, 3815, 2042, 1490, 2790, 2263),
        CenaStana("Vračar", 905, 3125, 1840, 1221, 3019, 2002),
        CenaStana("Savski venac", 842, 2851, 1634, 1400, 8683, 2979),
        CenaStana("Novi Beograd", 652, 2936, 1500, 920, 3557, 2230),
        CenaStana("Palilula", 500, 2358, 1264, 800, 2731, 1535),
        CenaStana("Zvezdara", 619, 2441, 1426, 733, 2369, 1575),
        CenaStana("Voždovac", 600, 2024, 1247, 739, 2226, 1640),
        CenaStana("Čukarica", 605, 2089, 1200, 769, 2171, 1356),
        CenaStana("Zemun", 500, 2190, 1274, 784, 2315, 1610),
        CenaStana("Stara Rakovica", 500, 1519, 997, 850, 1194, 1077)
    ],
    2018: [
        CenaStana("Stari Grad", 900, 2800, 1838, 1650, 2760, 2194),
        CenaStana("Vračar", 920, 2500, 1712, 1200, 2987, 1859),
        CenaStana("Savski venac", 912, 2979, 1572, 1522, 7777, 2739),
        CenaStana("Novi Beograd", 500, 2843, 1334, 700, 3140, 1982),
        CenaStana("Palilula", 500, 2860, 1194, 825, 2884, 1450),
        CenaStana("Zvezdara", 606, 2286, 1346, 620, 2678, 1528),
        CenaStana("Voždovac", 600, 2005, 1149, 645, 2044, 1534),
        CenaStana("Čukarica", 500, 2418, 1115, 620, 2102, 1339),
        CenaStana("Zemun", 500, 2090, 1160, 606, 1961, 1411)
    ],
    2017: [
        CenaStana("Stari Grad", 800, 2800, 1750, 1300, 2310, 1918),
        CenaStana("Vračar", 900, 2500, 1606, 1220, 2552, 1756),
        CenaStana("Savski venac", 800, 2225, 1425, 1946, 7111, 2649),
        CenaStana("Novi Beograd", 700, 2095, 1206, 611, 2450, 1643),
        CenaStana("Palilula", 700, 1773, 1114, 1042, 2475, 1573),
        CenaStana("Zvezdara", 606, 2099, 1226, 808, 2100, 1472),
        CenaStana("Voždovac", 606, 1768, 1100, 814, 1884, 1520),
        CenaStana("Čukarica", 600, 1698, 1052, 800, 1792, 1205),
        CenaStana("Zemun", 600, 1700, 1113, 611, 1900, 1419)
    ]
}


# Calculates home cagr data between 2 years, returns a list strings that can be shown on UI
# Each string in the list should be divided by new lines (\n) before printing.
def calculate_cagr_homes(year_from: int, year_to: int, prices: Dict[int, List[CenaStana]]) -> List[str]:
    if year_from not in prices or year_to not in prices:
        return ["Greška! Nema podataka za stanove za izabrane godine."]

    output_lines = []
    years_diff = year_to - year_from

    data_from: Dict[str, CenaStana] = {o.naziv: o for o in prices[year_from]}
    data_to: Dict[str, CenaStana] = {o.naziv: o for o in prices[year_to]}

    # ---------- STAROGRADNJA ----------
    output_lines.append("STAROGRADNJA – CAGR (%)")
    output_lines.append("-" * 40)

    cagr_starogradnja = []

    for opstina in sorted(data_from.keys()):
        if opstina not in data_to:
            continue

        start_starogradnja_average_price = data_from[opstina].average_starogradnja
        end_starogradnja_average_price = data_to[opstina].average_starogradnja

        if start_starogradnja_average_price <= 0:
            continue

        cagr = (end_starogradnja_average_price / start_starogradnja_average_price) ** (1 / years_diff) - 1
        cagr_starogradnja.append(cagr * 100)

        output_lines.append(f"{opstina:20s} {cagr * 100:6.2f}%")

    if cagr_starogradnja:
        output_lines.append(f"\nUKUPNO (starogradnja): {sum(cagr_starogradnja) / len(cagr_starogradnja):.2f}%\n")

    # ---------- NOVOGRADNJA ----------
    output_lines.append("NOVOGRADNJA – CAGR (%)")
    output_lines.append("-" * 40)

    cagr_novogradnja = []

    for opstina in sorted(data_from.keys()):
        if opstina not in data_to:
            continue

        start = data_from[opstina].average_novogradnja
        end = data_to[opstina].average_novogradnja

        if start <= 0:
            continue

        cagr = (end / start) ** (1 / years_diff) - 1
        cagr_novogradnja.append(cagr * 100)

        output_lines.append(f"{opstina:20s} {cagr * 100:6.2f}%")

    if cagr_novogradnja:
        output_lines.append(f"\nUKUPNO (novogradnja): {sum(cagr_novogradnja) / len(cagr_novogradnja):.2f}%")

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
        text_output.insert(tk.END, "Greška! Unesite validne godine.")
        return

    if year_from >= year_to:
        text_output.insert(tk.END, "Greška! Godina OD mora biti manja od godine DO.")
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
    root.title("CAGR rast cena nekretnina/deonice")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    tk.Label(frame, text="Godina OD:").grid(row=0, column=0, sticky="e")
    entry_from = tk.Entry(frame, width=10)
    entry_from.grid(row=0, column=1)

    tk.Label(frame, text="Godina DO:").grid(row=1, column=0, sticky="e")
    entry_to = tk.Entry(frame, width=10)
    entry_to.grid(row=1, column=1)

    btn = tk.Button(frame, text="Izračunaj",
                    command=lambda: calculate_cagr(text_output, entry_from, entry_to, sp500_yearly))
    btn.grid(row=2, column=0, columnspan=2, pady=5)

    text_output = tk.Text(root, width=70, height=30)
    text_output.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
