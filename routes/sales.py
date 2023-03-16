import json
import falcon
import logging
from datetime import date, timedelta


class Sales:

    def __init__(self, nz):
        self.nz = nz

    def __date_from(self):
        today = date.today()
        days_since = today.weekday() + 1
        return today - timedelta(days=days_since)

    def __date_to(self):
        return date.today()

    def on_get(self, request, response, store):
        if self.nz is None:
            raise falcon.HTTPInternalServerError(
                title='Database Connection Error',
                description='Database connection is not available. Please contact support.')

        date_from = request.get_param_as_date('from') or self.__date_from()
        date_to = request.get_param_as_date('to') or self.__date_to()

        statement = '''
          select
              s.store_name   as store
            , sum(f.amount)  as sales
          from dw.sales f
            inner join dw.store s on s.id = f.store_id
          where s.id = ?
            and f.transaction_date between ? and ?
          group by s.store_name
        '''

        with self.nz.cursor() as cursor:
            try:
                cursor.execute(statement, (store, date_from, date_to))
            except Exception as e:
                logging.error('Query failed')
                logging.error(e)
                raise falcon.HTTPInternalServerError(title='Database Query Error',
                                                     description='Database query failed. Please contact support.')

            if cursor.rowcount == 0:
                raise falcon.HTTPNotFound()

            body = {}
            results = cursor.fetchall()
            for store, sales in results:
                body = {'store': store, 'sales': sales}

            response.body = json.dumps(body)
