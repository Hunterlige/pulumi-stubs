

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PremiumMicrosoftDefenderForThreatIntelligenceArgs', 'PremiumMicrosoftDefenderForThreatIntelligence']
@pulumi.input_type
class PremiumMicrosoftDefenderForThreatIntelligenceArgs:
    def __init__(__self__, *, data_types: pulumi.Input[PremiumMdtiDataConnectorDataTypesArgs], kind: pulumi.Input[_builtins.str], lookback_period: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], data_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., required_skus_present: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> pulumi.Input[PremiumMdtiDataConnectorDataTypesArgs]:
        
        ...
    
    @data_types.setter
    def data_types(self, value: pulumi.Input[PremiumMdtiDataConnectorDataTypesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackPeriod")
    def lookback_period(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lookback_period.setter
    def lookback_period(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataConnectorId")
    def data_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_connector_id.setter
    def data_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredSKUsPresent")
    def required_skus_present(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @required_skus_present.setter
    def required_skus_present(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PremiumMicrosoftDefenderForThreatIntelligence(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., data_types: Optional[pulumi.Input[Union[PremiumMdtiDataConnectorDataTypesArgs, PremiumMdtiDataConnectorDataTypesArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., lookback_period: Optional[pulumi.Input[_builtins.str]] = ..., required_skus_present: Optional[pulumi.Input[_builtins.bool]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PremiumMicrosoftDefenderForThreatIntelligenceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PremiumMicrosoftDefenderForThreatIntelligence:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> pulumi.Output[outputs.PremiumMdtiDataConnectorDataTypesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookbackPeriod")
    def lookback_period(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredSKUsPresent")
    def required_skus_present(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


