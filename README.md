# PicoDB

PicoDB is lightweight, fast, and simple database with namespaces.

## PicoDB is simple
```python
import picodb

db = picodb.load('test.db', False)

db.set_ns('space')
db.set('space', 'key', 'value')
db.delete('space', 'key')
db.get('space', 'key')
db.save()
```


## And Easy to Install

```shell
pip install picodb
```

