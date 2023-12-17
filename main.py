from faker import Faker


def parse(query: str) -> dict:
    result = {}
    if '?' in query:
        temp = query.split('?')[1].split('&')
        for i in temp:
            if i:
                kv = i.split('=')
                result[kv[0]] = kv[1]

    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=Dima&age=28') == {'name': 'Dima', 'age': '28'}
    assert parse('http://example.com/?name=Dima&last_name=komarov&age=28') == {'name': 'Dima', 'age': '28', 'last_name': 'komarov'}
    assert parse('http://example.com/?name=Dima&age=28&&') == {'name': 'Dima', 'age': '28'}





def parse_cookie(query: str) -> dict:
    result = {}
    if query:
        temp = query.split(';')
        for i in temp:
            if i:
                kv = i.split('=', 1)
                result[kv[0]] = kv[1]

    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;last_name=d=komarov') == {'name': 'Dima=User', 'age': '28', 'last_name': 'd=komarov'}
    assert parse_cookie(';age=28;') == {'age': '28'}
    assert parse_cookie('age=28;citi=kyiv') == {'age': '28', 'citi': 'kyiv'}

fake = Faker()
list_date = sorted([fake.date() for _ in range(5)])
my_list = []
for i in range(5):
    my_list.append(list_date[i])
print(list_date)
print(my_list)