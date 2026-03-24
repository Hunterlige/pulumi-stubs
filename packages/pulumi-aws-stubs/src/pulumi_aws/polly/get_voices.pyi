import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVoicesResult",
    "AwaitableGetVoicesResult",
    "get_voices",
    "get_voices_output",
]

@pulumi.output_type
class GetVoicesResult:
    def __init__(
        __self__,
        engine=...,
        id=...,
        include_additional_language_codes=...,
        language_code=...,
        region=...,
        voices=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeAdditionalLanguageCodes")
    def include_additional_language_codes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def voices(self) -> Optional[Sequence[outputs.GetVoicesVoiceResult]]: ...

class AwaitableGetVoicesResult(GetVoicesResult):
    def __await__(self): ...

def get_voices(
    engine: Optional[_builtins.str] = ...,
    include_additional_language_codes: Optional[_builtins.bool] = ...,
    language_code: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    voices: Optional[Sequence[Union[GetVoicesVoiceArgs, GetVoicesVoiceArgsDict]]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVoicesResult: ...
def get_voices_output(
    engine: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    include_additional_language_codes: Optional[
        pulumi.Input[Optional[_builtins.bool]]
    ] = ...,
    language_code: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    voices: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetVoicesVoiceArgs, GetVoicesVoiceArgsDict]]]
        ]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVoicesResult]: ...
