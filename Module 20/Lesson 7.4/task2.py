server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
print()
for server_data_key, server_data_value in server_data.items():
    print(server_data_key, ':', sep='')
    for key, value in server_data[server_data_key].items():
        print('     ', key, ': ', value, sep='')
