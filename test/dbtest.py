import pytest
import pyorient
from app.DbManager import DbManager

def test_db_connect_with_invalid_args():
	dbManager = DbManager("localhost",2424,'','')
	with pytest.raises(Exception):
		dbManager.connect("root","root2")

def test_db_connect_with_valid_args():
	dbManager = DbManager("localhost",2424,'','')
	dbManager.connect("root","root")
