#-------------------------------------------------------------------------------
# Name:        views.py
# Purpose:
#
# Author:      dloshkobanov
#
# Created:     31.10.2013
# Copyright:   (c) dloshkobanov 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import render_template
from app import app
from app import func

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = '�������� ����� �� �����')

@app.route('/<hash>')
def coordinates(hash=None):
    #���� � ���� ��� ���������� �� ����
    #����������� ���������� ���� ������
    lstPoint = [(57.616667,39.85),(57.616667,39.85), (56.616667,39.85), (57.616667,38.85), (56.616667,38.85), (58.616667,40.85), (58.616667,39.85), (57.616667,40.85) ,(60.616667,39.85)]
    numPolygon = func.grahamscan(lstPoint)# ������ ����� ��������������
    lstPolygon = [lstPoint[i] for i in numPolygon]# ������ ����� ��������������
    centerPoint= func.centeroffravity(lstPolygon)# ������ ������� ��������������
    return render_template('coordinates.html', centerPoint=centerPoint, lstPolygon=lstPolygon, lstPoint=lstPoint)