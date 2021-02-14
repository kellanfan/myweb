# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   pg_client.py
@Time    :   2019/11/03 18:13:37
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import yaml
import psycopg2
import sys

class Mypostgres(object):
    def __init__(self):
        pg_config = self.__get_config()
        self.database = pg_config.get('database')
        self.user = pg_config.get('user')
        self.password = pg_config.get('password')
        self.host = pg_config.get('host')
        self.port = int(pg_config.get('port'))

    def __get_config(self):
        with open('/config/pg.yaml') as f:
            pg_config = yaml.safe_load(f.read())
        return pg_config

    def __init_conn(self):
        try:
            conn=psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except Exception as e:
            conn = None
            print('Connect to PostgreSQL failed: [{0}]'.format(e))
        return conn

    def execute(self, sql, parameters=None):
        '''
        @param sql - the sql statement to be executed.
            e.g. "INSERT INTO test (num, data) VALUES (%s, %s)"
        @param parameters - a sequence of variables in the sql operation.
            e.g. (100, "abc") or [10, 'def']
        '''
        action = sql.split()[0].strip().lower()
        if action not in ['select', 'insert', 'delete', 'update', 'create']:
            print('The action [{0}] of SQL [{1}] is not supported!'.format(action, sql))
            return None

        conn = self.__init_conn()
        if conn is not None:
            cursor = conn.cursor()
        else:
            return None

        try:
            cursor.execute(sql, parameters)
            if action == 'select':
                rows = cursor.fetchall()
                result = rows
            else:
                conn.commit()
                rowcount = cursor.rowcount
                result = rowcount
        except Exception as e:
            conn.rollback()
            result = None
            print('Execute SQL [{0}] failed: [{1}]'.format(sql, e))
        finally:
            cursor.close()
            conn.close()

        return result

