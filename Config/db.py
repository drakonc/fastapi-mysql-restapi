from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Passw0rd!!@localhost:3306/storedb")

con = engine.connect()
