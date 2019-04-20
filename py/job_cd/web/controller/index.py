# -*- coding: utf-8 -*-

import json
from flask import render_template, flash, abort, url_for, redirect, session, Response, request, jsonify
from web import app
from web.model.job import Job
from .utils import generate_mongodb_queryset


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/ajax_table', methods=['GET'])
def ajax_table():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    salary_list = request.args.getlist('salary[]')
    benefit_list = request.args.getlist('benefit[]')
    sort_list = request.args.getlist('sort[]')
    find_dict, sorted_list = generate_mongodb_queryset(salary_list=salary_list, benefit_list=benefit_list, sort_list=sort_list)
    jobs = Job.find(find_dict, sorted_list)[limit * (page - 1):limit * page]
    return jsonify({'code': 0, 'msg': '', 'count': jobs.count(), 'data': list(jobs)})


@app.route('/map', methods=['GET'])
def open_map():
    jobs = Job.find({}, [])
    infos = json.dumps([{
        'coordinate': x['coordinate'],
        'company': x['company'],
        'address': x['address'],
        'description': x['description'],
        'name': x['name'],
    } for x in jobs])
    return render_template('map.html', infos=infos)
