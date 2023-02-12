# A. Камень, ножницы, бумага
first_player, second_player = int(input()), int(input())
if first_player == second_player:
    print('draw')
elif first_player+1 == second_player or (first_player+1) % 3 == second_player:
    print('first')
else:
    print('second')
