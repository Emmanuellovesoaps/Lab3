import price_info

def test_total_cost_shopping():
    
    expected = 46.75
    result = price_info.total_cost_shopping()
    assert result == expected

def test_cost_of_fruits():
    fruit = 'apple'
    quantity = 10
    expected = 12.0  # 1.20 * 10
    result = price_info.cost_of_fruits(fruit, quantity)
    assert result == expected