def coordinate(movement):
    x,y = 0,0
    for symbol in movement:
        if symbol == 'S':
            y-= 1
        elif movement == 'N':
            y +=1
        elif movement == 'W':
            x-=1
        elif movement == 'E':
            x+=1
    return (x,y)

a = 'SNNNWEEENSWWW'
print(coordinate(a))


