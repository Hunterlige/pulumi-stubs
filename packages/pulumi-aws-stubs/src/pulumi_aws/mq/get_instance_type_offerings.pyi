import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceTypeOfferingsResult",
    "AwaitableGetInstanceTypeOfferingsResult",
    "get_instance_type_offerings",
    "get_instance_type_offerings_output",
]

@pulumi.output_type
class GetInstanceTypeOfferingsResult:
    def __init__(
        __self__,
        broker_instance_options=...,
        engine_type=...,
        host_instance_type=...,
        id=...,
        region=...,
        storage_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="brokerInstanceOptions")
    def broker_instance_options(
        self,
    ) -> Sequence[outputs.GetInstanceTypeOfferingsBrokerInstanceOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetInstanceTypeOfferingsResult(GetInstanceTypeOfferingsResult):
    def __await__(self): ...

def get_instance_type_offerings(
    engine_type: Optional[_builtins.str] = ...,
    host_instance_type: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    storage_type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceTypeOfferingsResult: ...
def get_instance_type_offerings_output(
    engine_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    host_instance_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    storage_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceTypeOfferingsResult]: ...
