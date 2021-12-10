Global_Variable=100
def function(num1=1,num2=2,num3=3):
	Local_Variable=Global_Variable
	sum=(num1-num2+Local_Variable)
	print("Sum = ",sum)
	print(num1,"-",num2,"+",Local_Variable)
function(82,60,50)