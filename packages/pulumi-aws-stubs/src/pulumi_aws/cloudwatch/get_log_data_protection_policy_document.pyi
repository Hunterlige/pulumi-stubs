import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLogDataProtectionPolicyDocumentResult",
    "AwaitableGetLogDataProtectionPolicyDocumentResult",
    "get_log_data_protection_policy_document",
    "get_log_data_protection_policy_document_output",
]

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentResult:
    def __init__(
        __self__,
        configuration=...,
        description=...,
        id=...,
        json=...,
        name=...,
        statements=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.GetLogDataProtectionPolicyDocumentConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def statements(
        self,
    ) -> Sequence[outputs.GetLogDataProtectionPolicyDocumentStatementResult]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetLogDataProtectionPolicyDocumentResult(
    GetLogDataProtectionPolicyDocumentResult
):
    def __await__(self): ...

def get_log_data_protection_policy_document(
    configuration: Optional[
        Union[
            GetLogDataProtectionPolicyDocumentConfigurationArgs,
            GetLogDataProtectionPolicyDocumentConfigurationArgsDict,
        ]
    ] = ...,
    description: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    statements: Optional[
        Sequence[
            Union[
                GetLogDataProtectionPolicyDocumentStatementArgs,
                GetLogDataProtectionPolicyDocumentStatementArgsDict,
            ]
        ]
    ] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLogDataProtectionPolicyDocumentResult: ...
def get_log_data_protection_policy_document_output(
    configuration: Optional[
        pulumi.Input[
            Optional[
                Union[
                    GetLogDataProtectionPolicyDocumentConfigurationArgs,
                    GetLogDataProtectionPolicyDocumentConfigurationArgsDict,
                ]
            ]
        ]
    ] = ...,
    description: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    statements: Optional[
        pulumi.Input[
            Sequence[
                Union[
                    GetLogDataProtectionPolicyDocumentStatementArgs,
                    GetLogDataProtectionPolicyDocumentStatementArgsDict,
                ]
            ]
        ]
    ] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLogDataProtectionPolicyDocumentResult]: ...
