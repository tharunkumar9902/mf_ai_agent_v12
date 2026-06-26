def generate_compare_summary(f1_name: str, f1_metrics: dict, f2_name: str, f2_metrics: dict) -> str:
    r1 = f1_metrics.get("one_year_return_percent")
    r2 = f2_metrics.get("one_year_return_percent")
    if r1 is None or r2 is None:
        return (
            f"{f1_name} and {f2_name} were compared using available NAV data, "
            "but complete 1-year return data was not available for one or both funds."
        )
    if r1 > r2:
        better = f1_name
        diff = round(r1 - r2, 2)
    elif r2 > r1:
        better = f2_name
        diff = round(r2 - r1, 2)
    else:
        return f"{f1_name} and {f2_name} have similar 1-year returns based on available NAV data."
    return f"Based on available 1-year return data, {better} has outperformed by about {diff}%."
