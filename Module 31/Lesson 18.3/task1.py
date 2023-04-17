from re import findall

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
print('Слова на гласную:', findall(r'\b[aouieAOUIEYy]\w*', text))
print('Слова на любой символ, кроме гласной:', findall(r'\b[^aouieAOUIEyY\W]\w*', text))
