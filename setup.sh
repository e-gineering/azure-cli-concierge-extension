#!/bin/bash
python setup.py bdist_wheel
az.cmd extension remove -n concierge
az.cmd extension add -s ./dist/concierge-0.0.3-py2.py3-none-any.whl -y
