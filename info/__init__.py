# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf import CSRFProtect
from flask_session import Session
from config import config

# 工厂方法创建app
db = SQLAlchemy()
redis_store = None


def create_app(config_name):

    app = Flask(__name__)
    # 配置数据库
    db.init_app(app)

    #　配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启CSRF保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)
    return app