packets_amount = int(input('Кол-во пакетов: '))
packets_rejected = 0

message_received = []
current_packet = []

for packet_number in range(packets_amount):
    print('\nПакет номер', packet_number + 1)
    for packet_byte in range(4):
        print(packet_byte + 1, 'бит: ', end=' ')
        current_packet.append(int(input()))
    if current_packet.count(-1) > 1:
        print('Много ошибок в пакете.')
        packets_rejected += 1
    else:
        message_received.extend(current_packet)
    current_packet = []

print('\nПолученное сообщение:', message_received)
print('Кол-во ошибок в сообщении:', packets_rejected)
print('Кол-во потерянных пакетов:', packets_rejected)
