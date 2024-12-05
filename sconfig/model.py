from enum import StrEnum
from typing import Optional
from sqlmodel import SQLModel, Field


class FileType(StrEnum):
    """文件类型"""

    FILE = "file"
    FOLDER = "Folder"


class TrackPath(SQLModel, table=True):
    """记录需要跟踪的文件&路径"""
    id: Optional[int] = Field(default=None, primary_key=True)
    type: FileType
    path: str
    name: str


# class FileItems(SQLModel, table=True):
#     """记录所有的文件"""
    