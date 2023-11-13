import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between a minimum and maximum value.

    Parameters:
    min_value (int): The lower bound for the random number generation.
    max_value (int): The upper bound for the random number generation.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Randomly choose a mathematical operator from a list of operators.

    Returns:
    str: A string representing a mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(number1, number2, operator):
    """
    Create a math problem using two numbers and an operator, and calculate the answer.

    Parameters:
    number1 (int): The first number in the math problem.
    number2 (int): The second number in the math problem.
    operator (str): The operator for the math problem.

    Returns:
    tuple: A tuple containing the math problem as a string and the answer as an integer.
    """
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    else:
        raise ValueError(f"Invalid operator: {operator}")
    return problem, answer

def math_quiz():
    """
    Run a simple math quiz game that asks the user to solve math problems.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        try:
            number1 = generate_random_integer(1, 10)
            number2 = generate_random_integer(1, 10)
            operator = choose_random_operator()

            problem, answer = create_math_problem(number1, number2, operator)
            print(f"\nQuestion: {problem}")
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)

            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

        except ValueError as e:
            print(f"An error occurred: {e}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()