#장고 데이터베이스의 Join

1. 정방향참조 select_related

## ex)

Board는 user를 가지고 있다(Board를 user와 조인한다.)
=> Board의 입장에서 정방향으로 join

```python
 => Board.objects.select_related('user')
```

2. 역방향참조 prefetch_related

## ex)

Comment는 board와 user를 가지고 있다()
=> Comment의 입장에서 Board를 역방향으로 join

```python
 => Board.objects.select_related('user')\
    .prefetch_related('comment_set')
```

3. html에서 보여주기

```html
=> {% for board in boards %}<br />
=>>>>>{{ board.text }}<br />
=>>>>>{% for comment in board.comment_set.all %}<br />
=>>>>>>>>>>{{ comment.user.user_name }}<br />
=>>>>>{% endfor %}<br />
<hr />
<br />
=>>>{% endfor %}
```
