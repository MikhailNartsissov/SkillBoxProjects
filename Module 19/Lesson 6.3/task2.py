players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
rest_a = [player['name']
          for player in players_dict.values()
          if player['team'] == 'A' and player['status'] == 'Rest'
          ]
training_b = [player['name']
              for player in players_dict.values()
              if player['team'] == 'B' and player['status'] == 'Training'
              ]
travel_c = [player['name']
            for player in players_dict.values()
            if player['team'] == 'C' and player['status'] == 'Travel'
            ]
print('\nВ команде А отдыхают: ', ', '.join(rest_a))
print('В команде B тренируются: ', ', '.join(training_b))
print('В команде C путешествуют: ', ', '.join(travel_c))
