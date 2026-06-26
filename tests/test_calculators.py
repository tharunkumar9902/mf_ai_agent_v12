from app.tools.calculators import calculate_returns

def test_calculate_returns():
    nav_data = [
        {"date": "01-01-2022", "nav": "100"},
        {"date": "01-01-2023", "nav": "110"},
        {"date": "01-01-2024", "nav": "125"},
        {"date": "01-01-2025", "nav": "150"},
    ]
    result = calculate_returns(nav_data)
    assert result["latest_nav"] == 150.0
    assert "total_return_percent" in result
