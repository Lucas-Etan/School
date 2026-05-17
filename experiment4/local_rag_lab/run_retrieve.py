from retriever import retrieve
from student_info import print_student_id

print_student_id()
for question in ["原石有什么用途？", "圣遗物有什么作用？", "今天现实天气怎么样？"]:
    print("=" * 80)
    print("Q:", question)
    for item in retrieve(question):
        print(item)