# --utf8-- 

"""
Script para configurar o engine do Flask 
e com isso iremos colocar a regra de negocio com a as informações de execução.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api