'''
配置文件
'''
DEBUG=True
DB_USERNAME='root'
DB_PASSWORD='root'
DB_HOST='127.0.0.1'
DB_PORT=3306
DB_NAME='cms2'
## dialect + driver://username:passwor@host:port/database
DB_URI=f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLALCHEMY_DATABASE_URI=DB_URI
##动态追踪修改设置 必须设置
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_ECHO=True # 查询时候显示sql语句