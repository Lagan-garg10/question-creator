prompt_template = """
you are an expert at creating questions based on given material and context.
your goal is to prepare a student for their exams and test.
create subjective type questions only. create maximum of 20 questions
Instructions:
Generate only normal subjective questions.
Do not include target numbers, percentages, or technical formatting.
Questions should be open-ended, simple, and encourage descriptive answers.
create only questions do not add any any extra text remove all extra text
Keep them suitable for school/college exams or general assessments.
you do this by asking the questions about the text below:

...................
{text}
..................

create questions that will prepare the student for their tests. 
make sure not to lose any important information
"""

refine_template = ("""
You are an expert at creating practice subjective type questions based on given material and context.
Your goal is to help a student prepare for a his test.
Instructions:
Generate only normal subjective questions.
Do not include target numbers, percentages, or technical formatting.
create only questions do not add any any extra text remove all extra text
Questions should be open-ended, simple, and encourage descriptive answers.
Keep them suitable for school/college exams or general assessments.
We have received some practice questions to a certain extent: {existing_answer}.
We have the option to refine the existing questions or add new ones.
(only if necessary) with some more context below.
------------
{text}
------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the original questions.
QUESTIONS:
"""
)