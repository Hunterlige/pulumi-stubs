import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOntapStorageVirtualMachineResult",
    "AwaitableGetOntapStorageVirtualMachineResult",
    "get_ontap_storage_virtual_machine",
    "get_ontap_storage_virtual_machine_output",
]

@pulumi.output_type
class GetOntapStorageVirtualMachineResult:
    def __init__(
        __self__,
        active_directory_configurations=...,
        arn=...,
        creation_time=...,
        endpoints=...,
        file_system_id=...,
        filters=...,
        id=...,
        lifecycle_status=...,
        lifecycle_transition_reasons=...,
        name=...,
        region=...,
        subtype=...,
        tags=...,
        uuid=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfigurations")
    def active_directory_configurations(
        self,
    ) -> Sequence[
        outputs.GetOntapStorageVirtualMachineActiveDirectoryConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Sequence[outputs.GetOntapStorageVirtualMachineEndpointResult]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetOntapStorageVirtualMachineFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleStatus")
    def lifecycle_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleTransitionReasons")
    def lifecycle_transition_reasons(
        self,
    ) -> Sequence[
        outputs.GetOntapStorageVirtualMachineLifecycleTransitionReasonResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subtype(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str: ...

class AwaitableGetOntapStorageVirtualMachineResult(GetOntapStorageVirtualMachineResult):
    def __await__(self): ...

def get_ontap_storage_virtual_machine(
    filters: Optional[
        Sequence[
            Union[
                GetOntapStorageVirtualMachineFilterArgs,
                GetOntapStorageVirtualMachineFilterArgsDict,
            ]
        ]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOntapStorageVirtualMachineResult: ...
def get_ontap_storage_virtual_machine_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetOntapStorageVirtualMachineFilterArgs,
                        GetOntapStorageVirtualMachineFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOntapStorageVirtualMachineResult]: ...
