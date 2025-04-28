import difflib
from typing import List
from app.models.diff_models import DiffItem

def calculate_diff(before: str, after: str) -> List[DiffItem]:
    """
    두 문자열(before, after)을 비교하여 변경(diff) 내용을 리스트로 반환하는 함수

    Args:
        before (str): 수정 전 텍스트
        after (str): 수정 후 텍스트

    Returns:
        List[DiffItem]: 삽입(insert) 또는 삭제(delete)된 내용을 담은 리스트
    """
    sequence_matcher = difflib.SequenceMatcher(None, before, after)
    diffs = []

    # 문자열 간 변경 구간(opcode) 순회
    for tag, i1, i2, j1, j2 in sequence_matcher.get_opcodes():
        if tag == 'replace':
            # 교체(replace)는 delete + insert 두 번 처리
            diffs.append(DiffItem(type='delete', position=i1, length=i2 - i1))
            diffs.append(DiffItem(type='insert', position=i1, text=after[j1:j2]))
        elif tag == 'delete':
            # 삭제(delete)된 부분 처리
            diffs.append(DiffItem(type='delete', position=i1, length=i2 - i1))
        elif tag == 'insert':
            # 삽입(insert)된 부분 처리
            diffs.append(DiffItem(type='insert', position=i1, text=after[j1:j2]))

    return diffs
