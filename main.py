from pypika import Query, Table
import pandas
from constants import *
from orders import build_orders


def logger():
    path = create_file_path(LOGGER_PATH)

    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, format=LOGGER_MESSAGE,
                        datefmt=LOGGER_DATE_FORMAT)
    log = logging.getLogger(__name__)
    return log


def create_file_path(path):
    try:
        file_path = Path(path)
    except OSError:
        logger.warning("Failed to create file.")
        return LEFT
    return file_path


logger = logger()


def init():
    pass


def setup():
    pass


def workflow():
    pass


def generate_sql_list():
    orders = Table('Orders')

    orders_list = build_orders()
    orders_sql_list = []

    for i in orders_list:
        orders_sql_list.append((Query.from_(orders).into(SQL_ORDER_ATTRIBUTES).insert(i)).get_sql())

    return orders_sql_list


def out():
    logger.info("Generating a list of orders")
    orders = build_orders()
    logger.info(f"The list's been generated successfully.")

    try:
        csv_path = create_file_path(CSV_PATH)
        sql_csv_path = create_file_path(SQL_CSV_PATH)
    except KeyError:
        logger.warning("Missing CSV's path file. Creating a file.")
        csv_path = CSV_PATH
        sql_csv_path = SQL_CSV_PATH

    logger.info(f"Writing a list to a csv file. \nPath: {csv_path}.")
    write_csv_file(csv_path, orders, ORDER_ATTRIBUTES)

    logger.info(f"Reading a csv file. \nPath: {csv_path}.")
    read_csv_file(csv_path)

    sql_orders = generate_sql_list()
    logger.info(f"The list's been generated successfully.")

    logger.info(f"Writing a queries to a csv file. \nPath: {sql_csv_path}.")
    write_csv_file(sql_csv_path, sql_orders, SQL_ATTRIBUTES)

    logger.info(f"Reading a sql csv file. \nPath: {sql_csv_path}.")
    read_csv_file(sql_csv_path)


def write_csv_file(path, list, columns):
    try:
        csv_file = pandas.DataFrame(data=list, columns=columns)
        csv_file.to_csv(path, index_label=False, sep='\t')
        return csv_file
    except OSError:
        logger.error(f"Failed to write data.")
        return LEFT


def read_csv_file(file):
    try:
        csv_file = pandas.read_csv(file, sep='\t')
        return csv_file
    except OSError:
        logger.error(f"Failed to read data.")
        return LEFT


if __name__ == '__main__':
    try:
        init()
        setup()
        workflow()
        out()
    except Exception as ex:
        logging.error(ex)