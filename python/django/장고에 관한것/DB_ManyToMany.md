## 3개의 테이블로 조인하는것 대신 ManyToManyField를 통해 내부적으로 새로운 테이블을 생성

Board, User, Like의 세개의 테이블에서 조인을 사용해서 하는 방법도 있지만

ManyToManyField를 Model내에서 사용해 줌으로써 내부적인 로직으로 새로 모델을 생성하도록 할 수있다.

ex)

```python
class Board(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField(blank=True)
  like = models.ManyToManyField(User, related_name='like', blank=True)
```

- User모델과 M:M 관계를 가지는 like
- 여기서 related_name은 첫번째 인자에서 접근할때 사용하는 변수명을 의미한다.

  - Board -> Board.like
  - User -> User.like

=> 사용방법

- 특정 게시글을 찾기 (board)
- 특정 유저를 찾기 (user)
- like를 추가 => board.like.add(user)
- like 삭제 => board.like.remove(user)
- board.like.count()등의 메소드 적용도 가능하다

## **=> 생성되는 board_like의 형태**

- id (like 자체의 pk)
- board_id (board의 pk인 id를 의미)
- user_id (user의 pk인 id를 의미)
