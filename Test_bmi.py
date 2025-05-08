import Lab2.Bmi as bmi

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(weight= 57, height= 1.73) == 0)
def test_bmi_over_weight():
    assert(bmi.calculate_bmi(weight= 90, height= 1.73) == 1)
def test_bmi_under_weight():
    assert(bmi.calculate_bmi(weight= 10, height= 1.73) == -1)