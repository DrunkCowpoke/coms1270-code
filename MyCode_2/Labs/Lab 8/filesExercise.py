# Trevor Bentley        7-20-2025
# Lab 8 

# This code takes all the fun out of manual grading

# ----- Open and pull data -----
def read_students(filename):
    students = {}
    with open(filename, "r") as file:
        next(file)  # skip header
        for line in file:
            line = line.strip()
            if line:
                student_id, name = line.split(",", 1)
                students[student_id.strip()] = name.strip()
    return students

# ----- Scoring Definitions -----
def read_scores(filename):
    scores = {}
    with open(filename, "r") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(",")
            student_id = parts[0].strip()
            score = int(parts[2].strip())
            if student_id not in scores:
                scores[student_id] = []
            scores[student_id].append(score)
    return scores

# ----- Grading -----
def calculate_grades(students, scores):
    grades = [["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]]
    
    for student_id in students:
        name = students[student_id]
        student_scores = scores.get(student_id, [])
        total = len(student_scores)
        total_sum = sum(student_scores)
        average = round(total_sum / total, 1) if total > 0 else 0.0
        grades.append([student_id, name, str(total), str(total_sum), str(average)])
    
    return grades

# ----- Submitting Grades -----
def write_grades(filename, grades):
    with open(filename, "w") as file:
        for i, row in enumerate(grades):
            line = ",".join(row)
            if i < len(grades) - 1:
                file.write(line + "\n")
            else:
                file.write(line)  # No trailing newline

# ----- Main FXN -----
def main():
    students = read_students("students.txt")
    scores = read_scores("scores.txt")
    grades = calculate_grades(students, scores)
    write_grades("grades.txt", grades)
    print("grades.txt is now available.")

if __name__ == "__main__":
    main()

