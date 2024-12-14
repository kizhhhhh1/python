def calculate_student_users(total_users, staff_users):
    # Calculate non-teaching staff users
    non_teaching_staff_users = staff_users // 3
    
    # Calculate student users
    student_users = total_users - (staff_users + non_teaching_staff_users)
    
    return student_users

# Sample Input
total_users = 856
staff_users = 126

# Calculate and print the number of student users
student_users = calculate_student_users(total_users, staff_users)
print(f"Number of Student Users: {student_users}")
