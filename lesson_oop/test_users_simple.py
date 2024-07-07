import  csv


def test_workers_are_adults(some_dict=None):
    with open('users.csv') as file:
        users = csv.DictReader(file, delimiter=';')
        workers = [user for user in users if user['status'] == 'worker']
    for worker in workers:
        assert int(worker['age']) >= 18

