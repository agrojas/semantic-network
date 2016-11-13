import pytest
import pyorient
from app.DbManager import DbManager

def test_db_connect_with_invalid_args():
	dbManager = DbManager("localhost",2424,'','')
	with pytest.raises(pyorient.exceptions.PyOrientSecurityAccessException):
		dbManager.connect("root","root2")
	excinfo.match(r'.* 123 .*')

def test_db_connect_with_valid_args():
	dbManager = DbManager("localhost",2424,'','')
	with pytest.raises(pyorient.exceptions.PyOrientSecurityAccessException):
		dbManager.connect("root","root")
	excinfo.match(r'.* 123 .*')


if __name__ == '__main__':
    test_db_connect_with_valid_args()
    test_db_connect_with_invalid_args()
