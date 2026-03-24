import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LanguageModelInputDataConfig"]

@pulumi.output_type
class LanguageModelInputDataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_access_role_arn: _builtins.str,
        s3_uri: _builtins.str,
        tuning_data_s3_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tuningDataS3Uri")
    def tuning_data_s3_uri(self) -> Optional[_builtins.str]: ...
