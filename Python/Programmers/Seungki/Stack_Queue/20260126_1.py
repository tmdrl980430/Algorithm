# 올바른 괄호


# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.


# s	        answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

def solution(s):
    answer = True
    stack = []
    for i in s:
        
        # 괄호가 열리면 stack에 넣는다.
        if i == "(":
            stack.append(i)
        # 괄호가 닫혔을 경우 스택에서 '('하나 제거한다.
        else :
            # 제거하기 전에 '('가 없다면 return False
            if stack == []:
                return False
            # 있다면 제거하고 계속 진행한다.
            else:
                stack.pop()

    return stack == []

A = "()()"
solution(A)