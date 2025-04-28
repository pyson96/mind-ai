from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DiffItem(BaseModel):
    """
    수정된 부분 하나를 나타내는 데이터 모델
    """
    type: str  # 변경 유형 ('insert' 또는 'delete')
    position: int  # 변경이 발생한 위치 (기준: before 문자열 인덱스)
    text: Optional[str] = None  # 삽입(insert)된 텍스트 (type이 'insert'일 때 사용)
    length: Optional[int] = None  # 삭제(delete)된 텍스트 길이 (type이 'delete'일 때 사용)

class DiffRequest(BaseModel):
    """
    Diff 계산 요청을 위한 입력 모델
    """
    before: str  # 수정 전 텍스트
    after: str   # 수정 후 텍스트

class DiffResponse(BaseModel):
    """
    Diff 계산 결과를 반환하는 응답 모델
    """
    diff: List[DiffItem]  # 수정된 항목(DiffItem) 리스트
    timestamp: datetime   # Diff 계산 시각 (UTC 기준)
