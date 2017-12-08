from weather import Weather
weather = Weather()

def main(): 

	x = 'henderson'

	location = weather.lookup_by_location(x)
	condition = location.condition()
	print(condition.text())

	#
	#forecasts = location.forecast()
	#for forecast in forecasts:
	#    print(forecast.text())
	#    print(forecast.date())
	#    print(forecast.high())
	#    print(forecast.low())


if __name__ == '__main__': 
	main()