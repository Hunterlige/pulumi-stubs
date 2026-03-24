import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["Datapolicyv2DataPolicyArgs", "Datapolicyv2DataPolicy"]

@pulumi.input_type
class Datapolicyv2DataPolicyArgs:
    def __init__(
        __self__,
        *,
        data_policy_id: pulumi.Input[_builtins.str],
        data_policy_type: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        data_masking_policy: Optional[
            pulumi.Input[Datapolicyv2DataPolicyDataMaskingPolicyArgs]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyId")
    def data_policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_policy_id.setter
    def data_policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyType")
    def data_policy_type(self) -> pulumi.Input[_builtins.str]: ...
    @data_policy_type.setter
    def data_policy_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataMaskingPolicy")
    def data_masking_policy(
        self,
    ) -> Optional[pulumi.Input[Datapolicyv2DataPolicyDataMaskingPolicyArgs]]: ...
    @data_masking_policy.setter
    def data_masking_policy(
        self, value: Optional[pulumi.Input[Datapolicyv2DataPolicyDataMaskingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def grantees(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grantees.setter
    def grantees(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _Datapolicyv2DataPolicyState:
    def __init__(
        __self__,
        *,
        data_masking_policy: Optional[
            pulumi.Input[Datapolicyv2DataPolicyDataMaskingPolicyArgs]
        ] = ...,
        data_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataMaskingPolicy")
    def data_masking_policy(
        self,
    ) -> Optional[pulumi.Input[Datapolicyv2DataPolicyDataMaskingPolicyArgs]]: ...
    @data_masking_policy.setter
    def data_masking_policy(
        self, value: Optional[pulumi.Input[Datapolicyv2DataPolicyDataMaskingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyId")
    def data_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_policy_id.setter
    def data_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyType")
    def data_policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_policy_type.setter
    def data_policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def grantees(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grantees.setter
    def grantees(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyTag")
    def policy_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_tag.setter
    def policy_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class Datapolicyv2DataPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_masking_policy: Optional[
            pulumi.Input[
                Union[
                    Datapolicyv2DataPolicyDataMaskingPolicyArgs,
                    Datapolicyv2DataPolicyDataMaskingPolicyArgsDict,
                ]
            ]
        ] = ...,
        data_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Datapolicyv2DataPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_masking_policy: Optional[
            pulumi.Input[
                Union[
                    Datapolicyv2DataPolicyDataMaskingPolicyArgs,
                    Datapolicyv2DataPolicyDataMaskingPolicyArgsDict,
                ]
            ]
        ] = ...,
        data_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        grantees: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Datapolicyv2DataPolicy: ...
    @_builtins.property
    @pulumi.getter(name="dataMaskingPolicy")
    def data_masking_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.Datapolicyv2DataPolicyDataMaskingPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyId")
    def data_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicyType")
    def data_policy_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grantees(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyTag")
    def policy_tag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
