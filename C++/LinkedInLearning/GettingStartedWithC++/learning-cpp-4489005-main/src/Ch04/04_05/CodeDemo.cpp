// Learning C++ 
// Challenge 04_05
// Calculate a GPA, by Eduardo Corpeño 

#include <iostream>
#include <vector>
#include "records.h"

int main(){
    float GPA = 0.0f;
    int id;
    
    std::vector<Student> students = {Student(1, "George P. Burdell"),
                                    Student(2, "Nancy Rhodes")};

    std::vector<Course> courses = {Course(1, "Algebra", 5),
                                Course(2, "Physics", 4),
                                Course(3, "English", 3),
                                Course(4, "Economics", 4)};

    std::vector<Grade> grades = {Grade(1, 1, 'B'), Grade(1, 2, 'A'), Grade(1, 3, 'C'),
                                Grade(2, 1, 'A'), Grade(2, 2, 'A'), Grade(2, 4, 'B')};

    std::cout << "Enter a student ID: " << std::flush;
    std::cin >> id;

    // Calculate the GPA for the selected student.
    // Write your code here
    float gained_points;
    int total_points;
    for(auto grade : grades)  {
        if (grade.get_student_id() == id) {
            int currCourseID = grade.get_course_id();
            total_points += courses[currCourseID].get_credits();
            switch (grade.get_grade())
            {
            case 'A':
                gained_points += 4;
                break;
            case 'B':
                gained_points += 3;
                break;
            case 'C':
                gained_points += 2;
                break;
            case 'D':
                gained_points += 1;
                break;
            default:
                break;
            }
        }
    }
    GPA = gained_points / total_points;

    std::string student_str;
    student_str = students[id].get_name(); // Change this to the selected student's name

    std::cout << "The GPA for " << student_str << " is " << GPA << std::endl;
    
    std::cout << std::endl << std::endl;
    return (0);
}
