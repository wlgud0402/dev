 1. pk는 DB 클래스에서 지정하지 않아도 장고에서 자동으로 부여한다.

 2. polls/<<int:question_id>> polls/3
    - 일경우 URL스트링에서 3이 추출되고 뷰함수 호출시 
    - (request, question_id = 3) 의 형태로 인자가 대입된다.

 3. ### user.board_set.all() => user객체의 board_set 속성에 들어있는 항목 모두 : User테이블의 user레코드에 연결된 Board 테이블의 레코드 모두

 4. Admin페이지 (필드순서변경, 각 필드를 분리해서 보여주기(제목), 필드접기(collapse), Question 및 Choice를 한 화면에서 변경하기, 테이블형식(TabularInline), 리스트컬럼, list_filter(사이드바), search_fields(검색), base_site.html(제목변경), 연산자사용(`__startswith`), )

 5. Admin페이지 꾸미기 => 페이지내 데이터들의 순서 변경
```python
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    class QuestionAdmin(admin.ModelAdmin):
        fields = ['pub_date','question_text'] #필드순서변경

    admin.site.register(Question, QuestionAdmin)
                        순서를 변경하고 새로 정의한 QuestionAdmin을 두번째 인자로 등록
```

 5. Admin페이지 꾸미기 (2) => fieldsets 각 튜플의 첫번째 인자가 해당필드의 제목이 된다.
```python
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Question Statment', {'fields':['question_text']}),
            ('Date Information', {'fields':['pub_date']}),
        ]
```

 6. 