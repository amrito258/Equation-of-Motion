import math

print('s, u, v, a, t')
main_quan = input(
    'Which one do you want to calculate from this quantities? --> ')

if 's' in main_quan:
    print('1. u, v, t \n2. u, v, a \n3. u, a, t')
    known_quan = input('Which three do you have? Enter the number --> ')

    if '1' in known_quan:
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = float(input('Enter the time(t)(s): '))
        s = ((u + v) * t) / 2
        print(f'The Displacement(s) is {s} m')

    elif '2' in known_quan:
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        s = (v ** 2 - u ** 2) / 2 * a
        print(f'The Displacement(s) is {s} m')

    elif '3' in known_quan:
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        t = float(input('Enter the time(t)(s): '))
        s = (u * t) + 0.5 * a * (t ** 2)
        print(f'The Displacement(s) is {s} m')

elif 'u' in main_quan:
    print('1. s, v, a \n2. v, a, t \n3. s, a, t \n4. s, v, t')
    known_quan = input('Which three do you have? --> ')

    if '1' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        u = v ** 2 - 2*a*s
        u = math.sqrt(u)
        print(f'The Initial Velocity is {u} m/s')

    elif '2' in known_quan:
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        t = float(input('Enter the time(t)(s): '))
        u = v - a*t
        print(f'The Initial Velocity is {u} m/s')

    elif '3' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        t = float(input('Enter the time(t)(s): '))
        u = ((0.5 * a * (t ** 2)) - s) / t
        print(f'The Initial Velocity is {u} m/s')

    elif '4' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = float(input('Enter the time(t)(s): '))
        u = ((2 * s) / t) - v
        print(f'The Initial Velocity is {u}m/s')

elif 'v' in main_quan:
    print('1. s, u, a \n2. u, a, t \n3. s, u, t')
    known_quan = input('Which three do you have? --> ')

    if '1' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        v = (u ** 2) + (2 * a * s)
        v = math.sqrt(v)
        print(f'The Final Velocity is {v} m/s')

    elif '2' in known_quan:
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        t = float(input('Enter the time(t)(s): '))
        v = u + (a * t)
        print(f'The Final Velocity is {v} m/s')

    elif '3' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        t = float(input('Enter the time(t)(s): '))
        v = ((2 * s) / t) - u
        print(f'The Final Velocity is {v} m/s')

elif 'a' in main_quan:
    print('1. s, u, v \n2. u, v, t \n3. s, u, t')
    known_quan = input('Which three do you have? --> ')

    if '1' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        a = ((v ** 2) - (u ** 2)) / (2 * s)
        print(f'The Accelaration is {a} m/s²')

    elif '2' in known_quan:
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = float(input('Enter the time(t)(s): '))
        a = (v - u) / t
        print(f'The Accelaration is {a} m/s²')

    elif '3' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        t = float(input('Enter the time(t)(s): '))
        a = (2 * (s - (u * t))) / t ** 2
        print(f'The Accelaration is {a} m/s²')

elif 't' in main_quan:
    print('1. s, u, v \n2. u, v, a \n3. s, u, a')
    known_quan = input('Which three do you have? --> ')

    if '1' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        t = (2 * s) / (v + u)
        print(f'The Time is {t} s')

    elif '2' in known_quan:
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        v = float(input('Enter the Final Velocity(v)(m/s): '))
        a = float(input('Enter the Accelaration(a)(m/s²): '))
        t = (v - u) / a
        print(f'The Time is {t} s')

    elif '3' in known_quan:
        s = float(input('Enter the Displacment(s)(m): '))
        u = float(input('Enter the Initial Velocity(u)(m/s): '))
        acc = float(input('Enter the Accelaration(a)(m/s²): '))
        a = 0.5 * acc
        b = u
        c = -s
        discriminant = (b ** 2) - (4 * a * c)
        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(t1, t2)

else:
    print('This is may be a another quantity')
