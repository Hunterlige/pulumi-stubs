import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ResiliencyPolicyPolicyArgs",
    "ResiliencyPolicyPolicyArgsDict",
    "ResiliencyPolicyPolicyAzArgs",
    "ResiliencyPolicyPolicyAzArgsDict",
    "ResiliencyPolicyPolicyHardwareArgs",
    "ResiliencyPolicyPolicyHardwareArgsDict",
    "ResiliencyPolicyPolicyRegionArgs",
    "ResiliencyPolicyPolicyRegionArgsDict",
    "ResiliencyPolicyPolicySoftwareArgs",
    "ResiliencyPolicyPolicySoftwareArgsDict",
    "ResiliencyPolicyTimeoutsArgs",
    "ResiliencyPolicyTimeoutsArgsDict",
]

class ResiliencyPolicyPolicyArgsDict(TypedDict):
    az: NotRequired[pulumi.Input[ResiliencyPolicyPolicyAzArgsDict]]
    hardware: NotRequired[pulumi.Input[ResiliencyPolicyPolicyHardwareArgsDict]]
    region: NotRequired[pulumi.Input[ResiliencyPolicyPolicyRegionArgsDict]]
    software: NotRequired[pulumi.Input[ResiliencyPolicyPolicySoftwareArgsDict]]
    ...

@pulumi.input_type
class ResiliencyPolicyPolicyArgs:
    def __init__(
        __self__,
        *,
        az: Optional[pulumi.Input[ResiliencyPolicyPolicyAzArgs]] = ...,
        hardware: Optional[pulumi.Input[ResiliencyPolicyPolicyHardwareArgs]] = ...,
        region: Optional[pulumi.Input[ResiliencyPolicyPolicyRegionArgs]] = ...,
        software: Optional[pulumi.Input[ResiliencyPolicyPolicySoftwareArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def az(self) -> Optional[pulumi.Input[ResiliencyPolicyPolicyAzArgs]]: ...
    @az.setter
    def az(self, value: Optional[pulumi.Input[ResiliencyPolicyPolicyAzArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def hardware(
        self,
    ) -> Optional[pulumi.Input[ResiliencyPolicyPolicyHardwareArgs]]: ...
    @hardware.setter
    def hardware(
        self, value: Optional[pulumi.Input[ResiliencyPolicyPolicyHardwareArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[ResiliencyPolicyPolicyRegionArgs]]: ...
    @region.setter
    def region(
        self, value: Optional[pulumi.Input[ResiliencyPolicyPolicyRegionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def software(
        self,
    ) -> Optional[pulumi.Input[ResiliencyPolicyPolicySoftwareArgs]]: ...
    @software.setter
    def software(
        self, value: Optional[pulumi.Input[ResiliencyPolicyPolicySoftwareArgs]]
    ): ...

class ResiliencyPolicyPolicyAzArgsDict(TypedDict):
    rpo: pulumi.Input[_builtins.str]
    rto: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ResiliencyPolicyPolicyAzArgs:
    def __init__(
        __self__, *, rpo: pulumi.Input[_builtins.str], rto: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> pulumi.Input[_builtins.str]: ...
    @rpo.setter
    def rpo(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rto(self) -> pulumi.Input[_builtins.str]: ...
    @rto.setter
    def rto(self, value: pulumi.Input[_builtins.str]): ...

class ResiliencyPolicyPolicyHardwareArgsDict(TypedDict):
    rpo: pulumi.Input[_builtins.str]
    rto: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ResiliencyPolicyPolicyHardwareArgs:
    def __init__(
        __self__, *, rpo: pulumi.Input[_builtins.str], rto: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> pulumi.Input[_builtins.str]: ...
    @rpo.setter
    def rpo(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rto(self) -> pulumi.Input[_builtins.str]: ...
    @rto.setter
    def rto(self, value: pulumi.Input[_builtins.str]): ...

class ResiliencyPolicyPolicyRegionArgsDict(TypedDict):
    rpo: NotRequired[pulumi.Input[_builtins.str]]
    rto: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ResiliencyPolicyPolicyRegionArgs:
    def __init__(
        __self__,
        *,
        rpo: Optional[pulumi.Input[_builtins.str]] = ...,
        rto: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rpo.setter
    def rpo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rto(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rto.setter
    def rto(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResiliencyPolicyPolicySoftwareArgsDict(TypedDict):
    rpo: pulumi.Input[_builtins.str]
    rto: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ResiliencyPolicyPolicySoftwareArgs:
    def __init__(
        __self__, *, rpo: pulumi.Input[_builtins.str], rto: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rpo(self) -> pulumi.Input[_builtins.str]: ...
    @rpo.setter
    def rpo(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rto(self) -> pulumi.Input[_builtins.str]: ...
    @rto.setter
    def rto(self, value: pulumi.Input[_builtins.str]): ...

class ResiliencyPolicyTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ResiliencyPolicyTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
