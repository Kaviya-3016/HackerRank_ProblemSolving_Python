if __name__ == '__main__':
    n = int(input())  
    # Reads how many students you are going to enter.

    student_marks = {}  
    # Dictionary to store {name : [marks]} for each student.

    for _ in range(n):  
        # Loop n times to take student input
        name, *line = input().split()  
        # Splits input → first word is name, remaining are marks.
        # Example: "Harry 37.5 40 41"
        # name = "Harry", line = ["37.5", "40", "41"]

        scores = list(map(float, line))  
        # Convert the marks into float list → [37.5, 40.0, 41.0]

        student_marks[name] = scores  
        # Add to dictionary → {"Harry": [37.5, 40.0, 41.0]}

    query_name = input()  
    # Read which student’s marks we want (example: Harry)

    x = student_marks[query_name]  
    # Fetch the list of marks for that student.

    avg = sum(x) / len(x)  
    # Calculate the average.

    print(f"{avg:.2f}")  
    # Print with exactly 2 decimal places (important for HackerRank).
