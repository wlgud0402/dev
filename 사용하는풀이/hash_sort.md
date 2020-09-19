# 만들어진 딕셔너리의 값을 기준으로 정렬

```python
hash_map = {}
hash_map = sorted(
    hash_map.items(), key=(lambda x: x[1]))#기본 오름차순

# 리스트안 튜플의 요소의 값을 기준으로 정렬
list_tuple = [("지형", 1), ("민수", 2), ("현성", 3)]
list_tuple.sort(key=lambda element: element[1], reverse=True)#내림차순
```
