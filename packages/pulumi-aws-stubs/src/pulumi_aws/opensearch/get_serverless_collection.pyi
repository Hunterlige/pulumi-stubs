import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerlessCollectionResult",
    "AwaitableGetServerlessCollectionResult",
    "get_serverless_collection",
    "get_serverless_collection_output",
]

@pulumi.output_type
class GetServerlessCollectionResult:
    def __init__(
        __self__,
        arn=...,
        collection_endpoint=...,
        created_date=...,
        dashboard_endpoint=...,
        description=...,
        failure_code=...,
        failure_message=...,
        id=...,
        kms_key_arn=...,
        last_modified_date=...,
        name=...,
        region=...,
        standby_replicas=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="collectionEndpoint")
    def collection_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dashboardEndpoint")
    def dashboard_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failureCode")
    def failure_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failureMessage")
    def failure_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="standbyReplicas")
    def standby_replicas(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerlessCollectionResult(GetServerlessCollectionResult):
    def __await__(self): ...

def get_serverless_collection(
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerlessCollectionResult: ...
def get_serverless_collection_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerlessCollectionResult]: ...
