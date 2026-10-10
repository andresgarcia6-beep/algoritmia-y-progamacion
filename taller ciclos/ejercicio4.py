# Diccionario inicial de estudiantes y sus puntajes
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

# Diccionario donde guardaremos los resultados
student_grades = {}

# Recorremos cada estudiante y su puntaje
for student, score in student_scores.items():
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    # Asignamos la nota descriptiva al nuevo diccionario
    student_grades[student] = grade

# Mostrar el diccionario resultante
print("📌 Diccionario student_grades final:")
print(student_grades)