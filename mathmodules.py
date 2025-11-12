#Using Math modules with dictionary and functions
import math

def math_value(n):
	value = {}
	sqrt_value = math.sqrt(n)
	tr1_value  = math.sin(n)
	tr2_value  = math.cos(n)
	fact_value = math.factorial(n)
	exp_value  = math.exp(n)
	pow_value  = math.pow(n, 3)
	gcd_value  = math.gcd(n, 2)

	value['sqrt'] = sqrt_value
	value['sin'] = tr1_value
	value['cos'] = tr2_value
	value['factorial'] = fact_value
	value['exp'] = exp_value
	value['pow_n_3'] = pow_value
	value['gcd_n_2'] = gcd_value

	return value

n = int(input("Enter a value: "))
print(math_value(n))


