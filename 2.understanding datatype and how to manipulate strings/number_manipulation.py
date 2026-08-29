bmi = 84/1.65**2
print(bmi)
# 30.85399449035813

print(int(bmi))
# 30

print(round(bmi))
# 31

# round(number,ndigits)

print(round(bmi,2))
# 30.85

# Assignment operators

score=0

score+=1
print(score)

score-=1
print(score)

score*=1
print(score)

score/=1
print(score)

# f-strings

score=0
height=1.8
is_winning = True

print(f"your score is {score}, your height is {height}, you're winning is {is_winning}")
