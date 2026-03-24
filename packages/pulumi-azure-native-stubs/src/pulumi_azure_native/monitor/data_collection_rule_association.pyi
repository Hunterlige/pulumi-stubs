

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataCollectionRuleAssociationArgs', 'DataCollectionRuleAssociation']
@pulumi.input_type
class DataCollectionRuleAssociationArgs:
    def __init__(__self__, *, resource_uri: pulumi.Input[_builtins.str], association_name: Optional[pulumi.Input[_builtins.str]] = ..., data_collection_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., data_collection_rule_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationName")
    def association_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_name.setter
    def association_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointId")
    def data_collection_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_collection_endpoint_id.setter
    def data_collection_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionRuleId")
    def data_collection_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_collection_rule_id.setter
    def data_collection_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:monitor:DataCollectionRuleAssociation")
class DataCollectionRuleAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., association_name: Optional[pulumi.Input[_builtins.str]] = ..., data_collection_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., data_collection_rule_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataCollectionRuleAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DataCollectionRuleAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointId")
    def data_collection_endpoint_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionRuleId")
    def data_collection_rule_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[outputs.DataCollectionRuleAssociationResponseMetadata]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.DataCollectionRuleAssociationProxyOnlyResourceResponseSystemData]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


