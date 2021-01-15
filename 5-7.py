import json

with open('my_file.txt') as my_file:
    firm_name = []
    firm_profit = []
    sum_profit = 0
    profit_firm_count = 0
    for line in my_file:
        firm_name.append(line.split()[0])
        firm_profit.append(int(line.split()[2]) - int(line.split()[3]))
        if int(line.split()[2]) - int(line.split()[3]) > 0:
            sum_profit += int(line.split()[2]) - int(line.split()[3])
            profit_firm_count += 1

data = [dict(zip(firm_name, firm_profit)), {'average_profit': sum_profit / profit_firm_count}]
with open('my_file.json', 'w') as my_json_file:
    json.dump(data, my_json_file)
