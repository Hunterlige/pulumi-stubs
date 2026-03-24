import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GatewayAssociationProposalArgs", "GatewayAssociationProposal"]

@pulumi.input_type
class GatewayAssociationProposalArgs:
    def __init__(
        __self__,
        *,
        associated_gateway_id: pulumi.Input[_builtins.str],
        dx_gateway_id: pulumi.Input[_builtins.str],
        dx_gateway_owner_account_id: pulumi.Input[_builtins.str],
        allowed_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayId")
    def associated_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @associated_gateway_id.setter
    def associated_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> pulumi.Input[_builtins.str]: ...
    @dx_gateway_id.setter
    def dx_gateway_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @dx_gateway_owner_account_id.setter
    def dx_gateway_owner_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedPrefixes")
    def allowed_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_prefixes.setter
    def allowed_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _GatewayAssociationProposalState:
    def __init__(
        __self__,
        *,
        allowed_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_gateway_owner_account_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        associated_gateway_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dx_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dx_gateway_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedPrefixes")
    def allowed_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_prefixes.setter
    def allowed_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayId")
    def associated_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @associated_gateway_id.setter
    def associated_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayOwnerAccountId")
    def associated_gateway_owner_account_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @associated_gateway_owner_account_id.setter
    def associated_gateway_owner_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayType")
    def associated_gateway_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @associated_gateway_type.setter
    def associated_gateway_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dx_gateway_id.setter
    def dx_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dx_gateway_owner_account_id.setter
    def dx_gateway_owner_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class GatewayAssociationProposal(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowed_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dx_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dx_gateway_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GatewayAssociationProposalArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowed_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        associated_gateway_owner_account_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        associated_gateway_type: Optional[pulumi.Input[_builtins.str]] = ...,
        dx_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
        dx_gateway_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GatewayAssociationProposal: ...
    @_builtins.property
    @pulumi.getter(name="allowedPrefixes")
    def allowed_prefixes(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayId")
    def associated_gateway_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayOwnerAccountId")
    def associated_gateway_owner_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associatedGatewayType")
    def associated_gateway_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayId")
    def dx_gateway_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dxGatewayOwnerAccountId")
    def dx_gateway_owner_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
