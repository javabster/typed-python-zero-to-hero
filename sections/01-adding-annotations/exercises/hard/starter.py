"""HARD — annotate this small data-processing module.

The module parses raw sales rows into structured records, groups by region,
and computes totals. There are optional fields, nested containers, and one
generator function to annotate.
"""

RAW_ROWS = [
    "2026-01-14,APAC,Widgets,1200,42",
    "2026-01-14,EMEA,Widgets,,17",         # missing price
    "2026-01-15,APAC,Gadgets,850,,",       # missing quantity
    "2026-01-15,AMER,Widgets,1200,30",
    "2026-01-16,APAC,Widgets,1200,55",
]

REGIONS = ("APAC", "EMEA", "AMER")


def parse_row(row):
    parts = [p.strip() for p in row.split(",")]
    date, region, product, price, quantity = parts[0], parts[1], parts[2], parts[3], parts[4]
    return {
        "date": date,
        "region": region,
        "product": product,
        "price": int(price) if price else None,
        "quantity": int(quantity) if quantity else None,
    }


def parse_all(rows):
    return [parse_row(r) for r in rows]


def group_by_region(records):
    groups = {}
    for record in records:
        groups.setdefault(record["region"], []).append(record)
    return groups


def region_totals(groups):
    totals = {}
    for region, records in groups.items():
        revenue = 0
        for record in records:
            if record["price"] is not None and record["quantity"] is not None:
                revenue += record["price"] * record["quantity"]
        totals[region] = revenue
    return totals


def top_regions(totals, n=2):
    ordered = sorted(totals.items(), key=lambda pair: pair[1], reverse=True)
    return ordered[:n]


def iter_complete_records(records):
    """Yield records with no missing fields."""
    for record in records:
        if record["price"] is not None and record["quantity"] is not None:
            yield record


if __name__ == "__main__":
    records = parse_all(RAW_ROWS)
    groups = group_by_region(records)
    totals = region_totals(groups)
    print("Totals:", totals)
    print("Top 2:", top_regions(totals))
    print("Complete records:", list(iter_complete_records(records)))
