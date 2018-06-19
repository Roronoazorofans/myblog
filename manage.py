from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db


app = create_app("development")

manager = Manager(app)
# 数据库迁移
Migrate(app, db)
# 添加迁移脚本到脚本管理器
manager.add_command('db', MigrateCommand)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
