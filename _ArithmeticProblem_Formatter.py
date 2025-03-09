def arrange_arithmetic_problems(problems, show_answers = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Lists to store problem components
    first_numbers = []
    second_numbers = []
    operators_list = []
    calculated_results = []

    # Splitting and validating each problem
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Incorrect format"
        
        first_number, operator, second_number = parts
        
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers must only contain digits."
        # Calculate result
        result = str(int(first_number) + int(second_number)) if operator == "+" else str(int(first_number) - int(second_number))

        # Store values
        first_numbers.append(first_number)
        second_numbers.append(second_number)
        operators_list.append(operator)
        calculated_results.append(result)

    # Constructing the formatted output
    top_row = ""
    middle_row = ""
    separator_row = ""
    result_row = ""

    for i in range(len(problems)):
        width = max(len(first_numbers[i]), len(second_numbers[i])) + 2

        top_row += first_numbers[i].rjust(width) + "  "
        middle_row += operators_list[i] + second_numbers[i].rjust(width - 1) + "  "
        separator_row += "-" * width + "  "
        result_row += calculated_results[i].rjust(width) + "  "

    # Trim trailing spaces
    arranged_problems = top_row.rstrip() + "\n" + middle_row.rstrip() + "\n" + separator_row.rstrip()
    if show_answers:
        arranged_problems += "\n" + result_row.rstrip()

    return arranged_problems
