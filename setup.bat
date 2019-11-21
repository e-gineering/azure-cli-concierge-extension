python setup.py bdist_wheel
az extension remove -n concierge
az extension add -s .\dist\concierge-0.0.3-py2.py3-none-any.whl -y
