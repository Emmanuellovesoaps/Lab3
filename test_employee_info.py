import employee_info

def test_get_employees_by_age_range():
    
    result = employee_info.get_employees_by_age_range(25, 35)
    names = [item["name"] for item in result]
    assert "Jane" not in names  
    assert "John" in names      
    assert "Mike" in names      
    assert "Mary" not in names      
    assert "Chloe" not in names

def test_calculate_average_salary():
    
    input_value = 2
    expected = 60166.666666666664
    result = employee_info.calculate_average_salary()
    assert abs(result - expected) < 0.01
    
def test_get_employees_by_dept():

    result = employee_info.get_employees_by_dept("Sales")
    names = [item["name"] for item in result]
    assert "John" in names
    assert "Peter" in names
    assert "Jane" not in names
    