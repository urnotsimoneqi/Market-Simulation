import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


def fuzzy_logic(revenue, profit):
    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    revenuevalue = ctrl.Antecedent(np.arange(0, 2100, 100), 'revenuevalue')
    profitsvalue = ctrl.Antecedent(np.arange(-21, 21, 1), 'profitsvalue')
    grade = ctrl.Consequent(np.arange(0, 100, 1), 'grade')

    # Auto-membership function population is possible with .automf(3, 5, or 7)
    revenuevalue.automf(3)
    profitsvalue.automf(3)

    # Custom membership functions can be built interactively with a familiar
    grade['low'] = fuzz.trimf(grade.universe, [0, 60, 70])
    grade['medium'] = fuzz.trimf(grade.universe, [60, 70, 80])
    grade['high'] = fuzz.trimf(grade.universe, [70, 80, 100])

    # You can see how these look with .view()
    # revenuevalue['average'].view()

    # rofitsvalue.view()

    # grade.view()

    rule1 = ctrl.Rule(revenuevalue['poor'] | profitsvalue['poor'], grade['low'])
    rule2 = ctrl.Rule(profitsvalue['average'], grade['medium'])
    rule3 = ctrl.Rule(profitsvalue['good'] | revenuevalue['good'], grade['high'])

    # rule1.view()

    investment_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    investment = ctrl.ControlSystemSimulation(investment_ctrl)

    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    investment.input['revenuevalue'] = revenue
    investment.input['profitsvalue'] = profit

    # Crunch the numbers
    investment.compute()
    # grade.view(sim=investment)
    return investment.output['grade']
