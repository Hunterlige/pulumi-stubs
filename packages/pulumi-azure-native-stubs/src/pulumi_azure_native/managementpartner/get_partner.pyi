import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPartnerResult",
    "AwaitableGetPartnerResult",
    "get_partner",
    "get_partner_output",
]

@pulumi.output_type
class GetPartnerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        created_time=...,
        etag=...,
        id=...,
        name=...,
        object_id=...,
        partner_id=...,
        partner_name=...,
        tenant_id=...,
        type=...,
        updated_time=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]: ...

class AwaitableGetPartnerResult(GetPartnerResult):
    def __await__(self): ...

def get_partner(
    partner_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPartnerResult: ...
def get_partner_output(
    partner_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPartnerResult]: ...
