hon
def evaluate_credit_eligibility(income, credit_score):
    if income >= 30000 and credit_score >= 700:
        return "Eligible for high-limit credit score"
    elif income >= 20000 and credit_score >= 600:
        return "Eligible for moderate-limit credit score"
    else:
        return "Ineligible for high-limit or moderate-limit credit score"

def main():
    try:
        income = float(input("Enter your annual income: "))
        credit_score = int(input("Enter your credit score: "))
        result = evaluate_credit_eligibility(income, credit_score)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values for income and credit score.")

if __name__ == "__main__":
    main()
