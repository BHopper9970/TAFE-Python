salary_untaxed = float(input('salary before tax: '))

if salary_untaxed <= 18200:
    taxpaid = 0
elif salary_untaxed > 18200 and salary_untaxed <= 45000:
    taxpaid = (salary_untaxed - 18200) * 0.16
elif salary_untaxed > 45000 and salary_untaxed <= 135000:
    taxpaid = (salary_untaxed - 45000) * 0.3 + 4288
else:
    taxpaid = 0

print('personal income tax paid:', taxpaid)
print('income after tax', salary_untaxed - taxpaid)