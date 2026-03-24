import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetBotResult", "AwaitableGetBotResult", "get_bot", "get_bot_output"]

@pulumi.output_type
class GetBotResult:
    def __init__(
        __self__,
        arn=...,
        checksum=...,
        child_directed=...,
        created_date=...,
        description=...,
        detect_sentiment=...,
        enable_model_improvements=...,
        failure_reason=...,
        id=...,
        idle_session_ttl_in_seconds=...,
        last_updated_date=...,
        locale=...,
        name=...,
        nlu_intent_confidence_threshold=...,
        region=...,
        status=...,
        version=...,
        voice_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="childDirected")
    def child_directed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detectSentiment")
    def detect_sentiment(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableModelImprovements")
    def enable_model_improvements(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="voiceId")
    def voice_id(self) -> _builtins.str: ...

class AwaitableGetBotResult(GetBotResult):
    def __await__(self): ...

def get_bot(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBotResult: ...
def get_bot_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBotResult]: ...
