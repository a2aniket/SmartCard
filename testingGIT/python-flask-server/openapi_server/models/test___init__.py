from __init__ import *
def test_course_model():
    # Test creating a course and adding it to the database
    course = Course(course_name='Math', instructor='John Smith')
    db.session.add(course)
    db.session.commit()
    assert course.id is not None

    # Test updating a course and saving it to the database
    course.course_name = 'Mathematics'
    db.session.add(course)
    db.session.commit()
    assert course.course_name == 'Mathematics'

    # Test deleting a course from the database
    db.session.delete(course)
    db.session.commit()
    assert Course.query.filter_by(id=course.id).first() is None

def test_student_model():
    # Test creating a student and adding it to the database
    student = Student(name='John Doe', email='johndoe@example.com')
    db.session.add(student)
    db.session.commit()
    assert student.id is not None

    # Test updating a student and saving it to the database
    student.name = 'Jane Doe'
    db.session.add(student)
    db.session.commit()
    assert student.name == 'Jane Doe'

    # Test deleting a student from the database
    db.session.delete(student)
    db.session.commit()
    assert Student.query.filter_by(id=student.id).first() is None