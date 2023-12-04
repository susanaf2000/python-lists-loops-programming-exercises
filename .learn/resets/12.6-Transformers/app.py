incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

def data_transformer(user):
    name = user["name"]
    last_name = user["last_name"]
    return name + " " + last_name

def transform_data_list(data_list):
    return list(map(data_transformer, data_list))

new_list = transform_data_list(incoming_ajax_data)

print(new_list)