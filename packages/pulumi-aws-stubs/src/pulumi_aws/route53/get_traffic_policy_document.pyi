import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTrafficPolicyDocumentResult",
    "AwaitableGetTrafficPolicyDocumentResult",
    "get_traffic_policy_document",
    "get_traffic_policy_document_output",
]

@pulumi.output_type
class GetTrafficPolicyDocumentResult:
    def __init__(
        __self__,
        endpoints=...,
        id=...,
        json=...,
        record_type=...,
        rules=...,
        start_endpoint=...,
        start_rule=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[Sequence[outputs.GetTrafficPolicyDocumentEndpointResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordType")
    def record_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[Sequence[outputs.GetTrafficPolicyDocumentRuleResult]]: ...
    @_builtins.property
    @pulumi.getter(name="startEndpoint")
    def start_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startRule")
    def start_rule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetTrafficPolicyDocumentResult(GetTrafficPolicyDocumentResult):
    def __await__(self): ...

def get_traffic_policy_document(
    endpoints: Optional[
        Sequence[
            Union[
                GetTrafficPolicyDocumentEndpointArgs,
                GetTrafficPolicyDocumentEndpointArgsDict,
            ]
        ]
    ] = ...,
    record_type: Optional[_builtins.str] = ...,
    rules: Optional[
        Sequence[
            Union[
                GetTrafficPolicyDocumentRuleArgs, GetTrafficPolicyDocumentRuleArgsDict
            ]
        ]
    ] = ...,
    start_endpoint: Optional[_builtins.str] = ...,
    start_rule: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTrafficPolicyDocumentResult: ...
def get_traffic_policy_document_output(
    endpoints: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetTrafficPolicyDocumentEndpointArgs,
                        GetTrafficPolicyDocumentEndpointArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    record_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    rules: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetTrafficPolicyDocumentRuleArgs,
                        GetTrafficPolicyDocumentRuleArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    start_endpoint: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    start_rule: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTrafficPolicyDocumentResult]: ...
