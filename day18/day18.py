class Quiz:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

Question=[
    '1.What is the full form of OOP?\n a.Object Oriented Programming \n b.Objective of Program \n c.Object of Procedural',
    '2.What is Python? \n a.Programming Language b.Snake c.Both'

]
Answer=['a','c']
quiz_list=[
    Quiz(Question[0],Answer[0]),
    Quiz(Question[1],Answer[1])
]
def fun_game(quiz):
    marks=0
    for q in quiz:
        answer=input(f'{q.question} \n enter your answer:')
        if answer==q.answer:
            marks+=1
    print(f'you got {marks} out of {len(Question)}')
fun_game(quiz_list)









