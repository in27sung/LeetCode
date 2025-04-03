import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Generate all student-subject pairs
    all_pairs = students.merge(subjects, how='cross')

    # Count how many times each student attended each subject
    attended_exams = (
        examinations.groupby(['student_id', 'subject_name'])
        .size()
        .reset_index(name='attended_exams')
    )

    # Merge with all pairs to ensure zero attendance is included
    result = pd.merge(all_pairs, attended_exams, how='left', on=['student_id', 'subject_name'])

    # Replace NaNs with 0 and ensure integer type
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    return result.sort_values(by=['student_id', 'subject_name'])

