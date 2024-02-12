# %% isalpha, isalnum

"""
isalpha
: 문자열이 문자로만 이루어져 있는지 확인 후 True, False 리턴
  (공백, 숫자, 특수 기호 불가능)
isalnum
: 문자열이 영어 or 한글 or 숫자로 이루어져 있는지 확인 후 True, False 리턴
  (공백, 특수 기호 불가능)
"""

text1 = "check me"
text2 = "123456"
text3 = "안녕하세요2"

# isalpha()
print(text1.isalpha())  # False
print(text2.isalpha())  # False
print(text3.isalpha())  # False

# isalnum()
print(text1.isalnum())  # False
print(text2.isalnum())  # True
print(text3.isalnum())  # True
# %% isdigit, isnumeric, isdecimal

"""
isdigit
: 문자열이 숫자인지 확인 후 True, False 반환
  숫자처럼 생긴 글자는 제곱 or 세제곱 표현된 특수 기호까지 판별
isnumeric
: 숫자처럼 생긴 글자 모두 판별 (제곱근, 분수, 거듭제곱 특수문자까지)
isdecimal
: 문자열이 int로 변환 가능한 문자로 구성되었을 때 True 반환
"""

print("3²".isnumeric())  # True
print("3²".isdigit())  # True
print("3²".isdecimal())  # False

print("½".isnumeric())  # True
print("½".isdigit())  # False
print("½".isdecimal())  # False

# %%
