def main():
    fraction = str(input("Fraction: "))
    gauge(convert(fraction))

def convert(fraction):
    while True:
        try:
            fraction = str(fraction)
            x, y = fraction.split("/")
            if int(x) > int(y):
                continue
            else:
                return round(int(x)/ int(y) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()