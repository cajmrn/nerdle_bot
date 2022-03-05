import unittest

from src.server.db.DbConfig import *
from src.server.db.MikeDB import MikeDB


class MikeDBTestCase(unittest.TestCase):
    def test_config(self):
        self.assertEqual(DB_CONFIG['DB_HOST'], 'gerdov.com')
        self.assertEqual(DB_CONFIG['DB_NAME'], 'nerdleDB')
        self.assertEqual(DB_CONFIG['DB_KEY'], 'NRDL3cr3tK3y')

    def test_db_init(self):
        db = MikeDB(db_host=DB_CONFIG['DB_HOST'], db_name=DB_CONFIG['DB_NAME'], db_key=DB_CONFIG['DB_KEY'])

        self.assertEqual(db.dbUrl, 'http://gerdov.com/mike-db/api/nerdleDB/')
        self.assertEqual(db.wsUrl, 'ws://gerdov.com/mike-db/subscribe/nerdleDB')

    def test_db_add_simple(self):
        db = MikeDB(db_host=DB_CONFIG['DB_HOST'], db_name=DB_CONFIG['DB_NAME'], db_key=DB_CONFIG['DB_KEY'])

        db.delete('test-key-1', None)

        # store one item into a list
        value = {'name': 'Ian', 'age': 69, 'sex': True}
        r = db.add(key='test-key-1', value=value)

        self.assertIsNotNone(r)
        # NOTE! See how original 'value' object had no 'id' field, but once it is added to DB, the unique ID is generated and added to the object.
        self.assertGreater(r['id'], 0)

        rr = db.get(key='test-key-1')

        # NOTE! 'add' always create a list, even for a single item! For basic DB operation use 'update' instead.
        self.assertEqual(r['id'], rr[0]['id'])
        # NOTE! 'add' always create a list, even for a single item! For basic DB operation use 'update' instead.

    def test_db_add_list(self):
        db = MikeDB(db_host=DB_CONFIG['DB_HOST'], db_name=DB_CONFIG['DB_NAME'], db_key=DB_CONFIG['DB_KEY'])

        db.delete('test-key-2', None)

        # store item after item into a list
        value = {'name': 'Ian', 'age': 69, 'sex': True}
        db.add(key='test-key-2', value=value)
        value = {'name': 'Carlo', 'age': 420, 'sex': False}
        db.add(key='test-key-2', value=value)
        value = {'name': 'Mike', 'age': 0, 'sex': None}
        db.add(key='test-key-2', value=value)

        r = db.get(key='test-key-2')

        self.assertIsNotNone(r)
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 3)

    def test_db_update_simple(self):
        db = MikeDB(db_host=DB_CONFIG['DB_HOST'], db_name=DB_CONFIG['DB_NAME'], db_key=DB_CONFIG['DB_KEY'])

        db.delete('test-key-3', None)

        value1 = {'name': 'Ian', 'age': 69, 'sex': True}
        value2 = {'name': 'Carlo', 'age': 420, 'sex': False}
        value3 = {'name': 'Mike', 'age': 0, 'sex': None}

        # store a single item
        db.update(key='test-key-3', value=value1)

        r = db.get(key='test-key-3')
        print("\n", r)
        self.assertIsNotNone(r)
        self.assertNotIsInstance(r, list)
        self.assertGreater(r['id'], 0)

        # replace it with  a list
        db.update(key='test-key-3', value=[value1, value2, value3])

        r = db.get(key='test-key-3')
        print("\n", r)
        self.assertIsNotNone(r)
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 3)

        # replace it with a basic string
        r = db.update(key='test-key-3', value='and now something completely different')
        print("\n", r)
        self.assertIsNotNone(r)
        self.assertIsInstance(r.decode('utf-8'), str)

    def test_db_update_list(self):
        db = MikeDB(db_host=DB_CONFIG['DB_HOST'], db_name=DB_CONFIG['DB_NAME'], db_key=DB_CONFIG['DB_KEY'])

        db.delete('test-key-4', None)

        # create a list and store it
        value1 = db.add('test-key-4', {'name': 'Ian', 'age': 69, 'sex': True})
        value2 = db.add('test-key-4', {'name': 'Carlo', 'age': 420, 'sex': False})
        self.assertGreater(value2['id'], 0) # see how db ID is added to each stored item
        value3 = db.add('test-key-4', {'name': 'Mike', 'age': 0, 'sex': None})

        r = db.get(key='test-key-4')
        print("\n", r)
        self.assertIsNotNone(r)
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 3)

        # change one item and update it in the list
        value2['name'] = "The Greatest";
        r = db.update(key='test-key-4', value=value2)

        r = db.get(key='test-key-4')
        print("\n", r)
        self.assertIsNotNone(r)
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 3)

        self.assertEqual(r[1]['name'], "The Greatest")

if __name__ == '__main__':
    unittest.main()
