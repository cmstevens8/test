print("Welcome to the Tax Calculator.")
print("This program calculates your net salary after federal, state, and FICA deductions based on the 2023 U.S. tax rules.")

# Constants
FEDERAL_STANDARD_DEDUCTION = 13200

STATE_STANDARD_DEDUCTION = {
    'California': 4609,
    'New York': 8000
}

FEDERAL_TAX_BRACKETS = [
    (10400, 0.10),
    (41225, 0.12),
    (89400, 0.22),
    (174050, 0.24),
    (215400, 0.32),
    (549900, 0.35),
    (1000000, 0.37)
]

STATE_TAX_BRACKETS = {
    'California': [
        (10420, 0.01),
        (24684, 0.02),
        (38959, 0.04),
        (54081, 0.06),
        (68350, 0.08),
        (349137, 0.093),
        (418961, 0.103),
        (698271, 0.113),
        (698272, 0.123)
    ],
    'New York': [
        (8500, 0.04),
        (11700, 0.045),
        (13900, 0.0525),
        (21400, 0.059),
        (80650, 0.0645),
        (215400, 0.0685),
        (1077550, 0.0882),
        (5000000, 0.103)
    ]
}

GROSS_SALARY = float(input("Enter your gross salary: $"))
STATE = input("Enter your state (California or New York): ").strip().title()

deducted_salary = GROSS_SALARY - FEDERAL_STANDARD_DEDUCTION

def calculate_federal_tax(salary):
    deducted_salary = salary - FEDERAL_STANDARD_DEDUCTION
    federal_tax = 0
    previous_limit = 0
    for limit, rate in FEDERAL_TAX_BRACKETS:
        if deducted_salary > previous_limit:
            taxable_income = min(deducted_salary, limit) - previous_limit
            federal_tax += taxable_income * rate
            previous_limit = limit
        else:
            break
    return federal_tax
    
def calculate_state_tax(state, salary):
    state_tax = 0
    if state in STATE_TAX_BRACKETS:
        state_deduction = STATE_STANDARD_DEDUCTION.get(state, 0)
        deducted_salary = salary - state_deduction
        previous_limit = 0
        for limit, rate in STATE_TAX_BRACKETS[state]:
            if deducted_salary > previous_limit:
                taxable_income = min(deducted_salary, limit) - previous_limit
                state_tax += taxable_income * rate
                previous_limit = limit
            else:
                break
    return state_tax

def calculate_fica_tax(salary):
    fica_tax = 0.0765 * salary  # Social Security and Medicare combined
    return fica_tax

federal_tax = calculate_federal_tax(GROSS_SALARY)
state_tax = calculate_state_tax(STATE, GROSS_SALARY)
fica_tax = calculate_fica_tax(GROSS_SALARY)

NET_SALARY = GROSS_SALARY - federal_tax - state_tax - fica_tax

print(f"\nSalary Breakdown:")
print(f"-----------------")
print(f"Gross Salary:   ${GROSS_SALARY:,.2f}")
print(f"Federal Tax:    ${federal_tax:,.2f}")
print(f"State Tax:      ${state_tax:,.2f}")
print(f"FICA Tax:       ${fica_tax:,.2f}")
print(f"-----------------")
print(f"Net Salary:     ${NET_SALARY:,.2f}")

